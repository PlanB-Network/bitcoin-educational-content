#!/usr/bin/env python3
"""Find translated files that still contain mostly English (failed translation fallback).

Uses a reference language (de, DeepL-backed) as baseline for each tutorial.
A Google-translated file (hi/rn/sw/vi) is flagged as broken when its
English-overlap ratio exceeds the baseline by more than DELTA_THRESHOLD
percentage points — this filters out code-heavy tutorials that naturally
have high overlap in every language.

Usage:
    python3 find_untranslated.py          # list affected files
    python3 find_untranslated.py --delete  # delete affected files
"""

import os
import sys
from pathlib import Path

GOOGLE_LANGS = ['hi', 'rn', 'sw', 'vi']
REFERENCE_LANG = 'de'
DELTA_THRESHOLD = 0.15  # flag if >15pp above baseline
ABSOLUTE_MIN = 0.25     # ignore files below 25% overlap regardless

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TUTORIALS_DIR = PROJECT_ROOT / "tutorials"


def get_text_lines(filepath):
    """Extract non-empty, non-markup text lines from a markdown file."""
    lines = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            in_frontmatter = False
            for line in f:
                stripped = line.strip()
                if stripped == '---':
                    in_frontmatter = not in_frontmatter
                    continue
                if in_frontmatter:
                    continue
                if not stripped:
                    continue
                if stripped.startswith('!['):
                    continue
                if stripped.startswith('```'):
                    continue
                if len(stripped) > 20:
                    lines.append(stripped)
    except Exception:
        pass
    return lines


def check_file(en_path, lang_path):
    """Return ratio of identical lines between en and lang file."""
    en_lines = get_text_lines(en_path)
    lang_lines = get_text_lines(lang_path)

    if not en_lines or not lang_lines:
        return 0.0

    en_set = set(en_lines)
    identical = sum(1 for line in lang_lines if line in en_set)
    return identical / len(lang_lines)


def find_untranslated():
    affected = []

    for dirpath, dirnames, filenames in os.walk(TUTORIALS_DIR):
        en_file = os.path.join(dirpath, 'en.md')
        if not os.path.exists(en_file):
            continue

        # Compute baseline from reference language
        ref_file = os.path.join(dirpath, f'{REFERENCE_LANG}.md')
        baseline = check_file(en_file, ref_file) if os.path.exists(ref_file) else 0.0

        for lang in GOOGLE_LANGS:
            lang_file = os.path.join(dirpath, f'{lang}.md')
            if not os.path.exists(lang_file):
                continue

            ratio = check_file(en_file, lang_file)
            delta = ratio - baseline

            if ratio >= ABSOLUTE_MIN and delta > DELTA_THRESHOLD:
                rel_path = os.path.relpath(lang_file, PROJECT_ROOT)
                affected.append((rel_path, ratio, baseline, delta))

    return sorted(affected)


def main():
    delete_mode = '--delete' in sys.argv

    affected = find_untranslated()

    if not affected:
        print("No untranslated files found.")
        return

    print(f"Found {len(affected)} broken files (>{DELTA_THRESHOLD*100:.0f}pp above {REFERENCE_LANG} baseline):\n")
    print(f"  {'file':<60} {'ratio':>6} {'de ref':>6} {'delta':>6}")
    print(f"  {'-'*60} {'-'*6} {'-'*6} {'-'*6}")
    for path, ratio, baseline, delta in affected:
        print(f"  {path:<60} {ratio*100:5.1f}% {baseline*100:5.1f}% +{delta*100:4.1f}p")

    if delete_mode:
        print(f"\nDeleting {len(affected)} files...")
        for path, _, _, _ in affected:
            full_path = PROJECT_ROOT / path
            full_path.unlink()
            print(f"  Deleted: {path}")
        print("Done.")
    else:
        print(f"\nRun with --delete to remove these files.")


if __name__ == '__main__':
    main()
