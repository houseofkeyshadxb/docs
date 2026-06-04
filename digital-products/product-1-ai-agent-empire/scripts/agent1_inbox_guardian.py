#!/usr/bin/env python3
"""
Script: Agent 1 — The Inbox Guardian
Purpose: Triage Gmail inbox, categorize emails, and draft intelligent replies using Claude AI
Business: AI Agent Empire Product

Usage:
    python agent1_inbox_guardian.py
    python agent1_inbox_guardian.py --dry-run    # Preview without making changes
    python agent1_inbox_guardian.py --limit 10   # Process only 10 emails

Setup:
    1. pip install -r requirements.txt
    2. Copy .env.example to .env and fill in your credentials
    3. Run once to authenticate Gmail: python agent1_setup.py
    4. Then run this script (or add to cron for automation)
"""

import os
import sys
import json
import logging
import argparse
import base64
from datetime import datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [InboxGuardian] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'logs/inbox_guardian_{datetime.now().strftime("%Y%m%d")}.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# CONFIGURATION — Edit these for your business
# ─────────────────────────────────────────────
CONFIG = {
    "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
    "gmail_credentials": os.getenv("GMAIL_CREDENTIALS_PATH", "./credentials.json"),
    "gmail_token": "./gmail_token.json",
    "slack_webhook": os.getenv("SLACK_WEBHOOK_URL"),
    "business_name": os.getenv("BUSINESS_NAME", "My Business"),
    "owner_name": os.getenv("OWNER_NAME", "Business Owner"),
    "owner_email": os.getenv("OWNER_EMAIL"),
    "model": "claude-haiku-4-5-20251001",  # Fast + cheap for email tasks
    "max_emails": 50,    # Max emails to process per run
    "draft_categories": ["CLIENT", "HOT_LEAD", "WARM_LEAD", "URGENT"],
}

# VIP clients — always prioritized
VIP_EMAILS = os.getenv("VIP_EMAILS", "").split(",")

# Urgency trigger words
URGENCY_KEYWORDS = [
    "refund", "money back", "complaint", "legal", "lawyer",
    "urgent", "asap", "immediately", "disappointed", "cancel my account",
    "not working", "broken", "failed", "fraud", "chargeback"
]


def get_gmail_service():
    """Authenticate and return Gmail API service."""
    try:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build

        SCOPES = [
            'https://www.googleapis.com/auth/gmail.readonly',
            'https://www.googleapis.com/auth/gmail.compose',
            'https://www.googleapis.com/auth/gmail.labels',
            'https://mail.google.com/'
        ]

        creds = None
        if os.path.exists(CONFIG["gmail_token"]):
            creds = Credentials.from_authorized_user_file(CONFIG["gmail_token"], SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CONFIG["gmail_credentials"], SCOPES)
                creds = flow.run_local_server(port=0)

            with open(CONFIG["gmail_token"], 'w') as token:
                token.write(creds.to_json())

        return build('gmail', 'v1', credentials=creds)

    except Exception as e:
        logger.error(f"Gmail auth failed: {e}")
        logger.info("Run 'python agent1_setup.py' first to set up Gmail authentication")
        sys.exit(1)


def fetch_unread_emails(service, limit=50):
    """Fetch unread emails from Gmail inbox."""
    try:
        results = service.users().messages().list(
            userId='me',
            labelIds=['INBOX', 'UNREAD'],
            maxResults=limit
        ).execute()

        messages = results.get('messages', [])
        emails = []

        for msg in messages:
            msg_data = service.users().messages().get(
                userId='me',
                id=msg['id'],
                format='full'
            ).execute()

            headers = {h['name']: h['value'] for h in msg_data['payload']['headers']}

            # Extract body
            body = ""
            if 'parts' in msg_data['payload']:
                for part in msg_data['payload']['parts']:
                    if part['mimeType'] == 'text/plain':
                        data = part['body'].get('data', '')
                        body = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
                        break
            elif 'body' in msg_data['payload']:
                data = msg_data['payload']['body'].get('data', '')
                body = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')

            emails.append({
                "id": msg['id'],
                "from": headers.get('From', ''),
                "to": headers.get('To', ''),
                "subject": headers.get('Subject', '(No subject)'),
                "date": headers.get('Date', ''),
                "body": body[:2000],  # Limit body to 2000 chars for AI processing
                "snippet": msg_data.get('snippet', ''),
            })

        logger.info(f"Fetched {len(emails)} unread emails")
        return emails

    except Exception as e:
        logger.error(f"Failed to fetch emails: {e}")
        return []


def analyze_email_with_claude(email_data):
    """Use Claude to categorize email and draft a reply."""
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=CONFIG["anthropic_api_key"])

        prompt = f"""You are the Inbox Guardian for {CONFIG['business_name']}.

Analyze this email and provide a JSON response.

EMAIL DETAILS:
From: {email_data['from']}
Subject: {email_data['subject']}
Body: {email_data['body'][:1500]}

VIP clients: {', '.join(VIP_EMAILS) if VIP_EMAILS[0] else 'none set'}
Urgency keywords to watch for: {', '.join(URGENCY_KEYWORDS)}

TASK:
1. Categorize this email: CLIENT, HOT_LEAD, WARM_LEAD, URGENT, ADMIN, NEWSLETTER, SPAM, or FYI
2. Set priority: HIGH, MEDIUM, or LOW
3. If category is CLIENT, HOT_LEAD, WARM_LEAD, or URGENT — draft a professional reply
4. Determine if a Slack alert is needed (URGENT or VIP client only)

Respond with ONLY valid JSON in this exact format:
{{
  "category": "...",
  "priority": "...",
  "action_taken": "DRAFT_REPLY|ARCHIVED|FLAGGED|UNSUBSCRIBE",
  "draft_reply": "...(full email reply text, or empty string if no reply needed)",
  "draft_subject": "Re: {email_data['subject']}",
  "slack_alert": true/false,
  "slack_message": "...(brief alert message if slack_alert is true, else empty string)",
  "notes": "...(brief reasoning)"
}}"""

        response = client.messages.create(
            model=CONFIG["model"],
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        result = json.loads(response.content[0].text)
        return result

    except json.JSONDecodeError as e:
        logger.error(f"Claude returned invalid JSON: {e}")
        return {
            "category": "FYI",
            "priority": "LOW",
            "action_taken": "ARCHIVED",
            "draft_reply": "",
            "slack_alert": False,
            "notes": "Parse error — manual review needed"
        }
    except Exception as e:
        logger.error(f"Claude API call failed: {e}")
        return None


def save_draft_to_gmail(service, email_data, analysis):
    """Save a draft reply to Gmail."""
    try:
        if not analysis.get('draft_reply'):
            return None

        message = MIMEText(analysis['draft_reply'])
        message['to'] = email_data['from']
        message['subject'] = analysis.get('draft_subject', f"Re: {email_data['subject']}")

        raw_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode('utf-8')

        draft = service.users().drafts().create(
            userId='me',
            body={
                'message': {
                    'raw': raw_message,
                    'threadId': email_data['id']
                }
            }
        ).execute()

        logger.info(f"Draft saved: '{message['subject']}'")
        return draft['id']

    except Exception as e:
        logger.error(f"Failed to save draft: {e}")
        return None


def send_slack_alert(message):
    """Send urgent alert to Slack."""
    try:
        import requests
        if not CONFIG["slack_webhook"]:
            logger.warning("Slack webhook not configured — skipping alert")
            return

        payload = {
            "text": f"🚨 *Inbox Guardian Alert*\n{message}",
            "username": "Inbox Guardian",
            "icon_emoji": ":email:"
        }

        response = requests.post(CONFIG["slack_webhook"], json=payload, timeout=5)
        if response.status_code == 200:
            logger.info("Slack alert sent")
        else:
            logger.error(f"Slack alert failed: {response.status_code}")

    except Exception as e:
        logger.error(f"Slack alert error: {e}")


def mark_email_as_read(service, email_id):
    """Mark email as read in Gmail."""
    try:
        service.users().messages().modify(
            userId='me',
            id=email_id,
            body={'removeLabelIds': ['UNREAD']}
        ).execute()
    except Exception as e:
        logger.error(f"Could not mark email as read: {e}")


def main():
    """Main execution — process unread emails."""
    parser = argparse.ArgumentParser(description='Inbox Guardian Agent')
    parser.add_argument('--dry-run', action='store_true', help='Preview without making changes')
    parser.add_argument('--limit', type=int, default=CONFIG["max_emails"], help='Max emails to process')
    args = parser.parse_args()

    logger.info("=" * 50)
    logger.info("Inbox Guardian — Starting run")
    logger.info(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    logger.info("=" * 50)

    # Ensure log directory exists
    os.makedirs('logs', exist_ok=True)

    # Connect to Gmail
    service = get_gmail_service()

    # Fetch emails
    emails = fetch_unread_emails(service, limit=args.limit)

    if not emails:
        logger.info("No unread emails found. Inbox is clean! ✅")
        return

    # Process each email
    stats = {"client": 0, "hot_lead": 0, "warm_lead": 0, "urgent": 0,
             "admin": 0, "newsletter": 0, "spam": 0, "fyi": 0,
             "drafts_created": 0, "slack_alerts": 0}

    results = []

    for i, email in enumerate(emails, 1):
        logger.info(f"Processing {i}/{len(emails)}: '{email['subject'][:60]}'")

        analysis = analyze_email_with_claude(email)
        if not analysis:
            logger.warning(f"Skipping email {email['id']} — analysis failed")
            continue

        category = analysis.get('category', 'FYI').lower()
        stats[category] = stats.get(category, 0) + 1

        # Save draft if needed
        if analysis.get('draft_reply') and not args.dry_run:
            draft_id = save_draft_to_gmail(service, email, analysis)
            if draft_id:
                stats["drafts_created"] += 1
                analysis['draft_id'] = draft_id

        # Send Slack alert if urgent
        if analysis.get('slack_alert') and not args.dry_run:
            send_slack_alert(
                f"*{analysis.get('category')}* from {email['from']}\n"
                f"Subject: {email['subject']}\n"
                f"Note: {analysis.get('notes', '')}"
            )
            stats["slack_alerts"] += 1

        # Mark as read (so we don't process again)
        if not args.dry_run:
            mark_email_as_read(service, email['id'])

        results.append({**email, **analysis})

    # Print summary
    logger.info("\n" + "=" * 50)
    logger.info("INBOX GUARDIAN SUMMARY")
    logger.info("=" * 50)
    logger.info(f"Emails processed: {len(emails)}")
    logger.info(f"Clients: {stats['client']} | Hot Leads: {stats['hot_lead']} | "
                f"Warm Leads: {stats['warm_lead']}")
    logger.info(f"Urgent: {stats['urgent']} | Admin: {stats['admin']} | "
                f"Newsletter: {stats['newsletter']} | Spam: {stats['spam']}")
    logger.info(f"Drafts created: {stats['drafts_created']}")
    logger.info(f"Slack alerts sent: {stats['slack_alerts']}")
    logger.info("=" * 50)

    # Save results to JSON for review
    output_file = f"logs/inbox_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    logger.info(f"Full results saved to: {output_file}")


if __name__ == "__main__":
    main()
