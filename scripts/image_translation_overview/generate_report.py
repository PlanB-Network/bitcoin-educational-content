#!/usr/bin/env python3
"""
Image Translation Overview Generator

Analyzes image translation progress across all courses and languages.
Generates an HTML report showing translated vs untranslated images.

Usage:
    python generate_report.py

The HTML report will be saved in the same directory as this script.
"""

import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Languages to check
LANGUAGES = ['en', 'fr', 'es', 'it', 'de', 'ru', 'zh-Hant']

# Regex pattern to match markdown image references
IMAGE_PATTERN = re.compile(r'!\[.*?\]\((.*?)\)')

def get_courses_directory():
    """Get the courses directory path relative to this script."""
    script_dir = Path(__file__).parent.resolve()
    courses_dir = script_dir / '../../courses'
    return courses_dir.resolve()

def extract_images_from_markdown(md_file_path):
    """Extract all image references from a markdown file."""
    if not md_file_path.exists():
        return []

    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all image references
        images = IMAGE_PATTERN.findall(content)
        return images

    except Exception as e:
        print(f"⚠️  Error reading {md_file_path}: {e}")
        return []

def analyze_course_images(course_path):
    """Analyze image translation status for a course."""
    course_id = course_path.name

    # Check if course has markdown files
    md_files = list(course_path.glob('*.md'))
    if not md_files:
        return None

    analysis = {
        'course_id': course_id,
        'languages': {}
    }

    for lang in LANGUAGES:
        md_file = course_path / f'{lang}.md'

        if not md_file.exists():
            analysis['languages'][lang] = {
                'total_images': 0,
                'translated_images': 0,
                'percentage': 0,
                'exists': False
            }
            continue

        # Extract images from the markdown file
        images = extract_images_from_markdown(md_file)

        if not images:
            analysis['languages'][lang] = {
                'total_images': 0,
                'translated_images': 0,
                'percentage': 0,
                'exists': True
            }
            continue

        # Count translated images (those with language code in path)
        translated_count = 0
        for img_path in images:
            # Check if the image path contains the language code
            # Patterns: assets/en/, /en/, -en-, _en_, etc.
            if f'/{lang}/' in img_path or f'-{lang}-' in img_path or f'_{lang}_' in img_path:
                translated_count += 1

        percentage = (translated_count / len(images) * 100) if len(images) > 0 else 0

        analysis['languages'][lang] = {
            'total_images': len(images),
            'translated_images': translated_count,
            'percentage': percentage,
            'exists': True
        }

    return analysis

def generate_html_report(all_analyses, output_file):
    """Generate HTML report with color-coded table."""

    # Calculate summary statistics
    total_courses = len(all_analyses)
    total_images = sum(
        sum(data['total_images'] for data in analysis['languages'].values())
        for analysis in all_analyses
    )
    total_translated = sum(
        sum(data['translated_images'] for data in analysis['languages'].values())
        for analysis in all_analyses
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Translation Overview</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 10px;
        }}
        .stats {{
            margin: 20px auto;
            text-align: center;
            font-size: 14px;
            color: #666;
            max-width: 800px;
        }}
        .stats strong {{
            color: #333;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: center;
        }}
        th {{
            background-color: #9C27B0;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        th.course-header {{
            background-color: #673AB7;
            text-align: left;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        .translation-cell {{
            position: relative;
            min-width: 120px;
        }}
        .translation-complete {{
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }}
        .translation-partial {{
            background-color: #FFC107;
            color: black;
        }}
        .translation-low {{
            background-color: #FF9800;
            color: white;
        }}
        .translation-none {{
            background-color: #f44336;
            color: white;
        }}
        .translation-na {{
            background-color: #9E9E9E;
            color: white;
        }}
        .translation-info {{
            font-size: 12px;
            display: block;
            margin-top: 4px;
        }}
        .legend {{
            margin: 20px auto;
            padding: 15px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 900px;
        }}
        .legend h3 {{
            margin-top: 0;
            color: #333;
        }}
        .legend-item {{
            display: inline-block;
            margin: 5px 15px 5px 0;
        }}
        .legend-color {{
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-right: 5px;
            vertical-align: middle;
            border-radius: 3px;
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 20px;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        .header {{
            position: relative;
            padding: 20px 0;
        }}
        .back-button {{
            display: inline-block;
            padding: 8px 16px;
            background-color: #f7931a;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            transition: background-color 0.2s;
            margin-bottom: 20px;
        }}
        .back-button:hover {{
            background-color: #e08316;
        }}
        .back-button::before {{
            content: '← ';
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://surfer.planb.network/translation_report/index.html" class="back-button">Back to Reports</a>
            <h1>🖼️ Image Translation Overview</h1>
        </div>
        <div class="stats">
            <strong>Languages analyzed:</strong> {", ".join(LANGUAGES)}<br>
            <strong>Total courses:</strong> {total_courses} |
            <strong>Total images:</strong> {total_images} |
            <strong>Translated:</strong> {total_translated} ({(total_translated/total_images*100):.1f}% overall)
        </div>

        <div class="legend">
            <h3>Legend</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #4CAF50;"></span>
                <span>Complete (100%)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FFC107;"></span>
                <span>Partial (50-99%)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FF9800;"></span>
                <span>Low (1-49%)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #f44336;"></span>
                <span>None (0%)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #9E9E9E;"></span>
                <span>N/A (No content)</span>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th class="course-header">Course</th>
"""

    for lang in LANGUAGES:
        html += f"                    <th>{lang.upper()}</th>\n"

    html += """                </tr>
            </thead>
            <tbody>
"""

    # Sort courses by ID
    sorted_analyses = sorted(all_analyses, key=lambda x: x['course_id'])

    for analysis in sorted_analyses:
        course_id = analysis['course_id']

        html += f"                <tr>\n"
        html += f"                    <td style='text-align: left; font-weight: bold;'>{course_id}</td>\n"

        for lang in LANGUAGES:
            lang_data = analysis['languages'][lang]

            if not lang_data['exists']:
                # Language file doesn't exist
                html += f"                    <td class='translation-cell translation-na'>\n"
                html += f"                        <strong>N/A</strong>\n"
                html += f"                        <span class='translation-info'>No content</span>\n"
                html += f"                    </td>\n"
                continue

            total_images = lang_data['total_images']
            translated_images = lang_data['translated_images']
            percentage = lang_data['percentage']

            # Determine color class
            if total_images == 0:
                color_class = 'translation-na'
                display_text = 'N/A'
                info_text = 'No images'
            elif percentage == 100:
                color_class = 'translation-complete'
                display_text = f'{translated_images}/{total_images}'
                info_text = '100%'
            elif percentage >= 50:
                color_class = 'translation-partial'
                display_text = f'{translated_images}/{total_images}'
                info_text = f'{percentage:.0f}%'
            elif percentage > 0:
                color_class = 'translation-low'
                display_text = f'{translated_images}/{total_images}'
                info_text = f'{percentage:.0f}%'
            else:
                color_class = 'translation-none'
                display_text = f'{translated_images}/{total_images}'
                info_text = '0%'

            html += f"                    <td class='translation-cell {color_class}'>\n"
            html += f"                        <strong>{display_text}</strong>\n"
            html += f"                        <span class='translation-info'>{info_text}</span>\n"
            html += f"                    </td>\n"

        html += "                </tr>\n"

    html += f"""            </tbody>
        </table>

        <div class="footer">
            📅 Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            🔄 Run <code>python generate_report.py</code> to update this report<br>
            <br>
            <small>Note: Images are considered translated when their path contains the language code (e.g., /en/, /fr/, etc.)</small>
        </div>
    </div>
</body>
</html>
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ HTML report generated: {output_file}")

def main():
    """Main execution function."""
    print("🚀 Image Translation Overview Generator")
    print("=" * 50)

    # Get script directory and reports folder for output
    script_dir = Path(__file__).parent.resolve()
    reports_dir = script_dir.parent / 'reports'
    reports_dir.mkdir(exist_ok=True)
    output_file = reports_dir / 'image_translation_overview.html'

    # Get courses directory
    courses_dir = get_courses_directory()

    if not courses_dir.exists():
        print(f"❌ Error: Courses directory not found at {courses_dir}")
        return 1

    print(f"📂 Courses directory: {courses_dir}")
    print(f"📄 Output file: {output_file}")
    print()

    # Find all course directories
    course_dirs = [d for d in courses_dir.iterdir()
                   if d.is_dir() and not d.name.startswith('.')]

    print(f"📂 Found {len(course_dirs)} course directories")
    print()

    all_analyses = []

    for course_dir in sorted(course_dirs):
        print(f"🔍 Analyzing {course_dir.name}...")
        analysis = analyze_course_images(course_dir)
        if analysis:
            all_analyses.append(analysis)

    print()
    print(f"✅ Successfully analyzed {len(all_analyses)} courses")
    print()

    # Generate HTML report
    generate_html_report(all_analyses, output_file)

    print()
    print(f"🎉 Done! Open the following file in your browser:")
    print(f"   {output_file}")

    return 0

if __name__ == '__main__':
    exit(main())
