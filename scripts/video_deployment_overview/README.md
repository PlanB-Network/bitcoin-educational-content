# Video Deployment Overview Generator

This tool analyzes video deployment across all courses and generates an HTML report showing coverage by language and provider.

## Features

- Analyzes all courses in the `courses/` directory
- Tracks video deployment for 7 languages: **en, fr, es, it, de, ru, zh-Hant**
- Shows provider coverage: **YouTube**, **PeerTube**, or **Both**
- Color-coded visualization:
  - 🟢 Green = 100% coverage
  - 🟡 Yellow = 50-99% coverage
  - 🟠 Orange = 1-49% coverage
  - 🔴 Red = 0% coverage

## Requirements

```bash
pip install pyyaml
```

## Usage

```bash
cd scripts/video_deployment_overview
python generate_report.py
```

Or from the project root:

```bash
python scripts/video_deployment_overview/generate_report.py
```

## Output

The script generates `video_deployment_overview.html` in the central `scripts/reports/` folder. Open it in your browser to view the interactive report.

## How it Works

1. Scans all course directories in `courses/`
2. Parses each `course.yml` file
3. Extracts video IDs and provider URLs for each language
4. Aggregates coverage statistics
5. Generates color-coded HTML table with provider badges

## Report Structure

| Course | Total Videos | EN | FR | ES | IT | DE | RU | ZH-HANT |
|--------|-------------|----|----|----|----|----|----|---------|
| btc101 | 23 | ✅ | ✅ | 🟡 | 🟡 | 🔴 | 🔴 | 🔴 |

Each cell shows:
- Coverage fraction (e.g., 23/23)
- Coverage percentage (e.g., 100%)
- Provider badges:
  - **Y:X** = X videos on YouTube only
  - **P:X** = X videos on PeerTube only
  - **B:X** = X videos on both providers
