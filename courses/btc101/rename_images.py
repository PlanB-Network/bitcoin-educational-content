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

def find_all_webp_files_recursive(directory):
    """Find all .webp files recursively in directory and subdirectories."""
    image_files = []
    
    # Use rglob for recursive search
    for file_path in Path(directory).rglob('*.webp'):
        # Extract just the filename
        filename = file_path.name
        
        # Try to find a number in the filename
        # Look for patterns like: anything_01.webp, 01_anything.webp, anything01.webp, etc.
        matches = re.findall(r'\d+', filename)
        
        if matches:
            # Take the last number found (usually the most relevant)
            # For example: BTC101_images_de_slide_01.webp -> 01
            number = matches[-1]
            
            # Check if already in correct format
            if filename == f"{number.zfill(2)}.webp" or filename == f"{number.zfill(3)}.webp" or filename == f"{number}.webp":
                continue  # Already in correct format
            
            # Determine the appropriate zero-padding
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

def rename_image_files():
    """Rename actual image files in the assets directory and all subdirectories."""
    print("\n" + "=" * 60)
    print("Image File Renaming (Recursive)")
    print("=" * 60)
    
    # Ask for the directory path
    assets_path = input("\nEnter the path to the assets directory (e.g., assets or ./assets): ").strip()
    
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
    
    print(f"\nScanning {assets_path} and all subdirectories for .webp files...")
    
    # Find all image files that need renaming
    files_to_rename = find_all_webp_files_recursive(assets_dir)
    
    if not files_to_rename:
        print(f"\nNo .webp files need renaming in {assets_path}")
        print("All files might already be in the correct format (e.g., 01.webp, 02.webp)")
        return
    
    # Group files by directory
    files_by_dir = {}
    for file_info in files_to_rename:
        dir_key = str(file_info['directory'])
        if dir_key not in files_by_dir:
            files_by_dir[dir_key] = []
        files_by_dir[dir_key].append(file_info)
    
    print(f"\nFound {len(files_to_rename)} files to rename across {len(files_by_dir)} directories:")
    print("-" * 60)
    
    # Show summary by directory
    for dir_path, files in sorted(files_by_dir.items())[:10]:  # Show first 10 directories
        try:
            rel_dir = Path(dir_path).relative_to(Path.cwd())
        except ValueError:
            # If not relative to cwd, try relative to the assets directory
            try:
                rel_dir = Path(dir_path).relative_to(assets_dir.parent)
            except ValueError:
                # If still not relative, just use the last parts of the path
                rel_dir = Path(*Path(dir_path).parts[-2:])
        print(f"\n📁 {rel_dir}/ ({len(files)} files)")
        for file_info in files[:3]:  # Show first 3 files per directory
            print(f"    {file_info['name']} → {file_info['new_name']}")
        if len(files) > 3:
            print(f"    ... and {len(files) - 3} more files")
    
    if len(files_by_dir) > 10:
        print(f"\n... and {len(files_by_dir) - 10} more directories")
    
    print("\n" + "-" * 60)
    print(f"Total: {len(files_to_rename)} files across {len(files_by_dir)} directories")
    
    # Confirm before renaming
    confirm = input(f"\nRename all these files? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("Operation cancelled.")
        return
    
    # Perform the renaming
    print("\nRenaming files...")
    renamed_count = 0
    errors = []
    
    for file_info in files_to_rename:
        old_path = file_info['path']
        new_path = old_path.parent / file_info['new_name']
        
        try:
            # Check if target already exists
            if new_path.exists() and new_path != old_path:
                errors.append(f"Cannot rename {file_info['relative_path']} → {file_info['new_name']}: target already exists")
            else:
                old_path.rename(new_path)
                renamed_count += 1
                # Show progress for first few and then periodically
                if renamed_count <= 10 or renamed_count % 10 == 0:
                    print(f"  ✓ [{renamed_count}/{len(files_to_rename)}] {file_info['relative_path']} → {file_info['new_name']}")
        except Exception as e:
            errors.append(f"Error renaming {file_info['relative_path']}: {str(e)}")
    
    # Report results
    print("\n" + "=" * 50)
    print(f"✅ Successfully renamed {renamed_count} files")
    
    if errors:
        print(f"\n⚠️  {len(errors)} errors occurred:")
        for error in errors[:5]:  # Show first 5 errors
            print(f"  - {error}")
        if len(errors) > 5:
            print(f"  ... and {len(errors) - 5} more errors")
    
    # Show summary by directory
    print(f"\n📊 Summary by directory:")
    for dir_path, files in sorted(files_by_dir.items())[:5]:
        try:
            rel_dir = Path(dir_path).relative_to(Path.cwd())
        except ValueError:
            # If not relative to cwd, try relative to the assets directory
            try:
                rel_dir = Path(dir_path).relative_to(assets_dir.parent)
            except ValueError:
                # If still not relative, just use the last parts of the path
                rel_dir = Path(*Path(dir_path).parts[-2:])
        success_count = sum(1 for f in files if not any(str(f['relative_path']) in e for e in errors))
        print(f"  {rel_dir}/: {success_count}/{len(files)} files renamed")

def update_language_references():
    """Update image references in markdown files to use their corresponding language folders."""
    print("\n" + "=" * 60)
    print("Update Language References in Markdown Files")
    print("=" * 60)
    
    current_dir = Path('.')
    assets_dir = Path('assets')
    
    if not assets_dir.exists():
        print("Error: 'assets' directory not found in current directory.")
        return
    
    # Find all markdown files
    md_files = list(current_dir.glob('*.md'))
    
    if not md_files:
        print("No markdown files found in the current directory.")
        return
    
    print(f"\nFound {len(md_files)} markdown files")
    print("Checking for corresponding language folders in assets/...")
    print("-" * 50)
    
    files_to_update = []
    
    for md_file in sorted(md_files):
        # Get language code from filename (e.g., de.md -> de)
        lang_code = md_file.stem
        
        # Skip en.md as it's the reference
        if lang_code == 'en':
            print(f"  ✓ Skipping {md_file.name} (reference language)")
            continue
        
        # Check if corresponding folder exists in assets
        lang_assets_dir = assets_dir / lang_code
        
        if lang_assets_dir.exists() and lang_assets_dir.is_dir():
            # Check if there are any .webp files in that directory
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
    
    # Confirm before updating
    confirm = input(f"\nUpdate these {len(files_to_update)} files? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("Operation cancelled.")
        return
    
    # Perform the updates
    print("\nUpdating files...")
    updated_count = 0
    
    for info in files_to_update:
        md_file = info['file']
        lang_code = info['lang']
        
        # Read the file
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count existing /en/ references
        en_refs = len(re.findall(r'assets/en/', content))
        
        if en_refs == 0:
            print(f"  ⚠ {md_file.name}: No /en/ references found")
            continue
        
        # Replace /en/ with /{lang}/
        modified_content = content.replace('assets/en/', f'assets/{lang_code}/')
        
        # Write back the modified content
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        updated_count += 1
        print(f"  ✅ {md_file.name}: Replaced {en_refs} references (/en/ → /{lang_code}/)")
    
    # Report results
    print("\n" + "=" * 50)
    print(f"✅ Successfully updated {updated_count} files")
    
    # Show a sample to verify
    if updated_count > 0:
        print("\nSample verification (first updated file):")
        sample_file = files_to_update[0]['file']
        sample_lang = files_to_update[0]['lang']
        
        with open(sample_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find first few image references
        pattern = rf'assets/{sample_lang}/\d+\.webp'
        matches = re.findall(pattern, content)[:3]
        
        if matches:
            print(f"  First references in {sample_file.name}:")
            for match in matches:
                print(f"    • {match}")

def main():
    """Main function with user interaction."""
    print("=" * 60)
    print("Image Reference and File Renaming Script")
    print("=" * 60)
    print("\nThis script can:")
    print("1. Rename image references in markdown files")
    print("2. Rename actual image files in assets directories")
    print("3. Update language-specific image references")
    print("\nMain Menu:")
    print("1. Rename references in a SINGLE markdown file to sequential numbers")
    print("2. Rename references in ALL markdown files to sequential numbers")
    print("3. Rename ALL IMAGE FILES recursively (remove any prefix, keep only numbers)")
    print("4. Update language references (replace /en/ with appropriate language)")
    print("   Example: de.md will use assets/de/ instead of assets/en/")
    
    while True:
        choice = input("\nEnter your choice (1, 2, 3, or 4): ").strip()
        
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
        elif choice == '4':
            update_language_references()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()