#!/usr/bin/env python3
"""
Video Deployment Overview Generator

Analyzes video deployment across all courses and languages.
Generates an HTML report showing video coverage by provider (YouTube/PeerTube).

Usage:
    python generate_report.py

The HTML report will be saved in the same directory as this script.
"""

import yaml
import os
from pathlib import Path
from datetime import datetime

# Languages to check
LANGUAGES = ['en', 'fr', 'es', 'it', 'de', 'ru', 'zh-Hant']

# Courses that should have NO VIDEOS (0 is green for all languages)
NO_VIDEO_COURSES = {
    'btc202', 'btc302', 'cyp302', 'dev103', 'eco104',
    'net302', 'phi302', 'pos305', 'scu202'
}

# Courses that should have ENGLISH ONLY VIDEOS (0 is green for non-English)
ENGLISH_ONLY_VIDEO_COURSES = {
    'btc401', 'csv404', 'csv402', 'dev203', 'min306',
    'pro202', 'sid202', 'sid302'
}

def get_courses_directory():
    """Get the courses directory path relative to this script."""
    script_dir = Path(__file__).parent.resolve()
    courses_dir = script_dir / '../../courses'
    return courses_dir.resolve()

def parse_course_yml(course_path):
    """Parse course.yml and extract video deployment information."""
    yml_file = course_path / 'course.yml'

    if not yml_file.exists():
        return None

    try:
        with open(yml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if not data or 'videos' not in data:
            return None

        course_id = course_path.name
        videos = data.get('videos', [])

        # Track deployment per language
        deployment = {
            'course_id': course_id,
            'total_videos': len(videos),
            'languages': {}
        }

        for lang in LANGUAGES:
            deployment['languages'][lang] = {
                'youtube': 0,
                'peertube': 0,
                'both': 0,
                'total_videos': len(videos)
            }

        # Analyze each video
        for video in videos:
            video_id = video.get('id', 'unknown')

            # Check YouTube
            youtube_data = video.get('youtube', [])
            peertube_data = video.get('peertube', [])

            for lang in LANGUAGES:
                has_youtube = False
                has_peertube = False

                # Check if language exists in YouTube
                if youtube_data:
                    for entry in youtube_data:
                        if isinstance(entry, dict) and lang in entry:
                            has_youtube = True
                            break

                # Check if language exists in PeerTube
                if peertube_data:
                    for entry in peertube_data:
                        if isinstance(entry, dict) and lang in entry:
                            has_peertube = True
                            break

                # Count coverage
                if has_youtube and has_peertube:
                    deployment['languages'][lang]['both'] += 1
                elif has_youtube:
                    deployment['languages'][lang]['youtube'] += 1
                elif has_peertube:
                    deployment['languages'][lang]['peertube'] += 1

        return deployment

    except Exception as e:
        print(f"⚠️  Error parsing {yml_file}: {e}")
        return None

def generate_html_report(all_deployments, output_file):
    """Generate HTML report with color-coded table."""

    # Calculate summary statistics
    total_courses = len(all_deployments)
    total_videos = sum(d['total_videos'] for d in all_deployments)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Deployment Overview</title>
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
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        th.course-header {{
            background-color: #2196F3;
            text-align: left;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        .coverage-cell {{
            position: relative;
            min-width: 120px;
        }}
        .coverage-complete {{
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }}
        .coverage-partial {{
            background-color: #FFC107;
            color: black;
        }}
        .coverage-low {{
            background-color: #FF9800;
            color: white;
        }}
        .coverage-none {{
            background-color: #f44336;
            color: white;
        }}
        .coverage-info {{
            font-size: 12px;
            display: block;
            margin-top: 4px;
        }}
        .provider-badge {{
            display: inline-block;
            padding: 2px 6px;
            margin: 2px;
            border-radius: 3px;
            font-size: 10px;
            font-weight: bold;
        }}
        .youtube-badge {{
            background-color: #FF0000;
            color: white;
        }}
        .peertube-badge {{
            background-color: #FF6C00;
            color: white;
        }}
        .both-badge {{
            background-color: #4CAF50;
            color: white;
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
            <h1>🎥 Video Deployment Overview</h1>
        </div>
        <div class="stats">
            <strong>Languages analyzed:</strong> {", ".join(LANGUAGES)}<br>
            <strong>Total courses:</strong> {total_courses} |
            <strong>Total videos:</strong> {total_videos}
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
            <br><br>
            <div class="legend-item">
                <span class="provider-badge youtube-badge">Y</span>
                <span>YouTube only</span>
            </div>
            <div class="legend-item">
                <span class="provider-badge peertube-badge">P</span>
                <span>PeerTube only</span>
            </div>
            <div class="legend-item">
                <span class="provider-badge both-badge">B</span>
                <span>Both providers</span>
            </div>
            <br><br>
            <div style="font-size: 12px; color: #666; margin-top: 10px;">
                <strong>Special course types:</strong><br>
                📝 <strong>No-video courses</strong> (0 videos = ✅ green): {", ".join(sorted(NO_VIDEO_COURSES))}<br>
                🇬🇧 <strong>English-only courses</strong> (non-English 0 videos = ✅ green): {", ".join(sorted(ENGLISH_ONLY_VIDEO_COURSES))}
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th class="course-header">Course</th>
                    <th>Total Videos</th>
"""

    for lang in LANGUAGES:
        html += f"                    <th>{lang.upper()}</th>\n"

    html += """                </tr>
            </thead>
            <tbody>
"""

    # Sort courses by ID
    sorted_deployments = sorted(all_deployments, key=lambda x: x['course_id'])

    for deployment in sorted_deployments:
        course_id = deployment['course_id']
        total_videos = deployment['total_videos']

        html += f"                <tr>\n"
        html += f"                    <td style='text-align: left; font-weight: bold;'>{course_id}</td>\n"
        html += f"                    <td>{total_videos}</td>\n"

        for lang in LANGUAGES:
            lang_data = deployment['languages'][lang]
            youtube_count = lang_data['youtube']
            peertube_count = lang_data['peertube']
            both_count = lang_data['both']
            total_covered = youtube_count + peertube_count + both_count

            # Calculate coverage percentage
            if total_videos > 0:
                coverage_pct = (total_covered / total_videos) * 100
            else:
                coverage_pct = 0

            # Determine color class based on course type
            is_no_video_course = course_id in NO_VIDEO_COURSES
            is_english_only_course = course_id in ENGLISH_ONLY_VIDEO_COURSES
            is_non_english = lang != 'en'

            if is_no_video_course and total_covered == 0:
                # No video courses: 0 videos = green for all languages
                color_class = 'coverage-complete'
            elif is_english_only_course and is_non_english and total_covered == 0:
                # English-only courses: 0 videos = green for non-English
                color_class = 'coverage-complete'
            elif coverage_pct == 100:
                color_class = 'coverage-complete'
            elif coverage_pct >= 50:
                color_class = 'coverage-partial'
            elif coverage_pct > 0:
                color_class = 'coverage-low'
            else:
                color_class = 'coverage-none'

            # Build provider info
            provider_info = []
            if youtube_count > 0:
                provider_info.append(f'<span class="provider-badge youtube-badge">Y:{youtube_count}</span>')
            if peertube_count > 0:
                provider_info.append(f'<span class="provider-badge peertube-badge">P:{peertube_count}</span>')
            if both_count > 0:
                provider_info.append(f'<span class="provider-badge both-badge">B:{both_count}</span>')

            provider_html = ' '.join(provider_info) if provider_info else '-'

            html += f"                    <td class='coverage-cell {color_class}'>\n"
            html += f"                        <strong>{total_covered}/{total_videos}</strong>\n"
            html += f"                        <span class='coverage-info'>{coverage_pct:.0f}%</span>\n"
            html += f"                        <div style='margin-top: 5px;'>{provider_html}</div>\n"
            html += f"                    </td>\n"

        html += "                </tr>\n"

    html += f"""            </tbody>
        </table>

        <div class="footer">
            📅 Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            🔄 Run <code>python generate_report.py</code> to update this report
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
    print("🚀 Video Deployment Overview Generator")
    print("=" * 50)

    # Get script directory and reports folder for output
    script_dir = Path(__file__).parent.resolve()
    reports_dir = script_dir.parent / 'reports'
    reports_dir.mkdir(exist_ok=True)
    output_file = reports_dir / 'video_deployment_overview.html'

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

    all_deployments = []

    for course_dir in sorted(course_dirs):
        print(f"🔍 Analyzing {course_dir.name}...")
        deployment = parse_course_yml(course_dir)
        if deployment:
            all_deployments.append(deployment)

    print()
    print(f"✅ Successfully analyzed {len(all_deployments)} courses")
    print()

    # Generate HTML report
    generate_html_report(all_deployments, output_file)

    print()
    print(f"🎉 Done! Open the following file in your browser:")
    print(f"   {output_file}")

    return 0

if __name__ == '__main__':
    exit(main())
