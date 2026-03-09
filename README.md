# WeChat Official Account Auto-Writing System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Automated writing and publishing system for WeChat Official Accounts (微信公众号). Features multiple themes, smart recommendations, and a complete content workflow.

## Features

- **Two Writing Modes**: Auto (full automatic) and Guided (semi-automatic)
- **8 Built-in Themes**: Minimal Business, Warm Artistic, Tech Modern, Fresh Lively, Magazine Premium, Academic Professional, Retro Classic, Dark Minimal
- **Smart Theme Recommendation**: Auto-suggests best theme based on content keywords
- **Content Validation**: Identifies facts needing verification
- **Cover Generation**: HTML-based 2x HD cover images
- **One-Click Draft Push**: Direct publishing to WeChat Official Account

## Quick Start

### Prerequisites

- Python 3.8 or higher
- WeChat Official Account (公众号) with API access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/wechat-allauto-gzh.git
cd wechat-allauto-gzh
```

2. Install dependencies:
```bash
pip install requests
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your WeChat credentials
```

### Usage

#### Auto Writing Mode
```bash
python3 scripts/write_article.py "AI Development Trends"
python3 scripts/write_article.py "Coffee Culture" --words 2000
```

#### Guided Writing Mode
```bash
python3 scripts/write_article.py "Coffee Culture" --mode guided --style life --words 1500
```

#### Push Draft
```bash
python3 scripts/push_draft.py --file _drafts/article.html --title "Article Title"
python3 scripts/push_draft.py --list-themes  # View all themes
```

## Themes

| `minimal_business` | Business, Career, Management |
| `warm_artistic` | Lifestyle, Emotion, Books |
| `tech_modern` | Tech, Programming, Digital |
| `fresh_lively` | Food, Travel, Lifestyle |
| `magazine_premium` | Fashion, Art, Deep Reading |
| `academic_professional` | Academic Papers, Research |
| `retro_classic` | History, Culture, Memoirs |
| `dark_minimal` | Gaming, Anime, Night Reading |

## Configuration

### Required Environment Variables

| Variable | Description |
|----------|-------------|
| `WECHAT_APP_ID` | WeChat Official Account AppID |
| `WECHAT_APP_SECRET` | WeChat Official Account AppSecret |

### Optional Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Claude API for AI writing |
| `OPENAI_API_KEY` | OpenAI API for AI writing |
| `TAVILY_API_KEY` | Tavily API for content search |

## Project Structure

```
wechat-allauto-gzh/
├── SKILL.md                    # Skill definition
├── scripts/                    # Python scripts
│   ├── write_article.py        # Main writing flow
│   ├── outline_generator.py    # Outline generator
│   ├── html_writer.py          # HTML writer
│   ├── content_validator.py    # Content validator
│   ├── markdown_to_wechat_html.py  # Theme system
│   ├── push_draft.py           # Push draft to WeChat
│   └── generate_covers.py      # Cover generator
├── references/                 # Documentation
├── .env.example               # Environment template
└── LICENSE                    # MIT License
```

## Using with OpenCode

This project follows the [Agent Skills Standard](https://agentskills.io). Users can install it directly:

```bash
npx openskills install YOUR_USERNAME/wechat-allauto-gzh
```

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- WeChat Official Account API
- Content Pipeline project for design inspiration
- Agent Skills Standard for skill specification