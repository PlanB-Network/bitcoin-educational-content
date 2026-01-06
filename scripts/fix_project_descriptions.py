#!/usr/bin/env python3
"""
Fix project description formatting in YAML files.

This script rewrites descriptions that span multiple lines with indentation
to be single-line paragraphs. Empty lines between text indicate separate
paragraphs and are preserved.

List items (lines starting with -, *, or numbers) are preserved as-is.
"""

import os
import re
from pathlib import Path


def is_list_item(line: str) -> bool:
    """Check if a line is a list item (bullet or numbered)."""
    stripped = line.lstrip()
    # Bullet lists (-, *)
    if stripped.startswith(('- ', '* ')):
        return True
    # Numbered lists (1. 2. etc)
    if re.match(r'^\d+\.\s', stripped):
        return True
    return False


def needs_fixing(description_lines: list) -> bool:
    """
    Check if description actually needs fixing.

    Returns True only if there are lines that continue a paragraph
    (non-empty, non-list lines that don't start a new paragraph).
    """
    if len(description_lines) <= 1:
        return False

    # Check if there are any wrapped lines (lines within a paragraph)
    in_paragraph = False
    has_wrapped_lines = False

    for line in description_lines:
        if line == '':
            in_paragraph = False
        elif is_list_item(line):
            in_paragraph = False
        else:
            if in_paragraph:
                # This is a continuation line
                has_wrapped_lines = True
                break
            in_paragraph = True

    return has_wrapped_lines


def fix_description(content: str) -> tuple[str, bool]:
    """
    Fix description formatting in YAML content.

    Merges lines within paragraphs while preserving paragraph breaks and lists.

    Returns: (fixed_content, was_modified)
    """
    lines = content.split('\n')
    result = []
    i = 0
    was_modified = False

    while i < len(lines):
        line = lines[i]

        # Check if this is the description field
        if line.strip() == 'description: |':
            result.append(line)
            i += 1

            # Collect all description lines
            description_lines = []
            base_indent = None

            while i < len(lines):
                current = lines[i]

                # Check if we've moved past the description block
                # (non-indented line or different field)
                if current and not current.startswith('  '):
                    break

                # Get the content after the indentation
                if current.strip():
                    # Determine base indentation from first non-empty line
                    if base_indent is None:
                        base_indent = len(current) - len(current.lstrip())

                    # Extract content (removing base indentation)
                    if len(current) >= base_indent:
                        content_part = current[base_indent:]
                        description_lines.append(content_part)
                    else:
                        description_lines.append(current.strip())
                else:
                    # Empty line indicates paragraph break
                    description_lines.append('')

                i += 1

            # Check if this description actually needs fixing
            if not needs_fixing(description_lines):
                # Write back as-is
                for line in description_lines:
                    if line:
                        result.append(f'  {line}')
                    else:
                        result.append('')
                continue

            # Process description lines into paragraphs
            paragraphs = []
            current_paragraph = []

            for line in description_lines:
                if line == '':
                    # Empty line - end current paragraph if any
                    if current_paragraph:
                        # Join lines in paragraph with a space
                        paragraph_text = ' '.join(current_paragraph)
                        paragraphs.append(paragraph_text)
                        current_paragraph = []
                    # Keep the empty line to separate paragraphs
                    paragraphs.append('')
                elif is_list_item(line):
                    # List item - end current paragraph and add list item as-is
                    if current_paragraph:
                        paragraph_text = ' '.join(current_paragraph)
                        paragraphs.append(paragraph_text)
                        current_paragraph = []
                    paragraphs.append(line.strip())
                else:
                    # Regular text - add to current paragraph
                    current_paragraph.append(line.strip())

            # Don't forget the last paragraph
            if current_paragraph:
                paragraph_text = ' '.join(current_paragraph)
                paragraphs.append(paragraph_text)

            # Remove trailing empty lines
            while paragraphs and paragraphs[-1] == '':
                paragraphs.pop()

            # Write the reformatted description
            for paragraph in paragraphs:
                if paragraph:
                    result.append(f'  {paragraph}')
                else:
                    result.append('')

            was_modified = True

        else:
            result.append(line)
            i += 1

    return '\n'.join(result), was_modified


def process_file(file_path: Path) -> bool:
    """
    Process a single YAML file.

    Returns True if the file was modified, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Skip if no description field
        if 'description: |' not in original_content:
            return False

        fixed_content, was_modified = fix_description(original_content)

        # Only write if content was actually modified
        if was_modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main function to process all project YAML files."""
    # Get the repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    projects_dir = repo_root / 'resources' / 'projects'

    if not projects_dir.exists():
        print(f"Projects directory not found: {projects_dir}")
        return

    # Find all YAML files in project directories
    yaml_files = list(projects_dir.glob('*/*.yml'))

    # Exclude project.yml files, only process language files
    language_files = [f for f in yaml_files if f.name != 'project.yml']

    print(f"Found {len(language_files)} language YAML files to check")

    modified_count = 0

    for file_path in sorted(language_files):
        if process_file(file_path):
            print(f"✓ Fixed: {file_path.relative_to(repo_root)}")
            modified_count += 1

    print(f"\nCompleted! Modified {modified_count} files.")


if __name__ == '__main__':
    main()
