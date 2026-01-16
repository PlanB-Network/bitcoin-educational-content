#!/usr/bin/env python3
"""
PlanB Network Bulk Content Validator

Validates all content folders in the repository against their respective schemas.
Uses validate.py to validate each folder individually.

Usage:
    python validate_all.py                    # Validate all content
    python validate_all.py --courses-only     # Validate only courses
    python validate_all.py --tutorials-only   # Validate only tutorials
    python validate_all.py --resources-only   # Validate only resources
    python validate_all.py --json             # Output as JSON
"""

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ANSI color codes for terminal output
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    END = "\033[0m"


@dataclass
class ContentFolderResult:
    """Holds validation results for a single content folder."""
    folder: str
    content_type: str
    total_errors: int = 0
    total_warnings: int = 0
    file_results: list = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return self.total_errors == 0


# Content types and their root directories
CONTENT_TYPE_ROOTS = {
    "courses": "courses",
    "tutorials": "tutorials",
    "professors": "professors",
    "events": "events",
    "resources/bet": "resources/bet",
    "resources/books": "resources/books",
    "resources/channels": "resources/channels",
    "resources/conferences": "resources/conferences",
    "resources/glossary": "resources/glossary",
    "resources/movies": "resources/movies",
    "resources/newsletters": "resources/newsletters",
    "resources/papers": "resources/papers",
    "resources/podcasts": "resources/podcasts",
    "resources/projects": "resources/projects",
}


def find_repo_root() -> Path:
    """Find the repository root by looking for .git directory."""
    current = Path(__file__).resolve().parent
    for _ in range(10):
        if (current / ".git").exists():
            return current
        if current.parent == current:
            break
        current = current.parent

    # Fallback: assume we're in scripts/validation-format/
    return Path(__file__).resolve().parent.parent.parent


def get_content_folders(repo_root: Path, content_type: str) -> list[Path]:
    """Get all content folders for a given content type."""
    root_path = repo_root / content_type

    if not root_path.exists():
        return []

    folders = []

    # Special handling for tutorials (has category subfolders)
    if content_type == "tutorials":
        for category in root_path.iterdir():
            if category.is_dir() and not category.name.startswith('.'):
                for tutorial in category.iterdir():
                    if tutorial.is_dir() and not tutorial.name.startswith('.'):
                        # Check if it has a tutorial.yml file
                        if (tutorial / "tutorial.yml").exists():
                            folders.append(tutorial)
    else:
        # Direct content folders (courses, professors, etc.)
        for item in root_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                folders.append(item)

    return sorted(folders)


def validate_folder(repo_root: Path, folder: Path, json_output: bool = True) -> dict:
    """Run validate.py on a single folder and return the result."""
    validate_script = repo_root / "scripts" / "validation-format" / "validate.py"

    # Calculate relative path from repo root
    try:
        rel_path = folder.relative_to(repo_root)
    except ValueError:
        rel_path = folder

    cmd = [sys.executable, str(validate_script), str(rel_path), "--json"]

    try:
        result = subprocess.run(
            cmd,
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            timeout=60
        )

        # Parse JSON output
        if result.stdout:
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                return {
                    "folder": str(rel_path),
                    "results": [],
                    "total_errors": 1,
                    "total_warnings": 0,
                    "error": f"Failed to parse validator output: {result.stdout[:200]}"
                }
        else:
            return {
                "folder": str(rel_path),
                "results": [],
                "total_errors": 1,
                "total_warnings": 0,
                "error": f"No output from validator. stderr: {result.stderr[:200] if result.stderr else 'none'}"
            }
    except subprocess.TimeoutExpired:
        return {
            "folder": str(rel_path),
            "results": [],
            "total_errors": 1,
            "total_warnings": 0,
            "error": "Validation timed out"
        }
    except Exception as e:
        return {
            "folder": str(rel_path),
            "results": [],
            "total_errors": 1,
            "total_warnings": 0,
            "error": str(e)
        }


def print_progress(current: int, total: int, folder: str, result: dict, width: int = 50):
    """Print progress bar and current folder status."""
    percent = current / total
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)

    status = ""
    if result["total_errors"] > 0:
        status = f"{Colors.RED}✗{Colors.END}"
    elif result["total_warnings"] > 0:
        status = f"{Colors.YELLOW}!{Colors.END}"
    else:
        status = f"{Colors.GREEN}✓{Colors.END}"

    # Clear line and print progress
    print(f"\r{Colors.CYAN}[{bar}]{Colors.END} {current}/{total} {status} {folder[:60]:<60}", end="", flush=True)


def main():
    parser = argparse.ArgumentParser(
        description="Validate all PlanB Network content against JSON schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate_all.py                    # Validate everything
  python validate_all.py --courses-only     # Validate only courses
  python validate_all.py --tutorials-only   # Validate only tutorials
  python validate_all.py --resources-only   # Validate all resource types
  python validate_all.py --json             # Output as JSON
  python validate_all.py --summary-only     # Show only summary, not individual errors
        """
    )

    # Filter options
    parser.add_argument(
        "--courses-only",
        action="store_true",
        help="Validate only courses"
    )
    parser.add_argument(
        "--tutorials-only",
        action="store_true",
        help="Validate only tutorials"
    )
    parser.add_argument(
        "--professors-only",
        action="store_true",
        help="Validate only professors"
    )
    parser.add_argument(
        "--events-only",
        action="store_true",
        help="Validate only events"
    )
    parser.add_argument(
        "--resources-only",
        action="store_true",
        help="Validate only resources (all resource types)"
    )
    parser.add_argument(
        "--type",
        type=str,
        help="Validate specific content type (e.g., 'resources/papers', 'tutorials')"
    )

    # Output options
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "--summary-only", "-s",
        action="store_true",
        help="Show only summary statistics, not individual errors"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show all results including passed validations"
    )

    args = parser.parse_args()

    repo_root = find_repo_root()

    # Determine which content types to validate
    content_types_to_validate = []

    if args.type:
        if args.type in CONTENT_TYPE_ROOTS:
            content_types_to_validate = [args.type]
        else:
            print(f"{Colors.RED}Error:{Colors.END} Unknown content type '{args.type}'")
            print(f"Available types: {', '.join(CONTENT_TYPE_ROOTS.keys())}")
            sys.exit(1)
    elif args.courses_only:
        content_types_to_validate = ["courses"]
    elif args.tutorials_only:
        content_types_to_validate = ["tutorials"]
    elif args.professors_only:
        content_types_to_validate = ["professors"]
    elif args.events_only:
        content_types_to_validate = ["events"]
    elif args.resources_only:
        content_types_to_validate = [t for t in CONTENT_TYPE_ROOTS if t.startswith("resources/")]
    else:
        content_types_to_validate = list(CONTENT_TYPE_ROOTS.keys())

    # Collect all folders to validate
    all_folders = []
    for content_type in content_types_to_validate:
        folders = get_content_folders(repo_root, content_type)
        for folder in folders:
            all_folders.append((content_type, folder))

    if not all_folders:
        if args.json:
            print(json.dumps({"error": "No content folders found to validate", "results": []}))
        else:
            print(f"{Colors.YELLOW}No content folders found to validate.{Colors.END}")
        sys.exit(0)

    # Validate all folders
    all_results = []
    total_errors = 0
    total_warnings = 0
    passed_count = 0
    failed_count = 0
    warning_count = 0

    if not args.json:
        print(f"\n{Colors.BOLD}Validating {len(all_folders)} content folders...{Colors.END}\n")

    for i, (content_type, folder) in enumerate(all_folders, 1):
        result = validate_folder(repo_root, folder)
        result["content_type"] = content_type
        all_results.append(result)

        total_errors += result.get("total_errors", 0)
        total_warnings += result.get("total_warnings", 0)

        if result.get("total_errors", 0) > 0:
            failed_count += 1
        elif result.get("total_warnings", 0) > 0:
            warning_count += 1
        else:
            passed_count += 1

        if not args.json:
            print_progress(i, len(all_folders), result["folder"], result)

    if not args.json:
        print()  # New line after progress bar

    # Output results
    if args.json:
        output = {
            "summary": {
                "total_folders": len(all_folders),
                "passed": passed_count,
                "failed": failed_count,
                "warnings_only": warning_count,
                "total_errors": total_errors,
                "total_warnings": total_warnings,
            },
            "results": all_results
        }
        print(json.dumps(output, indent=2))
    else:
        # Print detailed results (errors and warnings)
        if not args.summary_only:
            print(f"\n{Colors.BOLD}{'='*70}{Colors.END}")
            print(f"{Colors.BOLD}Validation Details{Colors.END}")
            print(f"{'='*70}\n")

            # Group results by content type
            by_type: dict[str, list] = {}
            for result in all_results:
                ct = result.get("content_type", "unknown")
                if ct not in by_type:
                    by_type[ct] = []
                by_type[ct].append(result)

            for content_type in sorted(by_type.keys()):
                results = by_type[content_type]

                # Check if there are any errors or warnings in this type
                has_issues = any(
                    r.get("total_errors", 0) > 0 or r.get("total_warnings", 0) > 0
                    for r in results
                )

                if has_issues or args.verbose:
                    print(f"\n{Colors.MAGENTA}{Colors.BOLD}[{content_type}]{Colors.END}")

                    for result in results:
                        errors = result.get("total_errors", 0)
                        warnings = result.get("total_warnings", 0)

                        if errors > 0:
                            print(f"  {Colors.RED}✗{Colors.END} {result['folder']} - {errors} error(s), {warnings} warning(s)")
                            if not args.summary_only:
                                for file_result in result.get("results", []):
                                    for error in file_result.get("errors", []):
                                        print(f"      {Colors.RED}ERROR:{Colors.END} {error}")
                                    for warning in file_result.get("warnings", []):
                                        print(f"      {Colors.YELLOW}WARNING:{Colors.END} {warning}")
                        elif warnings > 0:
                            print(f"  {Colors.YELLOW}!{Colors.END} {result['folder']} - {warnings} warning(s)")
                            if not args.summary_only:
                                for file_result in result.get("results", []):
                                    for warning in file_result.get("warnings", []):
                                        print(f"      {Colors.YELLOW}WARNING:{Colors.END} {warning}")
                        elif args.verbose:
                            print(f"  {Colors.GREEN}✓{Colors.END} {result['folder']}")

        # Print summary
        print(f"\n{Colors.BOLD}{'='*70}{Colors.END}")
        print(f"{Colors.BOLD}Summary{Colors.END}")
        print(f"{'='*70}\n")

        print(f"  Total folders validated: {len(all_folders)}")
        print(f"  {Colors.GREEN}Passed:{Colors.END}         {passed_count}")
        print(f"  {Colors.YELLOW}Warnings only:{Colors.END}  {warning_count}")
        print(f"  {Colors.RED}Failed:{Colors.END}         {failed_count}")
        print()
        print(f"  Total errors:   {total_errors}")
        print(f"  Total warnings: {total_warnings}")

        print(f"\n{'='*70}")
        if total_errors == 0:
            if total_warnings == 0:
                print(f"{Colors.GREEN}{Colors.BOLD}All validations passed!{Colors.END}")
            else:
                print(f"{Colors.YELLOW}{Colors.BOLD}Validation passed with {total_warnings} warning(s){Colors.END}")
        else:
            print(f"{Colors.RED}{Colors.BOLD}Validation failed: {total_errors} error(s) in {failed_count} folder(s){Colors.END}")
        print(f"{'='*70}\n")

    # Exit codes: 0 = passed, 1 = errors, 2 = warnings only
    if total_errors > 0:
        sys.exit(1)
    elif total_warnings > 0:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
