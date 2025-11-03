# Markdown Translation Overview Generator

This tool analyzes markdown translation progress across all courses and generates an HTML report showing which language files exist for each course.

## Features

- Analyzes all courses in the `courses/` directory
- Auto-detects all supported languages from `btc101` folder
- Shows presence/absence of markdown files for each language
- Displays word count for existing translations
- Color-coded visualization:
  - 🟢 Green = Translation exists
  - 🔴 Red = Translation missing

## How It Works

The script:

1. **Detects supported languages** from `btc101` folder (reference course)
2. **Scans each course** for language-specific markdown files
3. **Counts content** (lines and words) for existing translations
4. **Generates HTML table** showing translation status

### Language Detection

Supported languages are automatically detected by scanning `.md` files in the `btc101` folder. Currently includes:

```
cs, de, en, es, et, fa, fi, fr, hi, id, it, ja, ko, nb-NO, nl,
pl, pt, rn, ru, si, sr-Latn, sv, sw, tr, vi, zh-Hans, zh-Hant
```

## Requirements

No external dependencies required - uses only Python standard library.

## Usage

```bash
cd scripts/md_translation_overview
python generate_report.py
```

Or from the project root:

```bash
python scripts/md_translation_overview/generate_report.py
```

## Output

The script generates `md_translation_overview.html` in the central `scripts/reports/` folder. Open it in your browser to view the interactive report.

## Report Structure

| Course | EN | FR | ES | ... | ZH-HANT |
|--------|----|----|----|----|---------|
| btc101 | ✓ 12,345w | ✓ 11,234w | ✓ 10,987w | ... | ✓ 9,876w |
| btc102 | ✓ 8,765w | ✗ | ✗ | ... | ✗ |

Each cell shows:
- **✓** = Translation exists (green)
- **✗** = Translation missing (red)
- **Word count** = Number of words in the file

## Statistics

The report includes:
- Total courses analyzed
- Total translations vs possible translations
- Overall translation percentage
- Per-language, per-course breakdown with word counts
