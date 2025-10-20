# Scripts Directory

This directory contains analysis and reporting tools for the Bitcoin Educational Content repository.

## 📊 Overview Report Generators

Three specialized tools analyze different aspects of course translations:

### 1. Video Deployment Overview
**Location:** `video_deployment_overview/`

Analyzes video coverage across courses and languages (YouTube/PeerTube providers).

- **Languages:** en, fr, es, it, de, ru, zh-Hant
- **Output:** Color-coded table showing video deployment by provider
- **Usage:** `python video_deployment_overview/generate_report.py`

### 2. Image Translation Overview
**Location:** `image_translation_overview/`

Tracks image translation progress by detecting language codes in image paths.

- **Languages:** en, fr, es, it, de, ru, zh-Hant
- **Output:** Visual report of translated vs untranslated images
- **Usage:** `python image_translation_overview/generate_report.py`

### 3. Markdown Translation Overview
**Location:** `md_translation_overview/`

Shows which markdown files exist for each course and language.

- **Languages:** Auto-detected from btc101 (27 languages)
- **Output:** Comprehensive table with word counts
- **Usage:** `python md_translation_overview/generate_report.py`

## 🚀 Quick Start

### Generate All Reports at Once

```bash
# From the scripts directory
cd scripts
python generate_all_reports.py
```

This single command will:
- ✅ Run all 3 report generators
- ✅ Create all 3 HTML reports
- ✅ Show summary of results
- ✅ Display file locations

### Generate Individual Reports

```bash
# Video deployment
python video_deployment_overview/generate_report.py

# Image translation
python image_translation_overview/generate_report.py

# Markdown translation
python md_translation_overview/generate_report.py
```

## 📁 Directory Structure

```
scripts/
├── generate_all_reports.py          # Master script (runs all 3)
├── README.md                         # This file
│
├── reports/                          # ⭐ All HTML reports go here
│   ├── video_deployment_overview.html
│   ├── image_translation_overview.html
│   └── md_translation_overview.html
│
├── video_deployment_overview/
│   ├── generate_report.py           # Video analysis script
│   └── README.md
│
├── image_translation_overview/
│   ├── generate_report.py           # Image analysis script
│   └── README.md
│
└── md_translation_overview/
    ├── generate_report.py           # Markdown analysis script
    └── README.md
```

## 🎨 Report Features

All reports include:
- **Color-coded visualization** for quick status assessment
- **Detailed statistics** (counts, percentages, totals)
- **Responsive tables** that work on all screen sizes
- **Auto-generated timestamps** to track when reports were created
- **Interactive legends** explaining the color schemes

### Color Coding

| Color | Meaning | Percentage Range |
|-------|---------|------------------|
| 🟢 Green | Complete | 100% |
| 🟡 Yellow | Partial | 50-99% |
| 🟠 Orange | Low | 1-49% |
| 🔴 Red | None/Missing | 0% |
| ⚫ Gray | N/A | No content |

## 📋 Requirements

- **Python 3.6+** (standard library only)
- **PyYAML** for video deployment analysis: `pip install pyyaml`

## 📍 Report Locations

All HTML reports are generated in a single location for easy access:

```
scripts/reports/
├── video_deployment_overview.html
├── image_translation_overview.html
└── md_translation_overview.html
```

Simply open the HTML files in your browser to view the reports.

## 🔄 Updating Reports

Reports are static HTML files generated from current course data. To update:

1. Make changes to course files (YAML, markdown, images)
2. Re-run the generator scripts
3. Refresh HTML files in browser

## 💡 Tips

- **Bookmark the HTML files** for quick access
- **Run after major updates** to track translation progress
- **Share reports** with translators to identify gaps
- **Use master script** for comprehensive analysis

## 🛠️ Customization

Each generator can be customized by editing:
- Language lists (in script constants)
- Color schemes (in HTML CSS)
- Statistics displayed (in generation logic)

See individual README files for script-specific details.

## 📝 Notes

- Video deployment analyzes `course.yml` files
- Image translation scans markdown for image references
- Markdown translation checks for `.md` file existence
- All scripts handle missing files gracefully
- Reports are self-contained HTML files (no external dependencies)
