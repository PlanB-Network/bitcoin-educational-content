#!/usr/bin/env python3
"""
Bitcoin Educational Content - Proofreading Dashboard Generator

Extracts proofreading data from course.yml and tutorial.yml files
and generates a self-contained HTML dashboard with embedded data.
"""

import yaml
import json
import glob
import os
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

# Language names mapping
LANGUAGE_NAMES = {
    'en': 'English', 'fr': 'French', 'de': 'German', 'es': 'Spanish',
    'it': 'Italian', 'pt': 'Portuguese', 'nl': 'Dutch', 'sv': 'Swedish',
    'nb-NO': 'Norwegian', 'cs': 'Czech', 'pl': 'Polish', 'ru': 'Russian',
    'sr-Latn': 'Serbian', 'et': 'Estonian', 'ja': 'Japanese',
    'zh-Hans': 'Chinese (Simplified)', 'zh-Hant': 'Chinese (Traditional)',
    'ko': 'Korean', 'vi': 'Vietnamese', 'hi': 'Hindi', 'id': 'Indonesian',
    'fa': 'Persian', 'tr': 'Turkish', 'sw': 'Swahili', 'rn': 'Kirundi'
}

# Excluded contributors from leaderboards
EXCLUDED_CONTRIBUTORS = ['LoicPandul', 'Asi0Flammeus', 'heyolaniran', 'Pivii', 'PaoloFoti']


def calculate_status(contributors):
    """Calculate proofreading status based on contributor count."""
    if not contributors:
        return 0
    count = len(contributors)
    if count == 1:
        return 1
    elif count == 2:
        return 2
    else:  # 3 or more
        return 3


def parse_course_file(filepath, base_dir):
    """Parse a course.yml file and extract proofreading data."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # Extract course ID from path
        course_id = Path(filepath).parent.name

        course_data = {
            'id': course_id,
            'name': data.get('name', course_id.upper()),
            'type': 'course',
            'topic': data.get('topic', 'unknown'),
            'subtopic': data.get('subtopic', ''),
            'level': data.get('level', 'unknown'),
            'original_language': data.get('original_language', 'en'),
            'proofreading': []
        }

        # Process proofreading data
        proofreading = data.get('proofreading', [])
        for pr in proofreading:
            contributors = pr.get('contributor_names', []) or []
            last_date = pr.get('last_contribution_date')
            # Convert date object to string if needed
            if last_date and not isinstance(last_date, str):
                last_date = last_date.isoformat()

            language = pr.get('language', '')
            status = calculate_status(contributors)

            course_data['proofreading'].append({
                'language': language,
                'status': status,
                'contributors': contributors,
                'last_date': last_date or None,
                'reward': float(pr.get('reward', 0)),
                'urgency': pr.get('urgency', 1)
            })

        return course_data
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None


def parse_tutorial_file(filepath, base_dir):
    """Parse a tutorial.yml file and extract proofreading data."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # Extract category and tutorial name from path
        parts = Path(filepath).parts
        category = parts[-3]  # tutorials/category/name/tutorial.yml
        tutorial_name = parts[-2]

        tutorial_data = {
            'id': f"{category}/{tutorial_name}",
            'name': data.get('name', tutorial_name.replace('-', ' ').title()),
            'type': 'tutorial',
            'category': category,
            'level': data.get('level', 'unknown'),
            'original_language': data.get('original_language', 'en'),
            'proofreading': []
        }

        # Process proofreading data
        proofreading = data.get('proofreading', [])
        for pr in proofreading:
            contributors = pr.get('contributor_names', []) or []
            last_date = pr.get('last_contribution_date')
            # Convert date object to string if needed
            if last_date and not isinstance(last_date, str):
                last_date = last_date.isoformat()

            language = pr.get('language', '')
            status = calculate_status(contributors)

            tutorial_data['proofreading'].append({
                'language': language,
                'status': status,
                'contributors': contributors,
                'last_date': last_date or None,
                'reward': float(pr.get('reward', 0)),
                'urgency': pr.get('urgency', 1)
            })

        return tutorial_data
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None


def calculate_contributor_stats(courses, tutorials):
    """Calculate contributor statistics across all content, excluding certain users."""
    course_stats = defaultdict(lambda: {
        'total_contributions': 0,
        'languages': set(),
        'courses': 0,
        'tutorials': 0
    })

    tutorial_stats = defaultdict(lambda: {
        'total_contributions': 0,
        'languages': set(),
        'courses': 0,
        'tutorials': 0
    })

    # Process courses
    for course in courses:
        for pr in course['proofreading']:
            for contributor in pr['contributors']:
                if contributor not in EXCLUDED_CONTRIBUTORS:
                    course_stats[contributor]['total_contributions'] += 1
                    course_stats[contributor]['languages'].add(pr['language'])
                    course_stats[contributor]['courses'] += 1

    # Process tutorials
    for tutorial in tutorials:
        for pr in tutorial['proofreading']:
            for contributor in pr['contributors']:
                if contributor not in EXCLUDED_CONTRIBUTORS:
                    tutorial_stats[contributor]['total_contributions'] += 1
                    tutorial_stats[contributor]['languages'].add(pr['language'])
                    tutorial_stats[contributor]['tutorials'] += 1

    # Convert sets to sorted lists
    course_result = {}
    for contributor, data in course_stats.items():
        course_result[contributor] = {
            'total_contributions': data['total_contributions'],
            'languages': sorted(list(data['languages'])),
            'courses': data['courses'],
            'tutorials': 0
        }

    tutorial_result = {}
    for contributor, data in tutorial_stats.items():
        tutorial_result[contributor] = {
            'total_contributions': data['total_contributions'],
            'languages': sorted(list(data['languages'])),
            'courses': 0,
            'tutorials': data['tutorials']
        }

    return course_result, tutorial_result


def calculate_language_stats(courses, tutorials):
    """Calculate statistics per language: total proofreadings and unique contributors."""
    lang_stats = defaultdict(lambda: {
        'total_proofreadings': 0,
        'contributors': set()
    })

    # Process courses
    for course in courses:
        for pr in course['proofreading']:
            if pr['contributors']:  # Only count if there are contributors
                lang_stats[pr['language']]['total_proofreadings'] += 1
                for contributor in pr['contributors']:
                    if contributor not in EXCLUDED_CONTRIBUTORS:
                        lang_stats[pr['language']]['contributors'].add(contributor)

    # Process tutorials
    for tutorial in tutorials:
        for pr in tutorial['proofreading']:
            if pr['contributors']:  # Only count if there are contributors
                lang_stats[pr['language']]['total_proofreadings'] += 1
                for contributor in pr['contributors']:
                    if contributor not in EXCLUDED_CONTRIBUTORS:
                        lang_stats[pr['language']]['contributors'].add(contributor)

    # Convert to final format
    result = {}
    for lang, data in lang_stats.items():
        result[lang] = {
            'total_proofreadings': data['total_proofreadings'],
            'unique_contributors': len(data['contributors']),
            'contributors': sorted(list(data['contributors']))
        }

    return result


def extract_all_data():
    """Extract all proofreading data from courses and tutorials."""
    print("Extracting proofreading data...")

    # Get base directory
    base_dir = Path(__file__).parent.parent.parent

    # Parse courses
    courses = []
    course_files = glob.glob(str(base_dir / 'courses' / '*' / 'course.yml'))
    print(f"Found {len(course_files)} courses")

    for filepath in course_files:
        course_data = parse_course_file(filepath, base_dir)
        if course_data:
            courses.append(course_data)

    # Sort courses alphabetically by ID
    courses.sort(key=lambda x: x['id'].lower())

    # Parse tutorials
    tutorials = []
    tutorial_files = glob.glob(str(base_dir / 'tutorials' / '*' / '*' / 'tutorial.yml'))
    print(f"Found {len(tutorial_files)} tutorials")

    for filepath in tutorial_files:
        tutorial_data = parse_tutorial_file(filepath, base_dir)
        if tutorial_data:
            tutorials.append(tutorial_data)

    # Sort tutorials alphabetically by ID
    tutorials.sort(key=lambda x: x['id'].lower())

    # Calculate contributor statistics
    course_contributor_stats, tutorial_contributor_stats = calculate_contributor_stats(courses, tutorials)

    # Calculate language statistics
    language_stats = calculate_language_stats(courses, tutorials)

    # Prepare languages list
    languages = [{'code': code, 'name': name} for code, name in sorted(LANGUAGE_NAMES.items())]

    # Extract unique topics and categories
    topics = sorted(list(set(c['topic'] for c in courses)))
    categories = sorted(list(set(t['category'] for t in tutorials)))

    # Compile full dataset
    data = {
        'metadata': {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'total_courses': len(courses),
            'total_tutorials': len(tutorials),
            'total_languages': len(LANGUAGE_NAMES),
            'excluded_contributors': EXCLUDED_CONTRIBUTORS
        },
        'courses': courses,
        'tutorials': tutorials,
        'languages': languages,
        'topics': topics,
        'categories': categories,
        'course_contributor_stats': course_contributor_stats,
        'tutorial_contributor_stats': tutorial_contributor_stats,
        'language_stats': language_stats
    }

    print(f"Extracted {len(courses)} courses and {len(tutorials)} tutorials")
    print(f"Found {len(course_contributor_stats)} course contributors and {len(tutorial_contributor_stats)} tutorial contributors")

    return data


def generate_html(data):
    """Generate complete HTML dashboard with embedded data."""

    # Convert data to JSON string with proper escaping
    json_data = json.dumps(data, indent=2, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bitcoin Educational Content - Proofreading Dashboard</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📚</text></svg>">
    <style>
        :root {{
            --color-bg: #f5f7fa;
            --color-card: #ffffff;
            --color-text: #2c3e50;
            --color-text-light: #7f8c8d;
            --color-border: #e1e8ed;
            --color-primary: #3498db;
            --color-primary-dark: #2980b9;
            --color-status-0: #e74c3c;
            --color-status-1: #e67e22;
            --color-status-2: #f39c12;
            --color-status-3: #27ae60;
            --color-hover: #ecf0f1;
            --color-purple: #9b59b6;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: var(--color-bg);
            color: var(--color-text);
            line-height: 1.6;
        }}

        header {{
            background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
            color: white;
            padding: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        header h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}

        .metadata {{
            font-size: 0.9rem;
            opacity: 0.9;
        }}

        .container {{
            max-width: 1600px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .section {{
            background: var(--color-card);
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        .section h2 {{
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            color: var(--color-primary);
            border-bottom: 2px solid var(--color-border);
            padding-bottom: 0.5rem;
        }}

        /* Content Type Selector */
        .type-selector {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: var(--color-bg);
            border-radius: 4px;
        }}

        .type-option {{
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1rem;
            border: 2px solid var(--color-border);
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            background: white;
        }}

        .type-option:hover {{
            border-color: var(--color-primary);
        }}

        .type-option input[type="radio"] {{
            margin-right: 0.5rem;
        }}

        .type-option.active {{
            border-color: var(--color-primary);
            background: var(--color-primary);
            color: white;
            font-weight: 600;
        }}

        /* Filters */
        .filters {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}

        .filter-group {{
            display: flex;
            flex-direction: column;
        }}

        .filter-group label {{
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
            color: var(--color-text);
        }}

        select, input[type="text"] {{
            padding: 0.5rem;
            border: 1px solid var(--color-border);
            border-radius: 4px;
            font-size: 0.9rem;
            background: white;
            cursor: pointer;
        }}

        select:hover, input[type="text"]:hover {{
            border-color: var(--color-primary);
        }}

        /* Matrix Table */
        .matrix-container {{
            overflow-x: auto;
        }}

        .matrix-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
        }}

        .matrix-table th {{
            background: var(--color-purple);
            color: white;
            padding: 0.75rem;
            text-align: center;
            font-weight: 600;
            border: 1px solid var(--color-border);
            position: sticky;
            top: 0;
            z-index: 10;
        }}

        .matrix-table th:first-child {{
            text-align: left;
            position: sticky;
            left: 0;
            z-index: 11;
        }}

        .matrix-table td {{
            padding: 0.75rem;
            border: 1px solid var(--color-border);
            text-align: center;
        }}

        .matrix-table td:first-child {{
            text-align: left;
            font-weight: 600;
            background: var(--color-bg);
            position: sticky;
            left: 0;
            z-index: 5;
        }}

        .matrix-cell {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 50px;
        }}

        .matrix-cell-count {{
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }}

        .matrix-cell-percentage {{
            font-size: 0.75rem;
        }}

        .matrix-complete {{
            background: var(--color-status-3);
            color: white;
        }}

        .matrix-partial {{
            background: var(--color-status-2);
            color: white;
        }}

        .matrix-empty {{
            background: var(--color-status-0);
            color: white;
        }}

        .matrix-na {{
            background: #95a5a6;
            color: white;
            font-size: 0.8rem;
        }}

        /* Contribution List */
        .contribution-list {{
            display: grid;
            gap: 1rem;
        }}

        .contribution-item {{
            border: 1px solid var(--color-border);
            border-radius: 4px;
            padding: 1rem;
            transition: all 0.2s;
        }}

        .contribution-item:hover {{
            border-color: var(--color-primary);
            box-shadow: 0 2px 8px rgba(52, 152, 219, 0.2);
        }}

        .contribution-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
        }}

        .contribution-title {{
            font-weight: 600;
            font-size: 1.1rem;
        }}

        .contribution-details {{
            display: flex;
            gap: 1rem;
            font-size: 0.9rem;
            color: var(--color-text-light);
            flex-wrap: wrap;
        }}

        .reward-badge {{
            background: var(--color-primary);
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-weight: 600;
        }}

        .status-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.85rem;
            font-weight: 600;
            color: white;
        }}

        .status-0 {{ background: var(--color-status-0); }}
        .status-1 {{ background: var(--color-status-1); }}
        .status-2 {{ background: var(--color-status-2); }}
        .status-3 {{ background: var(--color-status-3); }}

        .level-badge {{
            background: var(--color-purple);
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.8rem;
        }}

        /* Language Stats Table */
        .lang-stats-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
        }}

        .lang-stats-table th {{
            background: var(--color-bg);
            padding: 0.75rem;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid var(--color-border);
        }}

        .lang-stats-table td {{
            padding: 0.75rem;
            border-bottom: 1px solid var(--color-border);
        }}

        .lang-stats-table tr:hover {{
            background: var(--color-hover);
        }}

        .lang-code {{
            font-weight: 600;
            color: var(--color-primary);
            font-size: 0.95rem;
        }}

        .lang-name {{
            color: var(--color-text-light);
            font-size: 0.85rem;
        }}

        .stat-number {{
            font-weight: 700;
            font-size: 1.1rem;
            color: var(--color-primary);
        }}

        .contributor-count {{
            font-weight: 600;
            color: var(--color-purple);
        }}

        /* Leaderboards */
        .tabs {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid var(--color-border);
        }}

        .tab {{
            padding: 0.75rem 1.5rem;
            cursor: pointer;
            border: none;
            background: none;
            font-size: 1rem;
            color: var(--color-text-light);
            border-bottom: 2px solid transparent;
            margin-bottom: -2px;
            transition: all 0.2s;
        }}

        .tab.active {{
            color: var(--color-primary);
            border-bottom-color: var(--color-primary);
            font-weight: 600;
        }}

        .tab-content {{
            display: none;
        }}

        .tab-content.active {{
            display: block;
        }}

        .leaderboard-item {{
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1rem;
            border-bottom: 1px solid var(--color-border);
        }}

        .leaderboard-item:last-child {{
            border-bottom: none;
        }}

        .rank {{
            font-size: 1.2rem;
            font-weight: 700;
            min-width: 40px;
            text-align: center;
        }}

        .medal {{
            font-size: 1.5rem;
        }}

        .avatar {{
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: var(--color-border);
        }}

        .contributor-info {{
            flex: 1;
        }}

        .contributor-name {{
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 0.25rem;
        }}

        .contributor-name a {{
            color: var(--color-text);
            text-decoration: none;
        }}

        .contributor-name a:hover {{
            color: var(--color-primary);
            text-decoration: underline;
        }}

        .contributor-stats {{
            font-size: 0.85rem;
            color: var(--color-text-light);
        }}

        .contribution-count {{
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--color-primary);
        }}

        /* Stats Grid */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}

        .stat-card {{
            background: var(--color-bg);
            padding: 1rem;
            border-radius: 4px;
            text-align: center;
        }}

        .stat-value {{
            font-size: 2rem;
            font-weight: 700;
            color: var(--color-primary);
        }}

        .stat-label {{
            font-size: 0.9rem;
            color: var(--color-text-light);
            margin-top: 0.25rem;
        }}

        /* Empty state */
        .empty-state {{
            text-align: center;
            padding: 3rem;
            color: var(--color-text-light);
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}

            .section {{
                padding: 1rem;
            }}

            header h1 {{
                font-size: 1.5rem;
            }}

            .filters {{
                grid-template-columns: 1fr;
            }}

            .matrix-table {{
                font-size: 0.7rem;
            }}

            .matrix-table th, .matrix-table td {{
                padding: 0.5rem;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>📚 Bitcoin Educational Content - Proofreading Dashboard</h1>
        <div class="metadata">
            Last updated: <span id="last-update">Loading...</span> |
            <span id="total-content">0</span> content items |
            <span id="total-languages">0</span> languages
        </div>
    </header>

    <div class="container">
        <!-- Statistics -->
        <div class="section">
            <h2>📊 Overview</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value" id="stat-courses">0</div>
                    <div class="stat-label">Courses</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="stat-tutorials">0</div>
                    <div class="stat-label">Tutorials</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="stat-complete">0</div>
                    <div class="stat-label">Fully Proofread (Status 3)</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="stat-urgent">0</div>
                    <div class="stat-label">Needs Proofreading (Status 0)</div>
                </div>
            </div>
        </div>

        <!-- Section 1: Matrix Overview -->
        <div class="section">
            <h2>📋 Content Matrix Overview</h2>

            <div class="type-selector">
                <label class="type-option active">
                    <input type="radio" name="content-type" value="course" checked>
                    <span>Courses</span>
                </label>
                <label class="type-option">
                    <input type="radio" name="content-type" value="tutorial">
                    <span>Tutorials</span>
                </label>
            </div>

            <div class="filters">
                <div class="filter-group">
                    <label for="matrix-topic">Topic/Category:</label>
                    <select id="matrix-topic">
                        <option value="all">All Topics</option>
                    </select>
                </div>

                <div class="filter-group">
                    <label for="matrix-level">Difficulty:</label>
                    <select id="matrix-level">
                        <option value="all">All Levels</option>
                        <option value="beginner">Beginner</option>
                        <option value="intermediate">Intermediate</option>
                        <option value="advanced">Advanced</option>
                        <option value="expert">Expert</option>
                        <option value="wizard">Wizard</option>
                    </select>
                </div>

                <div class="filter-group">
                    <label for="matrix-search">Search:</label>
                    <input type="text" id="matrix-search" placeholder="Search content...">
                </div>
            </div>

            <div class="matrix-container">
                <table class="matrix-table" id="matrix-table">
                    <thead>
                        <tr id="matrix-header">
                            <th>Content</th>
                        </tr>
                    </thead>
                    <tbody id="matrix-tbody">
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Section 2: Contribution Finder -->
        <div class="section">
            <h2>🎯 Contribution Finder - Where You're Needed Most (Top 10)</h2>

            <div class="filters">
                <div class="filter-group">
                    <label for="contrib-language">Select Your Language:</label>
                    <select id="contrib-language">
                        <option value="">Choose a language...</option>
                    </select>
                </div>

                <div class="filter-group">
                    <label for="contrib-type">Content Type:</label>
                    <select id="contrib-type">
                        <option value="both">Both</option>
                        <option value="course">Courses Only</option>
                        <option value="tutorial">Tutorials Only</option>
                    </select>
                </div>

                <div class="filter-group">
                    <label for="contrib-category">Topic/Category:</label>
                    <select id="contrib-category">
                        <option value="all">All Topics</option>
                    </select>
                </div>

                <div class="filter-group">
                    <label for="contrib-level">Difficulty:</label>
                    <select id="contrib-level">
                        <option value="all">All Levels</option>
                        <option value="beginner">Beginner</option>
                        <option value="intermediate">Intermediate</option>
                        <option value="advanced">Advanced</option>
                        <option value="expert">Expert</option>
                        <option value="wizard">Wizard</option>
                    </select>
                </div>
            </div>

            <div id="contribution-results" class="contribution-list">
                <div class="empty-state">
                    Select a language to see where contributions are needed most.
                </div>
            </div>
        </div>

        <!-- Section 3: Leaderboards -->
        <div class="section">
            <h2>🏆 Leaderboards</h2>

            <div class="tabs">
                <button class="tab active" data-tab="course-contributors">Top Course Contributors</button>
                <button class="tab" data-tab="tutorial-contributors">Top Tutorial Contributors</button>
                <button class="tab" data-tab="top-languages">Top Languages</button>
            </div>

            <!-- Course Contributors Tab -->
            <div id="course-contributors" class="tab-content active">
                <div id="course-contributors-content"></div>
            </div>

            <!-- Tutorial Contributors Tab -->
            <div id="tutorial-contributors" class="tab-content">
                <div id="tutorial-contributors-content"></div>
            </div>

            <!-- Top Languages Tab -->
            <div id="top-languages" class="tab-content">
                <div class="table-container">
                    <table class="lang-stats-table">
                        <thead>
                            <tr>
                                <th>Language</th>
                                <th>Total Proofreadings</th>
                                <th>Unique Contributors</th>
                            </tr>
                        </thead>
                        <tbody id="lang-stats-tbody">
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Embedded proofreading data
        const PROOFREADING_DATA = {json_data};

        // Global state
        let currentContentType = 'course';
        let currentMatrixData = [];

        // Initialize dashboard
        function init() {{
            console.log('Initializing dashboard...');

            // Update metadata
            const {{ metadata }} = PROOFREADING_DATA;
            document.getElementById('last-update').textContent = new Date(metadata.generated_at).toLocaleString();
            document.getElementById('total-content').textContent = metadata.total_courses + metadata.total_tutorials;
            document.getElementById('total-languages').textContent = metadata.total_languages;

            // Update stats
            updateStats();

            // Populate filter dropdowns
            populateFilters();

            // Render language stats
            renderLanguageStats();

            // Render initial matrix
            renderMatrix();

            // Setup event listeners
            setupEventListeners();

            // Render leaderboards
            renderCourseContributors();
            renderTutorialContributors();

            console.log('Dashboard initialized successfully');
        }}

        function updateStats() {{
            const {{ courses, tutorials }} = PROOFREADING_DATA;

            document.getElementById('stat-courses').textContent = courses.length;
            document.getElementById('stat-tutorials').textContent = tutorials.length;

            let completeCount = 0;
            let urgentCount = 0;

            [...courses, ...tutorials].forEach(item => {{
                item.proofreading.forEach(pr => {{
                    if (pr.status === 3) completeCount++;
                    if (pr.status === 0) urgentCount++;
                }});
            }});

            document.getElementById('stat-complete').textContent = completeCount;
            document.getElementById('stat-urgent').textContent = urgentCount;
        }}

        function populateFilters() {{
            const {{ languages, topics, categories }} = PROOFREADING_DATA;

            // Contribution finder language filter
            const contribLang = document.getElementById('contrib-language');
            languages.forEach(lang => {{
                const option = document.createElement('option');
                option.value = lang.code;
                option.textContent = lang.name;
                contribLang.appendChild(option);
            }});

            // Initialize topic filters
            updateTopicFilter();
        }}

        function renderLanguageStats() {{
            const {{ language_stats, languages }} = PROOFREADING_DATA;
            const tbody = document.getElementById('lang-stats-tbody');

            // Convert to array and sort by total proofreadings (descending)
            const sortedLangs = Object.entries(language_stats)
                .map(([code, stats]) => ({{
                    code,
                    name: languages.find(l => l.code === code)?.name || code,
                    ...stats
                }}))
                .sort((a, b) => b.total_proofreadings - a.total_proofreadings);

            tbody.innerHTML = '';

            sortedLangs.forEach(lang => {{
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>
                        <div class="lang-code">${{lang.code.toUpperCase()}}</div>
                        <div class="lang-name">${{lang.name}}</div>
                    </td>
                    <td><span class="stat-number">${{lang.total_proofreadings}}</span></td>
                    <td><span class="contributor-count">${{lang.unique_contributors}}</span></td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        function updateTopicFilter() {{
            const {{ topics, categories }} = PROOFREADING_DATA;
            const topicSelect = document.getElementById('matrix-topic');
            const contribCategorySelect = document.getElementById('contrib-category');

            const items = currentContentType === 'course' ? topics : categories;

            // Matrix topic filter
            topicSelect.innerHTML = '<option value="all">All Topics</option>';
            items.forEach(item => {{
                const option = document.createElement('option');
                option.value = item;
                option.textContent = item.charAt(0).toUpperCase() + item.slice(1);
                topicSelect.appendChild(option);
            }});

            // Contribution finder category filter
            contribCategorySelect.innerHTML = '<option value="all">All Topics</option>';
            const allItems = [...topics, ...categories];
            [...new Set(allItems)].sort().forEach(item => {{
                const option = document.createElement('option');
                option.value = item;
                option.textContent = item.charAt(0).toUpperCase() + item.slice(1);
                contribCategorySelect.appendChild(option);
            }});
        }}

        function getContentData() {{
            return currentContentType === 'course' ? PROOFREADING_DATA.courses : PROOFREADING_DATA.tutorials;
        }}

        function filterMatrixData() {{
            let data = getContentData();

            const topic = document.getElementById('matrix-topic').value;
            const level = document.getElementById('matrix-level').value;
            const search = document.getElementById('matrix-search').value.toLowerCase();

            data = data.filter(item => {{
                if (topic !== 'all') {{
                    const itemTopic = currentContentType === 'course' ? item.topic : item.category;
                    if (itemTopic !== topic) return false;
                }}
                if (level !== 'all' && item.level !== level) return false;
                if (search && !item.id.toLowerCase().includes(search) && !item.name.toLowerCase().includes(search)) return false;
                return true;
            }});

            return data;
        }}

        function renderMatrix() {{
            const data = filterMatrixData();
            const {{ languages }} = PROOFREADING_DATA;

            // Render header
            const header = document.getElementById('matrix-header');
            header.innerHTML = '<th>Content</th>';
            languages.forEach(lang => {{
                const th = document.createElement('th');
                th.textContent = lang.code.toUpperCase();
                th.title = lang.name;
                header.appendChild(th);
            }});

            // Render body
            const tbody = document.getElementById('matrix-tbody');
            tbody.innerHTML = '';

            if (data.length === 0) {{
                const tr = document.createElement('tr');
                tr.innerHTML = `<td colspan="${{languages.length + 1}}" class="empty-state">No content found</td>`;
                tbody.appendChild(tr);
                return;
            }}

            data.forEach(item => {{
                const tr = document.createElement('tr');

                // Content name cell
                const nameTd = document.createElement('td');
                nameTd.textContent = item.id;
                nameTd.title = item.name;
                tr.appendChild(nameTd);

                // Language cells
                languages.forEach(lang => {{
                    const td = document.createElement('td');
                    const pr = item.proofreading.find(p => p.language === lang.code);

                    if (pr) {{
                        const status = pr.status; // 0, 1, 2, or 3
                        const total = 3;
                        const contributorCount = status;
                        const percentage = Math.round((status / 3) * 100);

                        let className = 'matrix-empty';
                        if (status === 3) className = 'matrix-complete';
                        else if (status === 2) className = 'matrix-partial';
                        else if (status === 1) className = 'matrix-partial';

                        td.className = className;
                        td.innerHTML = `
                            <div class="matrix-cell">
                                <div class="matrix-cell-count">${{contributorCount}}/${{total}}</div>
                                <div class="matrix-cell-percentage">${{percentage}}%</div>
                            </div>
                        `;
                    }} else {{
                        td.className = 'matrix-na';
                        td.innerHTML = `
                            <div class="matrix-cell">
                                <div>N/A</div>
                                <div style="font-size: 0.7rem;">No content</div>
                            </div>
                        `;
                    }}

                    tr.appendChild(td);
                }});

                tbody.appendChild(tr);
            }});
        }}

        function renderContributionFinder() {{
            const language = document.getElementById('contrib-language').value;
            const type = document.getElementById('contrib-type').value;
            const category = document.getElementById('contrib-category').value;
            const level = document.getElementById('contrib-level').value;

            const resultsDiv = document.getElementById('contribution-results');

            if (!language) {{
                resultsDiv.innerHTML = '<div class="empty-state">Select a language to see where contributions are needed most.</div>';
                return;
            }}

            // Flatten data
            const {{ courses, tutorials }} = PROOFREADING_DATA;
            let allItems = [];

            if (type === 'both' || type === 'course') {{
                courses.forEach(course => {{
                    const pr = course.proofreading.find(p => p.language === language);
                    if (pr) {{
                        allItems.push({{
                            ...course,
                            proofreading: pr,
                            topic_display: course.topic
                        }});
                    }}
                }});
            }}

            if (type === 'both' || type === 'tutorial') {{
                tutorials.forEach(tutorial => {{
                    const pr = tutorial.proofreading.find(p => p.language === language);
                    if (pr) {{
                        allItems.push({{
                            ...tutorial,
                            proofreading: pr,
                            topic_display: tutorial.category
                        }});
                    }}
                }});
            }}

            // Filter by category and level
            allItems = allItems.filter(item => {{
                if (category !== 'all' && item.topic_display !== category) return false;
                if (level !== 'all' && item.level !== level) return false;
                return true;
            }});

            // Sort by status (0 first) and then by reward
            allItems.sort((a, b) => {{
                if (a.proofreading.status !== b.proofreading.status) {{
                    return a.proofreading.status - b.proofreading.status;
                }}
                return b.proofreading.reward - a.proofreading.reward;
            }});

            // Limit to top 10
            allItems = allItems.slice(0, 10);

            if (allItems.length === 0) {{
                resultsDiv.innerHTML = '<div class="empty-state">No content found for the selected filters.</div>';
                return;
            }}

            resultsDiv.innerHTML = '';

            allItems.forEach(item => {{
                const pr = item.proofreading;
                const statusText = ['Urgent - No Contributors', 'Needs Review - 1 Contributor', 'In Progress - 2 Contributors', 'Complete - 3+ Contributors'][pr.status];
                const contributorsNeeded = Math.max(0, 3 - pr.contributors.length);
                const lastUpdate = pr.last_date ? `Last updated: ${{pr.last_date}}` : 'Never updated';

                const div = document.createElement('div');
                div.className = 'contribution-item';
                div.innerHTML = `
                    <div class="contribution-header">
                        <div class="contribution-title">${{item.name}} (${{item.id}})</div>
                        <span class="reward-badge">Reward: ${{pr.reward.toFixed(2)}}</span>
                    </div>
                    <div class="contribution-details">
                        <span class="status-badge status-${{pr.status}}">${{statusText}}</span>
                        <span class="level-badge">${{item.level}}</span>
                        <span>Contributors needed: <strong>${{contributorsNeeded}}</strong></span>
                        <span>${{lastUpdate}}</span>
                    </div>
                `;

                resultsDiv.appendChild(div);
            }});
        }}

        function renderCourseContributors() {{
            const contentDiv = document.getElementById('course-contributors-content');
            const {{ course_contributor_stats }} = PROOFREADING_DATA;

            // Sort contributors by total contributions
            const sortedContributors = Object.entries(course_contributor_stats)
                .map(([name, stats]) => ({{ name, ...stats }}))
                .sort((a, b) => b.total_contributions - a.total_contributions)
                .slice(0, 20); // Top 20

            if (sortedContributors.length === 0) {{
                contentDiv.innerHTML = '<div class="empty-state">No contributors found</div>';
                return;
            }}

            contentDiv.innerHTML = '';

            sortedContributors.forEach((contributor, index) => {{
                const medal = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : '';
                const rank = medal || `#${{index + 1}}`;

                const div = document.createElement('div');
                div.className = 'leaderboard-item';
                div.innerHTML = `
                    <div class="rank">${{rank}}</div>
                    <img class="avatar"
                         src="https://github.com/${{contributor.name}}.png"
                         alt="${{contributor.name}}"
                         onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Crect fill=%22%23ddd%22 width=%22100%22 height=%22100%22/%3E%3Ctext x=%2250%22 y=%2250%22 fill=%22%23999%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22sans-serif%22 font-size=%2240%22%3E?%3C/text%3E%3C/svg%3E'">
                    <div class="contributor-info">
                        <div class="contributor-name">
                            <a href="https://github.com/${{contributor.name}}" target="_blank">${{contributor.name}}</a>
                        </div>
                        <div class="contributor-stats">
                            ${{contributor.courses}} courses •
                            Languages: ${{contributor.languages.join(', ')}}
                        </div>
                    </div>
                    <div class="contribution-count">${{contributor.total_contributions}}</div>
                `;

                contentDiv.appendChild(div);
            }});
        }}

        function renderTutorialContributors() {{
            const contentDiv = document.getElementById('tutorial-contributors-content');
            const {{ tutorial_contributor_stats }} = PROOFREADING_DATA;

            // Sort contributors by total contributions
            const sortedContributors = Object.entries(tutorial_contributor_stats)
                .map(([name, stats]) => ({{ name, ...stats }}))
                .sort((a, b) => b.total_contributions - a.total_contributions)
                .slice(0, 20); // Top 20

            if (sortedContributors.length === 0) {{
                contentDiv.innerHTML = '<div class="empty-state">No contributors found</div>';
                return;
            }}

            contentDiv.innerHTML = '';

            sortedContributors.forEach((contributor, index) => {{
                const medal = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : '';
                const rank = medal || `#${{index + 1}}`;

                const div = document.createElement('div');
                div.className = 'leaderboard-item';
                div.innerHTML = `
                    <div class="rank">${{rank}}</div>
                    <img class="avatar"
                         src="https://github.com/${{contributor.name}}.png"
                         alt="${{contributor.name}}"
                         onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Crect fill=%22%23ddd%22 width=%22100%22 height=%22100%22/%3E%3Ctext x=%2250%22 y=%2250%22 fill=%22%23999%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22sans-serif%22 font-size=%2240%22%3E?%3C/text%3E%3C/svg%3E'">
                    <div class="contributor-info">
                        <div class="contributor-name">
                            <a href="https://github.com/${{contributor.name}}" target="_blank">${{contributor.name}}</a>
                        </div>
                        <div class="contributor-stats">
                            ${{contributor.tutorials}} tutorials •
                            Languages: ${{contributor.languages.join(', ')}}
                        </div>
                    </div>
                    <div class="contribution-count">${{contributor.total_contributions}}</div>
                `;

                contentDiv.appendChild(div);
            }});
        }}

        function setupEventListeners() {{
            // Content type selector
            document.querySelectorAll('input[name="content-type"]').forEach(radio => {{
                radio.addEventListener('change', (e) => {{
                    currentContentType = e.target.value;

                    // Update active state
                    document.querySelectorAll('.type-option').forEach(opt => {{
                        opt.classList.remove('active');
                    }});
                    e.target.closest('.type-option').classList.add('active');

                    updateTopicFilter();
                    renderMatrix();
                }});
            }});

            // Matrix filters
            document.getElementById('matrix-topic').addEventListener('change', renderMatrix);
            document.getElementById('matrix-level').addEventListener('change', renderMatrix);
            document.getElementById('matrix-search').addEventListener('input', renderMatrix);

            // Contribution finder
            document.getElementById('contrib-language').addEventListener('change', renderContributionFinder);
            document.getElementById('contrib-type').addEventListener('change', renderContributionFinder);
            document.getElementById('contrib-category').addEventListener('change', renderContributionFinder);
            document.getElementById('contrib-level').addEventListener('change', renderContributionFinder);

            // Tabs
            document.querySelectorAll('.tab').forEach(tab => {{
                tab.addEventListener('click', () => {{
                    const targetId = tab.dataset.tab;

                    // Update active tab
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    tab.classList.add('active');

                    // Update active content
                    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                    document.getElementById(targetId).classList.add('active');
                }});
            }});
        }}

        // Initialize on load
        window.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>"""

    return html


def main():
    """Main function to generate the dashboard."""
    print("=" * 60)
    print("Bitcoin Educational Content - Proofreading Dashboard Generator")
    print("=" * 60)

    # Extract data
    data = extract_all_data()

    # Generate HTML
    print("\nGenerating HTML dashboard...")
    html = generate_html(data)

    # Write to file
    output_file = 'proofreading_dashboard.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\n✅ Dashboard generated successfully: {output_file}")
    print(f"📊 File size: {len(html) / 1024:.1f} KB")
    print("\nTo view the dashboard, open the HTML file in your browser:")
    print(f"  file://{os.path.abspath(output_file)}")
    print("\nOr upload it to any web server.")
    print("=" * 60)


if __name__ == '__main__':
    main()
