#!/usr/bin/env python3

import re
import glob

# Pattern to match image lines
image_pattern = re.compile(r'!\[image\]\(\./assets/fr/[^)]+\.webp\)')

# Process each .md file in the current directory
for filepath in glob.glob("*.md"):
    print(f"Processing: {filepath}")
    
    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Process line by line
    counter = 1
    new_lines = []
    
    for line in lines:
        # Replace all image occurrences in this line
        while image_pattern.search(line):
            new_path = f"![image](assets/fr/{counter:03d}.webp)"
            line = image_pattern.sub(new_path, line, count=1)
            counter += 1
        new_lines.append(line)
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"  ✓ Renumbered {counter-1} images")

print("All files processed!")