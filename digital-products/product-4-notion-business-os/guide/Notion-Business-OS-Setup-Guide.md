# NOTION BUSINESS OS
## The Complete Entrepreneur Workspace — Setup in One Day
### Price: $37 | Platform: Etsy + Gumroad

---

# WHAT YOU GET

A complete, ready-to-duplicate Notion workspace with 8 interconnected databases that run your entire business — CRM, projects, content calendar, financial tracker, meeting notes, SOPs, knowledge base, and goals dashboard.

**Duplicate once → customise in 2 hours → run forever.**

---

# THE 8 DATABASES

## 1. CLIENT CRM 🤝
**Purpose:** Track every client relationship from lead to payment

### Properties:
- Client Name (Title)
- Stage (Select): Lead → Qualified → Proposal Sent → Active → Completed → Lost
- Value (Number — currency)
- Contact Email (Email)
- Phone (Phone)
- Company (Text)
- Industry (Select): Tech / Healthcare / Retail / F&B / Real Estate / Education / Other
- Source (Select): LinkedIn / Referral / Gumroad / Etsy / Instagram / WhatsApp / Cold Outreach
- Next Action (Text)
- Next Action Date (Date)
- Last Contact (Date)
- Notes (Text)
- Projects (Relation → Projects DB)
- Total Paid (Rollup from Projects)
- Created (Created Time)

### Views:
1. **Pipeline** (Board view, grouped by Stage)
2. **This Week's Follow-ups** (Filter: Next Action Date = This Week)
3. **Active Clients** (Filter: Stage = Active)
4. **All Clients** (Table, sorted by Created)
5. **By Industry** (Board, grouped by Industry)

### Automations (set manually in Notion):
- When Stage changes to Active → create a new Project automatically
- When Next Action Date passes → move to "Follow Up Needed" view

---

## 2. PROJECT TRACKER 📋
**Purpose:** Manage every project from kick-off to invoice

### Properties:
- Project Name (Title)
- Client (Relation → CRM)
- Status (Select): Not Started → In Progress → Review → Completed → On Hold
- Priority (Select): 🔴 Urgent / 🟡 High / 🟢 Normal / ⚪ Low
- Start Date (Date)
- Deadline (Date)
- Budget (Number — currency)
- Invoiced (Checkbox)
- Payment Received (Checkbox)
- Invoice Amount (Number)
- Deliverables (Text)
- Tags (Multi-select): Design / Development / Strategy / Content / Automation
- Tasks (Relation → Tasks DB)
- Completion % (Formula: count of done tasks / total tasks × 100)
- Notes (Text)

### Views:
1. **Active Projects** (Board by Status)
2. **Calendar** (Calendar view by Deadline)
3. **Unpaid Invoices** (Filter: Invoiced = true, Payment Received = false)
4. **This Month** (Filter: Deadline = This Month)
5. **All Projects** (Table)

---

## 3. TASK MANAGER ✅
**Purpose:** Every task across all projects in one place

### Properties:
- Task (Title)
- Project (Relation → Projects)
- Client (Rollup from Project)
- Status (Select): To Do → In Progress → Review → Done → Cancelled
- Priority (Select): Urgent / High / Normal / Low
- Due Date (Date)
- Assigned To (Person)
- Time Estimate (Number — hours)
- Time Actual (Number — hours)
- Tags (Multi-select)
- Notes (Text)

### Views:
1. **My Tasks Today** (Filter: Due = Today, Assigned = Me)
2. **This Week** (Calendar by Due Date, this week)
3. **By Project** (Group by Project)
4. **Backlog** (Filter: Status = To Do, sorted by Priority)
5. **Done This Month** (Filter: Status = Done, this month)

---

## 4. CONTENT CALENDAR 📅
**Purpose:** Plan, write, schedule, and track all content

### Properties:
- Title (Title)
- Platform (Multi-select): LinkedIn / Instagram / Twitter/X / Facebook / TikTok / Blog / Newsletter / WhatsApp
- Status (Select): Idea → Writing → Ready → Scheduled → Published
- Format (Select): Post / Thread / Story / Reel / Article / Newsletter / Video
- Publish Date (Date)
- Published (Checkbox)
- Caption/Body (Text)
- Hook (Text)
- Hashtags (Text)
- Link (URL)
- Engagement (Number)
- Notes (Text)
- Repurpose From (Relation → self, for content repurposing)

### Views:
1. **This Week** (Calendar, filter: This Week)
2. **This Month** (Calendar, filter: This Month)
3. **By Platform** (Board, group by Platform)
4. **Pipeline** (Board, group by Status)
5. **Top Performers** (Table, sort by Engagement descending)
6. **Ideas Bank** (Filter: Status = Idea)

### Weekly Content Rhythm Template:
```
Monday:    LinkedIn educational post
Tuesday:   Instagram carousel or reel
Wednesday: Twitter/X thread
Thursday:  LinkedIn personal story
Friday:    Newsletter or long-form article
Saturday:  Instagram story (behind the scenes)
Sunday:    Plan next week's content
```

---

## 5. FINANCIAL DASHBOARD 💰
**Purpose:** Know your numbers — revenue, expenses, runway

### Revenue Tracker Properties:
- Description (Title)
- Date (Date)
- Amount (Number — currency)
- Category (Select): Product Sale / Client Payment / Refund / Other
- Platform (Select): Gumroad / Etsy / PayPal / Bank Transfer / Stripe / Cash
- Client/Product (Text)
- Invoice # (Text)
- Notes (Text)

### Expense Tracker Properties:
- Description (Title)
- Date (Date)
- Amount (Number — currency)
- Category (Select): Software / Marketing / Freelancers / Equipment / Education / Tax / Other
- Recurring (Checkbox)
- Recurring Frequency (Select): Monthly / Annual / One-time
- Vendor (Text)
- Receipt (Files)
- Notes (Text)

### Dashboard Views:
1. **This Month Revenue** (Sum formula, filter: This Month)
2. **This Month Expenses** (Sum, filter: This Month)
3. **Net Profit** (Formula: Revenue − Expenses)
4. **By Category** (Board, group by Category)
5. **Recurring Costs** (Filter: Recurring = true) — know your monthly burn
6. **Annual View** (Gallery by month)

### Financial KPIs (set up as database properties):
- Monthly Recurring Revenue (MRR)
- One-time Revenue
- Total Expenses
- Net Margin %
- Runway (months)

---

## 6. MEETING NOTES & CRM LOG 📝
**Purpose:** Every call, meeting, and conversation documented

### Properties:
- Title (Title — auto format: "Client Name - DD/MM/YY")
- Date (Date)
- Type (Select): Discovery Call / Check-in / Strategy Session / Sales Call / Internal / Networking
- Client (Relation → CRM)
- Duration (Number — minutes)
- Attendees (Multi-select → People)
- Summary (Text)
- Action Items (Text)
- Next Steps (Text)
- Follow-up Date (Date)
- Recording Link (URL)

### Views:
1. **This Week's Meetings** (Filter: This Week)
2. **Action Items Due** (Filter: Follow-up Date = Past, checked off = false)
3. **By Client** (Group by Client)
4. **All Meetings** (Table, sorted by Date descending)

---

## 7. SOP LIBRARY 📖
**Purpose:** Document every repeatable process once

### Properties:
- SOP Title (Title)
- Category (Select): Client Onboarding / Content / Finance / Operations / Sales / Tech / HR
- Status (Select): Draft / Active / Needs Update / Archived
- Owner (Person)
- Last Updated (Last Edited Time)
- Version (Number)
- Frequency (Select): Daily / Weekly / Monthly / Per Project / As Needed
- Tags (Multi-select)
- Content (Page content — write the full SOP here)

### Core SOPs to Write First (templates included):
1. Client Onboarding Checklist
2. Content Publishing Process
3. Invoice & Payment Process
4. New Project Kick-off
5. Weekly Review Routine
6. Monthly Financial Close
7. New Lead Qualification
8. Refund/Dispute Process

### Views:
1. **By Category** (Board)
2. **Needs Update** (Filter: Status = Needs Update)
3. **Most Used** (sorted by Frequency)
4. **All SOPs** (Table)

---

## 8. GOALS & OKRs DASHBOARD 🎯
**Purpose:** Quarterly and annual goals with progress tracking

### Properties:
- Goal (Title)
- Type (Select): Annual / Quarterly / Monthly / Weekly
- Quarter (Select): Q1 / Q2 / Q3 / Q4
- Year (Number)
- Status (Select): Not Started / In Progress / On Track / At Risk / Completed / Dropped
- Progress % (Number)
- Target (Number)
- Current (Number)
- Unit (Select): $ Revenue / # Clients / # Products / # Followers / Other
- Key Results (Text — 3 measurable outcomes)
- Notes (Text)
- Review Date (Date)

### Views:
1. **This Quarter** (Filter: current quarter, Board by Status)
2. **Annual Goals** (Filter: Type = Annual)
3. **Weekly Check-in** (Filter: Type = Weekly, this week)
4. **Progress Dashboard** (Gallery view with progress bars)

---

# SETUP GUIDE — DAY 1 CHECKLIST

## Hour 1: Duplicate the template
1. Open the Notion template link (in your download)
2. Click "Duplicate" in the top right
3. Choose your workspace
4. Rename it: "Your Business Name — OS"

## Hour 2: Populate your CRM
1. Add all current clients (even informal ones)
2. Set their Stage correctly
3. Add their contact info
4. Set Next Action + Next Action Date for each

## Hour 3: Add your projects
1. Add every active project
2. Link to the client in CRM
3. Set deadline and budget
4. Break into tasks and add to Task Manager

## Hour 4: Set up your finances
1. Add last month's revenue entries
2. Add all recurring monthly expenses
3. Calculate your actual MRR and monthly burn
4. Set your monthly revenue target in Goals

## Hour 5: Content calendar
1. Add all scheduled posts for next 7 days
2. Add your content ideas bank (aim for 20+)
3. Set your weekly content rhythm (use the template above)

## Hour 6: SOPs
1. Write your top 3 most-used processes
2. Start with: Client Onboarding, Invoice Process, Content Publishing

**After Day 1:** Your entire business is in one place. Every day starts with a 15-minute review of Tasks, CRM follow-ups, and Content Calendar.

---

# NOTION SETUP TIPS

## Linking databases (critical)
Every database should connect to at least one other:
- CRM ↔ Projects (bidirectional)
- Projects ↔ Tasks (bidirectional)
- Content Calendar → Client (for client content work)
- Meetings → CRM (log every call automatically)

## Formulas to add
```
Days Until Deadline:
dateBetween(prop("Deadline"), now(), "days")

Project Completion %:
round(divide(length(filter(prop("Tasks"), current.prop("Status") == "Done")), length(prop("Tasks"))) * 100)

Revenue This Month (in Financial DB):
```

## Templates within pages
In Notion, create page templates for:
- Weekly Review (every Sunday)
- Client Meeting Notes
- Project Kick-off
- Monthly Financial Close

## Integrations
Connect Notion to:
- **Slack** — get task notifications in Slack
- **Google Calendar** — sync deadlines and meetings
- **Zapier/Make** — auto-create CRM entries from form submissions
- **Claude AI (Agent 6)** — dump weekly analytics reports directly into your Goals dashboard

---

# QUICK-WIN WORKFLOWS

## Monday Morning (15 min)
1. Open Goals Dashboard → check progress
2. Open Task Manager → set today's priorities
3. Open CRM → check who needs follow-up this week
4. Open Content Calendar → review what's scheduled

## Friday Evening (20 min)
1. Mark completed tasks as Done
2. Update project progress %
3. Log this week's revenue in Financial Dashboard
4. Plan next week's content in Content Calendar
5. Write weekly review note in Goals

## Monthly Close (30 min)
1. Calculate total revenue and expenses
2. Check which goals are On Track / At Risk
3. Review CRM pipeline — move stuck deals
4. Archive completed projects
5. Update SOPs that changed

---

# WHAT'S INCLUDED IN YOUR DOWNLOAD

```
Notion-Business-OS/
├── Setup-Guide.pdf          ← This document
├── Template-Links.txt       ← Direct Notion duplication links
├── Quick-Start.pdf          ← 1-page cheat sheet
├── Formula-Reference.pdf   ← All Notion formulas pre-written
└── Video-Walkthroughs/
    ├── 01-CRM-Setup.txt     ← Loom script
    ├── 02-Projects-Setup.txt
    └── 03-Content-Calendar.txt
```

---

*Notion Business OS | $37 one-time | Works with free Notion account*
