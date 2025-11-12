import os
import yaml
from datetime import datetime
from pathlib import Path
import re

def add_contributor_to_yaml(file_path, language, contributor_name):
    """Add a contributor name to a YAML file while preserving original formatting and structure."""
    try:
        # Read the original file content as text
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()

        # Parse the YAML content
        data = yaml.safe_load(original_content)

        # Get current date in YYYY-MM-DD format
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Find the element for the specified language
        language_found = False
        updated = False
        
        # Normalize language for comparison (strip whitespace, handle case)
        target_language = language.strip()
        
        for item in data.get('proofreading', []):
            item_language = item.get('language', '').strip()
            
            # Case-insensitive comparison for language matching
            if item_language.lower() == target_language.lower():
                language_found = True
                
                # Initialize contributor_names if it doesn't exist or is null
                if 'contributor_names' not in item or item['contributor_names'] is None:
                    item['contributor_names'] = []

                # Add contributor name if not already present (case-insensitive check)
                existing_contributors = [name.strip() for name in item['contributor_names']]
                if contributor_name not in existing_contributors:
                    item['contributor_names'].append(contributor_name)
                    updated = True
                else:
                    print(f"  ℹ {contributor_name} already exists in {item_language} contributors")

                # Update last contribution date
                item['last_contribution_date'] = current_date
                break

        if not language_found:
            print(f"  ⚠ Language '{target_language}' not found in proofreading section")
            # Debug: Show all available languages
            available_languages = [item.get('language', 'N/A') for item in data.get('proofreading', [])]
            print(f"  📋 Available languages: {available_languages}")
            return False

        if not updated:
            return True  # No changes needed, but operation was successful

        # Now we need to update the file while preserving the original structure
        # We'll use string manipulation to only update the proofreading section
        lines = original_content.split('\n')
        
        # Find the proofreading section
        proofreading_start = -1
        proofreading_indent = ""
        
        for i, line in enumerate(lines):
            if line.strip() == 'proofreading:' or line.strip().startswith('proofreading:'):
                proofreading_start = i
                # Determine indentation level
                proofreading_indent = line[:len(line) - len(line.lstrip())]
                break
        
        if proofreading_start == -1:
            print(f"  ❌ Could not find proofreading section in {file_path}")
            return False

        # Find where proofreading section ends
        proofreading_end = len(lines)
        base_indent_len = len(proofreading_indent)
        
        for i in range(proofreading_start + 1, len(lines)):
            line = lines[i]
            if line.strip() == '':
                continue
            
            # Check if this line is at the same level or less indented than "proofreading:"
            current_indent_len = len(line) - len(line.lstrip())
            if current_indent_len <= base_indent_len and line.strip() and not line.lstrip().startswith('-') and not line.lstrip().startswith(' '):
                proofreading_end = i
                break

        # Generate new proofreading section
        new_proofreading_lines = [f"{proofreading_indent}proofreading:"]
        
        for item in data.get('proofreading', []):
            new_proofreading_lines.append(f"{proofreading_indent}  - language: {item['language']}")
            
            # Handle last_contribution_date
            if item.get('last_contribution_date'):
                date_value = item['last_contribution_date']
                if isinstance(date_value, str) and ('-' in date_value or date_value.startswith('2025')):
                    new_proofreading_lines.append(f"{proofreading_indent}    last_contribution_date: '{date_value}'")
                else:
                    new_proofreading_lines.append(f"{proofreading_indent}    last_contribution_date: {date_value}")
            else:
                new_proofreading_lines.append(f"{proofreading_indent}    last_contribution_date:")
            
            new_proofreading_lines.append(f"{proofreading_indent}    urgency: {item.get('urgency', 1)}")
            
            # Handle contributor_names
            if item.get('contributor_names') and len(item['contributor_names']) > 0:
                new_proofreading_lines.append(f"{proofreading_indent}    contributor_names:")
                for name in item['contributor_names']:
                    new_proofreading_lines.append(f"{proofreading_indent}      - {name}")
            else:
                new_proofreading_lines.append(f"{proofreading_indent}    contributor_names:")
            
            new_proofreading_lines.append(f"{proofreading_indent}    reward: {item.get('reward', 0)}")

        # Reconstruct the file content
        new_content = (
            '\n'.join(lines[:proofreading_start]) + '\n' +
            '\n'.join(new_proofreading_lines) + '\n' +
            '\n'.join(lines[proofreading_end:])
        ).strip() + '\n'

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
            
        print(f"  ✅ File successfully written")
        return True
        
    except FileNotFoundError:
        print(f"  ❌ File not found: {file_path}")
        return False
    except yaml.YAMLError as e:
        print(f"  ❌ YAML parsing error in {file_path}: {str(e)}")
        return False
    except Exception as e:
        print(f"  ❌ Error modifying file {file_path}: {str(e)}")
        return False

def process_subfolders(folder_path, language, contributor_name, selected_subfolders=None):
    """Process selected subfolders and add contributor name to YAML files."""
    folder_path = Path(folder_path)
    
    # Get all subfolders
    try:
        subfolders = [f.name for f in folder_path.iterdir() if f.is_dir()]
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error accessing folder {folder_path}: {str(e)}")
        return

    if not subfolders:
        print("No subfolders found in the selected folder.")
        return

    # Sort subfolders alphabetically for consistent processing
    subfolders.sort()

    # Determine which subfolders to process
    if selected_subfolders is None:
        # Show list of subfolders for interactive selection
        print(f"\nSubfolders in '{folder_path.name}':")
        for i, subfolder in enumerate(subfolders):
            print(f"{i + 1:2d}. {subfolder}")

        # Input for subfolders to modify
        try:
            selection = input("\nEnter subfolder numbers to modify (comma-separated, or 'all' for all): ").strip()
            
            if selection.lower() == 'all':
                folders_to_process = subfolders
            else:
                selected_indices = [int(num.strip()) for num in selection.split(',')]
                folders_to_process = [subfolders[i - 1] for i in selected_indices if 1 <= i <= len(subfolders)]
                
                if not folders_to_process:
                    print("No valid selections made.")
                    return
                    
        except (ValueError, IndexError):
            print("Invalid input. Processing all subfolders.")
            folders_to_process = subfolders
    else:
        # Use provided subfolder list, filtering to only existing ones
        folders_to_process = [sf for sf in selected_subfolders if sf in subfolders]
        if not folders_to_process:
            print("None of the specified subfolders were found.")
            return

    print(f"\nProcessing {len(folders_to_process)} subfolder(s)...")
    
    # Process each selected subfolder
    success_count = 0
    for subfolder in folders_to_process:
        subfolder_path = folder_path / subfolder
        yaml_file = subfolder_path / 'tutorial.yml'
        
        print(f"\nProcessing: {subfolder}")
        if yaml_file.exists():
            if add_contributor_to_yaml(yaml_file, language, contributor_name):
                success_count += 1
        else:
            print(f"  ⚠ tutorial.yml not found in {subfolder}")

    print(f"\n✅ Successfully processed {success_count} out of {len(folders_to_process)} subfolders.")

def get_subfolders(folder_path):
    """Return a list of subfolders within a specified folder."""
    folder_path = Path(folder_path)
    
    if not folder_path.exists():
        return []

    try:
        return [f.name for f in folder_path.iterdir() if f.is_dir()]
    except PermissionError:
        print(f"Permission denied accessing {folder_path}")
        return []

def validate_inputs(contributor_name, language):
    """Validate user inputs."""
    if not contributor_name.strip():
        print("Error: Contributor name cannot be empty.")
        return False
        
    if not language.strip():
        print("Error: Language cannot be empty.")
        return False
        
    # Updated validation for language code to handle complex codes like zh-Hans, sr-Latn, nb-NO
    # Allow 2-10 characters, letters, hyphens, and allow uppercase letters for script codes
    if not re.match(r'^[a-zA-Z]{2,3}(-[a-zA-Z]{2,4})*$', language) or len(language) < 2 or len(language) > 10:
        print("Warning: Language should be a valid language code (e.g., 'en', 'fr', 'es', 'pt-br', 'zh-Hans', 'sr-Latn')")
        proceed = input("Continue anyway? (y/n): ").lower().startswith('y')
        if not proceed:
            return False
            
    return True

def process_alphabetical_range(main_folder_path, language, contributor_name):
    """Process subfolders in alphabetical range from start to end folder."""
    all_subfolders = get_subfolders(main_folder_path)
    if not all_subfolders:
        print("No subfolders found in the selected folder.")
        return
    
    all_subfolders.sort()
    
    print(f"\nAvailable subfolders in '{main_folder_path.name}':")
    for i, subfolder in enumerate(all_subfolders):
        print(f"{i + 1:2d}. {subfolder}")
    
    try:
        start_choice = int(input(f"\nSelect starting subfolder (1-{len(all_subfolders)}): "))
        end_choice = int(input(f"Select ending subfolder (1-{len(all_subfolders)}): "))
        
        if not (1 <= start_choice <= len(all_subfolders)) or not (1 <= end_choice <= len(all_subfolders)):
            print("Invalid selection.")
            return
        
        if start_choice > end_choice:
            print("Starting subfolder must come before or be the same as ending subfolder in alphabetical order.")
            return
        
        selected_subfolders = all_subfolders[start_choice-1:end_choice]
        print(f"\nSelected range: {selected_subfolders[0]} to {selected_subfolders[-1]}")
        print(f"This will process {len(selected_subfolders)} subfolder(s).")
        
        confirm = input("Continue? (y/n): ").lower().startswith('y')
        if confirm:
            process_subfolders(main_folder_path, language, contributor_name, selected_subfolders)
        else:
            print("Operation cancelled.")
            
    except ValueError:
        print("Invalid input. Please enter numbers.")

def process_glossary_subfolders(folder_path, language, contributor_name, selected_subfolders=None):
    """Process selected glossary subfolders and add contributor name to word.yml files."""
    folder_path = Path(folder_path)
    
    # Get all subfolders
    try:
        subfolders = [f.name for f in folder_path.iterdir() if f.is_dir()]
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error accessing folder {folder_path}: {str(e)}")
        return

    if not subfolders:
        print("No subfolders found in the selected folder.")
        return

    # Sort subfolders alphabetically for consistent processing
    subfolders.sort()

    # Determine which subfolders to process
    if selected_subfolders is None:
        # Show list of subfolders for interactive selection
        print(f"\nSubfolders in '{folder_path.name}':")
        for i, subfolder in enumerate(subfolders):
            print(f"{i + 1:2d}. {subfolder}")

        # Input for subfolders to modify
        try:
            selection = input("\nEnter subfolder numbers to modify (comma-separated, or 'all' for all): ").strip()
            
            if selection.lower() == 'all':
                folders_to_process = subfolders
            else:
                selected_indices = [int(num.strip()) for num in selection.split(',')]
                folders_to_process = [subfolders[i - 1] for i in selected_indices if 1 <= i <= len(subfolders)]
                
                if not folders_to_process:
                    print("No valid selections made.")
                    return
                    
        except (ValueError, IndexError):
            print("Invalid input. Processing all subfolders.")
            folders_to_process = subfolders
    else:
        # Use provided subfolder list, filtering to only existing ones
        folders_to_process = [sf for sf in selected_subfolders if sf in subfolders]
        if not folders_to_process:
            print("None of the specified subfolders were found.")
            return

    print(f"\nProcessing {len(folders_to_process)} subfolder(s)...")
    
    # Process each selected subfolder
    success_count = 0
    for subfolder in folders_to_process:
        subfolder_path = folder_path / subfolder
        yaml_file = subfolder_path / 'word.yml'  # Different filename for glossary
        
        print(f"\nProcessing: {subfolder}")
        if yaml_file.exists():
            if add_contributor_to_yaml(yaml_file, language, contributor_name):
                success_count += 1
        else:
            print(f"  ⚠ word.yml not found in {subfolder}")

    print(f"\n✅ Successfully processed {success_count} out of {len(folders_to_process)} subfolders.")

def process_alphabetical_range_glossary(main_folder_path, language, contributor_name):
    """Process glossary subfolders in alphabetical range from start to end folder."""
    all_subfolders = get_subfolders(main_folder_path)
    if not all_subfolders:
        print("No subfolders found in the selected folder.")
        return
    
    all_subfolders.sort()
    
    print(f"\nAvailable subfolders in '{main_folder_path.name}':")
    for i, subfolder in enumerate(all_subfolders):
        print(f"{i + 1:2d}. {subfolder}")
    
    try:
        start_choice = int(input(f"\nSelect starting subfolder (1-{len(all_subfolders)}): "))
        end_choice = int(input(f"Select ending subfolder (1-{len(all_subfolders)}): "))
        
        if not (1 <= start_choice <= len(all_subfolders)) or not (1 <= end_choice <= len(all_subfolders)):
            print("Invalid selection.")
            return
        
        if start_choice > end_choice:
            print("Starting subfolder must come before or be the same as ending subfolder in alphabetical order.")
            return
        
        selected_subfolders = all_subfolders[start_choice-1:end_choice]
        print(f"\nSelected range: {selected_subfolders[0]} to {selected_subfolders[-1]}")
        print(f"This will process {len(selected_subfolders)} subfolder(s).")
        
        confirm = input("Continue? (y/n): ").lower().startswith('y')
        if confirm:
            process_glossary_subfolders(main_folder_path, language, contributor_name, selected_subfolders)
        else:
            print("Operation cancelled.")
            
    except ValueError:
        print("Invalid input. Please enter numbers.")

def process_quiz_subfolders(course_path, language, contributor_name, selected_subfolders=None):
    """Process selected quiz subfolders and add contributor name to question.yml files."""
    quiz_path = course_path / 'quizz'
    
    if not quiz_path.exists():
        print(f"  ⚠ No 'quizz' folder found in {course_path.name}")
        return

    # Get all quiz subfolders
    try:
        subfolders = [f.name for f in quiz_path.iterdir() if f.is_dir()]
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error accessing folder {quiz_path}: {str(e)}")
        return

    if not subfolders:
        print("No quiz subfolders found.")
        return

    # Sort subfolders numerically for proper quiz order
    def sort_key(x):
        try:
            return int(x)
        except ValueError:
            return float('inf')  # Put non-numeric folders at the end
    
    subfolders.sort(key=sort_key)

    # Determine which subfolders to process
    if selected_subfolders is None:
        # Show list of subfolders for interactive selection
        print(f"\nQuiz subfolders in '{course_path.name}/quizz':")
        for i, subfolder in enumerate(subfolders):
            print(f"{i + 1:2d}. {subfolder}")

        # Input for subfolders to modify
        try:
            selection = input("\nEnter quiz numbers to modify (comma-separated, or 'all' for all): ").strip()
            
            if selection.lower() == 'all':
                folders_to_process = subfolders
            else:
                selected_indices = [int(num.strip()) for num in selection.split(',')]
                folders_to_process = [subfolders[i - 1] for i in selected_indices if 1 <= i <= len(subfolders)]
                
                if not folders_to_process:
                    print("No valid selections made.")
                    return
                    
        except (ValueError, IndexError):
            print("Invalid input. Processing all subfolders.")
            folders_to_process = subfolders
    else:
        # Use provided subfolder list, filtering to only existing ones
        folders_to_process = [sf for sf in selected_subfolders if sf in subfolders]
        if not folders_to_process:
            print("None of the specified quiz subfolders were found.")
            return

    print(f"\nProcessing {len(folders_to_process)} quiz subfolder(s)...")
    
    # Process each selected subfolder
    success_count = 0
    for subfolder in folders_to_process:
        subfolder_path = quiz_path / subfolder
        yaml_file = subfolder_path / 'question.yml'
        
        print(f"\nProcessing quiz: {subfolder}")
        if yaml_file.exists():
            if add_contributor_to_yaml(yaml_file, language, contributor_name):
                success_count += 1
        else:
            print(f"  ⚠ question.yml not found in quiz {subfolder}")

    print(f"\n✅ Successfully processed {success_count} out of {len(folders_to_process)} quiz subfolders.")

def process_course_folders(content_path, language, contributor_name, selected_courses=None):
    """Process selected course folders and add contributor name to course.yml files."""
    
    # Get all course folders
    try:
        course_folders = [f.name for f in content_path.iterdir() if f.is_dir()]
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error accessing folder {content_path}: {str(e)}")
        return

    if not course_folders:
        print("No course folders found.")
        return

    # Sort course folders alphabetically for consistent processing
    course_folders.sort()

    # Determine which courses to process
    if selected_courses is None:
        # Show list of courses for interactive selection
        print(f"\nCourse folders in '{content_path.name}':")
        for i, course in enumerate(course_folders):
            print(f"{i + 1:2d}. {course}")

        # Input for courses to modify
        try:
            selection = input("\nEnter course numbers to modify (comma-separated, or 'all' for all): ").strip()
            
            if selection.lower() == 'all':
                courses_to_process = course_folders
            else:
                selected_indices = [int(num.strip()) for num in selection.split(',')]
                courses_to_process = [course_folders[i - 1] for i in selected_indices if 1 <= i <= len(course_folders)]
                
                if not courses_to_process:
                    print("No valid selections made.")
                    return
                    
        except (ValueError, IndexError):
            print("Invalid input. Processing all courses.")
            courses_to_process = course_folders
    else:
        # Use provided course list, filtering to only existing ones
        courses_to_process = [cf for cf in selected_courses if cf in course_folders]
        if not courses_to_process:
            print("None of the specified courses were found.")
            return

    print(f"\nProcessing {len(courses_to_process)} course(s)...")
    
    # Process each selected course
    success_count = 0
    for course in courses_to_process:
        course_path = content_path / course
        yaml_file = course_path / 'course.yml'
        
        print(f"\nProcessing course: {course}")
        if yaml_file.exists():
            if add_contributor_to_yaml(yaml_file, language, contributor_name):
                success_count += 1
        else:
            print(f"  ⚠ course.yml not found in {course}")

    print(f"\n✅ Successfully processed {success_count} out of {len(courses_to_process)} courses.")

def process_alphabetical_range_course(content_path, language, contributor_name):
    """Process course folders in alphabetical range from start to end."""
    try:
        all_courses = [f.name for f in content_path.iterdir() if f.is_dir()]
    except PermissionError:
        print(f"Permission denied accessing {content_path}")
        return
    
    if not all_courses:
        print("No course folders found.")
        return
    
    all_courses.sort()
    
    print(f"\nAvailable courses in '{content_path.name}':")
    for i, course in enumerate(all_courses):
        print(f"{i + 1:2d}. {course}")
    
    try:
        start_choice = int(input(f"\nSelect starting course (1-{len(all_courses)}): "))
        end_choice = int(input(f"Select ending course (1-{len(all_courses)}): "))
        
        if not (1 <= start_choice <= len(all_courses)) or not (1 <= end_choice <= len(all_courses)):
            print("Invalid selection.")
            return
        
        if start_choice > end_choice:
            print("Starting course must come before or be the same as ending course in alphabetical order.")
            return
        
        selected_courses = all_courses[start_choice-1:end_choice]
        print(f"\nSelected range: {selected_courses[0]} to {selected_courses[-1]}")
        print(f"This will process {len(selected_courses)} course(s).")
        
        confirm = input("Continue? (y/n): ").lower().startswith('y')
        if confirm:
            process_course_folders(content_path, language, contributor_name, selected_courses)
        else:
            print("Operation cancelled.")
            
    except ValueError:
        print("Invalid input. Please enter numbers.")

def process_alphabetical_range_quiz(course_path, language, contributor_name):
    """Process quiz subfolders in numerical range from start to end."""
    quiz_path = course_path / 'quizz'
    
    if not quiz_path.exists():
        print(f"  ⚠ No 'quizz' folder found in {course_path.name}")
        return

    try:
        all_subfolders = [f.name for f in quiz_path.iterdir() if f.is_dir()]
    except PermissionError:
        print(f"Permission denied accessing {quiz_path}")
        return
    
    if not all_subfolders:
        print("No quiz subfolders found.")
        return
    
    # Sort numerically
    def sort_key(x):
        try:
            return int(x)
        except ValueError:
            return float('inf')
    
    all_subfolders.sort(key=sort_key)
    
    print(f"\nAvailable quiz subfolders in '{course_path.name}/quizz':")
    for i, subfolder in enumerate(all_subfolders):
        print(f"{i + 1:2d}. {subfolder}")
    
    try:
        start_choice = int(input(f"\nSelect starting quiz (1-{len(all_subfolders)}): "))
        end_choice = int(input(f"Select ending quiz (1-{len(all_subfolders)}): "))
        
        if not (1 <= start_choice <= len(all_subfolders)) or not (1 <= end_choice <= len(all_subfolders)):
            print("Invalid selection.")
            return
        
        if start_choice > end_choice:
            print("Starting quiz must come before or be the same as ending quiz in numerical order.")
            return
        
        selected_subfolders = all_subfolders[start_choice-1:end_choice]
        print(f"\nSelected range: {selected_subfolders[0]} to {selected_subfolders[-1]}")
        print(f"This will process {len(selected_subfolders)} quiz subfolder(s).")
        
        confirm = input("Continue? (y/n): ").lower().startswith('y')
        if confirm:
            process_quiz_subfolders(course_path, language, contributor_name, selected_subfolders)
        else:
            print("Operation cancelled.")
            
    except ValueError:
        print("Invalid input. Please enter numbers.")

def main():
    print("=== Contributor Management Script ===\n")
    
    while True:  # Loop to allow adding multiple contributors
        # Content type selection
        print("Content type options:")
        print("1. Tutorials")
        print("2. Glossary")
        print("3. Quizzes")
        print("4. Courses")
        
        try:
            content_choice = int(input("Select content type to update (1-4): "))
            if content_choice not in [1, 2, 3, 4]:
                print("Invalid selection.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # User input
        contributor_name = input("Enter the proofreader name to add: ").strip()
        language = input("Enter the language code (e.g., en, fr, es, pt-br, zh-Hans, sr-Latn): ").strip()
        
        # Don't convert language to lowercase automatically - preserve original case
        # This is important for script codes like "Hans" in "zh-Hans"
        
        # Validate inputs
        if not validate_inputs(contributor_name, language):
            continue

        # Base path - use pathlib for better path handling
        script_path = Path(__file__).resolve()
        base_path = script_path.parent.parent.parent  # Go up 3 levels to bitcoin-educational-content
        
        if content_choice == 1:
            # Tutorials
            content_path = base_path / 'tutorials'
            yaml_filename = 'tutorial.yml'
            content_type = 'tutorials'
        elif content_choice == 2:
            # Glossary
            content_path = base_path / 'resources' / 'glossary'
            yaml_filename = 'word.yml'
            content_type = 'glossary'
        elif content_choice == 3:
            # Quizzes
            content_path = base_path / 'courses'
            yaml_filename = 'question.yml'
            content_type = 'quizzes'
        else:
            # Courses
            content_path = base_path / 'courses'
            yaml_filename = 'course.yml'
            content_type = 'courses'

        # Verify the content directory exists
        if not content_path.exists():
            print(f"Error: {content_type.capitalize()} directory not found at {content_path}")
            print("Please ensure the script is in the correct location within the project structure.")
            continue

        if content_choice == 1:
            # Tutorials - show main folders for selection
            main_folders = get_subfolders(content_path)
            if not main_folders:
                print(f"No main folders found in the '{content_type}' directory.")
                continue

            print(f"\nMain folders in '{content_type}' directory:")
            for i, folder in enumerate(sorted(main_folders)):
                print(f"{i + 1:2d}. {folder}")

            # Input for main folder selection
            try:
                main_folder_choice = int(input(f"\nSelect a main folder (1-{len(main_folders)}): "))
                if 1 <= main_folder_choice <= len(main_folders):
                    selected_main_folder = sorted(main_folders)[main_folder_choice - 1]
                    main_folder_path = content_path / selected_main_folder
                else:
                    print("Invalid selection.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            print(f"\nSelected folder: {selected_main_folder}")
        elif content_choice == 2:
            # Glossary - work directly with the glossary folder
            main_folder_path = content_path
            print(f"\nWorking with glossary directory")
        elif content_choice == 3:
            # Quizzes - show course folders for selection
            course_folders = get_subfolders(content_path)
            if not course_folders:
                print(f"No course folders found in the '{content_type}' directory.")
                continue

            print(f"\nCourse folders in '{content_type}' directory:")
            for i, folder in enumerate(sorted(course_folders)):
                print(f"{i + 1:2d}. {folder}")

            # Input for course folder selection
            try:
                course_choice = int(input(f"\nSelect a course folder (1-{len(course_folders)}): "))
                if 1 <= course_choice <= len(course_folders):
                    selected_course_folder = sorted(course_folders)[course_choice - 1]
                    main_folder_path = content_path / selected_course_folder
                else:
                    print("Invalid selection.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            print(f"\nSelected course: {selected_course_folder}")
        else:
            # Courses - work directly with the courses folder
            main_folder_path = content_path
            print(f"\nWorking with courses directory")

        # Processing mode selection
        print("Processing options:")
        print("1. Process all subfolders automatically (alphabetical order)")
        print("2. Select specific subfolders interactively")
        
        try:
            mode_choice = int(input("Choose processing mode (1-2): "))
            if mode_choice == 1:
                # Alphabetical processing with sub-options
                print("\nAlphabetical processing options:")
                print("1. Process ALL subfolders")
                print("2. Process subfolders from a specific range (start to end)")
                
                try:
                    alpha_choice = int(input("Choose alphabetical option (1-2): "))
                    if alpha_choice == 1:
                        # Process all subfolders automatically
                        if content_choice == 1:
                            all_subfolders = get_subfolders(main_folder_path)
                            process_subfolders(main_folder_path, language, contributor_name, all_subfolders)
                        elif content_choice == 2:
                            all_subfolders = get_subfolders(main_folder_path)
                            process_glossary_subfolders(main_folder_path, language, contributor_name, all_subfolders)
                        elif content_choice == 3:
                            # For quizzes, get quiz subfolders from the quizz directory
                            quiz_path = main_folder_path / 'quizz'
                            if quiz_path.exists():
                                all_quiz_subfolders = get_subfolders(quiz_path)
                                process_quiz_subfolders(main_folder_path, language, contributor_name, all_quiz_subfolders)
                            else:
                                print(f"  ⚠ No 'quizz' folder found in {main_folder_path.name}")
                                continue
                        else:  # content_choice == 4
                            # For courses, get all course folders
                            all_courses = get_subfolders(main_folder_path)
                            process_course_folders(main_folder_path, language, contributor_name, all_courses)
                    elif alpha_choice == 2:
                        # Process alphabetical range
                        if content_choice == 1:
                            process_alphabetical_range(main_folder_path, language, contributor_name)
                        elif content_choice == 2:
                            process_alphabetical_range_glossary(main_folder_path, language, contributor_name)
                        elif content_choice == 3:
                            process_alphabetical_range_quiz(main_folder_path, language, contributor_name)
                        else:  # content_choice == 4
                            process_alphabetical_range_course(main_folder_path, language, contributor_name)
                    else:
                        print("Invalid selection.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                    
            elif mode_choice == 2:
                # Interactive subfolder selection
                if content_choice == 1:
                    process_subfolders(main_folder_path, language, contributor_name)
                elif content_choice == 2:
                    process_glossary_subfolders(main_folder_path, language, contributor_name)
                elif content_choice == 3:
                    process_quiz_subfolders(main_folder_path, language, contributor_name)
                else:  # content_choice == 4
                    process_course_folders(main_folder_path, language, contributor_name)
            else:
                print("Invalid selection.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Ask if user wants to add another contributor
        print("\n" + "="*50)
        add_another = input("Do you want to add another contributor? (y/n): ").lower().startswith('y')
        if not add_another:
            break
        print()  # Add blank line for readability

    print("\n=== Script completed ===")

if __name__ == "__main__":
    main()