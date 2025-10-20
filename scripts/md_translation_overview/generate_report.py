#!/usr/bin/env python3
"""
Markdown Translation Overview Generator

Analyzes markdown translation progress across all courses and languages.
Generates an HTML report showing which courses have been translated.

Usage:
    python generate_report.py

The HTML report will be saved in the same directory as this script.
"""

from pathlib import Path
from datetime import datetime

def get_courses_directory():
    """Get the courses directory path relative to this script."""
    script_dir = Path(__file__).parent.resolve()
    courses_dir = script_dir / '../../courses'
    return courses_dir.resolve()

def get_supported_languages(courses_dir):
    """Get all supported languages from btc101 folder."""
    btc101_dir = courses_dir / 'btc101'
    if not btc101_dir.exists():
        return []

    # Get all .md files and extract language codes
    languages = []
    for md_file in sorted(btc101_dir.glob('*.md')):
        lang = md_file.stem  # filename without extension
        languages.append(lang)

    return languages

def count_md_content(md_file_path):
    """Count lines and words in a markdown file."""
    if not md_file_path.exists():
        return 0, 0

    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = len(content.splitlines())
        words = len(content.split())

        return lines, words

    except Exception as e:
        return 0, 0

def analyze_course_translations(course_path, languages):
    """Analyze translation status for a course."""
    course_id = course_path.name

    analysis = {
        'course_id': course_id,
        'languages': {}
    }

    for lang in languages:
        md_file = course_path / f'{lang}.md'
        lines, words = count_md_content(md_file)

        analysis['languages'][lang] = {
            'exists': md_file.exists(),
            'lines': lines,
            'words': words
        }

    return analysis

def generate_html_report(all_analyses, languages, output_file):
    """Generate HTML report with color-coded table."""

    # Calculate summary statistics
    total_courses = len(all_analyses)
    total_translations = sum(
        sum(1 for data in analysis['languages'].values() if data['exists'])
        for analysis in all_analyses
    )
    total_possible = total_courses * len(languages)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Translation Overview</title>
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
            max-width: 1200px;
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
            padding: 8px;
            text-align: center;
            font-size: 11px;
        }}
        th {{
            background-color: #2196F3;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        th.course-header {{
            background-color: #1976D2;
            text-align: left;
            min-width: 100px;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        .translation-exists {{
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }}
        .translation-missing {{
            background-color: #f44336;
            color: white;
        }}
        .translation-info {{
            font-size: 9px;
            display: block;
            margin-top: 2px;
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
            max-width: 1800px;
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
        .lang-header {{
            writing-mode: vertical-rl;
            text-orientation: mixed;
            min-width: 30px;
            padding: 8px 4px !important;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://surfer.planb.network/translation_report/index.html" class="back-button">Back to Reports</a>
            <h1>📝 Markdown Translation Overview</h1>
        </div>
        <div class="stats">
            <strong>Languages analyzed:</strong> {len(languages)} languages<br>
            <strong>Total courses:</strong> {total_courses} |
            <strong>Translations:</strong> {total_translations}/{total_possible} ({(total_translations/total_possible*100):.1f}% overall)
        </div>

        <div class="legend">
            <h3>Legend</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #4CAF50;"></span>
                <span>✓ Translated (file exists)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #f44336;"></span>
                <span>✗ Missing (no file)</span>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th class="course-header">Course</th>
"""

    for lang in languages:
        html += f"                    <th class='lang-header'>{lang.upper()}</th>\n"

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

        for lang in languages:
            lang_data = analysis['languages'][lang]

            if lang_data['exists']:
                words = lang_data['words']
                lines = lang_data['lines']

                html += f"                    <td class='translation-exists'>\n"
                html += f"                        <strong>✓</strong>\n"
                html += f"                        <span class='translation-info'>{words:,}w</span>\n"
                html += f"                    </td>\n"
            else:
                html += f"                    <td class='translation-missing'>\n"
                html += f"                        <strong>✗</strong>\n"
                html += f"                    </td>\n"

        html += "                </tr>\n"

    html += f"""            </tbody>
        </table>

        <div class="footer">
            📅 Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            🔄 Run <code>python generate_report.py</code> to update this report<br>
            <br>
            <small>Note: Numbers shown are word counts (w = words). Supported languages detected from btc101 folder.</small>
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
    print("🚀 Markdown Translation Overview Generator")
    print("=" * 50)

    # Get script directory and reports folder for output
    script_dir = Path(__file__).parent.resolve()
    reports_dir = script_dir.parent / 'reports'
    reports_dir.mkdir(exist_ok=True)
    output_file = reports_dir / 'md_translation_overview.html'

    # Get courses directory
    courses_dir = get_courses_directory()

    if not courses_dir.exists():
        print(f"❌ Error: Courses directory not found at {courses_dir}")
        return 1

    print(f"📂 Courses directory: {courses_dir}")
    print(f"📄 Output file: {output_file}")
    print()

    # Get supported languages from btc101
    languages = get_supported_languages(courses_dir)
    if not languages:
        print("❌ Error: Could not detect supported languages from btc101 folder")
        return 1

    print(f"🌍 Detected {len(languages)} supported languages:")
    print(f"   {', '.join(languages)}")
    print()

    # Find all course directories
    course_dirs = [d for d in courses_dir.iterdir()
                   if d.is_dir() and not d.name.startswith('.')]

    print(f"📂 Found {len(course_dirs)} course directories")
    print()

    all_analyses = []

    for course_dir in sorted(course_dirs):
        print(f"🔍 Analyzing {course_dir.name}...")
        analysis = analyze_course_translations(course_dir, languages)
        all_analyses.append(analysis)

    print()
    print(f"✅ Successfully analyzed {len(all_analyses)} courses")
    print()

    # Generate HTML report
    generate_html_report(all_analyses, languages, output_file)

    print()
    print(f"🎉 Done! Open the following file in your browser:")
    print(f"   {output_file}")

    return 0

if __name__ == '__main__':
    exit(main())
