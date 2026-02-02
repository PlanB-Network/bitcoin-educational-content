#!/usr/bin/env python3
"""
Script to demote markdown headings by one level in tutorial files.
Only processes files where:
1. H1 headings exist outside code blocks
2. The first heading IS an H1 (otherwise headings make sense already)

If H1 is not the first heading, only demote from that H1 onward.
"""

import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class HeadingInfo:
    line_num: int
    level: int  # 1 for #, 2 for ##, etc.
    text: str

def parse_headings_outside_code_blocks(content: str) -> List[HeadingInfo]:
    """
    Parse all markdown headings that are outside code blocks.
    Returns list of HeadingInfo with line numbers (0-indexed).
    """
    lines = content.split('\n')
    headings = []
    in_code_block = False

    for i, line in enumerate(lines):
        # Detect code block start/end (``` with optional language)
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Match markdown heading: 1-6 # followed by space and text
        match = re.match(r'^(#{1,6}) (.+)$', line)
        if match:
            level = len(match.group(1))
            text = match.group(2)
            headings.append(HeadingInfo(line_num=i, level=level, text=text))

    return headings

def should_process_file(headings: List[HeadingInfo]) -> Tuple[bool, Optional[int]]:
    """
    Determine if file should be processed and from which line.

    Returns:
        (should_process, start_line_index)
        - If first heading is H1: (True, 0) - demote all
        - If H1 appears later: (True, index_of_first_h1) - demote from H1 onward
        - If no H1: (False, None) - don't process
    """
    if not headings:
        return False, None

    # Find first H1
    first_h1_idx = None
    for i, h in enumerate(headings):
        if h.level == 1:
            first_h1_idx = i
            break

    if first_h1_idx is None:
        # No H1 found
        return False, None

    if first_h1_idx == 0:
        # First heading is H1 - demote all headings
        return True, 0
    else:
        # H1 is not first - only demote from H1 onward
        return True, first_h1_idx

def demote_headings(content: str, headings: List[HeadingInfo], start_idx: int) -> str:
    """
    Demote headings starting from start_idx in the headings list.
    """
    lines = content.split('\n')

    # Get line numbers to demote
    lines_to_demote = {h.line_num for h in headings[start_idx:]}

    result = []
    for i, line in enumerate(lines):
        if i in lines_to_demote:
            # Add one # to demote
            match = re.match(r'^(#{1,6}) (.+)$', line)
            if match:
                hashes = match.group(1)
                text = match.group(2)
                result.append(f'#{hashes} {text}')
            else:
                result.append(line)
        else:
            result.append(line)

    return '\n'.join(result)

def process_file(filepath: Path, dry_run: bool = False, verbose: bool = False) -> bool:
    """
    Process a single file. Returns True if file was modified.
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    headings = parse_headings_outside_code_blocks(content)
    should_process, start_idx = should_process_file(headings)

    if not should_process:
        if verbose:
            print(f"Skipped (no H1 or H1 not first): {filepath}")
        return False

    if verbose:
        first_heading = headings[0] if headings else None
        if start_idx == 0:
            print(f"Processing (first heading is H1): {filepath}")
        else:
            print(f"Processing (H1 at index {start_idx}, demoting from there): {filepath}")

    new_content = demote_headings(content, headings, start_idx)

    if dry_run:
        print(f"Would modify: {filepath}")
        # Show what would change
        if verbose:
            for h in headings[start_idx:start_idx+3]:
                print(f"  Line {h.line_num+1}: {'#'*h.level} -> {'#'*(h.level+1)}")
        return True

    try:
        filepath.write_text(new_content, encoding='utf-8')
        print(f"Modified: {filepath}")
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False

def main():
    tutorials_dir = Path('/home/asi0/asi0-repos/bitcoin-educational-content/tutorials')

    dry_run = '--dry-run' in sys.argv
    verbose = '--verbose' in sys.argv or '-v' in sys.argv

    if dry_run:
        print("DRY RUN - No files will be modified\n")

    modified_count = 0
    skipped_count = 0
    total_files = 0

    for md_file in sorted(tutorials_dir.rglob('*.md')):
        total_files += 1
        if process_file(md_file, dry_run, verbose):
            modified_count += 1
        else:
            skipped_count += 1

    print(f"\n{'Would modify' if dry_run else 'Modified'}: {modified_count} files")
    print(f"Skipped: {skipped_count} files")
    print(f"Total: {total_files} files")

if __name__ == '__main__':
    main()
