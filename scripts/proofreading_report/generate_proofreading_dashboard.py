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
import re
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
from collections import defaultdict

# Load environment variables from .env file
def load_dotenv():
    """Load environment variables from .env file if it exists."""
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    os.environ.setdefault(key, value)

load_dotenv()

# GitHub API configuration
GITHUB_REPO = "PlanB-Network/bitcoin-educational-content"
GITHUB_API_BASE = "https://api.github.com"
GITHUB_CACHE_FILE = "github_pr_cache.json"

# Excluded contributors from monthly leaderboard (repo managers)
MONTHLY_EXCLUDED_CONTRIBUTORS = ['MariJJhodl']

# Language names mapping
LANGUAGE_NAMES = {
    'en': 'English', 'fr': 'French', 'de': 'German', 'es': 'Spanish',
    'it': 'Italian', 'pt': 'Portuguese', 'nl': 'Dutch', 'sv': 'Swedish',
    'nb-NO': 'Norwegian', 'cs': 'Czech', 'pl': 'Polish', 'ru': 'Russian',
    'sr-Latn': 'Serbian', 'et': 'Estonian', 'ja': 'Japanese',
    'zh-Hans': 'Chinese (Simplified)', 'zh-Hant': 'Chinese (Traditional)',
    'ko': 'Korean', 'vi': 'Vietnamese', 'hi': 'Hindi', 'id': 'Indonesian',
    'fa': 'Persian', 'tr': 'Turkish', 'sw': 'Swahili', 'rn': 'Kirundi',
    'bg': 'Bulgarian', 'th': 'Thai'
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


def extract_english_title(content_dir):
    """Extract the English title from en.md file."""
    en_file = Path(content_dir) / 'en.md'
    try:
        if en_file.exists():
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract YAML front matter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        yaml_content = parts[1]
                        yaml_data = yaml.safe_load(yaml_content)
                        return yaml_data.get('name', '')
        return ''
    except Exception as e:
        print(f"Error extracting title from {en_file}: {e}")
        return ''


def parse_course_file(filepath, base_dir):
    """Parse a course.yml file and extract proofreading data."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # Extract course ID from path
        course_id = Path(filepath).parent.name

        # Extract English title from en.md file
        course_dir = Path(filepath).parent
        english_title = extract_english_title(course_dir)

        course_data = {
            'id': course_id,
            'name': data.get('name', course_id.upper()),
            'english_title': english_title,
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

        # Extract English title from en.md file
        tutorial_dir = Path(filepath).parent
        english_title = extract_english_title(tutorial_dir)

        tutorial_data = {
            'id': f"{category}/{tutorial_name}",
            'name': data.get('name', tutorial_name.replace('-', ' ').title()),
            'english_title': english_title,
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


def load_github_cache():
    """Load cached GitHub PR data if available and fresh (less than 1 hour old)."""
    cache_path = Path(__file__).parent / GITHUB_CACHE_FILE
    if cache_path.exists():
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                cache = json.load(f)
            # Check if cache is fresh (less than 1 hour old)
            cached_at = datetime.fromisoformat(cache.get('cached_at', '2000-01-01T00:00:00'))
            if datetime.now(timezone.utc) - cached_at.replace(tzinfo=timezone.utc) < timedelta(hours=1):
                print(f"Using cached GitHub data (cached at {cache['cached_at']})")
                return cache.get('data')
            else:
                print("Cache expired, fetching fresh data...")
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Cache invalid: {e}")
    return None


def save_github_cache(data):
    """Save GitHub PR data to cache."""
    cache_path = Path(__file__).parent / GITHUB_CACHE_FILE
    cache = {
        'cached_at': datetime.now(timezone.utc).isoformat(),
        'data': data
    }
    try:
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2, default=str)
        print(f"Cached GitHub data to {cache_path}")
    except IOError as e:
        print(f"Failed to save cache: {e}")


def check_github_api_status():
    """Check if GitHub API is accessible and show rate limit status."""
    print("\n🔍 Checking GitHub API connection...")

    headers = {
        'User-Agent': 'Bitcoin-Educational-Content-Dashboard',
        'Accept': 'application/vnd.github.v3+json'
    }

    github_token = os.environ.get('GITHUB_TOKEN')
    if github_token:
        headers['Authorization'] = f'token {github_token}'
        print("   ✓ GITHUB_TOKEN found in environment")
    else:
        print("   ⚠ No GITHUB_TOKEN found - using unauthenticated access (60 req/hour)")

    try:
        req = urllib.request.Request(f"{GITHUB_API_BASE}/rate_limit", headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))

            core = data['resources']['core']
            search = data['resources']['search']

            core_remaining = core['remaining']
            core_limit = core['limit']
            search_remaining = search['remaining']
            search_limit = search['limit']

            reset_time = datetime.fromtimestamp(core['reset'])

            print(f"   ✓ GitHub API is accessible")
            print(f"   📊 Core API: {core_remaining}/{core_limit} requests remaining")
            print(f"   📊 Search API: {search_remaining}/{search_limit} requests remaining")
            print(f"   ⏰ Rate limit resets at: {reset_time.strftime('%H:%M:%S')}")

            if core_remaining < 50:
                print(f"   ⚠ Warning: Low API quota remaining!")

            return True, core_remaining, search_remaining

    except urllib.error.HTTPError as e:
        if e.code == 401:
            print(f"   ✗ Invalid GITHUB_TOKEN - authentication failed")
        else:
            print(f"   ✗ GitHub API error: {e.code} - {e.reason}")
        return False, 0, 0
    except urllib.error.URLError as e:
        print(f"   ✗ Network error: {e.reason}")
        return False, 0, 0
    except Exception as e:
        print(f"   ✗ Unexpected error: {e}")
        return False, 0, 0


def github_api_request(url, headers=None, retry_count=3, silent=False):
    """Make a request to the GitHub API with rate limit handling."""
    import time

    if headers is None:
        headers = {}
    headers['User-Agent'] = 'Bitcoin-Educational-Content-Dashboard'
    headers['Accept'] = 'application/vnd.github.v3+json'

    # Check for GitHub token in environment
    github_token = os.environ.get('GITHUB_TOKEN')
    if github_token:
        headers['Authorization'] = f'token {github_token}'

    for attempt in range(retry_count):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 403 or e.code == 429:
                # Rate limited - check for retry-after header
                retry_after = e.headers.get('Retry-After', '60')
                try:
                    wait_time = int(retry_after)
                except ValueError:
                    wait_time = 60

                if attempt < retry_count - 1:
                    # Use shorter wait for retries, max 5 seconds between retries
                    actual_wait = min(wait_time, 2 * (attempt + 1))
                    if not silent:
                        print(f"      ⏳ Rate limited, waiting {actual_wait}s before retry {attempt + 2}/{retry_count}...")
                    time.sleep(actual_wait)
                    continue
                else:
                    if not silent:
                        print(f"      ✗ Rate limit exceeded after {retry_count} attempts")
                        if not github_token:
                            print("      TIP: Add GITHUB_TOKEN to .env file for higher rate limits")
                    return None
            else:
                if not silent:
                    print(f"      ✗ GitHub API error: {e.code} - {e.reason}")
                return None
        except urllib.error.URLError as e:
            if not silent:
                print(f"      ✗ Network error: {e.reason}")
            if attempt < retry_count - 1:
                time.sleep(2)
                continue
            return None

    return None


def extract_language_from_path(file_path):
    """Extract language code from a file path.

    Patterns:
    - courses/course-name/fr.md -> fr
    - tutorials/category/tutorial-name/fr.md -> fr
    - courses/course-name/assets/fr/... -> fr
    """
    # Match language code in path (2-letter or with region like zh-Hans)
    # Common patterns: /fr.md, /fr/, /de.md, /zh-Hans.md, etc.

    # Pattern for direct language file (e.g., fr.md, de.md, zh-Hans.md)
    lang_file_match = re.search(r'/([a-z]{2}(?:-[A-Za-z]+)?)\.md$', file_path)
    if lang_file_match:
        return lang_file_match.group(1).lower()

    # Pattern for language folder (e.g., /fr/, /de/, /zh-Hans/)
    lang_folder_match = re.search(r'/([a-z]{2}(?:-[A-Za-z]+)?)/[^/]+$', file_path)
    if lang_folder_match:
        return lang_folder_match.group(1).lower()

    # Pattern for assets with language subfolder
    assets_match = re.search(r'/assets/([a-z]{2}(?:-[A-Za-z]+)?)/', file_path)
    if assets_match:
        return assets_match.group(1).lower()

    return None


def detect_content_type_from_path(file_path):
    """Detect if the file is from a course or tutorial."""
    if file_path.startswith('courses/'):
        return 'COURSE'
    elif file_path.startswith('tutorials/'):
        return 'TUTORIAL'
    return 'OTHER'


# Mapping of language names to language codes for title/label extraction
LANGUAGE_NAME_TO_CODE = {
    # English variations
    'english': 'en', 'en': 'en', 'eng': 'en',
    # French variations
    'french': 'fr', 'fr': 'fr', 'français': 'fr', 'francais': 'fr', 'fre': 'fr',
    # German variations
    'german': 'de', 'de': 'de', 'deutsch': 'de', 'ger': 'de',
    # Spanish variations
    'spanish': 'es', 'es': 'es', 'español': 'es', 'espanol': 'es', 'spa': 'es',
    # Italian variations
    'italian': 'it', 'it': 'it', 'italiano': 'it', 'ita': 'it',
    # Portuguese variations
    'portuguese': 'pt', 'pt': 'pt', 'português': 'pt', 'portugues': 'pt', 'por': 'pt',
    # Dutch variations
    'dutch': 'nl', 'nl': 'nl', 'nederlands': 'nl',
    # Swedish variations
    'swedish': 'sv', 'sv': 'sv', 'svenska': 'sv',
    # Norwegian variations
    'norwegian': 'nb-NO', 'nb-no': 'nb-NO', 'norsk': 'nb-NO',
    # Czech variations
    'czech': 'cs', 'cs': 'cs', 'čeština': 'cs', 'cestina': 'cs', 'cz': 'cs',
    # Polish variations
    'polish': 'pl', 'pl': 'pl', 'polski': 'pl', 'pol': 'pl',
    # Russian variations
    'russian': 'ru', 'ru': 'ru', 'русский': 'ru',
    # Serbian variations
    'serbian': 'sr-Latn', 'sr-latn': 'sr-Latn', 'sr latin': 'sr-Latn', 'srpski': 'sr-Latn',
    # Estonian variations
    'estonian': 'et', 'et': 'et', 'eesti': 'et',
    # Japanese variations
    'japanese': 'ja', 'ja': 'ja', '日本語': 'ja', 'jpn': 'ja',
    # Chinese variations - Simplified
    'chinese': 'zh-Hans', 'zh-hans': 'zh-Hans', 'simplified chinese': 'zh-Hans',
    'simplified': 'zh-Hans', 'zh hans': 'zh-Hans',
    # Chinese variations - Traditional
    'traditional chinese': 'zh-Hant', 'zh-hant': 'zh-Hant', 'traditional': 'zh-Hant',
    'zh hant': 'zh-Hant',
    # Korean variations
    'korean': 'ko', 'ko': 'ko', '한국어': 'ko', 'kor': 'ko',
    # Vietnamese variations
    'vietnamese': 'vi', 'vi': 'vi', 'tiếng việt': 'vi', 'viet': 'vi', 'vietnam': 'vi',
    # Hindi variations
    'hindi': 'hi', 'hi': 'hi', 'हिन्दी': 'hi',
    # Indonesian variations
    'indonesian': 'id', 'id': 'id', 'bahasa indonesia': 'id', 'indo': 'id',
    # Persian variations
    'persian': 'fa', 'fa': 'fa', 'farsi': 'fa', 'فارسی': 'fa',
    # Turkish variations
    'turkish': 'tr', 'tr': 'tr', 'türkçe': 'tr', 'turkce': 'tr', 'tur': 'tr',
    # Swahili variations
    'swahili': 'sw', 'sw': 'sw', 'kiswahili': 'sw',
    # Kirundi variations
    'kirundi': 'rn', 'rn': 'rn', 'rundi': 'rn',
    # Bulgarian variations
    'bulgarian': 'bg', 'bg': 'bg', 'български': 'bg', 'bul': 'bg',
}


def extract_language_from_title(title):
    """Extract language from PR title.

    Looks for language names at the end of title, typically after a dash.
    Examples:
    - [PROOFREADING] BTC101 - French -> fr
    - [PROOFREADING] SCU101 + quiz - Bulgarian -> bg
    - [PROOFREADING] BTC102 - Rundi -> rn
    - [PROOFREADING] BTC101 only quizzes - Vietnamese -> vi
    - [PROOFREADING] BTC202 + Quiz - Simplified Chinese -> zh-Hans
    """
    if not title:
        return None

    title_lower = title.lower()

    # Try to find language after last dash or hyphen
    parts = re.split(r'\s*[-–—]\s*', title_lower)
    if len(parts) >= 2:
        last_part = parts[-1].strip()
        # Remove common suffixes/extras like #1234, (123), .md, quizzes, only, &, +, section, numbers
        last_part_cleaned = re.sub(r'\s*(#\d+|\(\d+\)|\.md|quizz?e?s?|only|&|\+|section|\d+).*$', '', last_part).strip()

        if last_part_cleaned in LANGUAGE_NAME_TO_CODE:
            return LANGUAGE_NAME_TO_CODE[last_part_cleaned]

        # Also check the uncleaned last part for multi-word languages like "Simplified Chinese"
        if last_part in LANGUAGE_NAME_TO_CODE:
            return LANGUAGE_NAME_TO_CODE[last_part]

        # Check if it starts with a known language (e.g., "simplified chi..." truncated)
        for lang_name in sorted(LANGUAGE_NAME_TO_CODE.keys(), key=len, reverse=True):
            if last_part_cleaned.startswith(lang_name) or last_part.startswith(lang_name):
                return LANGUAGE_NAME_TO_CODE[lang_name]

    # Check full title for language names (longer names first to match "simplified chinese" before "chinese")
    for lang_name in sorted(LANGUAGE_NAME_TO_CODE.keys(), key=len, reverse=True):
        # Look for language name as a whole word (not part of another word)
        if re.search(rf'\b{re.escape(lang_name)}\b', title_lower):
            return LANGUAGE_NAME_TO_CODE[lang_name]

    return None


def extract_language_from_labels(labels):
    """Extract language from PR labels.

    Labels are typically like: 'lang:fr', 'language:french', 'French', etc.
    """
    if not labels:
        return None

    for label in labels:
        label_name = label.get('name', '').lower() if isinstance(label, dict) else str(label).lower()

        # Check for lang: prefix
        lang_prefix_match = re.match(r'^lang(?:uage)?[:\-]?\s*(.+)$', label_name)
        if lang_prefix_match:
            lang_value = lang_prefix_match.group(1).strip()
            if lang_value in LANGUAGE_NAME_TO_CODE:
                return LANGUAGE_NAME_TO_CODE[lang_value]

        # Check if label itself is a language name
        if label_name in LANGUAGE_NAME_TO_CODE:
            return LANGUAGE_NAME_TO_CODE[label_name]

    return None


def fetch_proofreading_prs_from_github(num_months=3):
    """Fetch merged PRs with [PROOFREADING] in title from GitHub API.

    Uses the Pulls API directly which includes merged_at date, avoiding
    the need for individual PR detail fetches.
    """
    print("\n🔄 Fetching proofreading PRs from GitHub API...")

    # Calculate date range
    now = datetime.now(timezone.utc)

    # Get first day of the month num_months ago
    target_month = now.month - num_months + 1
    target_year = now.year
    while target_month <= 0:
        target_month += 12
        target_year -= 1

    since_date = datetime(target_year, target_month, 1, tzinfo=timezone.utc)
    since_date_str = since_date.strftime('%Y-%m-%d')
    print(f"   📆 Searching for PRs since {since_date.strftime('%B %Y')}")

    all_prs = []
    page = 1
    per_page = 100

    # Use Pulls API endpoint which returns merged_at directly
    # Filter by state=closed and we'll check merged_at ourselves
    while True:
        print(f"   🔍 Fetching page {page}...", end='', flush=True)

        # List closed PRs sorted by update time (most recent first)
        pulls_url = (
            f"{GITHUB_API_BASE}/repos/{GITHUB_REPO}/pulls?"
            f"state=closed&sort=updated&direction=desc&per_page={per_page}&page={page}"
        )

        result = github_api_request(pulls_url, silent=True)
        if not result:
            print(" ✗ (API error)")
            break

        if not result:
            print(" (no more results)")
            break

        print(f" found {len(result)} closed PRs", end='', flush=True)

        prs_added = 0
        oldest_pr_date = None

        for pr in result:
            # Check if PR was merged (not just closed)
            merged_at_str = pr.get('merged_at')
            if not merged_at_str:
                continue

            merged_at = datetime.fromisoformat(merged_at_str.replace('Z', '+00:00'))
            oldest_pr_date = merged_at

            # Skip if before our date range
            if merged_at < since_date:
                continue

            # Check if title contains [PROOFREADING]
            title = pr.get('title', '')
            if '[PROOFREADING]' not in title.upper():
                continue

            all_prs.append({
                'number': pr['number'],
                'title': title,
                'merged_at': merged_at,
                'user': pr['user']['login'],
                'html_url': pr['html_url'],
                'labels': pr.get('labels', [])  # Include labels for language detection
            })
            prs_added += 1

        print(f" ✓ +{prs_added} proofreading PRs")

        # Stop if we've gone past our date range
        if oldest_pr_date and oldest_pr_date < since_date:
            print(f"   📆 Reached PRs from before {since_date.strftime('%B %Y')}, stopping")
            break

        # Stop if we got fewer results than requested (last page)
        if len(result) < per_page:
            break

        page += 1

        # Safety limit
        if page > 20:
            print("   ⚠️  Reached page limit, stopping pagination")
            break

    print(f"\n   ✅ Found {len(all_prs)} proofreading PRs in the last {num_months} months")
    return all_prs


def fetch_pr_files_and_contributors(pr_number):
    """Fetch the files changed and contributors for a specific PR."""
    # Get files changed
    files_url = f"{GITHUB_API_BASE}/repos/{GITHUB_REPO}/pulls/{pr_number}/files"
    files_data = github_api_request(files_url)

    files = []
    if files_data:
        files = [f['filename'] for f in files_data]

    # Get PR details for author
    pr_url = f"{GITHUB_API_BASE}/repos/{GITHUB_REPO}/pulls/{pr_number}"
    pr_data = github_api_request(pr_url)

    contributors = set()
    if pr_data:
        # Add PR author
        author = pr_data.get('user', {}).get('login')
        if author and author not in MONTHLY_EXCLUDED_CONTRIBUTORS:
            contributors.add(author)

    return files, list(contributors)


def calculate_monthly_language_stats(courses=None, tutorials=None, num_months=3, skip_api=False):
    """Calculate monthly language team statistics from GitHub PRs.

    Args:
        courses: Not used (kept for backwards compatibility)
        tutorials: Not used (kept for backwards compatibility)
        num_months: Number of months to fetch
        skip_api: If True, only use cached data, don't make API calls
    """

    # Try to load from cache first
    cached_data = load_github_cache()
    if cached_data:
        return cached_data

    if skip_api:
        print("⏭️  Skipping GitHub API calls (--skip-github-api flag)")
        print("   To fetch fresh data, remove the flag or wait for rate limit reset")
        return []

    # Check API status first
    api_ok, core_remaining, search_remaining = check_github_api_status()
    if not api_ok:
        print("\n❌ Cannot access GitHub API. Monthly leaderboard will be empty.")
        return []

    if core_remaining < 10 or search_remaining < 5:
        print("\n⚠️  Insufficient API quota remaining. Skipping GitHub fetch.")
        return []

    # Fetch PRs from GitHub
    prs = fetch_proofreading_prs_from_github(num_months)

    if not prs:
        print("❌ No PRs found or API error, returning empty stats")
        return []

    # Organize by month
    now = datetime.now(timezone.utc)
    monthly_data = {}

    for month_offset in range(num_months):
        # Calculate target month
        total_months = now.year * 12 + now.month - month_offset
        year = total_months // 12
        month = total_months % 12
        if month == 0:
            month = 12
            year -= 1

        month_key = f"{year}-{month:02d}"
        month_name = datetime(year, month, 1).strftime('%B %Y')

        monthly_data[month_key] = {
            'month_name': month_name,
            'year': year,
            'month': month,
            'lang_counts': defaultdict(lambda: {
                'count': 0,
                'contributors': set(),
                'content_types': defaultdict(int),
                'pr_numbers': []
            })
        }

    # Group PRs by month for better logging
    prs_by_month = defaultdict(list)
    for pr in prs:
        month_key = f"{pr['merged_at'].year}-{pr['merged_at'].month:02d}"
        if month_key in monthly_data:
            prs_by_month[month_key].append(pr)

    # Process PRs month by month
    total_processed = 0
    for month_key in sorted(prs_by_month.keys(), reverse=True):
        month_prs = prs_by_month[month_key]
        month_name = monthly_data[month_key]['month_name']

        print(f"\n📅 Processing {month_name} ({len(month_prs)} PRs)...")

        for i, pr in enumerate(month_prs):
            total_processed += 1
            # Show progress inline
            print(f"   [{i+1}/{len(month_prs)}] PR #{pr['number']}: {pr['title'][:45]}...", end='', flush=True)

            # Fetch files and contributors
            files, contributors = fetch_pr_files_and_contributors(pr['number'])

            # Detect languages from files
            languages_in_pr = set()
            content_types_in_pr = defaultdict(set)

            for file_path in files:
                lang = extract_language_from_path(file_path)
                if lang:
                    # Normalize language code
                    lang = lang.lower()
                    # Map common variations
                    if lang == 'zh-hans':
                        lang = 'zh-Hans'
                    elif lang == 'zh-hant':
                        lang = 'zh-Hant'
                    elif lang == 'nb-no':
                        lang = 'nb-NO'
                    elif lang == 'sr-latn':
                        lang = 'sr-Latn'

                    languages_in_pr.add(lang)
                    content_type = detect_content_type_from_path(file_path)
                    content_types_in_pr[lang].add(content_type)

            # If no language detected from files, try title and labels
            lang_source = "files"
            if not languages_in_pr:
                # Try title first
                title_lang = extract_language_from_title(pr['title'])
                if title_lang:
                    languages_in_pr.add(title_lang)
                    lang_source = "title"
                else:
                    # Try labels
                    label_lang = extract_language_from_labels(pr.get('labels', []))
                    if label_lang:
                        languages_in_pr.add(label_lang)
                        lang_source = "label"

            # Update monthly counts
            lang_counts = monthly_data[month_key]['lang_counts']
            for lang in languages_in_pr:
                lang_counts[lang]['count'] += 1
                lang_counts[lang]['pr_numbers'].append(pr['number'])

                for contributor in contributors:
                    lang_counts[lang]['contributors'].add(contributor)

                for content_type in content_types_in_pr[lang]:
                    if content_type in ('COURSE', 'TUTORIAL'):
                        lang_counts[lang]['content_types'][content_type] += 1

            # Show detected languages
            if languages_in_pr:
                source_indicator = f" ({lang_source})" if lang_source != "files" else ""
                print(f" ✓ [{', '.join(sorted(languages_in_pr))}]{source_indicator}")
            else:
                print(f" (no language detected)")

        # Summary for this month
        month_langs = monthly_data[month_key]['lang_counts']
        if month_langs:
            top_langs = sorted(month_langs.items(), key=lambda x: x[1]['count'], reverse=True)[:3]
            top_str = ', '.join([f"{l[0].upper()}:{l[1]['count']}" for l in top_langs])
            print(f"   ✅ {month_name} complete - Top languages: {top_str}")

    # Convert to final format
    monthly_stats = []
    for month_key in sorted(monthly_data.keys(), reverse=True):
        data = monthly_data[month_key]
        lang_counts = data['lang_counts']

        languages = []
        for lang_code, counts in sorted(lang_counts.items(), key=lambda x: x[1]['count'], reverse=True):
            languages.append({
                'language': lang_code,
                'total_prs': counts['count'],
                'contributors': sorted(list(counts['contributors'])),
                'contributor_count': len(counts['contributors']),
                'courses': counts['content_types'].get('COURSE', 0),
                'tutorials': counts['content_types'].get('TUTORIAL', 0),
                'pr_numbers': counts['pr_numbers']
            })

        monthly_stats.append({
            'month_name': data['month_name'],
            'year': data['year'],
            'month': data['month'],
            'languages': languages
        })

    # Final summary
    print(f"\n📊 Monthly Leaderboard Summary:")
    for month in monthly_stats:
        if month['languages']:
            top = month['languages'][0]
            print(f"   {month['month_name']}: {top['language'].upper()} leads with {top['total_prs']} PRs ({len(month['languages'])} languages active)")
        else:
            print(f"   {month['month_name']}: No activity")

    # Save to cache for future runs
    save_github_cache(monthly_stats)

    return monthly_stats


def get_recent_contributions(courses, tutorials, limit=10):
    """Get the most recent contributions with dates across all content."""
    recent_contributions = []

    # Process courses
    for course in courses:
        for pr in course['proofreading']:
            if pr['last_date'] and pr['contributors']:
                for contributor in pr['contributors']:
                    if contributor not in EXCLUDED_CONTRIBUTORS:
                        recent_contributions.append({
                            'contributor': contributor,
                            'content_id': course['id'],
                            'content_name': course['name'],
                            'content_type': 'course',
                            'language': pr['language'],
                            'date': pr['last_date'],
                            'status': pr['status']
                        })

    # Process tutorials
    for tutorial in tutorials:
        for pr in tutorial['proofreading']:
            if pr['last_date'] and pr['contributors']:
                for contributor in pr['contributors']:
                    if contributor not in EXCLUDED_CONTRIBUTORS:
                        recent_contributions.append({
                            'contributor': contributor,
                            'content_id': tutorial['id'],
                            'content_name': tutorial['name'],
                            'content_type': 'tutorial',
                            'language': pr['language'],
                            'date': pr['last_date'],
                            'status': pr['status']
                        })

    # Sort by date (most recent first) and limit to specified number
    recent_contributions.sort(key=lambda x: x['date'], reverse=True)
    return recent_contributions[:limit]


def extract_all_data(skip_github_api=False):
    """Extract all proofreading data from courses and tutorials.

    Args:
        skip_github_api: If True, skip GitHub API calls for monthly leaderboard
    """
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

    # Get recent contributions
    recent_contributions = get_recent_contributions(courses, tutorials, limit=10)

    # Calculate monthly language team statistics for the last 3 months (from GitHub API)
    monthly_language_stats = calculate_monthly_language_stats(
        courses, tutorials, num_months=3, skip_api=skip_github_api
    )

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
        'language_stats': language_stats,
        'recent_contributions': recent_contributions,
        'monthly_language_stats': monthly_language_stats
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
            --color-primary: #ff6b00;
            --color-primary-dark: #cc5500;
            --color-status-0: #e74c3c;
            --color-status-1: #e67e22;
            --color-status-2: #f39c12;
            --color-status-3: #27ae60;
            --color-hover: #ecf0f1;
            --color-purple: #ff8c42;
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
            color: #000000;
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

        /* Language Multi-Select */
        .language-selector {{
            position: relative;
        }}

        .language-dropdown-button {{
            width: 100%;
            padding: 0.5rem;
            border: 1px solid var(--color-border);
            border-radius: 4px;
            font-size: 0.9rem;
            background: white;
            cursor: pointer;
            text-align: left;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .language-dropdown-button:hover {{
            border-color: var(--color-primary);
        }}

        .language-dropdown-content {{
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            max-height: 300px;
            overflow-y: auto;
            background: white;
            border: 1px solid var(--color-border);
            border-radius: 4px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            z-index: 100;
            margin-top: 0.25rem;
        }}

        .language-dropdown-content.show {{
            display: block;
        }}

        .language-option {{
            padding: 0.5rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .language-option:hover {{
            background: var(--color-hover);
        }}

        .language-option input[type="checkbox"] {{
            cursor: pointer;
        }}

        .language-option label {{
            cursor: pointer;
            flex: 1;
            margin: 0;
        }}

        .select-all-languages {{
            padding: 0.5rem;
            border-bottom: 2px solid var(--color-border);
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .select-all-languages:hover {{
            background: var(--color-hover);
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
            background: #dfe4ea;
            color: #000000;
            padding: 0.75rem;
            text-align: center;
            font-weight: 600;
            border: 2px solid #ffffff;
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
            display: flex;
            gap: 1rem;
            align-items: center;
        }}

        .contribution-item:hover {{
            border-color: var(--color-primary);
            box-shadow: 0 2px 8px rgba(52, 152, 219, 0.2);
        }}

        .contribution-content {{
            flex: 1;
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
            background: #dfe4ea;
            color: #000000;
            padding: 0.75rem;
            text-align: left;
            font-weight: 600;
            border: 2px solid #ffffff;
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

        /* Table of Contents */
        .toc-section {{
            background: var(--color-card);
            border-radius: 8px;
            padding: 1.5rem 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-left: 4px solid var(--color-primary);
        }}

        .toc-section h2 {{
            font-size: 1.3rem;
            margin-bottom: 1rem;
            color: #000000;
        }}

        .toc-nav {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
        }}

        .toc-link {{
            display: inline-block;
            padding: 0.5rem 1rem;
            background: var(--color-bg);
            color: var(--color-text);
            text-decoration: none;
            border-radius: 4px;
            border: 1px solid var(--color-border);
            transition: all 0.2s;
            font-size: 0.9rem;
        }}

        .toc-link:hover {{
            background: var(--color-primary);
            color: white;
            border-color: var(--color-primary);
            transform: translateY(-2px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        /* Back to Top Button */
        .back-to-top {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 50px;
            height: 50px;
            background: var(--color-primary);
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            display: none;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: all 0.3s;
            z-index: 1000;
        }}

        .back-to-top:hover {{
            background: var(--color-primary-dark);
            transform: translateY(-4px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }}

        .back-to-top.show {{
            display: flex;
        }}

        /* Smooth scrolling */
        html {{
            scroll-behavior: smooth;
        }}

        /* Monthly Language Team Leaderboard */
        .monthly-leaderboard-section {{
            margin-top: 2rem;
        }}

        .monthly-leaderboard-tabs {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }}

        .monthly-tab {{
            padding: 0.75rem 1.5rem;
            cursor: pointer;
            border: 2px solid var(--color-border);
            background: white;
            border-radius: 8px;
            font-size: 0.95rem;
            color: var(--color-text);
            transition: all 0.2s;
        }}

        .monthly-tab:hover {{
            border-color: var(--color-primary);
            background: var(--color-bg);
        }}

        .monthly-tab.active {{
            background: var(--color-primary);
            color: white;
            border-color: var(--color-primary);
            font-weight: 600;
        }}

        .monthly-tab-content {{
            display: none;
        }}

        .monthly-tab-content.active {{
            display: block;
        }}

        .monthly-intro {{
            background: linear-gradient(135deg, #ff6b00 0%, #cc5500 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
        }}

        .monthly-intro h3 {{
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .monthly-intro p {{
            margin: 0.5rem 0;
            opacity: 0.95;
            line-height: 1.5;
        }}

        .podium-container {{
            display: flex;
            justify-content: center;
            align-items: flex-end;
            gap: 1rem;
            margin-bottom: 2rem;
            padding: 1rem;
        }}

        .podium-place {{
            text-align: center;
            padding: 1rem;
            border-radius: 8px;
            min-width: 150px;
            transition: transform 0.3s;
        }}

        .podium-place:hover {{
            transform: translateY(-5px);
        }}

        .podium-first {{
            background: linear-gradient(180deg, #FFD700 0%, #FFA500 100%);
            order: 2;
            padding-bottom: 3rem;
        }}

        .podium-second {{
            background: linear-gradient(180deg, #C0C0C0 0%, #A8A8A8 100%);
            order: 1;
            padding-bottom: 2rem;
        }}

        .podium-third {{
            background: linear-gradient(180deg, #CD7F32 0%, #B8860B 100%);
            order: 3;
            padding-bottom: 1.5rem;
        }}

        .podium-medal {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }}

        .podium-lang {{
            font-size: 1.3rem;
            font-weight: 700;
            color: #333;
            text-transform: uppercase;
            margin-bottom: 0.25rem;
        }}

        .podium-lang-name {{
            font-size: 0.85rem;
            color: #555;
            margin-bottom: 0.5rem;
        }}

        .podium-count {{
            font-size: 1.8rem;
            font-weight: 800;
            color: #333;
        }}

        .podium-label {{
            font-size: 0.75rem;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .monthly-full-list {{
            margin-top: 1.5rem;
        }}

        .monthly-full-list h4 {{
            margin-bottom: 1rem;
            color: var(--color-text);
            font-size: 1.1rem;
        }}

        .monthly-lang-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
        }}

        .monthly-lang-table th {{
            background: #dfe4ea;
            color: #000000;
            padding: 0.75rem;
            text-align: left;
            font-weight: 600;
            border: 2px solid #ffffff;
        }}

        .monthly-lang-table td {{
            padding: 0.75rem;
            border-bottom: 1px solid var(--color-border);
        }}

        .monthly-lang-table tr:hover {{
            background: var(--color-hover);
        }}

        .monthly-rank {{
            font-weight: 700;
            color: var(--color-primary);
            width: 50px;
        }}

        .monthly-empty {{
            text-align: center;
            padding: 2rem;
            color: var(--color-text-light);
            font-style: italic;
        }}

        .contributor-avatars {{
            display: flex;
            gap: -8px;
        }}

        .contributor-avatars img {{
            width: 28px;
            height: 28px;
            border-radius: 50%;
            border: 2px solid white;
            margin-left: -8px;
        }}

        .contributor-avatars img:first-child {{
            margin-left: 0;
        }}

        /* Responsive Monthly Leaderboard */
        @media (max-width: 768px) {{
            .podium-container {{
                flex-direction: column;
                align-items: stretch;
            }}

            .podium-place {{
                order: unset !important;
                padding-bottom: 1rem !important;
            }}

            .monthly-tab {{
                flex: 1;
                text-align: center;
                padding: 0.5rem 1rem;
                font-size: 0.85rem;
            }}
        }}

        /* Responsive TOC */
        @media (max-width: 768px) {{
            .toc-nav {{
                flex-direction: column;
            }}

            .toc-link {{
                width: 100%;
                text-align: center;
            }}

            .back-to-top {{
                bottom: 1rem;
                right: 1rem;
                width: 45px;
                height: 45px;
                font-size: 1.3rem;
            }}
        }}

        /* Resources Section at Bottom */
        .resources-section {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 3rem 2rem;
            margin-top: 3rem;
            border-top: 3px solid var(--color-primary);
        }}

        .resources-container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .resources-section h2 {{
            text-align: center;
            color: var(--color-primary);
            font-size: 2rem;
            margin-bottom: 1rem;
        }}

        .resources-intro {{
            text-align: center;
            color: var(--color-text-light);
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }}

        .resources-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }}

        .resource-card {{
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            text-decoration: none;
            color: var(--color-text);
            transition: all 0.3s;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border: 2px solid transparent;
            display: block;
        }}

        .resource-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
            border-color: var(--color-primary);
        }}

        .resource-card-icon {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            display: block;
        }}

        .resource-card-title {{
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            color: var(--color-text);
        }}

        .resource-card-desc {{
            font-size: 0.9rem;
            color: var(--color-text-light);
            line-height: 1.5;
        }}

        .resource-type-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: var(--color-primary);
            color: white;
            border-radius: 12px;
            font-size: 0.75rem;
            margin-top: 0.5rem;
            font-weight: 600;
        }}

        /* Thank You Section */
        .thank-you-section {{
            background: var(--color-card);
            color: var(--color-text);
            padding: 3rem 2rem;
            text-align: center;
            border-top: 4px solid var(--color-primary);
        }}

        .thank-you-section h2 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--color-text);
        }}

        .thank-you-section p {{
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
            line-height: 1.8;
            color: var(--color-text);
        }}

        .community-links {{
            display: flex;
            gap: 1.5rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 2rem;
        }}

        .community-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            padding: 1rem 2rem;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}

        .community-link.telegram {{
            background: #0088cc;
            color: white;
        }}

        .community-link.telegram:hover {{
            background: #006699;
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,136,204,0.3);
        }}

        .community-link.discord {{
            background: #5865F2;
            color: white;
        }}

        .community-link.discord:hover {{
            background: #4752C4;
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(88,101,242,0.3);
        }}

        .community-icon {{
            font-size: 1.5rem;
        }}

        @media (max-width: 768px) {{
            .community-links {{
                flex-direction: column;
                align-items: stretch;
            }}

            .community-link {{
                width: 100%;
                justify-content: center;
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
        <!-- Table of Contents -->
        <div class="toc-section">
            <h2>📑 Table of Contents</h2>
            <nav class="toc-nav">
                <a href="#overview" class="toc-link">📊 Overview</a>
                <a href="#content-matrix" class="toc-link">📋 Content Matrix Overview</a>
                <a href="#contribution-finder" class="toc-link">🎯 Contribution Finder</a>
                <a href="#recent-contributions" class="toc-link">🕒 Last Proofreading Contributions</a>
                <a href="#leaderboards" class="toc-link">🏆 Leaderboards</a>
                <a href="#monthly-leaderboard" class="toc-link">📅 Monthly Language Team Leaderboard</a>
                <a href="#resources" class="toc-link">📚 Proofreading Resources</a>
            </nav>
        </div>

        <!-- Statistics -->
        <div class="section">
            <h2 id="overview">📊 Overview</h2>
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
            <h2 id="content-matrix">📋 Content Matrix Overview</h2>

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
                    <label for="matrix-languages">Languages:</label>
                    <div class="language-selector">
                        <button type="button" class="language-dropdown-button" id="language-dropdown-button">
                            <span id="selected-languages-text">All Languages (26)</span>
                            <span>▼</span>
                        </button>
                        <div class="language-dropdown-content" id="language-dropdown-content">
                            <div class="select-all-languages" id="select-all-languages">
                                <input type="checkbox" id="select-all-checkbox" checked>
                                <label for="select-all-checkbox">Select All</label>
                            </div>
                            <div id="language-options"></div>
                        </div>
                    </div>
                </div>

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
            <h2 id="contribution-finder">🎯 Contribution Finder - Where You're Needed Most (Top 10)</h2>

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

        <!-- Section 3: Last Proofreading Contributions -->
        <div class="section">
            <h2 id="recent-contributions">🕒 Last Proofreading Contributions</h2>
            <div id="recent-contributions-list"></div>
        </div>

        <!-- Section 4: Leaderboards -->
        <div class="section">
            <h2 id="leaderboards">🏆 Leaderboards</h2>

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

        <!-- Section 5: Monthly Language Team Leaderboard -->
        <div class="section">
            <h2 id="monthly-leaderboard">📅 Monthly Language Team Leaderboard</h2>

            <div class="monthly-leaderboard-section">
                <div class="monthly-leaderboard-tabs" id="monthly-tabs">
                    <!-- Tabs will be populated by JavaScript -->
                </div>

                <div id="monthly-content">
                    <!-- Content will be populated by JavaScript -->
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
        let selectedLanguages = new Set();

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

            // Render recent contributions
            renderRecentContributions();

            // Render leaderboards
            renderCourseContributors();
            renderTutorialContributors();

            // Render monthly language team leaderboard
            renderMonthlyLeaderboard();

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

            // Initialize all languages as selected
            languages.forEach(lang => selectedLanguages.add(lang.code));

            // Populate language multi-select
            const languageOptionsDiv = document.getElementById('language-options');
            languages.forEach(lang => {{
                const div = document.createElement('div');
                div.className = 'language-option';
                div.innerHTML = `
                    <input type="checkbox" id="lang-${{lang.code}}" value="${{lang.code}}" checked>
                    <label for="lang-${{lang.code}}">${{lang.name}} (${{lang.code.toUpperCase()}})</label>
                `;
                languageOptionsDiv.appendChild(div);
            }});

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

        function updateSelectedLanguagesText() {{
            const {{ languages }} = PROOFREADING_DATA;
            const text = document.getElementById('selected-languages-text');
            const count = selectedLanguages.size;
            const total = languages.length;

            if (count === total) {{
                text.textContent = `All Languages (${{total}})`;
            }} else if (count === 0) {{
                text.textContent = 'No Languages Selected';
            }} else if (count === 1) {{
                const langCode = Array.from(selectedLanguages)[0];
                const lang = languages.find(l => l.code === langCode);
                text.textContent = lang ? `${{lang.name}}` : '1 Language';
            }} else {{
                text.textContent = `${{count}} Languages Selected`;
            }}
        }}

        function toggleLanguageDropdown() {{
            const dropdown = document.getElementById('language-dropdown-content');
            dropdown.classList.toggle('show');
        }}

        function handleLanguageChange(langCode, checked) {{
            if (checked) {{
                selectedLanguages.add(langCode);
            }} else {{
                selectedLanguages.delete(langCode);
            }}

            // Update select all checkbox
            const {{ languages }} = PROOFREADING_DATA;
            const selectAllCheckbox = document.getElementById('select-all-checkbox');
            selectAllCheckbox.checked = selectedLanguages.size === languages.length;

            updateSelectedLanguagesText();
            renderMatrix();
        }}

        function handleSelectAll(checked) {{
            const {{ languages }} = PROOFREADING_DATA;

            if (checked) {{
                languages.forEach(lang => selectedLanguages.add(lang.code));
            }} else {{
                selectedLanguages.clear();
            }}

            // Update all checkboxes
            document.querySelectorAll('#language-options input[type="checkbox"]').forEach(cb => {{
                cb.checked = checked;
            }});

            updateSelectedLanguagesText();
            renderMatrix();
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

            // Filter languages based on selection
            const filteredLanguages = languages.filter(lang => selectedLanguages.has(lang.code));

            // Render header
            const header = document.getElementById('matrix-header');
            header.innerHTML = '<th>English Title</th><th>Code</th>';
            filteredLanguages.forEach(lang => {{
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
                tr.innerHTML = `<td colspan="${{filteredLanguages.length + 2}}" class="empty-state">No content found</td>`;
                tbody.appendChild(tr);
                return;
            }}

            if (filteredLanguages.length === 0) {{
                const tr = document.createElement('tr');
                tr.innerHTML = `<td colspan="2" class="empty-state">Please select at least one language</td>`;
                tbody.appendChild(tr);
                return;
            }}

            data.forEach(item => {{
                const tr = document.createElement('tr');

                // English title cell
                const titleTd = document.createElement('td');
                titleTd.textContent = item.english_title || '';
                titleTd.title = item.english_title || '';
                tr.appendChild(titleTd);

                // Content code cell
                const codeTd = document.createElement('td');
                codeTd.textContent = item.id;
                codeTd.title = item.name;
                tr.appendChild(codeTd);

                // Language cells (only for selected languages)
                filteredLanguages.forEach(lang => {{
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

        function renderRecentContributions() {{
            const {{ recent_contributions, languages }} = PROOFREADING_DATA;
            const contentDiv = document.getElementById('recent-contributions-list');

            if (!recent_contributions || recent_contributions.length === 0) {{
                contentDiv.innerHTML = '<div class="empty-state">No recent contributions found</div>';
                return;
            }}

            contentDiv.innerHTML = '';

            recent_contributions.forEach((contribution) => {{
                const lang = languages.find(l => l.code === contribution.language);
                const languageName = lang ? lang.name : contribution.language.toUpperCase();
                const date = new Date(contribution.date);
                const formattedDate = date.toLocaleDateString('en-US', {{ year: 'numeric', month: 'short', day: 'numeric' }});
                const statusText = ['Needs Proofreading', 'In Progress (1)', 'In Progress (2)', 'Complete (3+)'][contribution.status];

                const div = document.createElement('div');
                div.className = 'contribution-item';
                div.innerHTML = `
                    <img class="avatar"
                         src="https://github.com/${{contribution.contributor}}.png"
                         alt="${{contribution.contributor}}"
                         onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Crect fill=%22%23ddd%22 width=%22100%22 height=%22100%22/%3E%3Ctext x=%2250%22 y=%2250%22 fill=%22%23999%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22sans-serif%22 font-size=%2240%22%3E?%3C/text%3E%3C/svg%3E'">
                    <div class="contribution-content">
                        <div class="contribution-header">
                            <div class="contribution-title">${{contribution.content_name}} (${{contribution.content_id}})</div>
                            <span class="status-badge status-${{contribution.status}}">${{statusText}}</span>
                        </div>
                        <div class="contribution-details">
                            <span>👤 <strong><a href="https://github.com/${{contribution.contributor}}" target="_blank">${{contribution.contributor}}</a></strong></span>
                            <span>🌐 ${{languageName}} (${{contribution.language.toUpperCase()}})</span>
                            <span>📝 ${{contribution.content_type}}</span>
                            <span>📅 ${{formattedDate}}</span>
                        </div>
                    </div>
                `;

                contentDiv.appendChild(div);
            }});
        }}

        function renderMonthlyLeaderboard() {{
            const {{ monthly_language_stats, languages }} = PROOFREADING_DATA;
            const tabsDiv = document.getElementById('monthly-tabs');
            const contentDiv = document.getElementById('monthly-content');

            if (!monthly_language_stats || monthly_language_stats.length === 0) {{
                contentDiv.innerHTML = '<div class="monthly-empty">No monthly data available</div>';
                return;
            }}

            // Create tabs
            tabsDiv.innerHTML = '';
            monthly_language_stats.forEach((monthData, index) => {{
                const tab = document.createElement('button');
                tab.className = `monthly-tab ${{index === 0 ? 'active' : ''}}`;
                tab.dataset.monthIndex = index;
                tab.textContent = monthData.month_name;
                tab.addEventListener('click', () => switchMonthlyTab(index));
                tabsDiv.appendChild(tab);
            }});

            // Render first month by default
            renderMonthlyContent(0);
        }}

        function switchMonthlyTab(index) {{
            // Update tab active states
            document.querySelectorAll('.monthly-tab').forEach((tab, i) => {{
                tab.classList.toggle('active', i === index);
            }});

            renderMonthlyContent(index);
        }}

        function renderMonthlyContent(monthIndex) {{
            const {{ monthly_language_stats, languages }} = PROOFREADING_DATA;
            const monthData = monthly_language_stats[monthIndex];
            const contentDiv = document.getElementById('monthly-content');

            if (!monthData || monthData.languages.length === 0) {{
                contentDiv.innerHTML = `
                    <div class="monthly-intro">
                        <h3>⚡️ ${{monthData?.month_name || 'Unknown Month'}} Proofreading Leaderboard</h3>
                        <p>No proofreading activity recorded for this month yet.</p>
                    </div>
                `;
                return;
            }}

            const top3 = monthData.languages.slice(0, 3);
            const allLangs = monthData.languages;

            // Generate intro message based on position
            const firstLang = top3[0];
            const firstLangName = languages.find(l => l.code === firstLang.language)?.name || firstLang.language.toUpperCase();
            const secondLangName = top3[1] ? (languages.find(l => l.code === top3[1].language)?.name || top3[1].language.toUpperCase()) : null;
            const thirdLangName = top3[2] ? (languages.find(l => l.code === top3[2].language)?.name || top3[2].language.toUpperCase()) : null;

            let introMessage = `⚡️ Here we go with the leaderboard of ${{monthData.month_name}} proofreading!`;
            let detailMessage = '';

            if (firstLang) {{
                detailMessage = `❕ The ${{firstLangName}} team leads the way with a total of ${{firstLang.total_prs}} proofreading PR${{firstLang.total_prs > 1 ? 's' : ''}}`;
                if (secondLangName && thirdLangName) {{
                    detailMessage += `, while ${{secondLangName}} and ${{thirdLangName}} are coming close in second and third place.`;
                }} else if (secondLangName) {{
                    detailMessage += `, with ${{secondLangName}} in second place.`;
                }} else {{
                    detailMessage += '.';
                }}
            }}

            // Determine the next month name for the teaser
            const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
            const nextMonthIndex = (monthData.month % 12);
            const nextMonthName = months[nextMonthIndex];

            let html = `
                <div class="monthly-intro">
                    <h3>⚡️ ${{monthData.month_name}} Proofreading Leaderboard</h3>
                    <p>${{introMessage}}</p>
                    <p>${{detailMessage}}</p>
                    <p>😎 Let's see if another team can overcome them in ${{nextMonthName}}. Lots of news coming up, and maybe a new proofreading challenge too 😉</p>
                    <p>Keep up the good work guys 🚀</p>
                </div>
            `;

            // Podium for top 3
            if (top3.length > 0) {{
                html += '<div class="podium-container">';

                top3.forEach((lang, index) => {{
                    const langInfo = languages.find(l => l.code === lang.language);
                    const langName = langInfo?.name || lang.language.toUpperCase();
                    const medals = ['🥇', '🥈', '🥉'];
                    const placeClasses = ['podium-first', 'podium-second', 'podium-third'];

                    html += `
                        <div class="podium-place ${{placeClasses[index]}}">
                            <div class="podium-medal">${{medals[index]}}</div>
                            <div class="podium-lang">${{lang.language.toUpperCase()}}</div>
                            <div class="podium-lang-name">${{langName}}</div>
                            <div class="podium-count">${{lang.total_prs}}</div>
                            <div class="podium-label">PR${{lang.total_prs > 1 ? 's' : ''}}</div>
                        </div>
                    `;
                }});

                html += '</div>';
            }}

            // Full list table
            html += `
                <div class="monthly-full-list">
                    <h4>📊 Full Rankings for ${{monthData.month_name}}</h4>
                    <table class="monthly-lang-table">
                        <thead>
                            <tr>
                                <th>Rank</th>
                                <th>Language</th>
                                <th>Total PRs</th>
                                <th>Courses</th>
                                <th>Tutorials</th>
                                <th>Contributors</th>
                            </tr>
                        </thead>
                        <tbody>
            `;

            allLangs.forEach((lang, index) => {{
                const langInfo = languages.find(l => l.code === lang.language);
                const langName = langInfo?.name || lang.language.toUpperCase();
                const rank = index < 3 ? ['🥇', '🥈', '🥉'][index] : `#${{index + 1}}`;

                // Generate contributor avatars
                let avatarsHtml = '<div class="contributor-avatars">';
                lang.contributors.slice(0, 5).forEach(contributor => {{
                    avatarsHtml += `<img src="https://github.com/${{contributor}}.png" alt="${{contributor}}" title="${{contributor}}" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Crect fill=%22%23ddd%22 width=%22100%22 height=%22100%22/%3E%3Ctext x=%2250%22 y=%2250%22 fill=%22%23999%22 text-anchor=%22middle%22 dy=%22.3em%22 font-family=%22sans-serif%22 font-size=%2240%22%3E?%3C/text%3E%3C/svg%3E'">`;
                }});
                if (lang.contributors.length > 5) {{
                    avatarsHtml += `<span style="margin-left: 4px; color: #666;">+${{lang.contributors.length - 5}}</span>`;
                }}
                avatarsHtml += '</div>';

                html += `
                    <tr>
                        <td class="monthly-rank">${{rank}}</td>
                        <td>
                            <strong>${{lang.language.toUpperCase()}}</strong>
                            <span style="color: #666; font-size: 0.85rem;"> - ${{langName}}</span>
                        </td>
                        <td><strong>${{lang.total_prs}}</strong></td>
                        <td>${{lang.courses}}</td>
                        <td>${{lang.tutorials}}</td>
                        <td>${{avatarsHtml}}</td>
                    </tr>
                `;
            }});

            html += `
                        </tbody>
                    </table>
                </div>
            `;

            contentDiv.innerHTML = html;
        }}

        function setupEventListeners() {{
            // Language dropdown toggle
            document.getElementById('language-dropdown-button').addEventListener('click', (e) => {{
                e.stopPropagation();
                toggleLanguageDropdown();
            }});

            // Close dropdown when clicking outside
            document.addEventListener('click', (e) => {{
                const dropdown = document.getElementById('language-dropdown-content');
                const button = document.getElementById('language-dropdown-button');
                if (!dropdown.contains(e.target) && !button.contains(e.target)) {{
                    dropdown.classList.remove('show');
                }}
            }});

            // Select all checkbox
            document.getElementById('select-all-checkbox').addEventListener('change', (e) => {{
                handleSelectAll(e.target.checked);
            }});

            // Individual language checkboxes
            document.querySelectorAll('#language-options input[type="checkbox"]').forEach(checkbox => {{
                checkbox.addEventListener('change', (e) => {{
                    handleLanguageChange(e.target.value, e.target.checked);
                }});
            }});

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

        // Back to Top Button functionality
        const backToTopButton = document.querySelector('.back-to-top');

        window.addEventListener('scroll', () => {{
            if (window.pageYOffset > 300) {{
                backToTopButton.classList.add('show');
            }} else {{
                backToTopButton.classList.remove('show');
            }}
        }});

        backToTopButton.addEventListener('click', () => {{
            window.scrollTo({{
                top: 0,
                behavior: 'smooth'
            }});
        }});
    </script>

    <!-- Resources Section at Bottom -->
    <section class="resources-section" id="resources">
        <div class="resources-container">
            <h2>📚 Proofreading Resources</h2>
            <p class="resources-intro">
                Learn how to proofread and review content effectively with our comprehensive guides and video tutorials
            </p>

            <div class="resources-grid">
                <a href="https://planb.academy/en/tutorials/contribution/content/proofreading-guidelines-52348db0-8cd0-4658-9de4-0e8c25bea1a0"
                   target="_blank" class="resource-card">
                    <span class="resource-card-icon">📖</span>
                    <div class="resource-card-title">Proofreading Guidelines</div>
                    <div class="resource-card-desc">
                        Complete guide on how to proofread educational content. Learn best practices, common mistakes, and quality standards.
                    </div>
                    <span class="resource-type-badge">GUIDE</span>
                </a>

                <a href="https://planb.academy/en/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017"
                   target="_blank" class="resource-card">
                    <span class="resource-card-icon">✅</span>
                    <div class="resource-card-title">Review Tutorial</div>
                    <div class="resource-card-desc">
                        Step-by-step tutorial on reviewing and approving proofreading submissions in the platform.
                    </div>
                    <span class="resource-type-badge">TUTORIAL</span>
                </a>

                <a href="https://workspace.planb.network/s/7FK5scZRK5cxRmf"
                   target="_blank" class="resource-card">
                    <span class="resource-card-icon">🎥</span>
                    <div class="resource-card-title">General Proofreading Process</div>
                    <div class="resource-card-desc">
                        Watch this video walkthrough of the complete proofreading workflow on GitHub, from start to finish.
                    </div>
                    <span class="resource-type-badge">VIDEO</span>
                </a>

                <a href="https://workspace.planb.network/s/RXq3ALHWZidASLD"
                   target="_blank" class="resource-card">
                    <span class="resource-card-icon">🎥</span>
                    <div class="resource-card-title">Proofread Quizzes and Tutorial Sections</div>
                    <div class="resource-card-desc">
                        Learn how to proofread tutorial quizzes and course sections effectively using GitHub's review tools.
                    </div>
                    <span class="resource-type-badge">VIDEO</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Thank You Section -->
    <section class="thank-you-section">
        <h2>🙏 Thank You!</h2>
        <p>Thank you to everyone who contributes to making Bitcoin education accessible worldwide.</p>
        <p>Join the Plan ₿ Community and start proofreading now!</p>
        <p style="font-size: 1rem; margin-top: 0.5rem; color: var(--color-text-light);">You only need to tag the admin to receive your first proofreading task!</p>
        <div class="community-links">
            <a href="https://t.me/PlanBNetwork_ContentBuilder" target="_blank" class="community-link telegram">
                <span class="community-icon">💬</span>
                <span>Join us on Telegram</span>
            </a>
            <a href="https://discord.com/invite/q9CFPmRNAD" target="_blank" class="community-link discord">
                <span class="community-icon">💬</span>
                <span>Join us on Discord</span>
            </a>
        </div>
    </section>

    <!-- Back to Top Button -->
    <button class="back-to-top" aria-label="Back to top">↑</button>
</body>
</html>"""

    return html


def main():
    """Main function to generate the dashboard."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate Bitcoin Educational Content Proofreading Dashboard'
    )
    parser.add_argument(
        '--skip-github-api',
        action='store_true',
        help='Skip GitHub API calls (use cached data only for monthly leaderboard)'
    )
    parser.add_argument(
        '--clear-cache',
        action='store_true',
        help='Clear the GitHub PR cache before fetching'
    )
    args = parser.parse_args()

    print("=" * 60)
    print("Bitcoin Educational Content - Proofreading Dashboard Generator")
    print("=" * 60)

    # Clear cache if requested
    if args.clear_cache:
        cache_path = Path(__file__).parent / GITHUB_CACHE_FILE
        if cache_path.exists():
            cache_path.unlink()
            print("Cleared GitHub PR cache")

    # Extract data
    data = extract_all_data(skip_github_api=args.skip_github_api)

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
