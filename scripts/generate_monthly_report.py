#!/usr/bin/env python3
"""
Generate a monthly activity report for the Bitcoin Educational Content repository.

Usage:
    python scripts/generate_monthly_report.py [YYYY-MM]

If no date is given, defaults to the previous month.
Output: docs/reports/YYYY-MM.md
"""

import subprocess
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta


REPO = "PlanB-Network/bitcoin-educational-content"
GITHUB_PR_URL = f"https://github.com/{REPO}/pull"

# Employees excluded from the community contributor list
EXCLUDED_CONTRIBUTORS = {
    "Loïc",
    "Asi0Flammeus",
    "MarJJ",
    "asi0",
    "jramos0",
}


# ── helpers ──────────────────────────────────────────────────────────────────

def git(args: str) -> str:
    """Run a git command and return stripped stdout."""
    result = subprocess.run(
        f"git {args}", shell=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def parse_month(arg: str | None) -> tuple[str, str, str]:
    """Return (label, after_date, before_date) for the given YYYY-MM or previous month."""
    if arg:
        dt = datetime.strptime(arg, "%Y-%m")
    else:
        today = datetime.today().replace(day=1)
        dt = today - timedelta(days=1)
        dt = dt.replace(day=1)

    year, month = dt.year, dt.month
    if month == 12:
        next_year, next_month = year + 1, 1
    else:
        next_year, next_month = year, month + 1

    label = f"{year}-{month:02d}"
    after = f"{year}-{month:02d}-00"          # --after is exclusive
    before = f"{next_year}-{next_month:02d}-01"  # --before is exclusive
    return label, after, before


# ── data collection ──────────────────────────────────────────────────────────

def get_commits(after: str, before: str) -> list[str]:
    """Return list of oneline commit messages."""
    raw = git(f'log --oneline --after="{after}" --before="{before}"')
    return [line for line in raw.splitlines() if line] if raw else []


def get_diff_stats(after: str, before: str) -> tuple[int, int]:
    """Return (lines_added, lines_removed)."""
    raw = git(f'log --after="{after}" --before="{before}" --shortstat --pretty=""')
    added = removed = 0
    for line in raw.splitlines():
        m_add = re.search(r'(\d+) insertion', line)
        m_del = re.search(r'(\d+) deletion', line)
        if m_add:
            added += int(m_add.group(1))
        if m_del:
            removed += int(m_del.group(1))
    return added, removed


def get_contributors(after: str, before: str) -> list[tuple[str, int]]:
    """Return [(name, count), ...] sorted by count desc."""
    raw = git(f'log --after="{after}" --before="{before}" --pretty=format:"%an"')
    counts: dict[str, int] = defaultdict(int)
    for name in raw.splitlines():
        name = name.strip()
        if name:
            counts[name] += 1
    return sorted(counts.items(), key=lambda x: -x[1])


def extract_pr(msg: str) -> str | None:
    """Extract PR number from commit message like '(#1234)'."""
    m = re.search(r'#(\d+)', msg)
    return m.group(1) if m else None


def extract_author(msg: str) -> str | None:
    """Extract @author from commit message (if present in PR title)."""
    m = re.search(r'by @(\S+)', msg, re.IGNORECASE)
    return m.group(1) if m else None


# ── categorisation ───────────────────────────────────────────────────────────

CATEGORIES = [
    ("PROOFREADING-META", r"\[PROOFREADING.?METADATA\]"),
    ("PROOFREADING", r"\[PROOFREADING\]|\[PROOFREDING\]"),
    ("BATCH-TRANSLATION", r"\[BATCH.?TRANSLATION\]|\[IMAGES?.?TRANSLATION\]"),
    ("TRANSLATION",  r"\[TRANSLATION\]"),
    ("TUTORIAL",     r"\[TUTORIAL\]"),
    ("COURSE",       r"\[COURSE\]|\[COURSES\]|\[BTC \d+\]|\[LNP \d+\]|\[MIN \d+\]|\[ECO \d+\]|\[HIS \d+\]|\[DEV \d+\]|\[SID \d+\]|\[PHI \d+\]|\[BIZ \d+\]|\[CYP \d+\]|\[CSV \d+\]|\[NET \d+\]|\[SCU \d+\]|\[SOC \d+\]|\[PRO \d+\]"),
    ("TYPO",         r"\[TYPO\]"),
    ("QUIZ",         r"\[QUIZ\]|\[QUIZZ\]"),
    ("SCRIPT",       r"\[SCRIPT\]|\[SCRIPTS\]"),
    ("DOCS",         r"\[DOCS\]"),
    ("DATA",         r"\[DATA\]"),
    ("SYNC",         r"\[SYNC\]"),
    ("PROJECT",      r"\[PROJECT\]"),
    ("PROFESSOR",    r"\[PROFESSOR\]"),
    ("EVENT",        r"\[EVENT\]"),
    ("GLOSSARY",     r"\[GLOSSARY\]"),
    ("RESOURCE",     r"\[RESOURCE\]|\[RESOURCES\]|\[NEW RESOURCE\S*\]|\[BOOK\]|\[PAPER\]"),
]


def categorise(commits: list[str]) -> dict[str, list[str]]:
    """Group commits by category tag. Unknown goes to 'OTHER'."""
    groups: dict[str, list[str]] = defaultdict(list)
    for line in commits:
        # strip the short sha
        msg = line.split(" ", 1)[1] if " " in line else line
        matched = False
        for cat, pattern in CATEGORIES:
            if re.search(pattern, msg, re.IGNORECASE):
                groups[cat].append(msg)
                matched = True
                break
        if not matched:
            groups["OTHER"].append(msg)
    return groups


def pr_link(msg: str) -> str:
    """Format a commit message as a markdown line with PR link."""
    pr = extract_pr(msg)
    # Clean up the message: remove the (#NNNN) suffix
    clean = re.sub(r'\s*\(#\d+\)\s*$', '', msg).strip()
    if pr:
        return f"- [PR #{pr}]({GITHUB_PR_URL}/{pr}): {clean}"
    return f"- {clean}"


# ── proofreading language extraction ─────────────────────────────────────────

LANGUAGE_MAP = {
    "french": "French", "fr": "French",
    "english": "English", "en": "English",
    "spanish": "Spanish", "es": "Spanish",
    "italian": "Italian", "it": "Italian",
    "german": "German", "de": "German",
    "japanese": "Japanese", "ja": "Japanese",
    "indonesian": "Indonesian", "id": "Indonesian",
    "bulgarian": "Bulgarian", "bg": "Bulgarian",
    "serbian": "Serbian", "sr": "Serbian",
    "swahili": "Swahili", "sw": "Swahili",
    "rundi": "Rundi", "rn": "Rundi",
    "korean": "Korean", "ko": "Korean",
    "czech": "Czech", "cs": "Czech",
    "chinese": "Chinese", "zh-hans": "Simplified Chinese",
    "simplified chinese": "Simplified Chinese",
    "traditional chinese": "Traditional Chinese", "zh-hant": "Traditional Chinese",
    "polish": "Polish", "pl": "Polish",
    "portuguese": "Portuguese", "pt": "Portuguese",
    "hindi": "Hindi", "hi": "Hindi",
    "thai": "Thai", "th": "Thai",
    "vietnamese": "Vietnamese", "vi": "Vietnamese",
    "russian": "Russian", "ru": "Russian",
    "arabic": "Arabic", "ar": "Arabic",
}


def extract_proofreading_languages(commits: list[str]) -> dict[str, list[str]]:
    """Map language -> list of proofread content from commit messages."""
    lang_content: dict[str, list[str]] = defaultdict(list)
    for msg in commits:
        # Try to find language at end: "- French", "- Japanese", etc.
        m = re.search(r'[-–]\s*(\w[\w\s\-]*\w)\s*(?:\(#\d+\))?\s*$', msg, re.IGNORECASE)
        if m:
            lang_raw = m.group(1).strip().lower()
            lang = LANGUAGE_MAP.get(lang_raw, lang_raw.title())
            # Extract course/content code
            code_m = re.search(r'\]\s*(.+?)(?:\s*[-–])', msg)
            content = code_m.group(1).strip() if code_m else msg
            lang_content[lang].append(content)
    return lang_content


# ── report builder ───────────────────────────────────────────────────────────

def month_name(label: str) -> str:
    dt = datetime.strptime(label, "%Y-%m")
    return dt.strftime("%B %Y")


def build_report(label: str, after: str, before: str) -> str:
    """Build the full markdown report."""
    commits = get_commits(after, before)
    added, removed = get_diff_stats(after, before)
    contributors = get_contributors(after, before)
    groups = categorise(commits)

    total_commits = len(commits)
    unique_contributors = len(contributors)
    community_contributors = [n for n, c in contributors if n not in EXCLUDED_CONTRIBUTORS]
    n_community = len(community_contributors)
    net = added - removed

    # Count key items
    n_courses = len(groups.get("COURSE", []))
    n_tutorials = len(groups.get("TUTORIAL", []))
    n_proofreading = len(groups.get("PROOFREADING", []))
    n_translations = len(groups.get("BATCH-TRANSLATION", [])) + len(groups.get("TRANSLATION", []))
    n_projects = len(groups.get("PROJECT", []))

    # Proofreading language breakdown
    proof_langs = extract_proofreading_languages(groups.get("PROOFREADING", []))
    n_proof_languages = len(proof_langs)

    lines = []
    w = lines.append

    # ── Header & TL;DR ──
    w(f"# Bitcoin Educational Content - {month_name(label)} Monthly Report")
    w("")
    w("## TL;DR")
    w("")
    w(f"- **{total_commits} commits** from **{n_community} community contributors** (+ {unique_contributors - n_community} team members)")
    w(f"- **{added:,} lines added**, {removed:,} lines removed (net {'+' if net >= 0 else ''}{net:,})")
    if n_courses:
        w(f"- **{n_courses} course-related commits** (new courses, updates, deployments)")
    if n_tutorials:
        w(f"- **{n_tutorials} tutorial commits** (new tutorials, updates, fixes)")
    if n_translations:
        w(f"- **{n_translations} translation commits** expanding multilingual coverage")
    if n_proofreading:
        w(f"- **{n_proofreading} proofreading commits** improving quality across {n_proof_languages} languages")
    if n_projects:
        w(f"- **{n_projects} new projects** added to the ecosystem directory")
    w("")
    w("---")
    w("")

    # ── Course Updates ──
    course_commits = groups.get("COURSE", [])
    if course_commits:
        w("## Course Updates")
        w("")

        new_deploy = [m for m in course_commits
                      if re.search(r'\b(deploy|publish|push)\b.*\b(testnet|mainnet)\b', m, re.IGNORECASE)]
        new_content = [m for m in course_commits
                       if re.search(r'\bAdd\b|\bnew\b', m, re.IGNORECASE) and m not in new_deploy]
        course_fixes = [m for m in course_commits
                        if m not in new_deploy and m not in new_content]

        if new_deploy:
            w("### New Course Deployments")
            w("")
            for msg in new_deploy:
                w(pr_link(msg))
            w("")

        if new_content:
            w("### New Course Content")
            w("")
            for msg in new_content:
                w(pr_link(msg))
            w("")

        if course_fixes:
            w("### Course Improvements & Fixes")
            w("")
            for msg in course_fixes:
                w(pr_link(msg))
            w("")

        w("---")
        w("")

    # ── Tutorial Additions ──
    tutorial_commits = groups.get("TUTORIAL", [])
    if tutorial_commits:
        w("## Tutorial Additions")
        w("")
        new_tutorials = [m for m in tutorial_commits if re.search(r'\bAdd\b', m, re.IGNORECASE)]
        updated_tutorials = [m for m in tutorial_commits if m not in new_tutorials]

        if new_tutorials:
            w(f"### New Tutorials ({len(new_tutorials)} total)")
            w("")
            for msg in new_tutorials:
                w(pr_link(msg))
            w("")

        if updated_tutorials:
            w("### Tutorial Updates & Fixes")
            w("")
            for msg in updated_tutorials:
                w(pr_link(msg))
            w("")

        w("---")
        w("")

    # ── Translation Efforts ──
    batch = groups.get("BATCH-TRANSLATION", [])
    trans = groups.get("TRANSLATION", [])
    if batch or trans:
        w("## Translation Efforts")
        w("")
        if batch:
            w("### Batch Translations")
            w("")
            for msg in batch:
                w(pr_link(msg))
            w("")
        if trans:
            w("### Individual Translations")
            w("")
            for msg in trans:
                w(pr_link(msg))
            w("")
        w("---")
        w("")

    # ── Proofreading ──
    proof_commits = groups.get("PROOFREADING", [])
    if proof_commits:
        w("## Proofreading")
        w("")

        # Language table
        if proof_langs:
            w("### Languages with Proofreading Activity")
            w("")
            w("| Language | Content Proofread |")
            w("|----------|-------------------|")
            for lang in sorted(proof_langs.keys()):
                items = ", ".join(proof_langs[lang])
                w(f"| **{lang}** | {items} |")
            w("")

        w(f"### Proofreading PRs ({n_proofreading} commits)")
        w("")
        for msg in proof_commits:
            w(pr_link(msg))
        w("")
        w("---")
        w("")

    # ── Contributor Recognition ──
    w("## Contributor Recognition")
    w("")
    w("### Top Contributors by Commits")
    w("")
    community = [(n, c) for n, c in contributors if n not in EXCLUDED_CONTRIBUTORS]
    w("| Contributor | Commits |")
    w("|-------------|---------|")
    for name, count in community[:15]:
        w(f"| @{name} | {count} |")
    w("")

    # ── Projects, Professors, Events, Resources ──
    extra_sections = [
        ("PROJECT", "Projects Added"),
        ("PROFESSOR", "Professors"),
        ("EVENT", "Events"),
        ("RESOURCE", "Resources"),
        ("GLOSSARY", "Glossary"),
    ]
    extras = []
    for key, title in extra_sections:
        items = groups.get(key, [])
        if items:
            extras.append((title, items))

    if extras:
        w("---")
        w("")
        w("## Infrastructure & Platform Updates")
        w("")
        for title, items in extras:
            w(f"### {title}")
            w("")
            for msg in items:
                w(pr_link(msg))
            w("")

    # ── Scripts, Docs, Data, Typos ──
    maintenance_sections = [
        ("SCRIPT", "Scripts & Tooling"),
        ("DOCS", "Documentation Updates"),
        ("DATA", "Data Fixes"),
        ("TYPO", "Typo Fixes"),
        ("QUIZ", "Quiz Fixes"),
        ("SYNC", "Sync Fixes"),
        ("PROOFREADING-META", "Proofreading Metadata"),
    ]
    maintenance = []
    for key, title in maintenance_sections:
        items = groups.get(key, [])
        if items:
            maintenance.append((title, items))

    if maintenance:
        if not extras:
            w("---")
            w("")
            w("## Infrastructure & Platform Updates")
            w("")
        for title, items in maintenance:
            w(f"### {title}")
            w("")
            for msg in items:
                w(pr_link(msg))
            w("")

    # ── Other ──
    other = groups.get("OTHER", [])
    if other:
        w("### Other")
        w("")
        for msg in other:
            w(pr_link(msg))
        w("")

    # ── Summary ──
    w("---")
    w("")
    w("## Summary")
    w("")
    w(f"{month_name(label)} saw **{total_commits} commits** from "
      f"**{n_community} community contributors** and "
      f"**{unique_contributors - n_community} team members**, adding **{added:,} lines** "
      f"and removing **{removed:,} lines** across the repository.")
    w("")
    w(f"Thank you to all {n_community} community contributors who made "
      f"{month_name(label)} another productive month for Bitcoin education!")
    w("")
    w("---")
    w("")
    w(f"*Report generated: {datetime.now().strftime('%B %d, %Y')}*")
    w("")

    return "\n".join(lines)


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    label, after, before = parse_month(arg)

    print(f"Generating report for {label}...")
    print(f"  Date range: after {after}, before {before}")

    report = build_report(label, after, before)

    out_dir = "docs/reports"
    out_path = f"{out_dir}/{label}.md"

    import os
    os.makedirs(out_dir, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report written to {out_path}")
    print(f"  Size: {len(report):,} bytes")


if __name__ == "__main__":
    main()
