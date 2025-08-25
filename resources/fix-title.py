#!/usr/bin/env python3
"""
Script to fix missing closing quotes in YAML title fields.
Scans through books directory structure and fixes title: "Book Title entries
that are missing the closing quote.
"""

import os
import re
import sys
from pathlib import Path

def is_language_yml_file(filepath):
    """Check if file is a language-specific YAML file (not book.yml)"""
    filename = os.path.basename(filepath)
    # Check if it's a .yml file and matches language code pattern (2-5 chars, possibly with hyphen)
    # Exclude book.yml files
    if filename == 'book.yml':
        return False
    return filename.endswith('.yml') and re.match(r'^[a-z]{2}(-[A-Za-z]+)?\.yml$', filename)

def fix_title_quotes(content):
    """Fix missing closing quotes in title field"""
    lines = content.split('\n')
    fixed_lines = []
    changed = False
    
    for line in lines:
        # Look for title lines that start with quote but don't end with quote
        if re.match(r'^title:\s*"[^"]*[^"]$', line.strip()):
            # Add missing closing quote
            fixed_line = line.rstrip() + '"'
            fixed_lines.append(fixed_line)
            changed = True
            print(f"  Fixed: {line.strip()} -> {fixed_line.strip()}")
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), changed

def scan_and_fix_directory(root_dir):
    """Scan directory and fix YAML files"""
    root_path = Path(root_dir)
    
    if not root_path.exists():
        print(f"Error: Directory '{root_dir}' does not exist")
        return
    
    total_files_scanned = 0
    total_files_fixed = 0
    
    print(f"Scanning directory: {root_dir}")
    print("=" * 50)
    
    # Walk through all subdirectories
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            
            # Check if this is a language-specific YAML file
            if is_language_yml_file(filepath):
                total_files_scanned += 1
                relative_path = os.path.relpath(filepath, root_dir)
                
                try:
                    # Read the file
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Fix quotes if needed
                    fixed_content, changed = fix_title_quotes(content)
                    
                    if changed:
                        # Write back the fixed content
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(fixed_content)
                        
                        print(f"✓ Fixed: {relative_path}")
                        total_files_fixed += 1
                    
                except Exception as e:
                    print(f"✗ Error processing {relative_path}: {e}")
    
    print("=" * 50)
    print(f"Scan complete!")
    print(f"Files scanned: {total_files_scanned}")
    print(f"Files fixed: {total_files_fixed}")

def main():
    """Main function"""
    # Default to current directory if no argument provided
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "books"  # Default books directory
    
    print("YAML Title Quote Fixer")
    print("=" * 50)
    print("This script will:")
    print("1. Scan for language-specific YAML files (e.g., en.yml, fr.yml)")
    print("2. Exclude book.yml files")
    print("3. Fix title fields missing closing quotes")
    print("4. Show progress and results")
    print()
    
    # Confirm before proceeding
    response = input(f"Proceed with scanning '{directory}'? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("Operation cancelled.")
        return
    
    scan_and_fix_directory(directory)

if __name__ == "__main__":
    main()