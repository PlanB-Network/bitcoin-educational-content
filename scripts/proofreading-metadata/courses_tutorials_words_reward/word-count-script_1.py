import os
from pathlib import Path
import pandas as pd

def find_project_root():
    """
    Find the project root by looking for 'bitcoin-educational-content' directory
    in parent directories.
    """
    current_dir = Path(__file__).resolve().parent
    while current_dir.name != 'bitcoin-educational-content' and current_dir != current_dir.parent:
        current_dir = current_dir.parent
    if current_dir.name != 'bitcoin-educational-content':
        raise FileNotFoundError("Could not find 'bitcoin-educational-content' directory in parent path")
    return current_dir

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return len(file.read().split())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def calculate_reward_multiplier(lines, start_idx):
    """
    Calculate reward multiplier based on number of contributors
    between contributors_id: and reward:
    """
    contributor_count = 0
    idx = start_idx + 1  # Start from next line after contributors_id
    
    while idx < len(lines) and not lines[idx].strip().startswith('reward:'):
        if lines[idx].strip().startswith('-'):
            contributor_count += 1
        idx += 1
    
    if contributor_count == 1:
        return 2
    elif contributor_count == 2:
        return 4
    return 1

def read_course_yaml(yaml_path):
    """
    Read the course.yml file and extract all language-reward pairs,
    applying multipliers based on contributor count.
    """
    try:
        with open(yaml_path, 'r', encoding='utf-8') as file:
            lines = [line.rstrip() for line in file.readlines()]
            language_rewards = {}
            current_language = None
            i = 0
            
            while i < len(lines):
                line = lines[i].strip()
                
                if line.startswith('- language:'):
                    current_language = line.split('- language:')[1].strip()
                elif line.startswith('contributors_id:'):
                    # Find reward multiplier based on contributors
                    multiplier = calculate_reward_multiplier(lines, i)
                    
                    # Find the reward value
                    reward_idx = i + 1
                    while reward_idx < len(lines):
                        if lines[reward_idx].strip().startswith('reward:'):
                            try:
                                base_reward = int(lines[reward_idx].split('reward:')[1].strip())
                                language_rewards[current_language] = base_reward * multiplier
                                print(f"Language: {current_language}, Base Reward: {base_reward}, "
                                      f"Multiplier: {multiplier}, Final Reward: {base_reward * multiplier}")
                            except ValueError:
                                print(f"Warning: Invalid reward value in {yaml_path} for language {current_language}")
                            break
                        reward_idx += 1
                i += 1
                        
            return language_rewards
    except Exception as e:
        print(f"Error reading YAML {yaml_path}: {e}")
        return {}

def process_courses(base_path):
    results = []
    languages = set()  # Set to store unique languages
    course_data = []  # List to store course data
    
    # First pass: collect all languages and course data
    for folder in base_path.iterdir():
        if folder.is_dir():
            yaml_file = folder / 'course.yml'
            md_file = folder / 'en.md'
            
            if yaml_file.exists():
                print(f"\nProcessing {yaml_file}")
                language_rewards = read_course_yaml(yaml_file)
                languages.update(language_rewards.keys())
                
                course_data.append({
                    'Folder': folder.name,
                    'Word Count': count_words_in_file(md_file) if md_file.exists() else 0,
                    'language_rewards': language_rewards
                })
    
    # Print all found languages for verification
    print("\nAll found languages:", sorted(languages))
    
    # Create the final data structure
    for course in course_data:
        row_data = {
            'Folder': course['Folder'],
            'Word Count': course['Word Count']
        }
        # Add the reward under the corresponding language column
        for lang in languages:
            row_data[lang] = course['language_rewards'].get(lang)
        
        results.append(row_data)
    
    return results

def process_tutorials(base_path):
    results = []
    # Only process level 2 directories (sub-sub-folders)
    for level1 in base_path.iterdir():
        if level1.is_dir():
            for level2 in level1.iterdir():
                if level2.is_dir():
                    md_file = level2 / 'en.md'
                    if md_file.exists():
                        results.append({
                            'Folder': level2.name,
                            'Word Count': count_words_in_file(md_file)
                        })
    return results

def main():
    try:
        # Find the project root directory
        project_root = find_project_root()
        
        # Define paths relative to the project root
        courses_path = project_root / 'courses'
        tutorials_path = project_root / 'tutorials'
        
        results = []
        results.extend(process_courses(courses_path))
        results.extend(process_tutorials(tutorials_path))
        
        # Save results in the same directory as the script
        output_path = Path(__file__).parent / 'word_counts.xlsx'
        df = pd.DataFrame(results)
        
        # Sort the columns to ensure Folder and Word Count are first, followed by alphabetically sorted languages
        columns = ['Folder', 'Word Count'] + sorted([col for col in df.columns if col not in ['Folder', 'Word Count']])
        df = df[columns]
        
        df.to_excel(output_path, index=False)
        print(f"\nResults saved to {output_path}")
        
    except FileNotFoundError as e:
        print("Error: Make sure this script is placed within the bitcoin-educational-content "
              "project directory structure.")
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
