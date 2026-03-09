---
name: wechat-article-writing-skill
description: |
  WeChat Official Account automated writing and publishing system. Use this skill when:
  - User needs to generate WeChat official account article drafts
  - User wants to switch between multiple formatting themes
  - User needs automated content production workflow
  - User wants to batch generate theme demonstration articles
  
  <example>User: "帮我写一篇关于人工智能的公众号文章"</example>
  <example>User: "Generate a WeChat article about coffee culture"</example>
  <example>User: "公众号文章排版，用科技主题"</example>
license: MIT
compatibility: agent-skills-standard
metadata:
  category: content-creation
  version: "2.0.0"
  tags: [wechat, writing, publishing, automation, themes]
---

# WeChat Official Account Auto-Writing Skill

Automated writing and publishing system for WeChat Official Accounts (公众号).

## When to Use

Load this skill when:
- User mentions "公众号", "微信文章", "写文章", "排版"
- User needs to create WeChat official account content
- User wants to format articles with professional themes
- User needs to push drafts to WeChat platform

## Quick Start

### 1. Auto Writing (Full Automatic)

```bash
# Quick article generation
python3 scripts/write_article.py "AI Development Trends"

# Specify word count
python3 scripts/write_article.py "AI Development Trends" --words 2000
```

### 2. Guided Writing (Semi-Automatic)

```bash
# Fine-grained control
python3 scripts/write_article.py "Coffee Culture" --mode guided --style life --words 1500
```

### 3. Push Draft

```bash
# Auto-recommend theme and push
python3 scripts/push_draft.py --file _drafts/article.html --title "Article Title"

# Specify theme
python3 scripts/push_draft.py --file _drafts/article.html --title "Article Title" --theme warm_artistic

# List all themes
python3 scripts/push_draft.py --list-themes
```

## Built-in Themes

### Classic Themes (8)

| Theme | Colors | Use Case | Design Features |
|-------|--------|----------|------------------|
| **minimal_business** | Blue-Black #1a1a2e + #0984e3 | Business, Career, Management | Professional, bottom border |
| **warm_artistic** | Gold #8b6914 + #fdf8f0 | Lifestyle, Emotion, Books | Soft, centered title |
| **tech_modern** | Dark #0d1117 + #58a6ff | Tech, Programming, Digital | GitHub style, code highlight |
| **fresh_lively** | Colorful #ff6b6b + #4ecdc4 | Food, Travel, Lifestyle | Youthful, rounded corners |
| **magazine_premium** | Black-White #1a1a1a + #c0a080 | Fashion, Art, Deep Reading | Elegant, generous whitespace |
| **academic_professional** | Navy #1a365d + #4299e1 | Academic Papers, Research | Rigorous, scholarly style |
| **retro_classic** | Sepia #5c3d2e + #c9a86c | History, Culture, Memoirs | Nostalgic, vintage feel |
| **dark_minimal** | Dark #1a202c + #63b3ed | Gaming, Anime, Night Reading | Dark theme with glow |

### Macaron Themes (12) - Soft Pastel Colors

| Theme | Colors | Use Case | Mood |
|-------|--------|----------|------|
| **macaron_pink** | Pink #fef6f9 + #d4859a | Emotion, Female, Romance | Sweet & Gentle |
| **macaron_blue** | Blue #f0f9ff + #4299e1 | Travel, Nature, Relax | Calm & Peaceful |
| **macaron_mint** | Mint #f0fdfa + #14b8a6 | Health, Eco, Fresh | Natural & Refreshing |
| **macaron_lavender** | Lavender #faf5ff + #a78bfa | Romance, Art, Dreamy | Elegant & Romantic |
| **macaron_peach** | Peach #fff7ed + #f97316 | Food, Dessert, Warm | Warm & Sweet |
| **macaron_lemon** | Lemon #fefce8 + #eab308 | Energy, Positive, Sunny | Bright & Vibrant |
| **macaron_coral** | Coral #fff5f5 + #f87171 | Passion, Summer, Beach | Warm & Energetic |
| **macaron_sage** | Sage #f0fdf4 + #4ade80 | Nature, Outdoor, Forest | Natural & Fresh |
| **macaron_lilac** | Lilac #fdf4ff + #d946ef | Elegant, Refined, Female | Sophisticated & Refined |
| **macaron_cream** | Cream #fffbeb + #d4a574 | Cozy, Home, Healing | Warm & Comfortable |
| **macaron_sky** | Sky #f0f9ff + #38bdf8 | Travel, Freedom, Dream | Fresh & Bright |
| **macaron_rose** | Rose #fdf2f8 + #ec4899 | Love, Romance, Elegant | Romantic & Exquisite |
### Smart Theme Recommendation

Automatic theme recommendation based on keyword matching:

```
"AI Development Trends" → tech_modern (confidence: 60%)
"Coffee Culture and Life" → warm_artistic (confidence: 75%)
"Business Strategy Analysis" → minimal_business (confidence: 80%)
```

## Complete Workflow

### Auto Writing Mode

```
User Input Topic
    ↓
[1] Analyze topic type → Keyword matching for article type
    ↓
[2] Generate search queries → Prepare search terms for content validation
    ↓
[3] Generate outline → Template-based section word count allocation
    ↓
[4] Auto write content → AI generates sections (requires API integration)
    ↓
[5] Convert to HTML → Apply theme styles, background blocks
    ↓
[6] Content validation → Identify facts needing verification
    ↓
[7] Save files → HTML + JSON outline
    ↓
[8] Push draft (optional) → Upload cover, create draft
```

## Configuration

### Required Environment Variables

Create a `.env` file based on `.env.example`:

```bash
# Required: WeChat Official Account credentials
WECHAT_APP_ID=your_app_id_here
WECHAT_APP_SECRET=your_app_secret_here

# Optional: AI Writing APIs
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key

# Optional: Search API for content validation
TAVILY_API_KEY=your_tavily_key
```

### Getting WeChat Credentials

1. Login to [WeChat Public Platform](https://mp.weixin.qq.com/)
2. Go to: Settings & Development → Basic Configuration
3. Copy `AppID` and `AppSecret`

## File Structure

```
wechat-allauto-gzh/
├── SKILL.md                    # This file
├── scripts/
│   ├── write_article.py        # Main writing flow
│   ├── outline_generator.py    # Outline generator
│   ├── html_writer.py          # HTML writer
│   ├── content_validator.py    # Content validator
│   ├── markdown_to_wechat_html.py  # Theme system
│   ├── push_draft.py           # Push draft to WeChat
│   ├── update_draft.py         # Update draft
│   └── generate_covers.py      # Cover generator
├── references/                 # Documentation
│   ├── WORKFLOW_DESIGN.md
│   ├── THEMES_GUIDE.md
│   └── SKILL_OVERVIEW.md
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
└── LICENSE                    # MIT License
```

## Core Modules

| File | Function |
|------|----------|
| `write_article.py` | Main writing flow, supports auto/guided modes |
| `outline_generator.py` | Outline generation, 5 article type templates |
| `html_writer.py` | HTML writing, compact mobile styles |
| `content_validator.py` | Content validation, fact identification |
| `markdown_to_wechat_html.py` | Theme system, CSS-in-Python architecture |
| `push_draft.py` | Draft push with auto theme recommendation |

## Article Structure Templates

**Technical Article:**
- Introduction (10%) → Background (15%) → Core Content (40%) → Case Study (20%) → Summary (15%)

**Business Analysis:**
- Phenomenon (10%) → Analysis (20%) → Deep Dive (35%) → Evidence (20%) → Trends (15%)

**Lifestyle Essay:**
- Opening (10%) → Personal Experience (25%) → Discussion (35%) → Tips (20%) → Closing (10%)

**Tutorial Guide:**
- Intro (10%) → Setup (15%) → Steps (50%) → FAQ (15%) → Summary (10%)

**Product Review:**
- Overview (10%) → First Impressions (15%) → Core Experience (40%) → Pros/Cons (20%) → Recommendation (15%)

## Adding New Themes

Edit `scripts/markdown_to_wechat_html.py`:

```python
THEME_PRESETS['my_theme'] = {
    'name': 'My Theme',
    'description': 'Theme description',
    'colors': {
        'primary': '#xxxxxx',
        'accent': '#xxxxxx',
        'background': '#ffffff',
        'text': '#333333'
    },
    'typography': {
        'h1': {...},
        'h2': {...},
    }
}
```

## Mobile Typography Optimization

### Core Principles

1. **Avoid margin stacking**
   ```css
   /* Correct: bottom margin only */
   p { margin: 0 0 16px 0; }
   ```

2. **Compact spacing**
   - Paragraph: 16px
   - Heading margin: 24px/20px
   - Blockquote padding: 12-16px

3. **Font sizes**
   - Body: 15-16px
   - H1: 19-22px
   - H2: 16-18px

## Dependencies

- Python 3.8+
- `requests` library
- WeChat Official Account API access
- Optional: Claude/OpenAI API for AI writing
- Optional: Tavily API for content search

---

**MIT License • Open Source**
