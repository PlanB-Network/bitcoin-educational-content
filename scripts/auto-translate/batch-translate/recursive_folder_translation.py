#!/usr/bin/env python3
"""
Recursive folder translation script.

Finds all {lang}.yml or {lang}.md files recursively in a folder
and translates them from source language to output language.

Usage:
    python recursive_folder_translation.py -s en -o fr --path ../../courses/phi102/quizz/
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

# Define base paths
SCRIPT_DIR = Path(__file__).resolve().parent
TRANSLATION_CONTROLLER = SCRIPT_DIR.parent / "translation_controller.py"


def find_language_files(base_path: Path, source_lang: str) -> List[Path]:
    """
    Recursively find all files matching {source_lang}.yml or {source_lang}.md pattern.

    Args:
        base_path: Directory to search in
        source_lang: Source language code (e.g., 'en', 'fr')

    Returns:
        List of Path objects for matching files
    """
    patterns = [f"{source_lang}.yml", f"{source_lang}.md"]
    found_files = []

    for pattern in patterns:
        found_files.extend(base_path.rglob(pattern))

    return sorted(found_files)


def check_translation_exists(source_file: Path, target_lang: str) -> bool:
    """
    Check if translation already exists for target language.

    Args:
        source_file: Source file path
        target_lang: Target language code

    Returns:
        True if translation file already exists
    """
    target_file = source_file.parent / f"{target_lang}{source_file.suffix}"
    return target_file.exists()


def translate_file(source_file: Path, target_lang: str, force: bool = False) -> Tuple[bool, str]:
    """
    Translate a single file to target language using translation_controller.

    Args:
        source_file: Source file path
        target_lang: Target language code
        force: If True, overwrite existing translations

    Returns:
        Tuple of (success, message)
    """
    if not force and check_translation_exists(source_file, target_lang):
        return False, f"Skipped (already exists): {source_file}"

    try:
        command = ["python3", str(TRANSLATION_CONTROLLER), str(source_file), target_lang]
        result = subprocess.run(command, check=True, capture_output=True, text=True)

        output_file = source_file.parent / f"{target_lang}{source_file.suffix}"
        return True, f"Translated: {source_file} -> {output_file}"
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else str(e)
        return False, f"Error translating {source_file}: {error_msg}"


def main():
    parser = argparse.ArgumentParser(
        description="Recursively translate language files in a folder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Translate all English files to French in quizz folder
    python recursive_folder_translation.py -s en -o fr --path ../../courses/phi102/quizz/

    # Translate French files to English, overwriting existing
    python recursive_folder_translation.py -s fr -o en --path ./content/ --force

    # Dry run to see what would be translated
    python recursive_folder_translation.py -s en -o de --path ./courses/ --dry-run
        """
    )

    parser.add_argument(
        "-s", "--source",
        required=True,
        help="Source language code (e.g., en, fr, de)"
    )

    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output/target language code (e.g., en, fr, de)"
    )

    parser.add_argument(
        "--path",
        required=True,
        type=Path,
        help="Path to folder to search recursively"
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing translation files"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be translated without actually translating"
    )

    args = parser.parse_args()

    # Resolve path relative to current working directory
    base_path = args.path.resolve()

    if not base_path.exists():
        print(f"Error: Path does not exist: {base_path}", file=sys.stderr)
        sys.exit(1)

    if not base_path.is_dir():
        print(f"Error: Path is not a directory: {base_path}", file=sys.stderr)
        sys.exit(1)

    if args.source == args.output:
        print("Error: Source and output languages must be different", file=sys.stderr)
        sys.exit(1)

    print(f"Searching for {args.source}.yml and {args.source}.md files in: {base_path}")
    print(f"Target language: {args.output}")
    print("-" * 60)

    files = find_language_files(base_path, args.source)

    if not files:
        print(f"No {args.source}.yml or {args.source}.md files found.")
        sys.exit(0)

    print(f"Found {len(files)} file(s) to process:\n")

    if args.dry_run:
        for f in files:
            exists = check_translation_exists(f, args.output)
            status = "[EXISTS]" if exists else "[WILL TRANSLATE]"
            if args.force and exists:
                status = "[WILL OVERWRITE]"
            print(f"  {status} {f}")
        print(f"\nDry run complete. Use without --dry-run to translate.")
        sys.exit(0)

    # Perform translations
    success_count = 0
    skip_count = 0
    error_count = 0

    for source_file in files:
        success, message = translate_file(source_file, args.output, args.force)
        print(message)

        if success:
            success_count += 1
        elif "Skipped" in message:
            skip_count += 1
        else:
            error_count += 1

    print("-" * 60)
    print(f"Summary: {success_count} translated, {skip_count} skipped, {error_count} errors")

    if error_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
