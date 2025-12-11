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
        content = f.read()
    
    # Counter for sequential numbering
    counter = 1
    
    # Keep replacing until no more matches
    while image_pattern.search(content):
        new_path = f"![image](assets/fr/{counter:03d}.webp)"
        content = image_pattern.sub(new_path, content, count=1)
        counter += 1
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Renumbered {counter-1} images")

print("All files processed!")