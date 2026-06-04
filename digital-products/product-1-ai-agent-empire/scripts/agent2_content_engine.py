#!/usr/bin/env python3
"""
Script: Agent 2 — The Content Engine
Purpose: Generate daily blog posts, social media content, and weekly newsletters using Claude AI
Business: AI Agent Empire Product

Usage:
    python agent2_content_engine.py                      # Generate all content for today
    python agent2_content_engine.py --type blog          # Blog post only
    python agent2_content_engine.py --type social        # Social posts only
    python agent2_content_engine.py --type newsletter    # Weekly newsletter only
    python agent2_content_engine.py --topic "AI tools"   # Generate for specific topic
"""

import os
import sys
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [ContentEngine] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'logs/content_engine_{datetime.now().strftime("%Y%m%d")}.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# CONFIGURATION — Customize for your business
# ─────────────────────────────────────────────
CONFIG = {
    "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
    "business_name": os.getenv("BUSINESS_NAME", "My Business"),
    "business_niche": os.getenv("BUSINESS_NICHE", "AI automation for entrepreneurs"),
    "target_audience": os.getenv("TARGET_AUDIENCE", "Small business owners who want to automate"),
    "brand_voice": os.getenv("BRAND_VOICE", "Practical, no-fluff, expert, slightly informal"),
    "website_url": os.getenv("WEBSITE_URL", "https://yourbusiness.com"),
    "owner_name": os.getenv("OWNER_NAME", "Business Owner"),
    "model": "claude-opus-4-7",  # Best quality for content creation
    "output_dir": "./content",
}

# Content pillars — rotate through these
CONTENT_PILLARS = [
    os.getenv("PILLAR_1", "AI automation for small business"),
    os.getenv("PILLAR_2", "Productivity tools and systems"),
    os.getenv("PILLAR_3", "Entrepreneurship and business growth"),
    os.getenv("PILLAR_4", "Success stories and case studies"),
    os.getenv("PILLAR_5", "Industry trends and AI news"),
]

# Day of week → pillar mapping
DAY_PILLAR_MAP = {
    0: CONTENT_PILLARS[0],  # Monday
    1: CONTENT_PILLARS[1],  # Tuesday
    2: CONTENT_PILLARS[2],  # Wednesday
    3: CONTENT_PILLARS[3],  # Thursday
    4: CONTENT_PILLARS[4],  # Friday
    5: CONTENT_PILLARS[0],  # Saturday (repurpose)
    6: CONTENT_PILLARS[2],  # Sunday (personal/story)
}


def get_todays_topic():
    """Get the content topic for today based on pillar rotation."""
    day_of_week = datetime.now().weekday()
    return DAY_PILLAR_MAP.get(day_of_week, CONTENT_PILLARS[0])


def generate_blog_post(topic, keyword=None):
    """Generate a full SEO-optimized blog post on the given topic."""
    import anthropic
    client = anthropic.Anthropic(api_key=CONFIG["anthropic_api_key"])

    keyword = keyword or topic
    today = datetime.now().strftime("%B %d, %Y")

    logger.info(f"Generating blog post on: {topic}")

    prompt = f"""You are a professional content writer for {CONFIG['business_name']},
a {CONFIG['business_niche']} company.

Write a complete, SEO-optimized blog post with these specifications:

TOPIC: {topic}
PRIMARY KEYWORD: {keyword}
TARGET AUDIENCE: {CONFIG['target_audience']}
BRAND VOICE: {CONFIG['brand_voice']}
DATE: {today}

REQUIREMENTS:
- Length: 1,400-1,800 words
- Structure: H1 → Hook intro → 5 H2 sections → Conclusion with CTA
- Include primary keyword in H1, intro paragraph, 2-3 H2s
- Flesch-Kincaid grade 8 or lower (simple, clear language)
- Include at least 2 specific examples or statistics
- End with CTA linking to: {CONFIG['website_url']}
- Write as a human expert, not an AI assistant
- No fluff intros ("In today's world...")

Also provide:
- META_DESCRIPTION (150-160 chars, includes keyword)
- SLUG (URL-friendly version of title)
- INTERNAL_LINK_SUGGESTIONS: 3 topic ideas to internally link to
- TAGS: 5-8 relevant tags/categories

Format your response as:
---TITLE---
[H1 title here]
---META---
[meta description here]
---SLUG---
[url-slug-here]
---TAGS---
[tag1, tag2, tag3]
---CONTENT---
[Full markdown blog post here]
---INTERNAL_LINKS---
[List 3 internal link suggestions]
---END---"""

    response = client.messages.create(
        model=CONFIG["model"],
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )

    return parse_blog_response(response.content[0].text, topic)


def generate_social_posts(topic, blog_title=None):
    """Generate platform-specific social media posts."""
    import anthropic
    client = anthropic.Anthropic(api_key=CONFIG["anthropic_api_key"])

    logger.info(f"Generating social posts for: {topic}")

    prompt = f"""Create social media posts for {CONFIG['business_name']} about: {topic}

Business niche: {CONFIG['business_niche']}
Target audience: {CONFIG['target_audience']}
Brand voice: {CONFIG['brand_voice']}
{f'Related blog post: {blog_title}' if blog_title else ''}

Generate posts for each platform in this EXACT format:

---LINKEDIN---
[150-250 word LinkedIn post. Start with a bold hook line. Use short paragraphs.
End with a question or soft CTA. Professional but personal tone.]

---TWITTER_THREAD---
[Tweet 1/7: Hook tweet under 240 chars]
[Tweet 2/7: ...]
[Tweet 3/7: ...]
[Tweet 4/7: ...]
[Tweet 5/7: ...]
[Tweet 6/7: ...]
[Tweet 7/7: CTA tweet]

---INSTAGRAM---
[Caption: 150-200 word caption. First line is the hook (shows before More).
Then value content. End with 12 hashtags on new lines starting with #]

---FACEBOOK---
[100-150 word casual post. Include a question to drive comments.]

---END---"""

    response = client.messages.create(
        model=CONFIG["model"],
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )

    return parse_social_response(response.content[0].text)


def generate_newsletter(week_number=None):
    """Generate weekly email newsletter."""
    import anthropic
    client = anthropic.Anthropic(api_key=CONFIG["anthropic_api_key"])

    week_num = week_number or datetime.now().isocalendar()[1]
    logger.info(f"Generating newsletter for week {week_num}")

    prompt = f"""Write a weekly email newsletter for {CONFIG['business_name']}.

Business: {CONFIG['business_niche']}
Audience: {CONFIG['target_audience']}
Voice: {CONFIG['brand_voice']}
Sender: {CONFIG['owner_name']}
Week: {week_num} of {datetime.now().year}

Newsletter requirements:
- Feel personal, like it's from a friend who happens to be an expert
- Main insight/tip they can use this week (300-400 words)
- "Tool of the week" section (1 relevant tool + how to use it)
- "Worth reading" (2 links to suggest — use placeholder [LINK] if needed)
- A question at the end to drive replies
- Compelling subject line under 50 characters

Format:
---SUBJECT---
[Email subject line]
---PREVIEW---
[Preview text (90 chars max)]
---BODY---
[Full newsletter body in HTML-friendly markdown]
---END---"""

    response = client.messages.create(
        model=CONFIG["model"],
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )

    return parse_newsletter_response(response.content[0].text)


def parse_blog_response(text, topic):
    """Parse Claude's blog post response into structured data."""
    result = {
        "type": "blog",
        "topic": topic,
        "title": "",
        "meta_description": "",
        "slug": "",
        "tags": [],
        "content": "",
        "internal_links": [],
        "generated_at": datetime.now().isoformat(),
    }

    sections = {
        "TITLE": "title",
        "META": "meta_description",
        "SLUG": "slug",
        "TAGS": "tags",
        "CONTENT": "content",
        "INTERNAL_LINKS": "internal_links",
    }

    current_section = None
    current_content = []

    for line in text.split('\n'):
        matched = False
        for marker, field in sections.items():
            if line.strip() == f"---{marker}---":
                if current_section and current_content:
                    value = '\n'.join(current_content).strip()
                    if current_section == "tags":
                        result[current_section] = [t.strip() for t in value.split(',')]
                    elif current_section == "internal_links":
                        result[current_section] = [l.strip() for l in value.split('\n') if l.strip()]
                    else:
                        result[current_section] = value
                current_section = field
                current_content = []
                matched = True
                break
        if not matched and line.strip() != "---END---" and current_section:
            current_content.append(line)

    # Handle last section
    if current_section and current_content:
        value = '\n'.join(current_content).strip()
        if current_section == "tags":
            result[current_section] = [t.strip() for t in value.split(',')]
        else:
            result[current_section] = value

    return result


def parse_social_response(text):
    """Parse Claude's social media response."""
    result = {
        "type": "social",
        "linkedin": "",
        "twitter_thread": [],
        "instagram": "",
        "facebook": "",
        "generated_at": datetime.now().isoformat(),
    }

    current_platform = None
    current_content = []

    platform_map = {
        "LINKEDIN": "linkedin",
        "TWITTER_THREAD": "twitter_thread",
        "INSTAGRAM": "instagram",
        "FACEBOOK": "facebook",
    }

    for line in text.split('\n'):
        matched = False
        for marker, field in platform_map.items():
            if line.strip() == f"---{marker}---":
                if current_platform and current_content:
                    content = '\n'.join(current_content).strip()
                    if current_platform == "twitter_thread":
                        result[current_platform] = [t.strip() for t in content.split('\n') if t.strip()]
                    else:
                        result[current_platform] = content
                current_platform = field
                current_content = []
                matched = True
                break
        if not matched and line.strip() != "---END---" and current_platform:
            current_content.append(line)

    if current_platform and current_content:
        content = '\n'.join(current_content).strip()
        if current_platform == "twitter_thread":
            result[current_platform] = [t.strip() for t in content.split('\n') if t.strip()]
        else:
            result[current_platform] = content

    return result


def parse_newsletter_response(text):
    """Parse Claude's newsletter response."""
    result = {
        "type": "newsletter",
        "subject": "",
        "preview_text": "",
        "body": "",
        "generated_at": datetime.now().isoformat(),
    }

    sections = {
        "SUBJECT": "subject",
        "PREVIEW": "preview_text",
        "BODY": "body",
    }

    current_section = None
    current_content = []

    for line in text.split('\n'):
        matched = False
        for marker, field in sections.items():
            if line.strip() == f"---{marker}---":
                if current_section and current_content:
                    result[current_section] = '\n'.join(current_content).strip()
                current_section = field
                current_content = []
                matched = True
                break
        if not matched and line.strip() != "---END---" and current_section:
            current_content.append(line)

    if current_section and current_content:
        result[current_section] = '\n'.join(current_content).strip()

    return result


def save_content(content_data, output_dir):
    """Save generated content to files."""
    today = datetime.now().strftime("%Y-%m-%d")
    base_dir = Path(output_dir)

    if content_data["type"] == "blog":
        save_dir = base_dir / "blog"
        save_dir.mkdir(parents=True, exist_ok=True)
        slug = content_data.get("slug", "post").replace(" ", "-").lower()
        filename = f"{today}-{slug}.md"
        filepath = save_dir / filename

        with open(filepath, 'w') as f:
            f.write(f"---\n")
            f.write(f"title: {content_data.get('title', '')}\n")
            f.write(f"date: {today}\n")
            f.write(f"meta_description: {content_data.get('meta_description', '')}\n")
            f.write(f"tags: {', '.join(content_data.get('tags', []))}\n")
            f.write(f"---\n\n")
            f.write(content_data.get("content", ""))

        logger.info(f"Blog post saved: {filepath}")
        return filepath

    elif content_data["type"] == "social":
        save_dir = base_dir / "social"
        save_dir.mkdir(parents=True, exist_ok=True)
        filepath = save_dir / f"{today}-social-posts.md"

        with open(filepath, 'w') as f:
            f.write(f"# Social Media Posts — {today}\n\n")
            f.write(f"## LinkedIn\n{content_data.get('linkedin', '')}\n\n")
            f.write(f"## Twitter Thread\n")
            for tweet in content_data.get('twitter_thread', []):
                f.write(f"- {tweet}\n")
            f.write(f"\n## Instagram\n{content_data.get('instagram', '')}\n\n")
            f.write(f"## Facebook\n{content_data.get('facebook', '')}\n")

        logger.info(f"Social posts saved: {filepath}")
        return filepath

    elif content_data["type"] == "newsletter":
        save_dir = base_dir / "newsletter"
        save_dir.mkdir(parents=True, exist_ok=True)
        week_num = datetime.now().isocalendar()[1]
        filepath = save_dir / f"week-{week_num}-newsletter.md"

        with open(filepath, 'w') as f:
            f.write(f"---\n")
            f.write(f"subject: {content_data.get('subject', '')}\n")
            f.write(f"preview: {content_data.get('preview_text', '')}\n")
            f.write(f"week: {week_num}\n")
            f.write(f"date: {today}\n")
            f.write(f"---\n\n")
            f.write(content_data.get("body", ""))

        logger.info(f"Newsletter saved: {filepath}")
        return filepath


def main():
    """Main execution — generate all content for today."""
    import argparse
    parser = argparse.ArgumentParser(description='Content Engine Agent')
    parser.add_argument('--type', choices=['blog', 'social', 'newsletter', 'all'],
                        default='all', help='Type of content to generate')
    parser.add_argument('--topic', type=str, help='Custom topic override')
    args = parser.parse_args()

    os.makedirs('logs', exist_ok=True)
    os.makedirs(CONFIG["output_dir"], exist_ok=True)

    logger.info("=" * 50)
    logger.info(f"Content Engine — {datetime.now().strftime('%A, %B %d %Y')}")
    logger.info("=" * 50)

    topic = args.topic or get_todays_topic()
    logger.info(f"Today's content topic: {topic}")

    generated_files = []

    if args.type in ['blog', 'all']:
        blog_data = generate_blog_post(topic)
        path = save_content(blog_data, CONFIG["output_dir"])
        generated_files.append(path)
        logger.info(f"✅ Blog post complete: '{blog_data.get('title', '')}'")

    if args.type in ['social', 'all']:
        social_data = generate_social_posts(topic)
        path = save_content(social_data, CONFIG["output_dir"])
        generated_files.append(path)
        logger.info("✅ Social posts complete")

    # Only generate newsletter on Thursdays (day 3)
    if args.type == 'newsletter' or (args.type == 'all' and datetime.now().weekday() == 3):
        newsletter_data = generate_newsletter()
        path = save_content(newsletter_data, CONFIG["output_dir"])
        generated_files.append(path)
        logger.info(f"✅ Newsletter complete: '{newsletter_data.get('subject', '')}'")

    logger.info("\n📁 Files generated today:")
    for f in generated_files:
        logger.info(f"   → {f}")
    logger.info("\nContent Engine run complete. ✅")


if __name__ == "__main__":
    main()
