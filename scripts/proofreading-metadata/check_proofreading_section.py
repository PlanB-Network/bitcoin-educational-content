import os
from proofreading import *


def check_files_for_original_language(root_dir):
    counter = 0

    # Walk through all directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude the 'docs' directory
        dirnames[:] = [d for d in dirnames if d != 'docs']
        
        for specific_file in specific_files:
            if specific_file in filenames:
                file_path = os.path.join(dirpath, specific_file)
                
                # Check if the file contains a line starting with 'original_language:'
                with open(file_path, 'r', encoding='utf-8') as file:
                    contains_original_language = any(line.startswith('original_language:') for line in file)
                
                if not contains_original_language:
                    counter += 1
                    print(f"File {specific_file} in {dirpath} does not contain 'original_language:'. Adding the section.")
                    
                    # Add the specified section to the end of the file
                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write('\n\n')
                        file.write('# Proofreading metadata\n')
                        file.write('original_language: fr\n')
                        file.write('proofreading:\n')
                        file.write('  - language: fr\n')
                        file.write('    last_contribution_date: 2024-08-31\n')
                        file.write('    urgency: 1\n')
                        file.write('    contributors_id:\n')
                        file.write('      - LoicPandul\n')
                        file.write('    reward:\n')
    
    print(f"Total files updated with 'original_language:' section: {counter}")
    return counter

# Replace '/path/to/your/root/directory' with the path to your root directory
root_dir = '../../'
check_files_for_original_language(root_dir)

