# Image Translation Overview Generator

This tool analyzes image translation progress across all courses and generates an HTML report showing which images have been translated for each language.

## Features

- Analyzes all courses in the `courses/` directory
- Tracks image translations for 7 languages: **en, fr, es, it, de, ru, zh-Hant**
- Counts total images vs translated images per language
- Color-coded visualization:
  - 🟢 Green = 100% translated
  - 🟡 Yellow = 50-99% translated
  - 🟠 Orange = 1-49% translated
  - 🔴 Red = 0% translated
  - ⚫ Gray = N/A (no content or no images)

## How It Works

The script analyzes each course's markdown files and:

1. **Extracts image references** from markdown files (e.g., `![alt](path)`)
2. **Checks if images are translated** by looking for language code in the path
   - Translated: `assets/fr/001.webp` (contains `/fr/`)
   - Untranslated: `assets/001.webp` (no language code)
3. **Calculates translation percentage** for each language
4. **Generates color-coded HTML table** with statistics

### Translation Detection

An image is considered **translated** if its path contains the language code in one of these formats:
- `/en/`, `/fr/`, `/es/`, `/it/`, `/de/`, `/ru/`, `/zh-Hant/`
- `-en-`, `-fr-`, `-es-`, etc.
- `_en_`, `_fr_`, `_es_`, etc.

## Requirements

No external dependencies required - uses only Python standard library.

## Usage

```bash
cd scripts/image_translation_overview
python generate_report.py
```

Or from the project root:

```bash
python scripts/image_translation_overview/generate_report.py
```

## Output

The script generates `image_translation_overview.html` in the central `scripts/reports/` folder. Open it in your browser to view the interactive report.

## Report Structure

| Course | EN | FR | ES | IT | DE | RU | ZH-HANT |
|--------|----|----|----|----|----|----|---------|
| btc101 | 23/23 (100%) | 23/23 (100%) | 15/23 (65%) | ... | ... | ... | ... |

Each cell shows:
- **X/Y** = X translated images out of Y total images
- **Percentage** = Translation completion percentage
- **Color coding** = Visual indicator of translation status

## Example

For a course `btc101` with French translation:

**en.md:**
```markdown
![image](assets/en/001.webp)
![image](assets/en/002.webp)
```

**fr.md:**
```markdown
![image](assets/fr/001.webp)
![image](assets/fr/002.webp)
```

Result: **2/2 (100%)** 🟢 for both English and French

## Statistics

The report includes:
- Total courses analyzed
- Total images across all courses
- Overall translation percentage
- Per-language, per-course breakdown
