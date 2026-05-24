# NOTION DATABASE STRUCTURE
## 500 Claude Code Prompts — Notion Template Guide

---

## HOW TO SET UP THE NOTION DATABASE

### Step 1: Create a New Database
1. Open Notion
2. New page → Database → Full page (Table view)
3. Name it: "Claude Prompts Library"

### Step 2: Add These Properties

| Property Name | Type | Options/Notes |
|---------------|------|---------------|
| **Prompt Name** | Title | Main name/description of prompt |
| **Prompt Number** | Number | 1-500 |
| **Category** | Select | See categories below |
| **Subcategory** | Select | See subcategories below |
| **The Prompt** | Text | Full prompt text (copy-paste ready) |
| **Use Case** | Text | When to use this prompt |
| **Best Model** | Select | Haiku / Sonnet / Opus |
| **Output Type** | Multi-select | Email, Blog, Script, Analysis, etc. |
| **Difficulty** | Select | Beginner / Intermediate / Advanced |
| **My Rating** | Select | ⭐ / ⭐⭐ / ⭐⭐⭐ / ⭐⭐⭐⭐ / ⭐⭐⭐⭐⭐ |
| **Notes** | Text | Personal notes on how to improve it |
| **Last Used** | Date | Track when you last used it |
| **Times Used** | Number | How often you've used it |
| **Tags** | Multi-select | Keywords for searching |

---

### Category Options:
- 📧 Email & Communication
- 💰 Sales & Marketing  
- ✍️ Content Creation
- 🏢 Business Operations
- 🤖 AI & Automation
- 📋 Notion & Productivity

### Subcategory Options:
- Client Emails
- Cold Outreach
- Team Communication
- Sales Pages & Copy
- Email Marketing
- Social Media
- Blog & Articles
- Video Scripts
- Strategy & Planning
- Finance & Legal
- Claude Optimization
- Python Scripts
- Automation Workflows
- Notion Systems
- Personal Productivity

### Best Model Options:
- ⚡ Haiku (fast, simple tasks)
- 🎯 Sonnet (balanced)
- 🔥 Opus (complex reasoning)

### Output Type Options:
- Email
- Blog Post
- Social Post
- Script/Copy
- Analysis
- Template
- Code/Script
- Strategy Doc
- System Design
- Summary

---

## RECOMMENDED VIEWS TO CREATE

### View 1: Full Library (default table view)
- Show all properties
- Sort by: Prompt Number (ascending)
- Filter: None (see all)

### View 2: By Category (Board view)
- Group by: Category
- Show: Prompt Name + Subcategory + My Rating
- Use this to browse by type of task

### View 3: My Favorites (Gallery view)
- Filter: My Rating = ⭐⭐⭐⭐⭐ or ⭐⭐⭐⭐
- Gallery shows: Prompt Name + Category + Use Case
- Use this for your most-used prompts

### View 4: Quick Search (Table view)
- Show: Prompt Number, Prompt Name, Category, The Prompt
- Sort by: Times Used (descending)
- Filter: None
- This is your "search by scrolling" view

### View 5: Recently Used (Table view)
- Sort by: Last Used (descending)
- Show: All key properties
- Filter: Last Used is not empty

### View 6: By Task Today (Filtered view)
- Filter: Category = [whichever you need today]
- Sort by: My Rating (descending)
- Switch filters as needed for quick access

---

## SAMPLE DATABASE ENTRIES (Copy These In)

### Entry 1:
| Field | Value |
|-------|-------|
| Prompt Name | Cold Outreach Email |
| Number | 14 |
| Category | Email & Communication |
| Subcategory | Cold Outreach |
| Use Case | When reaching out to new prospects cold |
| Best Model | Sonnet |
| Output Type | Email |
| Difficulty | Beginner |
| Tags | sales, outreach, email, lead generation |

### Entry 2:
| Field | Value |
|-------|-------|
| Prompt Name | Full Sales Page |
| Number | 53 |
| Category | Sales & Marketing |
| Subcategory | Sales Pages & Copy |
| Use Case | When launching a new product or service |
| Best Model | Opus |
| Output Type | Script/Copy |
| Difficulty | Intermediate |
| Tags | sales, landing page, conversion, copywriting |

---

## HOW TO IMPORT ALL 500 PROMPTS

### Option A: Manual Import (Best for Notion Free)
1. Open the PDF
2. Copy each prompt into its own Notion row
3. Fill in properties as you go
4. Do 50-100 per session (takes ~2-3 hours total)

### Option B: CSV Import
1. I've included a CSV file in your download: `prompts-database.csv`
2. In Notion: + New page → Import → CSV
3. Map columns to properties
4. All 500 prompts import in seconds

### Option C: Notion API (Advanced)
If you're comfortable with Python, use the included `import_to_notion.py` script to auto-import all 500 prompts via the Notion API.

---

## TIPS FOR GETTING THE MOST FROM YOUR PROMPT LIBRARY

**Build Your Personal Ratings System:**
Rate prompts as you use them. After 30 days, you'll have a personalized "top 50" that actually fits your workflow.

**Add Your Customizations:**
When you modify a prompt and it works better, update the Notes field with your version. Your personalized prompt beats the generic one every time.

**Create Your Own Category:**
Add a "My Custom Prompts" category for the prompts you create yourself based on what you learn here.

**Weekly Prompt Review:**
Every Monday, pick one new category to explore. Spend 15 minutes trying 3-5 new prompts. Your prompt skills will compound fast.

**Share What Works:**
If you find a prompt that changes your business, share it in our community [Community Link]. You'll get better prompts back.
