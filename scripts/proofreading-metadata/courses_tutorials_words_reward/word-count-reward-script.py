import os
from pathlib import Path
import pandas as pd
import openpyxl
from openpyxl.styles import Font

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

def read_yaml_file(yaml_path):
    """
    Read the yaml file (course.yml or tutorial.yml) and extract all language-reward pairs,
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
                language_rewards = read_yaml_file(yaml_file)
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
    languages = set()  # Set to store unique languages
    tutorial_data = []  # List to store tutorial data
    
    # Process level 2 directories (sub-sub-folders)
    for level1 in base_path.iterdir():
        if level1.is_dir():
            for level2 in level1.iterdir():
                if level2.is_dir():
                    yaml_file = level2 / 'tutorial.yml'
                    md_file = level2 / 'en.md'
                    
                    if yaml_file.exists():
                        print(f"\nProcessing tutorial {yaml_file}")
                        language_rewards = read_yaml_file(yaml_file)
                        languages.update(language_rewards.keys())
                        
                        tutorial_data.append({
                            'Folder': level2.name,
                            'Word Count': count_words_in_file(md_file) if md_file.exists() else 0,
                            'language_rewards': language_rewards
                        })
    
    # Print all found languages in tutorials:", sorted(languages))
    
    # Create the final data structure
    for tutorial in tutorial_data:
        row_data = {
            'Folder': tutorial['Folder'],
            'Word Count': tutorial['Word Count']
        }
        # Add the reward under the corresponding language column
        for lang in languages:
            row_data[lang] = tutorial['language_rewards'].get(lang)
        
        results.append(row_data)
    
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
        
        # Rename 'Word Count' to 'Word Count EN'
        df = df.rename(columns={'Word Count': 'Word Count EN'})
        
        # Sort the columns to ensure Folder and Word Count EN are first, followed by alphabetically sorted languages
        columns = ['Folder', 'Word Count EN'] + sorted([col for col in df.columns if col not in ['Folder', 'Word Count EN']])
        df = df[columns]
        
        # Calculate totals for proofreading
        first_proofreading = {}
        first_proofreading['Folder'] = 'Total for first proofreading'
        first_proofreading['Word Count EN'] = None
        for col in columns[2:]:  # Skip Folder and Word Count EN
            first_proofreading[col] = df[col].sum()
        
        # Add empty row
        empty_row = {col: None for col in columns}
        
        # Calculate second proofreading
        second_proofreading = {}
        second_proofreading['Folder'] = 'Total for second proofreading'
        second_proofreading['Word Count EN'] = None
        for col in columns[2:]:
            second_proofreading[col] = first_proofreading[col] / 2
        
        # Calculate third proofreading
        third_proofreading = {}
        third_proofreading['Folder'] = 'Total for third proofreading'
        third_proofreading['Word Count EN'] = None
        for col in columns[2:]:
            third_proofreading[col] = second_proofreading[col] / 2
        
        # Calculate total for all proofreading
        total_all = {}
        total_all['Folder'] = 'Total for all the proofreading'
        total_all['Word Count EN'] = None
        for col in columns[2:]:
            total_all[col] = first_proofreading[col] + second_proofreading[col] + third_proofreading[col]
        
        # Append all new rows to the DataFrame
        df = pd.concat([df, 
                       pd.DataFrame([first_proofreading]),
                       pd.DataFrame([empty_row]),
                       pd.DataFrame([second_proofreading]),
                       pd.DataFrame([empty_row]),
                       pd.DataFrame([third_proofreading]),
                       pd.DataFrame([empty_row]),
                       pd.DataFrame([total_all])], 
                      ignore_index=True)
        
        # Create Excel file with formatting
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Write the DataFrame to Excel
            df.to_excel(writer, index=False)
            
            # Get the worksheet
            worksheet = writer.sheets['Sheet1']
            
            # Find the row index of "Total for all the proofreading"
            total_row = None
            for idx, row in enumerate(worksheet.iter_rows(min_row=1, max_row=worksheet.max_row), 1):
                if row[0].value == 'Total for all the proofreading':
                    total_row = idx
                    break
            
            # Apply bold formatting to the entire row
            if total_row:
                for cell in worksheet[total_row]:
                    cell.font = Font(bold=True)

        print(f"\nResults saved to {output_path}")
        
    except FileNotFoundError as e:
        print("Error: Make sure this script is placed within the bitcoin-educational-content "
              "project directory structure.")
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
