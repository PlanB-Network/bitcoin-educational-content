import os
import re
from pathlib import Path

def has_reviewed_field(content):
    """Check if the file already has a 'reviewed:' field."""
    # Check if 'reviewed:' appears in the content (case-insensitive)
    return re.search(r'^\s*reviewed\s*:', content, re.MULTILINE | re.IGNORECASE) is not None

def add_reviewed_field(file_path):
    """Add 'reviewed: false' to a YAML file if it's missing."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not has_reviewed_field(content):
            # Add 'reviewed: false' at the end
            # Remove trailing whitespace and add the field
            content = content.rstrip()
            if content and not content.endswith('\n'):
                content += '\n'
            content += 'reviewed: false\n'
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Find all .yml files in subfolders and add missing 'reviewed' field."""
    current_dir = Path('.')
    yml_files = list(current_dir.rglob('*.yml'))
    
    if not yml_files:
        print("No .yml files found in subfolders.")
        return
    
    print(f"Found {len(yml_files)} .yml file(s)")
    print("-" * 50)
    
    modified_count = 0
    for yml_file in yml_files:
        if yml_file.is_file():
            # Skip files named 'question.yml'
            if yml_file.name == 'question.yml':
                print(f"  Skipped (ignored file): {yml_file}")
                continue
            
            if add_reviewed_field(yml_file):
                print(f"✓ Added 'reviewed: false' to: {yml_file}")
                modified_count += 1
            else:
                print(f"  Skipped (already has 'reviewed:'): {yml_file}")
    
    print("-" * 50)
    print(f"\nSummary: Modified {modified_count} out of {len(yml_files)} file(s)")

if __name__ == "__main__":
    main()