#!/usr/bin/env python3
"""
Script to rename image references in markdown files and/or rename actual image files.
Works with course directories and includes fuzzy search for course selection.
"""

import os
import re
from pathlib import Path
import sys

def fuzzy_search(query, choices):
    """Simple fuzzy search implementation for course names."""
    query = query.lower()
    results = []
    
    for choice in choices:
        choice_lower = choice.lower()
        score = 0
        
        # Exact match
        if query == choice_lower:
            score = 1000
        # Starts with query
        elif choice_lower.startswith(query):
            score = 100
        # Contains query
        elif query in choice_lower:
            score = 50
        # All characters from query are in choice (in order)
        else:
            query_idx = 0
            for char in choice_lower:
                if query_idx < len(query) and char == query[query_idx]:
                    query_idx += 1
                    score += 1
            if query_idx != len(query):
                score = 0
        
        if score > 0:
            results.append((choice, score))
    
    # Sort by score (highest first)
    results.sort(key=lambda x: x[1], reverse=True)
    return [r[0] for r in results]

def select_course():
    """Let user select a course directory with fuzzy search."""
    # Try different possible paths for the courses directory
    possible_paths = [
        Path('../../courses'),  # From scripts/rename_image
        Path('../courses'),     # From scripts
        Path('courses'),        # From root
    ]
    
    courses_dir = None
    for path in possible_paths:
        if path.exists() and path.is_dir():
            courses_dir = path
            break
    
    if not courses_dir:
        print("Error: courses directory not found.")
        print("Make sure the courses directory exists relative to this script.")
        return None
    
    courses_dir = Path('../../courses')
    
    if not courses_dir.exists():
        print("Error: courses directory not found. Make sure you're running this from the scripts/rename_image directory.")
        return None
    
    # Get all course directories
    course_dirs = [d.name for d in courses_dir.iterdir() if d.is_dir()]
    
    if not course_dirs:
        print("No course directories found in ../courses/")
        return None
    
    print("\n" + "=" * 60)
    print("Course Selection")
    print("=" * 60)
    print(f"\nFound {len(course_dirs)} courses available:")
    
    # Show first 10 courses
    for course in sorted(course_dirs)[:10]:
        print(f"  • {course}")
    if len(course_dirs) > 10:
        print(f"  ... and {len(course_dirs) - 10} more")
    
    while True:
        print("\nEnter course name (or part of it for fuzzy search):")
        query = input("Course: ").strip()
        
        if not query:
            print("No input provided. Exiting.")
            return None
        
        # Perform fuzzy search
        matches = fuzzy_search(query, course_dirs)
        
        if not matches:
            print(f"No courses found matching '{query}'")
            retry = input("Try again? (y/n): ").strip().lower()
            if retry != 'y':
                return None
            continue
        
        if len(matches) == 1:
            selected = matches[0]
            print(f"\n✓ Selected course: {selected}")
            confirm = input("Is this correct? (y/n): ").strip().lower()
            if confirm == 'y':
                return courses_dir / selected
        else:
            print(f"\nFound {len(matches)} matches:")
            for i, match in enumerate(matches[:10], 1):
                print(f"  {i}. {match}")
            if len(matches) > 10:
                print(f"  ... and {len(matches) - 10} more")
            
            choice = input("\nEnter number to select (or 'r' to retry): ").strip()
            
            if choice.lower() == 'r':
                continue
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(matches):
                    selected = matches[idx]
                    print(f"\n✓ Selected course: {selected}")
                    return courses_dir / selected
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input.")
        
        retry = input("Try again? (y/n): ").strip().lower()
        if retry != 'y':
            return None

def find_all_image_references(content):
    """Find all .webp image references in the content, preserving order."""
    pattern = r'(\./)?assets/([a-zA-Z-]+)/(\d+)\.webp'
    matches = re.finditer(pattern, content)
    
    all_refs = []
    for match in matches:
        all_refs.append({
            'start': match.start(),
            'end': match.end(),
            'full_match': match.group(0),
            'prefix': match.group(1) or '',
            'lang': match.group(2),
            'num': match.group(3)
        })
    
    return all_refs

def rename_references_in_file(file_path, course_dir):
    """Rename all image references in a single markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    all_refs = find_all_image_references(content)
    
    if not all_refs:
        print(f"  No .webp images found in {file_path.name}")
        return 0
    
    languages_found = set(ref['lang'] for ref in all_refs)
    print(f"  Found {len(all_refs)} total .webp image references")
    print(f"  Original language codes: {', '.join(sorted(languages_found))}")
    
    total_images = len(all_refs)
    digit_format = 2 if total_images < 100 else 3
    
    modified_content = content
    
    for i, ref in enumerate(reversed(all_refs), 1):
        seq_num = total_images - i + 1
        new_num = str(seq_num).zfill(digit_format)
        new_path = f"{ref['prefix']}assets/en/{new_num}.webp"
        
        modified_content = (
            modified_content[:ref['start']] + 
            new_path + 
            modified_content[ref['end']:]
        )
    
    if content != modified_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print(f"  ✅ Renamed {len(all_refs)} image references to assets/en/XX.webp ({digit_format} digits)")
        print(f"     Sequential numbering from 01 to {str(total_images).zfill(digit_format)}")
        
        example_refs = all_refs[:3]
        for i, ref in enumerate(example_refs, 1):
            new_num = str(i).zfill(digit_format)
            print(f"     {ref['full_match']} → assets/en/{new_num}.webp")
        if len(all_refs) > 3:
            print(f"     ... and {len(all_refs) - 3} more references")
        
        return len(all_refs)
    else:
        print(f"  No changes needed")
    
    return 0

def process_single_file(course_dir):
    """Process a single markdown file in the course directory."""
    file_name = input("Enter the markdown filename (e.g., fr.md): ").strip()
    md_file = course_dir / file_name
    
    if not md_file.exists():
        print(f"Error: File '{file_name}' not found in {course_dir.name}.")
        return
    
    if not md_file.suffix == '.md':
        print(f"Error: '{file_name}' is not a markdown file.")
        return
    
    print(f"\nProcessing {md_file.name}...")
    renamed_count = rename_references_in_file(md_file, course_dir)
    
    print("\n" + "=" * 50)
    print(f"Complete! Processed {md_file.name}")
    if renamed_count > 0:
        print(f"All {renamed_count} image references now use sequential assets/en/ paths")

def process_all_files(course_dir):
    """Process all markdown files in the course directory."""
    md_files = list(course_dir.glob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in {course_dir.name}.")
        return
    
    print(f"Found {len(md_files)} markdown files to process")
    print("Will convert all .webp images to sequential assets/en/ paths")
    print("-" * 50)
    
    total_renamed = 0
    files_modified = 0
    
    for md_file in sorted(md_files):
        print(f"\nProcessing {md_file.name}...")
        renamed_count = rename_references_in_file(md_file, course_dir)
        if renamed_count > 0:
            total_renamed += renamed_count
            files_modified += 1
    
    print("\n" + "=" * 50)
    print(f"Complete! Processed {len(md_files)} files")
    print(f"Modified {files_modified} files with {total_renamed} total image references")

def find_all_webp_files_recursive(directory):
    """Find all .webp files recursively in directory and subdirectories."""
    image_files = []
    
    for file_path in Path(directory).rglob('*.webp'):
        filename = file_path.name
        matches = re.findall(r'\d+', filename)
        
        if matches:
            number = matches[-1]
            
            if filename == f"{number.zfill(2)}.webp" or filename == f"{number.zfill(3)}.webp" or filename == f"{number}.webp":
                continue
            
            if len(number) == 1:
                new_name = f"0{number}.webp"
            else:
                new_name = f"{number.zfill(len(number))}.webp"
            
            image_files.append({
                'path': file_path,
                'directory': file_path.parent,
                'name': filename,
                'number': number,
                'new_name': new_name,
                'relative_path': file_path.relative_to(directory)
            })
    
    return sorted(image_files, key=lambda x: (str(x['directory']), int(x['number'])))

def rename_image_files(course_dir):
    """Rename actual image files in the course's assets directory."""
    print("\n" + "=" * 60)
    print("Image File Renaming (Recursive)")
    print("=" * 60)
    
    assets_dir = course_dir / 'assets'
    
    if not assets_dir.exists():
        print(f"No assets directory found in {course_dir.name}")
        return
    
    print(f"\nScanning {assets_dir} and all subdirectories for .webp files...")
    
    files_to_rename = find_all_webp_files_recursive(assets_dir)
    
    if not files_to_rename:
        print(f"\nNo .webp files need renaming in {assets_dir}")
        return
    
    files_by_dir = {}
    for file_info in files_to_rename:
        dir_key = str(file_info['directory'])
        if dir_key not in files_by_dir:
            files_by_dir[dir_key] = []
        files_by_dir[dir_key].append(file_info)
    
    print(f"\nFound {len(files_to_rename)} files to rename across {len(files_by_dir)} directories:")
    print("-" * 60)
    
    for dir_path, files in sorted(files_by_dir.items())[:10]:
        try:
            rel_dir = Path(dir_path).relative_to(course_dir)
        except ValueError:
            rel_dir = Path(dir_path).name
        print(f"\n📁 {rel_dir}/ ({len(files)} files)")
        for file_info in files[:3]:
            print(f"    {file_info['name']} → {file_info['new_name']}")
        if len(files) > 3:
            print(f"    ... and {len(files) - 3} more files")
    
    if len(files_by_dir) > 10:
        print(f"\n... and {len(files_by_dir) - 10} more directories")
    
    print("\n" + "-" * 60)
    print(f"Total: {len(files_to_rename)} files across {len(files_by_dir)} directories")
    
    confirm = input(f"\nRename all these files? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("Operation cancelled.")
        return
    
    print("\nRenaming files...")
    renamed_count = 0
    errors = []
    
    for file_info in files_to_rename:
        old_path = file_info['path']
        new_path = old_path.parent / file_info['new_name']
        
        try:
            if new_path.exists() and new_path != old_path:
                errors.append(f"Cannot rename {file_info['relative_path']} → {file_info['new_name']}: target already exists")
            else:
                old_path.rename(new_path)
                renamed_count += 1
                if renamed_count <= 10 or renamed_count % 10 == 0:
                    print(f"  ✓ [{renamed_count}/{len(files_to_rename)}] {file_info['relative_path']} → {file_info['new_name']}")
        except Exception as e:
            errors.append(f"Error renaming {file_info['relative_path']}: {str(e)}")
    
    print("\n" + "=" * 50)
    print(f"✅ Successfully renamed {renamed_count} files")
    
    if errors:
        print(f"\n⚠️  {len(errors)} errors occurred:")
        for error in errors[:5]:
            print(f"  - {error}")
        if len(errors) > 5:
            print(f"  ... and {len(errors) - 5} more errors")

def update_language_references(course_dir):
    """Update image references in markdown files to use their corresponding language folders."""
    print("\n" + "=" * 60)
    print("Update Language References in Markdown Files")
    print("=" * 60)
    
    assets_dir = course_dir / 'assets'
    
    if not assets_dir.exists():
        print(f"No assets directory found in {course_dir.name}")
        return
    
    md_files = list(course_dir.glob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in {course_dir.name}")
        return
    
    print(f"\nFound {len(md_files)} markdown files")
    print("Checking for corresponding language folders in assets/...")
    print("-" * 50)
    
    files_to_update = []
    
    for md_file in sorted(md_files):
        lang_code = md_file.stem
        
        if lang_code == 'en':
            print(f"  ✓ Skipping {md_file.name} (reference language)")
            continue
        
        lang_assets_dir = assets_dir / lang_code
        
        if lang_assets_dir.exists() and lang_assets_dir.is_dir():
            webp_files = list(lang_assets_dir.glob('*.webp'))
            if webp_files:
                files_to_update.append({
                    'file': md_file,
                    'lang': lang_code,
                    'assets_dir': lang_assets_dir,
                    'webp_count': len(webp_files)
                })
                print(f"  ✓ {md_file.name} → assets/{lang_code}/ exists ({len(webp_files)} .webp files)")
            else:
                print(f"  ⚠ {md_file.name} → assets/{lang_code}/ exists but has no .webp files")
        else:
            print(f"  ✗ {md_file.name} → no assets/{lang_code}/ folder found")
    
    if not files_to_update:
        print("\nNo markdown files need updating.")
        return
    
    print(f"\n{len(files_to_update)} files will be updated:")
    for info in files_to_update:
        print(f"  • {info['file'].name}: /en/ → /{info['lang']}/")
    
    confirm = input(f"\nUpdate these {len(files_to_update)} files? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("Operation cancelled.")
        return
    
    print("\nUpdating files...")
    updated_count = 0
    
    for info in files_to_update:
        md_file = info['file']
        lang_code = info['lang']
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        en_refs = len(re.findall(r'assets/en/', content))
        
        if en_refs == 0:
            print(f"  ⚠ {md_file.name}: No /en/ references found")
            continue
        
        modified_content = content.replace('assets/en/', f'assets/{lang_code}/')
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        updated_count += 1
        print(f"  ✅ {md_file.name}: Replaced {en_refs} references (/en/ → /{lang_code}/)")
    
    print("\n" + "=" * 50)
    print(f"✅ Successfully updated {updated_count} files")
    
    if updated_count > 0:
        print("\nSample verification (first updated file):")
        sample_file = files_to_update[0]['file']
        sample_lang = files_to_update[0]['lang']
        
        with open(sample_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = rf'assets/{sample_lang}/\d+\.webp'
        matches = re.findall(pattern, content)[:3]
        
        if matches:
            print(f"  First references in {sample_file.name}:")
            for match in matches:
                print(f"    • {match}")

def main():
    """Main function with course selection and operation menu."""
    print("=" * 60)
    print("Course Image Reference and File Renaming Script")
    print("=" * 60)
    
    # Select course
    course_dir = select_course()
    
    if not course_dir:
        print("No course selected. Exiting.")
        return
    
    print(f"\n📚 Working with course: {course_dir.name}")
    print("=" * 60)
    
    while True:
        print("\nMain Menu:")
        print("1. Rename references in a SINGLE markdown file to sequential numbers")
        print("2. Rename references in ALL markdown files to sequential numbers")
        print("3. Rename ALL IMAGE FILES recursively (remove any prefix, keep only numbers)")
        print("4. Update language references (replace /en/ with appropriate language)")
        print("5. Change course")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            process_single_file(course_dir)
        elif choice == '2':
            confirm = input("\nThis will process ALL .md files. Continue? (y/n): ").strip().lower()
            if confirm == 'y':
                process_all_files(course_dir)
            else:
                print("Operation cancelled.")
        elif choice == '3':
            rename_image_files(course_dir)
        elif choice == '4':
            update_language_references(course_dir)
        elif choice == '5':
            course_dir = select_course()
            if not course_dir:
                print("No course selected. Returning to previous course.")
            else:
                print(f"\n📚 Now working with course: {course_dir.name}")
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    # Check for courses directory in various locations
    possible_paths = [
        Path('../../courses'),  # From scripts/rename_image
        Path('../courses'),     # From scripts
        Path('courses'),        # From root
    ]
    
    courses_found = False
    for path in possible_paths:
        if path.exists() and path.is_dir():
            courses_found = True
            break
    
    if not courses_found:
        print("Error: Could not find the courses directory.")
        print("This script should be run from the scripts/rename_image directory.")
        print("Current directory:", os.getcwd())
        sys.exit(1)
    
    main()