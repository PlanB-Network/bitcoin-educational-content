#!/usr/bin/env python3
"""Generate HTML report from schema validation results."""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

def parse_validation_output(raw_output: str) -> list[dict]:
    """Parse the raw validation output into structured data."""
    results = []

    # Split by course markers
    course_blocks = re.split(r'=== (courses/[^/]+/) ===\n', raw_output)

    # Process pairs of (course_name, json_output)
    for i in range(1, len(course_blocks), 2):
        if i + 1 < len(course_blocks):
            course_name = course_blocks[i].strip('/')
            json_str = course_blocks[i + 1].strip()

            # Find the JSON object
            try:
                # Find the start and end of JSON
                start = json_str.find('{')
                if start == -1:
                    continue

                # Find matching closing brace
                brace_count = 0
                end = start
                for idx, char in enumerate(json_str[start:], start):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end = idx + 1
                            break

                json_data = json.loads(json_str[start:end])
                json_data['course'] = course_name
                results.append(json_data)
            except json.JSONDecodeError as e:
                print(f"Warning: Failed to parse JSON for {course_name}: {e}", file=sys.stderr)

    return results

def generate_html_report(results: list[dict], output_path: str):
    """Generate an HTML report from validation results."""

    # Calculate statistics
    total_courses = len(results)
    courses_with_errors = sum(1 for r in results if r.get('total_errors', 0) > 0)
    courses_with_warnings = sum(1 for r in results if r.get('total_warnings', 0) > 0)
    total_files = sum(len(r.get('results', [])) for r in results)
    total_errors = sum(r.get('total_errors', 0) for r in results)
    total_warnings = sum(r.get('total_warnings', 0) for r in results)

    # Group errors by type
    error_types = {}
    for result in results:
        for file_result in result.get('results', []):
            for error in file_result.get('errors', []):
                # Simplify error message for grouping
                error_key = error.split(':')[0] if ':' in error else error[:50]
                if error_key not in error_types:
                    error_types[error_key] = []
                error_types[error_key].append({
                    'course': result.get('course', 'unknown'),
                    'file': file_result.get('file', 'unknown'),
                    'full_error': error
                })

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schema Validation Report - PlanB Network Courses</title>
    <style>
        :root {{
            --bg-color: #0d1117;
            --card-bg: #161b22;
            --border-color: #30363d;
            --text-primary: #e6edf3;
            --text-secondary: #8b949e;
            --success-color: #238636;
            --error-color: #da3633;
            --warning-color: #d29922;
            --link-color: #58a6ff;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            line-height: 1.6;
            padding: 2rem;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--border-color);
        }}

        h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, #f7931a, #ffcd00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .timestamp {{
            color: var(--text-secondary);
            font-size: 0.9rem;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }}

        .stat-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
        }}

        .stat-value {{
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }}

        .stat-value.success {{
            color: var(--success-color);
        }}

        .stat-value.error {{
            color: var(--error-color);
        }}

        .stat-value.warning {{
            color: var(--warning-color);
        }}

        .stat-label {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        section {{
            margin-bottom: 3rem;
        }}

        h2 {{
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--border-color);
        }}

        .error-summary {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 1.5rem;
        }}

        .error-header {{
            background: rgba(218, 54, 51, 0.1);
            padding: 1rem 1.5rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
        }}

        .error-header:hover {{
            background: rgba(218, 54, 51, 0.15);
        }}

        .error-type {{
            font-weight: 600;
            color: var(--error-color);
        }}

        .error-count {{
            background: var(--error-color);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
        }}

        .error-details {{
            padding: 1rem 1.5rem;
            display: none;
        }}

        .error-details.active {{
            display: block;
        }}

        .hidden-occurrences {{
            display: none;
        }}

        .hidden-occurrences.show {{
            display: block;
        }}

        .show-more-btn {{
            padding: 0.75rem;
            background: rgba(88, 166, 255, 0.1);
            border-radius: 6px;
            margin-bottom: 0.5rem;
            font-family: 'Monaco', 'Menlo', monospace;
            font-size: 0.85rem;
            color: var(--link-color);
            cursor: pointer;
            text-align: center;
            border: 1px dashed var(--link-color);
        }}

        .show-more-btn:hover {{
            background: rgba(88, 166, 255, 0.2);
        }}

        .error-item {{
            padding: 0.75rem;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 6px;
            margin-bottom: 0.5rem;
            font-family: 'Monaco', 'Menlo', monospace;
            font-size: 0.85rem;
        }}

        .error-file {{
            color: var(--link-color);
            margin-bottom: 0.25rem;
        }}

        .error-message {{
            color: var(--text-secondary);
        }}

        .course-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1rem;
        }}

        .course-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1rem;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .course-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }}

        .course-card.has-errors {{
            border-left: 4px solid var(--error-color);
        }}

        .course-card.has-warnings {{
            border-left: 4px solid var(--warning-color);
        }}

        .course-card.valid {{
            border-left: 4px solid var(--success-color);
        }}

        .course-name {{
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }}

        .course-stats {{
            display: flex;
            gap: 1rem;
            font-size: 0.85rem;
            color: var(--text-secondary);
        }}

        .files-count {{
            color: var(--text-secondary);
        }}

        .errors-count {{
            color: var(--error-color);
        }}

        .warnings-count {{
            color: var(--warning-color);
        }}

        .badge {{
            display: inline-block;
            padding: 0.15rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }}

        .badge.success {{
            background: rgba(35, 134, 54, 0.2);
            color: var(--success-color);
        }}

        .badge.error {{
            background: rgba(218, 54, 51, 0.2);
            color: var(--error-color);
        }}

        footer {{
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.85rem;
        }}

        footer a {{
            color: var(--link-color);
            text-decoration: none;
        }}

        footer a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Schema Validation Report</h1>
            <p class="timestamp">Generated: {timestamp}</p>
        </header>

        <section class="summary">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value">{total_courses}</div>
                    <div class="stat-label">Total Courses</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{total_files}</div>
                    <div class="stat-label">Files Validated</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value success">{total_courses - courses_with_errors}</div>
                    <div class="stat-label">Passing Courses</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value error">{courses_with_errors}</div>
                    <div class="stat-label">Courses with Errors</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value error">{total_errors}</div>
                    <div class="stat-label">Total Errors</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value warning">{total_warnings}</div>
                    <div class="stat-label">Total Warnings</div>
                </div>
            </div>
        </section>
'''

    # Add error summary section if there are errors
    if error_types:
        html += '''
        <section class="errors">
            <h2>Error Summary</h2>
'''
        for error_type, occurrences in sorted(error_types.items(), key=lambda x: -len(x[1])):
            error_id = hash(error_type) % 10000
            html += f'''
            <div class="error-summary">
                <div class="error-header" onclick="toggleDetails('error-{error_id}')">
                    <span class="error-type">{error_type[:80]}...</span>
                    <span class="error-count">{len(occurrences)} occurrence(s)</span>
                </div>
                <div class="error-details" id="error-{error_id}">
'''
            # Show first 4 occurrences
            visible_count = 4
            for occ in occurrences[:visible_count]:
                file_path = occ['file'].replace('/home/asi0/asi0-repos/bitcoin-educational-content/', '')
                html += f'''
                    <div class="error-item">
                        <div class="error-file">{file_path}</div>
                        <div class="error-message">{occ['full_error']}</div>
                    </div>
'''
            # If more than visible_count, add expandable section
            if len(occurrences) > visible_count:
                remaining = len(occurrences) - visible_count
                html += f'''
                    <div class="show-more-btn" onclick="toggleMore('more-{error_id}', this)">
                        ... and {remaining} more occurrence(s) - click to expand
                    </div>
                    <div class="hidden-occurrences" id="more-{error_id}">
'''
                for occ in occurrences[visible_count:]:
                    file_path = occ['file'].replace('/home/asi0/asi0-repos/bitcoin-educational-content/', '')
                    html += f'''
                        <div class="error-item">
                            <div class="error-file">{file_path}</div>
                            <div class="error-message">{occ['full_error']}</div>
                        </div>
'''
                html += '''
                    </div>
'''
            html += '''
                </div>
            </div>
'''
        html += '''
        </section>
'''

    # Add course details section
    html += '''
        <section class="courses">
            <h2>Course Details</h2>
            <div class="course-grid">
'''

    # Sort courses: errors first, then warnings, then valid
    sorted_results = sorted(results, key=lambda r: (-r.get('total_errors', 0), -r.get('total_warnings', 0), r.get('course', '')))

    for result in sorted_results:
        course = result.get('course', 'unknown')
        errors = result.get('total_errors', 0)
        warnings = result.get('total_warnings', 0)
        files = len(result.get('results', []))

        if errors > 0:
            card_class = 'has-errors'
            badge = '<span class="badge error">FAILED</span>'
        elif warnings > 0:
            card_class = 'has-warnings'
            badge = '<span class="badge warning">WARNINGS</span>'
        else:
            card_class = 'valid'
            badge = '<span class="badge success">PASSED</span>'

        html += f'''
                <div class="course-card {card_class}">
                    <div class="course-name">{course} {badge}</div>
                    <div class="course-stats">
                        <span class="files-count">{files} files</span>
'''
        if errors > 0:
            html += f'<span class="errors-count">{errors} errors</span>'
        if warnings > 0:
            html += f'<span class="warnings-count">{warnings} warnings</span>'

        html += '''
                    </div>
                </div>
'''

    html += '''
            </div>
        </section>

        <footer>
            <p>Schema Validator for <a href="https://planb.network">PlanB Network</a> Educational Content</p>
        </footer>
    </div>

    <script>
        function toggleDetails(id) {
            const element = document.getElementById(id);
            element.classList.toggle('active');
        }

        function toggleMore(id, btn) {
            const element = document.getElementById(id);
            element.classList.toggle('show');
            if (element.classList.contains('show')) {
                btn.textContent = '▲ Click to collapse';
                btn.style.background = 'rgba(88, 166, 255, 0.2)';
            } else {
                const count = element.querySelectorAll('.error-item').length;
                btn.textContent = '... and ' + count + ' more occurrence(s) - click to expand';
                btn.style.background = 'rgba(88, 166, 255, 0.1)';
            }
        }
    </script>
</body>
</html>
'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Report generated: {output_path}")
    print(f"\nSummary:")
    print(f"  Total courses: {total_courses}")
    print(f"  Courses with errors: {courses_with_errors}")
    print(f"  Total errors: {total_errors}")
    print(f"  Total warnings: {total_warnings}")

def main():
    # Read input
    input_file = sys.argv[1] if len(sys.argv) > 1 else '/tmp/validation_results.txt'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'validation_report.html'

    with open(input_file, 'r') as f:
        raw_output = f.read()

    results = parse_validation_output(raw_output)
    generate_html_report(results, output_file)

if __name__ == '__main__':
    main()
