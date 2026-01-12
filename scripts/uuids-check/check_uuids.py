#!/usr/bin/env python3
"""
UUID v4 Checker and Replacer for YAML files.

This script:
1. Scans all YAML files in the repository for UUIDs
2. Identifies UUIDs that are NOT valid UUIDv4
3. Generates new UUIDv4 replacements
4. Finds all references in .md and .yml files
5. Replaces the old UUID with the new one everywhere

Usage:
    python check_uuids.py [--dry-run] [--verbose]

Options:
    --dry-run   Show what would be changed without making changes
    --verbose   Show detailed output
"""

import os
import re
import sys
import uuid
from pathlib import Path
from dataclasses import dataclass
from typing import Generator


# UUID regex pattern (matches any UUID format)
UUID_PATTERN = re.compile(
    r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
    re.IGNORECASE
)

# UUIDv4 pattern: version digit is 4, variant is 8, 9, a, or b
UUIDV4_PATTERN = re.compile(
    r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$',
    re.IGNORECASE
)


@dataclass
class UUIDLocation:
    """Represents a UUID found in a file."""
    file_path: Path
    line_number: int
    uuid_value: str
    line_content: str


@dataclass
class UUIDReplacement:
    """Represents a UUID that needs replacement."""
    old_uuid: str
    new_uuid: str
    locations: list[UUIDLocation]


def is_uuid_v4(uuid_str: str) -> bool:
    """Check if a UUID string is a valid UUIDv4."""
    return bool(UUIDV4_PATTERN.match(uuid_str.lower()))


def generate_uuid_v4() -> str:
    """Generate a new UUIDv4."""
    return str(uuid.uuid4())


def find_yaml_files(repo_path: Path) -> Generator[Path, None, None]:
    """Find all YAML files in the repository."""
    for pattern in ['**/*.yml', '**/*.yaml']:
        yield from repo_path.glob(pattern)


def find_all_files(repo_path: Path) -> Generator[Path, None, None]:
    """Find all YAML and Markdown files in the repository."""
    for pattern in ['**/*.yml', '**/*.yaml', '**/*.md']:
        yield from repo_path.glob(pattern)


def extract_uuids_from_file(file_path: Path) -> list[UUIDLocation]:
    """Extract all UUIDs from a file with their locations."""
    locations = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                for match in UUID_PATTERN.finditer(line):
                    locations.append(UUIDLocation(
                        file_path=file_path,
                        line_number=line_num,
                        uuid_value=match.group().lower(),
                        line_content=line.rstrip()
                    ))
    except (UnicodeDecodeError, PermissionError) as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
    return locations


def find_uuid_references(uuid_str: str, repo_path: Path) -> list[UUIDLocation]:
    """Find all references to a UUID in YAML and Markdown files."""
    references = []
    uuid_lower = uuid_str.lower()

    for file_path in find_all_files(repo_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    if uuid_lower in line.lower():
                        references.append(UUIDLocation(
                            file_path=file_path,
                            line_number=line_num,
                            uuid_value=uuid_str,
                            line_content=line.rstrip()
                        ))
        except (UnicodeDecodeError, PermissionError):
            continue

    return references


def replace_uuid_in_file(file_path: Path, old_uuid: str, new_uuid: str) -> bool:
    """Replace all occurrences of old_uuid with new_uuid in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Case-insensitive replacement
        pattern = re.compile(re.escape(old_uuid), re.IGNORECASE)
        new_content = pattern.sub(new_uuid, content)

        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except (UnicodeDecodeError, PermissionError) as e:
        print(f"Error: Could not process {file_path}: {e}", file=sys.stderr)

    return False


def main():
    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    verbose = '--verbose' in sys.argv

    # Determine repository path (two levels up from script location)
    script_dir = Path(__file__).parent.resolve()
    repo_path = script_dir.parent.parent

    print(f"Scanning repository: {repo_path}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print("-" * 60)

    # Step 1: Find all UUIDs in YAML files
    all_uuids: dict[str, list[UUIDLocation]] = {}

    for yaml_file in find_yaml_files(repo_path):
        locations = extract_uuids_from_file(yaml_file)
        for loc in locations:
            uuid_key = loc.uuid_value
            if uuid_key not in all_uuids:
                all_uuids[uuid_key] = []
            all_uuids[uuid_key].append(loc)

    print(f"Found {len(all_uuids)} unique UUIDs in YAML files")

    # Step 2: Identify non-UUIDv4
    non_v4_uuids = {
        uuid_str: locations
        for uuid_str, locations in all_uuids.items()
        if not is_uuid_v4(uuid_str)
    }

    print(f"Found {len(non_v4_uuids)} non-UUIDv4 UUIDs that need replacement")
    print("-" * 60)

    if not non_v4_uuids:
        print("All UUIDs are valid UUIDv4. No changes needed.")
        return 0

    # Step 3: Process each non-v4 UUID
    replacements: list[UUIDReplacement] = []

    for old_uuid, yaml_locations in non_v4_uuids.items():
        # Find all references in repo (yml and md files)
        all_references = find_uuid_references(old_uuid, repo_path)

        # Generate new UUIDv4
        new_uuid = generate_uuid_v4()

        replacement = UUIDReplacement(
            old_uuid=old_uuid,
            new_uuid=new_uuid,
            locations=all_references
        )
        replacements.append(replacement)

        # Print info
        print(f"\n{'='*60}")
        print(f"OLD UUID (non-v4): {old_uuid}")
        print(f"NEW UUID (v4):     {new_uuid}")
        print(f"Found in {len(all_references)} location(s):")

        for loc in all_references:
            rel_path = loc.file_path.relative_to(repo_path)
            print(f"  - {rel_path}:{loc.line_number}")
            if verbose:
                print(f"    {loc.line_content[:80]}...")

    print(f"\n{'='*60}")
    print(f"SUMMARY: {len(replacements)} UUIDs to replace")
    print(f"Total file locations affected: {sum(len(r.locations) for r in replacements)}")

    if dry_run:
        print("\n[DRY RUN] No changes made. Run without --dry-run to apply changes.")
        return 0

    # Step 4: Apply replacements
    print("\nApplying replacements...")

    files_modified = set()
    for replacement in replacements:
        # Get unique files that need modification
        files_to_modify = {loc.file_path for loc in replacement.locations}

        for file_path in files_to_modify:
            if replace_uuid_in_file(file_path, replacement.old_uuid, replacement.new_uuid):
                files_modified.add(file_path)
                print(f"  Updated: {file_path.relative_to(repo_path)}")

    print(f"\nDone! Modified {len(files_modified)} file(s).")

    return 0


if __name__ == '__main__':
    sys.exit(main())
