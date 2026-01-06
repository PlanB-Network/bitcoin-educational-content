#!/usr/bin/env python3
"""
PlanB Network - Validate All Content

Simple script to validate all courses and tutorials and generate an HTML report.

Usage:
    python validate_all.py                    # Validate all, generate HTML report
    python validate_all.py --courses-only     # Only validate courses
    python validate_all.py --tutorials-only   # Only validate tutorials
    python validate_all.py --no-report        # Validate without generating HTML
"""

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    END = "\033[0m"


class ProgressBar:
    """Simple progress bar with single-line updates."""

    def __init__(self, total: int, prefix: str = "", width: int = 30):
        self.total = total
        self.prefix = prefix
        self.width = width
        self.current = 0
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.is_tty = sys.stdout.isatty()

    def update(self, name: str, errors: int = 0, warnings: int = 0):
        """Update progress bar with new item result."""
        self.current += 1
        if errors > 0:
            self.failed += 1
        elif warnings > 0:
            self.warnings += 1
        else:
            self.passed += 1

        if self.is_tty:
            self._draw(name)

    def _draw(self, name: str):
        """Draw the progress bar on a single line (TTY only)."""
        pct = self.current / self.total
        filled = int(self.width * pct)
        bar = "█" * filled + "░" * (self.width - filled)

        # Truncate name to fit
        max_name = 25
        if len(name) > max_name:
            name = name[:max_name-2] + ".."

        line = f"{self.prefix} │{bar}│ {self.current:3d}/{self.total} {name:<{max_name}}"

        sys.stdout.write(f"\r\033[K{line}")
        sys.stdout.flush()

    def finish(self):
        """Complete the progress bar and show summary."""
        bar = "█" * self.width

        parts = []
        if self.passed > 0:
            parts.append(f"{Colors.GREEN}{self.passed} ✓{Colors.END}")
        if self.failed > 0:
            parts.append(f"{Colors.RED}{self.failed} ✗{Colors.END}")
        if self.warnings > 0:
            parts.append(f"{Colors.YELLOW}{self.warnings} ⚠{Colors.END}")

        summary = " ".join(parts)

        if self.is_tty:
            line = f"{self.prefix} │{Colors.GREEN}{bar}{Colors.END}│ {self.total:3d}/{self.total} Done: {summary}"
            sys.stdout.write(f"\r\033[K{line}\n")
        else:
            # Non-TTY: just print final summary
            print(f"{self.prefix} {self.total}/{self.total} - {summary}")

        sys.stdout.flush()


def find_repo_root() -> Path:
    """Find the repository root by looking for .git directory."""
    current = Path(__file__).resolve().parent
    for _ in range(10):
        if (current / ".git").exists():
            return current
        if current.parent == current:
            break
        current = current.parent
    # Fallback: assume script is in repo_root/scripts/
    return Path(__file__).resolve().parent.parent


def find_courses(repo_root: Path) -> list[Path]:
    """Find all course folders."""
    courses_dir = repo_root / "courses"
    if not courses_dir.exists():
        return []

    courses = []
    for item in sorted(courses_dir.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            # Check if it has course.yml (it's a valid course)
            if (item / "course.yml").exists():
                courses.append(item)
    return courses


def find_tutorials(repo_root: Path) -> list[Path]:
    """Find all tutorial folders (nested under category)."""
    tutorials_dir = repo_root / "tutorials"
    if not tutorials_dir.exists():
        return []

    tutorials = []
    for category in sorted(tutorials_dir.iterdir()):
        if category.is_dir() and not category.name.startswith('.'):
            for tutorial in sorted(category.iterdir()):
                if tutorial.is_dir() and not tutorial.name.startswith('.'):
                    # Check if it has tutorial.yml (it's a valid tutorial)
                    if (tutorial / "tutorial.yml").exists():
                        tutorials.append(tutorial)
    return tutorials


def validate_folder(folder: Path, validator_script: Path) -> dict:
    """Run validator on a folder and return JSON result."""
    try:
        result = subprocess.run(
            [sys.executable, str(validator_script), str(folder), "--json"],
            capture_output=True,
            text=True,
            timeout=60
        )

        # Try to parse JSON from stdout
        if result.stdout.strip():
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                # stdout has non-JSON content (likely error message)
                error_msg = result.stdout.strip() + "\n" + result.stderr.strip()
                return {
                    "folder": str(folder),
                    "results": [{"file": str(folder), "errors": [error_msg.strip()], "warnings": []}],
                    "total_errors": 1,
                    "total_warnings": 0,
                }
        else:
            error_msg = result.stderr.strip() if result.stderr else "No output from validator"
            return {
                "folder": str(folder),
                "results": [{"file": str(folder), "errors": [error_msg], "warnings": []}],
                "total_errors": 1 if result.returncode != 0 else 0,
                "total_warnings": 0,
            }
    except subprocess.TimeoutExpired:
        return {
            "folder": str(folder),
            "results": [{"file": str(folder), "errors": ["Validation timed out"], "warnings": []}],
            "total_errors": 1,
            "total_warnings": 0,
        }
    except Exception as e:
        return {
            "folder": str(folder),
            "results": [{"file": str(folder), "errors": [str(e)], "warnings": []}],
            "total_errors": 1,
            "total_warnings": 0,
        }


def generate_html_report(courses: list[dict], tutorials: list[dict], output_path: Path, repo_root: Path):
    """Generate an HTML report from validation results."""

    # Calculate statistics
    course_total = len(courses)
    courses_with_errors = sum(1 for r in courses if r.get('total_errors', 0) > 0)
    course_errors = sum(r.get('total_errors', 0) for r in courses)
    course_warnings = sum(r.get('total_warnings', 0) for r in courses)

    tutorial_total = len(tutorials)
    tutorials_with_errors = sum(1 for r in tutorials if r.get('total_errors', 0) > 0)
    tutorial_errors = sum(r.get('total_errors', 0) for r in tutorials)
    tutorial_warnings = sum(r.get('total_warnings', 0) for r in tutorials)

    total_items = course_total + tutorial_total
    total_errors = course_errors + tutorial_errors
    total_warnings = course_warnings + tutorial_warnings

    # Group errors by type
    error_types = {}
    for result in courses + tutorials:
        content_type = 'courses' if 'courses' in result.get('folder', '') else 'tutorials'
        for file_result in result.get('results', []):
            for error in file_result.get('errors', []):
                # Extract error type (first part before specific details)
                error_key = error.split(']')[0] + ']' if ']' in error else error[:60]
                if error_key not in error_types:
                    error_types[error_key] = {'courses': [], 'tutorials': []}

                entry = {
                    'name': result.get('folder', 'unknown'),
                    'file': file_result.get('file', 'unknown'),
                    'full_error': error
                }
                error_types[error_key][content_type].append(entry)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Build HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schema Validation Report - PlanB Network</title>
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
            --course-color: #f7931a;
            --tutorial-color: #8b5cf6;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            line-height: 1.6;
            padding: 2rem;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
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
        .timestamp {{ color: var(--text-secondary); font-size: 0.9rem; }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        .stat-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.25rem;
            text-align: center;
        }}
        .stat-card.course {{ border-top: 3px solid var(--course-color); }}
        .stat-card.tutorial {{ border-top: 3px solid var(--tutorial-color); }}
        .stat-value {{
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.25rem;
        }}
        .stat-value.success {{ color: var(--success-color); }}
        .stat-value.error {{ color: var(--error-color); }}
        .stat-value.warning {{ color: var(--warning-color); }}
        .stat-label {{
            color: var(--text-secondary);
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        section {{ margin-bottom: 3rem; }}
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
            margin-bottom: 1rem;
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
        .error-header:hover {{ background: rgba(218, 54, 51, 0.15); }}
        .error-type {{ font-weight: 600; color: var(--error-color); font-size: 0.9rem; }}
        .error-counts {{ display: flex; gap: 0.5rem; }}
        .error-count {{
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
        }}
        .error-count.course {{ background: var(--course-color); color: white; }}
        .error-count.tutorial {{ background: var(--tutorial-color); color: white; }}
        .error-details {{ padding: 1rem 1.5rem; display: none; }}
        .error-details.active {{ display: block; }}
        .hidden-occurrences {{ display: none; }}
        .hidden-occurrences.show {{ display: block; }}
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
        .show-more-btn:hover {{ background: rgba(88, 166, 255, 0.2); }}
        .error-item {{
            padding: 0.75rem;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 6px;
            margin-bottom: 0.5rem;
            font-family: 'Monaco', 'Menlo', monospace;
            font-size: 0.85rem;
        }}
        .error-file {{ color: var(--link-color); margin-bottom: 0.25rem; }}
        .error-message {{ color: var(--text-secondary); word-break: break-word; }}
        .tabs {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.5rem;
        }}
        .tab {{
            padding: 0.5rem 1rem;
            border-radius: 6px 6px 0 0;
            cursor: pointer;
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-bottom: none;
            color: var(--text-secondary);
        }}
        .tab.active {{
            background: var(--bg-color);
            color: var(--text-primary);
            border-bottom: 2px solid var(--bg-color);
            margin-bottom: -1px;
        }}
        .tab.course.active {{ color: var(--course-color); }}
        .tab.tutorial.active {{ color: var(--tutorial-color); }}
        .tab-content {{ display: none; }}
        .tab-content.active {{ display: block; }}
        .content-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 0.75rem;
        }}
        .content-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 0.75rem 1rem;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .content-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }}
        .content-card.has-errors {{ border-left: 4px solid var(--error-color); }}
        .content-card.has-warnings {{ border-left: 4px solid var(--warning-color); }}
        .content-card.valid {{ border-left: 4px solid var(--success-color); }}
        .content-name {{
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 0.25rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .content-stats {{
            display: flex;
            gap: 1rem;
            font-size: 0.8rem;
            color: var(--text-secondary);
        }}
        .errors-count {{ color: var(--error-color); }}
        .warnings-count {{ color: var(--warning-color); }}
        .badge {{
            display: inline-block;
            padding: 0.1rem 0.4rem;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 600;
        }}
        .badge.success {{ background: rgba(35, 134, 54, 0.2); color: var(--success-color); }}
        .badge.error {{ background: rgba(218, 54, 51, 0.2); color: var(--error-color); }}
        .badge.warning {{ background: rgba(210, 153, 34, 0.2); color: var(--warning-color); }}
        .progress-bar {{
            height: 8px;
            background: var(--border-color);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 1rem;
        }}
        .progress-fill {{ height: 100%; border-radius: 4px; }}
        .progress-fill.success {{ background: var(--success-color); }}
        footer {{
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.85rem;
        }}
        footer a {{ color: var(--link-color); text-decoration: none; }}
        footer a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Schema Validation Report</h1>
            <p class="timestamp">Generated: {timestamp}</p>
        </header>

        <section class="summary">
            <h2>Overall Summary</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value">{total_items}</div>
                    <div class="stat-label">Total Content</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value success">{total_items - courses_with_errors - tutorials_with_errors}</div>
                    <div class="stat-label">Passing</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value error">{courses_with_errors + tutorials_with_errors}</div>
                    <div class="stat-label">With Errors</div>
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

            <div class="stats-grid">
                <div class="stat-card course">
                    <div class="stat-value">{course_total}</div>
                    <div class="stat-label">Courses</div>
                    <div class="progress-bar">
                        <div class="progress-fill success" style="width: {100*(course_total-courses_with_errors)/max(course_total,1):.1f}%"></div>
                    </div>
                </div>
                <div class="stat-card course">
                    <div class="stat-value success">{course_total - courses_with_errors}</div>
                    <div class="stat-label">Courses Passing</div>
                </div>
                <div class="stat-card course">
                    <div class="stat-value error">{courses_with_errors}</div>
                    <div class="stat-label">Courses Failed</div>
                </div>
            </div>

            <div class="stats-grid">
                <div class="stat-card tutorial">
                    <div class="stat-value">{tutorial_total}</div>
                    <div class="stat-label">Tutorials</div>
                    <div class="progress-bar">
                        <div class="progress-fill success" style="width: {100*(tutorial_total-tutorials_with_errors)/max(tutorial_total,1):.1f}%"></div>
                    </div>
                </div>
                <div class="stat-card tutorial">
                    <div class="stat-value success">{tutorial_total - tutorials_with_errors}</div>
                    <div class="stat-label">Tutorials Passing</div>
                </div>
                <div class="stat-card tutorial">
                    <div class="stat-value error">{tutorials_with_errors}</div>
                    <div class="stat-label">Tutorials Failed</div>
                </div>
            </div>
        </section>
'''

    # Error summary section
    if error_types:
        html += '''
        <section class="errors">
            <h2>Error Summary</h2>
'''
        sorted_errors = sorted(error_types.items(), key=lambda x: -(len(x[1]['courses']) + len(x[1]['tutorials'])))

        for error_type, occurrences in sorted_errors:
            course_count = len(occurrences['courses'])
            tutorial_count = len(occurrences['tutorials'])
            error_id = abs(hash(error_type)) % 100000

            html += f'''
            <div class="error-summary">
                <div class="error-header" onclick="toggleDetails('error-{error_id}')">
                    <span class="error-type">{error_type[:80]}</span>
                    <div class="error-counts">
'''
            if course_count > 0:
                html += f'                        <span class="error-count course">{course_count} courses</span>\n'
            if tutorial_count > 0:
                html += f'                        <span class="error-count tutorial">{tutorial_count} tutorials</span>\n'
            html += f'''                    </div>
                </div>
                <div class="error-details" id="error-{error_id}">
'''
            all_occurrences = occurrences['courses'] + occurrences['tutorials']
            visible_count = 4
            for occ in all_occurrences[:visible_count]:
                file_path = occ['file'].replace(str(repo_root) + '/', '')
                html += f'''                    <div class="error-item">
                        <div class="error-file">{file_path}</div>
                        <div class="error-message">{occ['full_error'][:300]}</div>
                    </div>
'''
            if len(all_occurrences) > visible_count:
                remaining = len(all_occurrences) - visible_count
                html += f'''                    <div class="show-more-btn" onclick="toggleMore('more-{error_id}', this)">
                        ... and {remaining} more occurrence(s) - click to expand
                    </div>
                    <div class="hidden-occurrences" id="more-{error_id}">
'''
                for occ in all_occurrences[visible_count:]:
                    file_path = occ['file'].replace(str(repo_root) + '/', '')
                    html += f'''                        <div class="error-item">
                            <div class="error-file">{file_path}</div>
                            <div class="error-message">{occ['full_error'][:300]}</div>
                        </div>
'''
                html += '''                    </div>
'''
            html += '''                </div>
            </div>
'''
        html += '''        </section>
'''

    # Content details with tabs
    html += f'''
        <section class="content">
            <h2>Content Details</h2>
            <div class="tabs">
                <div class="tab course active" onclick="showTab('courses')">Courses ({course_total})</div>
                <div class="tab tutorial" onclick="showTab('tutorials')">Tutorials ({tutorial_total})</div>
            </div>

            <div class="tab-content active" id="courses-tab">
                <div class="content-grid">
'''

    # Courses
    sorted_courses = sorted(courses, key=lambda r: (-r.get('total_errors', 0), r.get('folder', '')))
    for result in sorted_courses:
        name = Path(result.get('folder', 'unknown')).name
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
            badge = '<span class="badge success">OK</span>'

        html += f'''                    <div class="content-card {card_class}">
                        <div class="content-name">{name} {badge}</div>
                        <div class="content-stats">
                            <span>{files} files</span>
'''
        if errors > 0:
            html += f'                            <span class="errors-count">{errors} errors</span>\n'
        if warnings > 0:
            html += f'                            <span class="warnings-count">{warnings} warnings</span>\n'
        html += '''                        </div>
                    </div>
'''

    html += '''                </div>
            </div>

            <div class="tab-content" id="tutorials-tab">
                <div class="content-grid">
'''

    # Tutorials
    sorted_tutorials = sorted(tutorials, key=lambda r: (-r.get('total_errors', 0), r.get('folder', '')))
    for result in sorted_tutorials:
        folder = Path(result.get('folder', 'unknown'))
        name = f"{folder.parent.name}/{folder.name}"
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
            badge = '<span class="badge success">OK</span>'

        html += f'''                    <div class="content-card {card_class}">
                        <div class="content-name">{name} {badge}</div>
                        <div class="content-stats">
                            <span>{files} files</span>
'''
        if errors > 0:
            html += f'                            <span class="errors-count">{errors} errors</span>\n'
        if warnings > 0:
            html += f'                            <span class="warnings-count">{warnings} warnings</span>\n'
        html += '''                        </div>
                    </div>
'''

    html += '''                </div>
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

        function showTab(tabName) {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
            document.querySelector('.tab.' + tabName.slice(0, -1)).classList.add('active');
            document.getElementById(tabName + '-tab').classList.add('active');
        }
    </script>
</body>
</html>
'''

    output_path.write_text(html, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(
        description="Validate all PlanB Network courses and tutorials"
    )
    parser.add_argument('--courses-only', action='store_true', help='Only validate courses')
    parser.add_argument('--tutorials-only', action='store_true', help='Only validate tutorials')
    parser.add_argument('--no-report', action='store_true', help='Skip HTML report generation')
    parser.add_argument('--output', '-o', default=None, help='Output HTML file path')

    args = parser.parse_args()

    # Find paths
    repo_root = find_repo_root()
    template_repo = repo_root / "docs" / "PBN-template-repo"
    validator_script = template_repo / "scripts" / "schema_validator.py"

    if not validator_script.exists():
        print(f"{Colors.RED}ERROR: schema_validator.py not found at {validator_script}{Colors.END}")
        print(f"Make sure you're running from the bitcoin-educational-content repository.")
        sys.exit(1)

    # Check required dependencies
    missing_deps = []
    for mod in ['yaml', 'jsonschema', 'frontmatter']:
        try:
            __import__(mod)
        except ImportError:
            missing_deps.append(mod)

    if missing_deps:
        print(f"{Colors.RED}ERROR: Missing required Python packages:{Colors.END}")
        print(f"  pip install pyyaml jsonschema python-frontmatter")
        sys.exit(1)

    # Default output path - in scripts/reports/
    if args.output:
        output_path = Path(args.output)
    else:
        reports_dir = repo_root / "scripts" / "reports"
        reports_dir.mkdir(exist_ok=True)
        output_path = reports_dir / "validation_report.html"

    print(f"{Colors.BOLD}PlanB Network Schema Validator{Colors.END}")
    print(f"Repository: {repo_root}")
    print(f"{'='*60}\n")

    courses = []
    tutorials = []
    course_results = []
    tutorial_results = []

    # Find content
    if not args.tutorials_only:
        courses = find_courses(repo_root)
        print(f"{Colors.CYAN}Found {len(courses)} courses{Colors.END}")

    if not args.courses_only:
        tutorials = find_tutorials(repo_root)
        print(f"{Colors.CYAN}Found {len(tutorials)} tutorials{Colors.END}")

    print()

    # Validate courses
    if courses:
        progress = ProgressBar(len(courses), prefix="Courses  ")
        for course in courses:
            result = validate_folder(course, validator_script)
            result['folder'] = str(course)
            course_results.append(result)
            progress.update(
                course.name,
                errors=result.get('total_errors', 0),
                warnings=result.get('total_warnings', 0)
            )
        progress.finish()

    # Validate tutorials
    if tutorials:
        progress = ProgressBar(len(tutorials), prefix="Tutorials")
        for tutorial in tutorials:
            name = f"{tutorial.parent.name}/{tutorial.name}"
            result = validate_folder(tutorial, validator_script)
            result['folder'] = str(tutorial)
            tutorial_results.append(result)
            progress.update(
                name,
                errors=result.get('total_errors', 0),
                warnings=result.get('total_warnings', 0)
            )
        progress.finish()

    # Summary
    course_errors = sum(r.get('total_errors', 0) for r in course_results)
    course_warnings = sum(r.get('total_warnings', 0) for r in course_results)
    tutorial_errors = sum(r.get('total_errors', 0) for r in tutorial_results)
    tutorial_warnings = sum(r.get('total_warnings', 0) for r in tutorial_results)

    print(f"{'='*60}")
    print(f"{Colors.BOLD}Summary{Colors.END}")
    print(f"  Courses:   {len(course_results)} validated, {course_errors} errors, {course_warnings} warnings")
    print(f"  Tutorials: {len(tutorial_results)} validated, {tutorial_errors} errors, {tutorial_warnings} warnings")
    print(f"{'='*60}\n")

    # Generate HTML report
    if not args.no_report:
        print(f"Generating HTML report...", end=" ", flush=True)
        generate_html_report(course_results, tutorial_results, output_path, repo_root)
        print(f"{Colors.GREEN}Done!{Colors.END}")
        print(f"Report: {output_path}")

    # Exit code
    total_errors = course_errors + tutorial_errors
    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
