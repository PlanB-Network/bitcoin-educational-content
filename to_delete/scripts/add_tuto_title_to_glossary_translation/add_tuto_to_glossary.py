#!/usr/bin/env python3
"""
Script to add tutorial names to the translation glossary.
Scans all tutorials, extracts the 'name' from en.md headers,
and prompts user to add new entries to glossary.yml
"""

import os
import re
import sys
from pathlib import Path

# Paths relative to this script's location
SCRIPT_DIR = Path(__file__).parent
TUTORIALS_DIR = SCRIPT_DIR / "../../tutorials"
GLOSSARY_PATH = SCRIPT_DIR / "../auto-translate/translation_logic/glossary.yml"


def load_glossary_entries() -> set:
    """Load existing non_translatable entries from glossary.yml"""
    entries = set()

    if not GLOSSARY_PATH.exists():
        print(f"Error: Glossary file not found at {GLOSSARY_PATH}")
        sys.exit(1)

    with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse entries under non_translatable section
    in_section = False
    for line in content.split("\n"):
        if line.strip().startswith("non_translatable:"):
            in_section = True
            continue
        if in_section:
            # Stop if we hit another top-level key
            if line and not line.startswith(" ") and not line.startswith("#"):
                break
            # Extract entry (format: "  - EntryName" or "  - 'Entry Name'")
            match = re.match(r'^\s+-\s+(.+)$', line)
            if match:
                entry = match.group(1).strip()
                # Remove quotes if present
                if (entry.startswith('"') and entry.endswith('"')) or \
                   (entry.startswith("'") and entry.endswith("'")):
                    entry = entry[1:-1]
                entries.add(entry.lower())

    return entries


def extract_tutorial_name(en_md_path: Path) -> str | None:
    """Extract 'name' field from en.md YAML front matter"""
    try:
        with open(en_md_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"  Warning: Could not read {en_md_path}: {e}")
        return None

    # Check for YAML front matter
    if not content.startswith("---"):
        return None

    # Find end of front matter
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return None

    front_matter = content[3:end_match.start() + 3]

    # Extract name field
    name_match = re.search(r'^name:\s*(.+)$', front_matter, re.MULTILINE)
    if name_match:
        name = name_match.group(1).strip()
        # Remove quotes if present
        if (name.startswith('"') and name.endswith('"')) or \
           (name.startswith("'") and name.endswith("'")):
            name = name[1:-1]
        return name

    return None


def get_tutorial_friendly_name(path: Path) -> str:
    """Get a friendly display name for the tutorial from its path"""
    # Path structure: tutorials/category/tutorial-name/en.md
    parts = path.parts
    try:
        tuto_idx = parts.index("tutorials")
        category = parts[tuto_idx + 1] if len(parts) > tuto_idx + 1 else "unknown"
        tuto_name = parts[tuto_idx + 2] if len(parts) > tuto_idx + 2 else "unknown"
        return f"{category}/{tuto_name}"
    except (ValueError, IndexError):
        return str(path)


def add_to_glossary(name: str):
    """Add a new entry to the glossary.yml file"""
    with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the last entry in non_translatable section
    insert_idx = None
    in_section = False

    for i, line in enumerate(lines):
        if "non_translatable:" in line:
            in_section = True
            continue
        if in_section:
            # Check if this line is an entry
            if re.match(r'^\s+-\s+', line):
                insert_idx = i + 1
            # Stop if we hit another top-level key or end of entries
            elif line.strip() and not line.startswith(" ") and not line.startswith("#"):
                break

    if insert_idx is None:
        print(f"  Error: Could not find insertion point in glossary")
        return False

    # Prepare new entry - quote if contains special chars
    if " " in name or ":" in name or "-" in name:
        new_entry = f'  - "{name}"\n'
    else:
        new_entry = f"  - {name}\n"

    lines.insert(insert_idx, new_entry)

    with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)

    return True


def main():
    print("\n" + "=" * 60)
    print("  Tutorial Name → Glossary Importer")
    print("=" * 60 + "\n")

    # Load existing glossary entries
    print("Loading glossary entries...")
    existing_entries = load_glossary_entries()
    print(f"Found {len(existing_entries)} existing entries\n")

    # Find all en.md files
    tutorials_path = TUTORIALS_DIR.resolve()
    if not tutorials_path.exists():
        print(f"Error: Tutorials directory not found at {tutorials_path}")
        sys.exit(1)

    en_md_files = sorted(tutorials_path.rglob("en.md"))
    total_tutorials = len(en_md_files)
    print(f"Found {total_tutorials} tutorials to process\n")
    print("-" * 60)

    added_count = 0
    skipped_count = 0
    already_exists_count = 0

    for idx, en_md_path in enumerate(en_md_files, 1):
        friendly_name = get_tutorial_friendly_name(en_md_path)
        remaining = total_tutorials - idx

        # Extract tutorial name
        tuto_name = extract_tutorial_name(en_md_path)

        if not tuto_name:
            print(f"[{idx}/{total_tutorials}] {friendly_name}")
            print(f"  ⚠ No 'name' field found - skipping")
            print()
            continue

        # Check if already in glossary (case-insensitive)
        if tuto_name.lower() in existing_entries:
            already_exists_count += 1
            continue  # Silent skip for existing entries

        # Prompt user
        print(f"\n[{idx}/{total_tutorials}] {friendly_name}")
        print(f"  📝 Tutorial name: \033[1;36m{tuto_name}\033[0m")
        print(f"  📊 {remaining} tutorials remaining after this")

        while True:
            response = input(f"  Add to glossary? [Y/n]: ").strip().lower()

            if response == "" or response == "y" or response == "yes":
                if add_to_glossary(tuto_name):
                    existing_entries.add(tuto_name.lower())
                    print(f"  ✅ Added '{tuto_name}' to glossary")
                    added_count += 1
                break
            elif response == "n" or response == "no":
                print(f"  ⏭ Skipped")
                skipped_count += 1
                break
            else:
                print("  Please enter 'y' (yes) or 'n' (no)")

    # Summary
    print("\n" + "=" * 60)
    print("  Summary")
    print("=" * 60)
    print(f"  ✅ Added to glossary:     {added_count}")
    print(f"  ⏭ Skipped by user:       {skipped_count}")
    print(f"  📋 Already in glossary:  {already_exists_count}")
    print(f"  📁 Total processed:      {total_tutorials}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Interrupted by user. Exiting...")
        sys.exit(0)
