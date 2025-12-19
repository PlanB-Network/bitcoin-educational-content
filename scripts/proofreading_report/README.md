# Proofreading Dashboard

A comprehensive, self-contained HTML dashboard for tracking proofreading status across all Bitcoin Educational Content courses and tutorials.

## Overview

The dashboard provides:
- **Matrix Overview**: Visual table showing completion status for each content × language (like a progress heatmap)
- **Top Languages**: Statistics showing proofreading activity and contributors per language
- **Contribution Finder**: Interactive tool showing top 10 most-needed contributions
- **Leaderboards**: Separate rankings for course and tutorial contributors

## Files

- `generate_proofreading_dashboard.py` - Python script that generates the dashboard
- `proofreading_dashboard.html` - Generated dashboard (self-contained, no dependencies)

## Quick Start

### Generate the Dashboard

```bash
cd scripts/proofreading_report/
python3 generate_proofreading_dashboard.py
```

This will:
1. Parse all 34 courses from `../../courses/*/course.yml`
2. Parse all 277 tutorials from `../../tutorials/*/*/tutorial.yml`
3. Calculate proofreading status and contributor statistics
4. Generate `proofreading_dashboard.html` (approximately 1.9 MB)

### View the Dashboard

**Option 1: Open locally**
```bash
# Open in your default browser
xdg-open proofreading_dashboard.html

# Or manually open the file in any browser
firefox proofreading_dashboard.html
```

**Option 2: Upload to web server**
Simply upload `proofreading_dashboard.html` to any web hosting service. The file is completely self-contained and requires no server-side processing.

## Dashboard Features

### Section 1: Matrix Overview

A visual table showing completion status for all content across all languages (similar to the course overview table).

**Features:**
- **Content Type Selector**: Choose between Courses or Tutorials
- **Filters**:
  - Topic/Category: Filter by specific course topic or tutorial category
  - Difficulty: Beginner, Intermediate, Advanced, Expert, Wizard
  - Search: Find specific content by ID or name

**Matrix Display:**
- Each row represents a piece of content (course or tutorial)
- Each column represents a language
- Each cell shows:
  - Completion ratio (e.g., "31/31" = 31 sections complete out of 31)
  - Percentage (e.g., "100%")
  - Color coding:
    - 🟢 Green: 100% complete
    - 🟡 Yellow: Partially complete
    - 🔴 Red: 0% complete
    - ⚫ Gray: N/A (no content available in that language)

### Section 2: Top Languages by Proofreading Activity

A comprehensive table showing language statistics across all content:

**Display:**
- Language code and name
- Total proofreadings (number of content items with contributions in that language)
- Unique contributors (number of different people who contributed in that language)
- Sorted by total proofreadings (most active languages first)

**Purpose:**
- Identify which languages have the most activity
- See which languages have strong contributor communities
- Understand language diversity in the project

**Example:**
```
Language          Total Proofreadings    Unique Contributors
EN (English)      245                    45
FR (French)       198                    28
DE (German)       156                    18
```

### Section 3: Contribution Finder

Find where your contributions are most needed (limited to top 10 results):

**Filters:**
1. **Select Your Language**: Choose from 26 languages
2. **Content Type**: Courses | Tutorials | Both
3. **Topic/Category**: Filter by specific topics or categories
4. **Difficulty**: Filter by content difficulty level

**Results Display:**
- Ranked by urgency (Status 0 first) and reward amount
- Shows for each item:
  - Content name and ID
  - Current status badge
  - Difficulty level badge
  - Contributors needed (3 - current count)
  - Available reward
  - Last update date

**Status Meanings:**
- 🔴 **Status 0**: No contributors (urgent)
- 🟠 **Status 1**: One contributor (needs review)
- 🟡 **Status 2**: Two contributors (in progress)
- 🟢 **Status 3**: Three or more contributors (complete)

### Section 4: Leaderboards

**Two Separate Leaderboards:**

**1. Top Course Contributors**
- Top 20 contributors ranked by course contributions
- Shows: GitHub avatar, username, course count, languages
- Medals for top 3 (🥇🥈🥉)

**2. Top Tutorial Contributors**
- Top 20 contributors ranked by tutorial contributions
- Shows: GitHub avatar, username, tutorial count, languages
- Medals for top 3 (🥇🥈🥉)

**Excluded Contributors:**
The following contributors are excluded from leaderboards (as requested):
- LoicPandul
- Asi0Flammeus
- heyolaniran
- Pivii
- PaoloFoti

## Data Structure

### Status Calculation

Status is calculated based on the number of contributors:
```python
contributors_count = 0  →  status = 0  (No contributors)
contributors_count = 1  →  status = 1  (One contributor)
contributors_count = 2  →  status = 2  (Two contributors)
contributors_count ≥ 3  →  status = 3  (Complete)
```

### Completion Calculation

For the matrix view, completion is calculated by counting sections/parts:
- Total parts: Number of sections in the content (counted from markdown headers)
- Completed parts: Total parts if status = 3, otherwise 0
- Percentage: (completed_parts / total_parts) × 100

### Embedded Data Format

The dashboard embeds a complete dataset as a JavaScript constant:

```javascript
const PROOFREADING_DATA = {
  "metadata": {
    "generated_at": "2025-11-03T13:04:00+00:00",
    "total_courses": 34,
    "total_tutorials": 277,
    "total_languages": 26,
    "excluded_contributors": ["LoicPandul", "Asi0Flammeus", ...]
  },
  "courses": [...],
  "tutorials": [...],
  "languages": [...],
  "topics": [...],
  "categories": [...],
  "course_contributor_stats": {...},
  "tutorial_contributor_stats": {...}
};
```

## Updating the Dashboard

To update the dashboard with the latest proofreading data:

```bash
cd scripts/proofreading_report/
python3 generate_proofreading_dashboard.py
```

**Important:** Each run completely regenerates the HTML file with fresh data from the YAML files.

### Update Frequency Recommendations

- **Daily**: For active development periods
- **Weekly**: For regular maintenance
- **After bulk changes**: When multiple proofreading entries are updated
- **Before presentations**: When showcasing project status

## Technical Details

### Requirements

**Python Dependencies:**
- Python 3.8+
- `PyYAML` (install: `pip install pyyaml`)

**No Browser Dependencies:**
- Pure HTML + CSS + JavaScript
- No external libraries or frameworks
- Works offline
- Compatible with all modern browsers

### File Size

The generated HTML file is approximately **1.9 MB** because it contains:
- Complete data for 311 content items (34 courses + 277 tutorials)
- 26 languages per item
- Section/part counting for matrix display
- Separate contributor statistics for courses and tutorials
- Embedded CSS and JavaScript
- All styling and functionality

### Performance

- **Initial Load**: < 2 seconds (local file or fast server)
- **Matrix Rendering**: Handles 300+ rows × 26 columns efficiently
- **Filtering**: Real-time, no lag
- **Content Type Switching**: Instant
- **Search**: Live search with no delay

### Browser Compatibility

Tested and working on:
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Key Improvements (v2.1)

### Matrix Overview
- ✅ Visual table format like image provided
- ✅ Content type selector (Courses vs Tutorials)
- ✅ Shows completion ratio (X/Y) and percentage based on actual quiz sections
- ✅ Color-coded cells (green/yellow/red/gray)
- ✅ Topic/category filter added
- ✅ Difficulty filter added
- ✅ **Alphabetical sorting** of all content

### Top Languages Section (NEW)
- ✅ **New section showing language statistics**
- ✅ Total proofreadings per language
- ✅ Unique contributors per language
- ✅ Sorted by proofreading activity (most active first)
- ✅ Excludes specified contributors from counts

### Contribution Finder
- ✅ Limited to top 10 results (instead of all)
- ✅ Difficulty filter added
- ✅ Shows difficulty level badge for each item

### Leaderboards
- ✅ Split into separate Course and Tutorial leaderboards
- ✅ Excludes specified contributors: LoicPandul, Asi0Flammeus, heyolaniran, Pivii, PaoloFoti
- ✅ Separate statistics tracking for courses vs tutorials

### Bug Fixes
- ✅ **Fixed completion counting**: Now counts actual quiz sections for courses
- ✅ Courses sorted alphabetically by ID
- ✅ Tutorials sorted alphabetically by ID

### File Organization
- ✅ Moved to dedicated `proofreading_report/` subfolder
- ✅ Clean separation from other scripts

## Customization

### Modifying Excluded Contributors

Edit the `EXCLUDED_CONTRIBUTORS` list in the Python script:

```python
EXCLUDED_CONTRIBUTORS = ['LoicPandul', 'Asi0Flammeus', 'heyolaniran', 'Pivii', 'PaoloFoti']
```

### Changing Top Results Limit

In the JavaScript section of `generate_html()`, find:

```javascript
// Limit to top 10
allItems = allItems.slice(0, 10);
```

Change `10` to any number you prefer.

### Modifying Status Calculation

Edit the `calculate_status` function in the Python script:

```python
def calculate_status(contributors):
    # Modify logic here
    pass
```

### Adding More Languages

Update the `LANGUAGE_NAMES` dictionary:

```python
LANGUAGE_NAMES = {
    'en': 'English',
    # Add more languages
}
```

## Troubleshooting

### Script Errors

**Error: `ModuleNotFoundError: No module named 'yaml'`**
```bash
pip install pyyaml
```

**Error: `FileNotFoundError: [Errno 2] No such file or directory`**
Ensure you're running the script from the `scripts/proofreading_report/` directory:
```bash
cd scripts/proofreading_report/
python3 generate_proofreading_dashboard.py
```

**Warning about deprecation**
The script uses modern `datetime.now(timezone.utc)` to avoid deprecation warnings.

### Dashboard Display Issues

**Matrix not rendering properly**
- Check browser console for JavaScript errors
- Verify the embedded data is valid JSON
- Try regenerating the dashboard

**Filters not working**
- Clear browser cache
- Try a different browser
- Regenerate the dashboard

**Content type selector not switching**
- Verify JavaScript is enabled in your browser
- Check browser console for errors

**GitHub avatars not loading**
- Normal behavior - uses fallback placeholder
- Check internet connection for GitHub CDN access
- Fallback to default avatar is automatic

## Statistics (Current)

Based on latest generation:

- **Total Courses**: 34
- **Total Tutorials**: 277
- **Total Content Items**: 311
- **Supported Languages**: 26
- **Course Contributors**: ~53 (after exclusions)
- **Tutorial Contributors**: ~33 (after exclusions)
- **Excluded Contributors**: 5 users

## Data Sources

All data is extracted from:
- `../../courses/*/course.yml` - Course metadata and proofreading info
- `../../tutorials/*/*/tutorial.yml` - Tutorial metadata and proofreading info

The script uses the `proofreading` section from each YAML file:

```yaml
proofreading:
  - language: fr
    last_contribution_date: 2025-08-18
    urgency: 1
    contributor_names:
      - Asi0Flammeus
      - ProfScofield21
    reward: 4.13
```

Additionally, the script counts sections/parts from the actual content markdown files to calculate completion percentages for the matrix view.

## License

Same as the main Bitcoin Educational Content repository.

## Support

For issues or questions:
1. Check this README
2. Review the Python script comments
3. Open an issue in the repository
4. Contact the development team

---

**Last Updated**: 2025-11-03
**Version**: 2.1
**Generated Dashboard Size**: ~1.9 MB
**Major Changes from v2.0**:
- **Fixed completion counting**: Now accurately counts quiz sections
- **Added Top Languages section**: Shows proofreading activity and contributors per language
- **Alphabetical sorting**: All content now sorted by ID
- Matrix overview with completion tracking
- Split leaderboards (courses vs tutorials)
- Limited contribution finder to top 10
- Added difficulty filters
- Excluded specific contributors from leaderboards
