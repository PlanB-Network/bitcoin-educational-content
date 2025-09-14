#!/usr/bin/env python3
"""
Script to rename image references in markdown files and/or rename actual image files.
Can rename markdown references to sequential numbers and clean up image filenames.
"""

import os
import re
from pathlib import Path
import shutil

def find_all_image_references(content):
    """Find all .webp image references in the content, preserving order."""
    # Pattern to match any .webp image reference
    pattern = r'(\./)?assets/([a-zA-Z-]+)/(\d+)\.webp'
    matches = re.finditer(pattern, content)
    
    # Keep all references in order (including duplicates)
    all_refs = []
    for match in matches:
        all_refs.append({
            'start': match.start(),
            'end': match.end(),
            'full_match': match.group(0),
            'prefix': match.group(1) or '',  # ./ or empty
            'lang': match.group(2),  # language code
            'num': match.group(3)  # number
        })
    
    return all_refs

def rename_references_in_file(file_path):
    """Rename all image references in a single markdown file."""
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all image references (including duplicates)
    all_refs = find_all_image_references(content)
    
    if not all_refs:
        print(f"  No .webp images found in {file_path}")
        return 0
    
    # Show what was found
    languages_found = set(ref['lang'] for ref in all_refs)
    print(f"  Found {len(all_refs)} total .webp image references")
    print(f"  Original language codes: {', '.join(sorted(languages_found))}")
    
    # Determine digit format based on total count
    total_images = len(all_refs)
    if total_images < 100:
        digit_format = 2
    else:
        digit_format = 3
    
    # Build the new content by replacing from end to start (to preserve positions)
    modified_content = content
    
    # Process references in reverse order to maintain string positions
    for i, ref in enumerate(reversed(all_refs), 1):
        # Calculate the sequential number (counting from the end backwards)
        seq_num = total_images - i + 1
        new_num = str(seq_num).zfill(digit_format)
        
        # Create the new path
        new_path = f"{ref['prefix']}assets/en/{new_num}.webp"
        
        # Replace this specific occurrence
        modified_content = (
            modified_content[:ref['start']] + 
            new_path + 
            modified_content[ref['end']:]
        )
    
    # Write back the modified content
    if content != modified_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print(f"  ✅ Renamed {len(all_refs)} image references to assets/en/XX.webp ({digit_format} digits)")
        print(f"     Sequential numbering from 01 to {str(total_images).zfill(digit_format)}")
        
        # Show some examples of what was changed
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

def process_single_file(file_path):
    """Process a single markdown file."""
    md_file = Path(file_path)
    
    if not md_file.exists():
        print(f"Error: File '{file_path}' not found.")
        return
    
    if not md_file.suffix == '.md':
        print(f"Error: '{file_path}' is not a markdown file.")
        return
    
    print(f"\nProcessing {md_file.name}...")
    renamed_count = rename_references_in_file(md_file)
    
    print("\n" + "=" * 50)
    print(f"Complete! Processed {md_file.name}")
    if renamed_count > 0:
        print(f"All {renamed_count} image references now use sequential assets/en/ paths")

def process_all_files():
    """Process all markdown files in the current directory."""
    current_dir = Path('.')
    md_files = list(current_dir.glob('*.md'))
    
    if not md_files:
        print("No markdown files found in the current directory.")
        return
    
    print(f"Found {len(md_files)} markdown files to process")
    print("Will convert all .webp images to sequential assets/en/ paths")
    print("Each occurrence gets a new sequential number")
    print("-" * 50)
    
    total_renamed = 0
    files_modified = 0
    
    for md_file in sorted(md_files):
        print(f"\nProcessing {md_file.name}...")
        renamed_count = rename_references_in_file(md_file)
        if renamed_count > 0:
            total_renamed += renamed_count
            files_modified += 1
    
    print("\n" + "=" * 50)
    print(f"Complete! Processed {len(md_files)} files")
    print(f"Modified {files_modified} files with {total_renamed} total image references")

def scan_markdown_for_references(directory):
    """Scan markdown files to find which image numbers are actually referenced."""
    referenced_numbers = set()
    
    # Look for markdown files
    md_files = list(Path(directory).glob('*.md'))
    
    if md_files:
        print(f"\nScanning {len(md_files)} markdown files for image references...")
        
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all image number references
            pattern = r'assets/[a-zA-Z-]+/(\d+)\.webp'
            matches = re.finditer(pattern, content)
            
            for match in matches:
                referenced_numbers.add(match.group(1))
        
        if referenced_numbers:
            sorted_refs = sorted(referenced_numbers, key=lambda x: int(x))
            print(f"  Found references to {len(referenced_numbers)} unique image numbers")
            print(f"  Referenced numbers: {', '.join(sorted_refs[:10])}" + 
                  (' ...' if len(sorted_refs) > 10 else ''))
    
    return referenced_numbers

def find_image_files_to_rename(directory):
    """Find all .webp files that need renaming based on markdown references."""
    image_files = []
    
    # First, scan markdown files to see what numbers are referenced
    parent_dir = directory.parent if directory.name != '.' else directory
    referenced_numbers = scan_markdown_for_references(parent_dir)
    
    # Pattern to match any .webp file with numbers
    for file_path in Path(directory).glob('*.webp'):
        # Try different patterns to extract the number
        patterns = [
            r'^.*?(\d+)\.webp$',  # Any prefix followed by digits
            r'^(\d+)\.webp$',      # Just digits
        ]
        
        for pattern in patterns:
            match = re.match(pattern, file_path.name)
            if match:
                number = match.group(1)
                # Check if this is already in correct format
                if file_path.name == f"{number.zfill(2)}.webp" or file_path.name == f"{number.zfill(3)}.webp":
                    continue  # Already in correct format
                
                image_files.append({
                    'path': file_path,
                    'name': file_path.name,
                    'number': number,
                    'new_name': f"{number.zfill(2)}.webp",  # Use 2-digit format by default
                    'is_referenced': number in referenced_numbers or number.zfill(2) in referenced_numbers
                })
                break
    
    return sorted(image_files, key=lambda x: int(x['number']))

def rename_image_files():
    """Rename actual image files in the assets directory."""
    print("\n" + "=" * 60)
    print("Image File Renaming")
    print("=" * 60)
    
    # Ask for the directory path
    assets_path = input("\nEnter the path to the assets directory (e.g., assets/en or ./assets/en): ").strip()
    
    if not assets_path:
        print("No path provided. Cancelled.")
        return
    
    assets_dir = Path(assets_path)
    
    if not assets_dir.exists():
        print(f"Error: Directory '{assets_path}' not found.")
        return
    
    if not assets_dir.is_dir():
        print(f"Error: '{assets_path}' is not a directory.")
        return
    
    # Find all image files that need renaming
    files_to_rename = find_image_files_to_rename(assets_dir)
    
    if not files_to_rename:
        print(f"\nNo .webp files need renaming in {assets_path}")
        print("All files might already be in the correct format (e.g., 01.webp, 02.webp)")
        return
    
    print(f"\nFound {len(files_to_rename)} files to rename in {assets_path}:")
    print("-" * 40)
    
    # Separate referenced and unreferenced files
    referenced = [f for f in files_to_rename if f['is_referenced']]
    unreferenced = [f for f in files_to_rename if not f['is_referenced']]
    
    # Show what will be renamed
    if referenced:
        print("\nFiles referenced in markdown:")
        for file_info in referenced[:10]:  # Show first 10
            print(f"  {file_info['name']} → {file_info['new_name']}")
        if len(referenced) > 10:
            print(f"  ... and {len(referenced) - 10} more referenced files")
    
    if unreferenced:
        print(f"\n⚠️  Files NOT referenced in any markdown (might be unused):")
        for file_info in unreferenced[:5]:  # Show first 5
            print(f"  {file_info['name']}")
        if len(unreferenced) > 5:
            print(f"  ... and {len(unreferenced) - 5} more unreferenced files")
    
    # Confirm before renaming
    confirm = input(f"\nRename these {len(files_to_rename)} files? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("Operation cancelled.")
        return
    
    # Perform the renaming
    renamed_count = 0
    errors = []
    
    for file_info in files_to_rename:
        old_path = file_info['path']
        new_path = old_path.parent / file_info['new_name']
        
        try:
            # Check if target already exists
            if new_path.exists() and new_path != old_path:
                errors.append(f"Cannot rename {file_info['name']} → {file_info['new_name']}: target already exists")
            else:
                old_path.rename(new_path)
                renamed_count += 1
                print(f"  ✓ {file_info['name']} → {file_info['new_name']}")
        except Exception as e:
            errors.append(f"Error renaming {file_info['name']}: {str(e)}")
    
    # Report results
    print("\n" + "=" * 50)
    print(f"✅ Successfully renamed {renamed_count} files")
    
    if errors:
        print(f"\n⚠️  {len(errors)} errors occurred:")
        for error in errors[:5]:  # Show first 5 errors
            print(f"  - {error}")
        if len(errors) > 5:
            print(f"  ... and {len(errors) - 5} more errors")

def main():
    """Main function with user interaction."""
    print("=" * 60)
    print("Image Reference and File Renaming Script")
    print("=" * 60)
    print("\nThis script can:")
    print("1. Rename image references in markdown files")
    print("2. Rename actual image files in assets directories")
    print("\nMain Menu:")
    print("1. Rename references in a SINGLE markdown file")
    print("2. Rename references in ALL markdown files")
    print("3. Rename actual IMAGE FILES (remove prefixes, keep only numbers)")
    
    while True:
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            file_name = input("Enter the markdown filename (e.g., fr.md): ").strip()
            process_single_file(file_name)
            break
        elif choice == '2':
            confirm = input("\nThis will process ALL .md files. Continue? (y/n): ").strip().lower()
            if confirm == 'y':
                process_all_files()
            else:
                print("Operation cancelled.")
            break
        elif choice == '3':
            rename_image_files()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()