#!/usr/bin/env python3

import os
import yaml
import glob
from decimal import Decimal, getcontext
from pathlib import Path

# Set high precision for decimal calculations
getcontext().prec = 50

def get_courses_directory():
    """Get the path to the courses directory from the script location"""
    script_dir = Path(__file__).parent
    courses_dir = script_dir / ".." / ".." / "courses"
    return courses_dir.resolve()

def get_glossary_directory():
    """Get the path to the glossary directory from the script location"""
    script_dir = Path(__file__).parent
    glossary_dir = script_dir / ".." / ".." / "resources" / "glossary"
    return glossary_dir.resolve()

def get_available_courses():
    """Get list of available course codes from the courses directory"""
    courses_dir = get_courses_directory()
    if not courses_dir.exists():
        return []
    
    courses = []
    for item in courses_dir.iterdir():
        if item.is_dir():
            # Check if it has a quizz subfolder
            quizz_dir = item / "quizz"
            if quizz_dir.exists() and quizz_dir.is_dir():
                courses.append(item.name)
    
    return sorted(courses)

def find_question_files(course_code):
    """Find all question.yml files in the specified course's quizz folder"""
    courses_dir = get_courses_directory()
    quizz_dir = courses_dir / course_code / "quizz"
    
    if not quizz_dir.exists():
        return []
    
    return list(quizz_dir.glob("**/question.yml"))

def find_word_files():
    """Find all word.yml files in the glossary directory"""
    glossary_dir = get_glossary_directory()
    
    if not glossary_dir.exists():
        return []
    
    return list(glossary_dir.glob("**/word.yml"))

def extract_reward_for_language(file_path, target_language):
    """Extract reward for a specific language from a YAML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            
        # Check if proofreading section exists
        if 'proofreading' not in data:
            return None
            
        # Look for the target language in proofreading entries
        for entry in data['proofreading']:
            if entry.get('language') == target_language:
                reward = entry.get('reward')
                if reward is not None:
                    return Decimal(str(reward))
        
        return None
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def get_available_languages_for_course(course_code):
    """Get a list of all available languages for a specific course"""
    languages = set()
    files = find_question_files(course_code)
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                
            if 'proofreading' in data:
                for entry in data['proofreading']:
                    lang = entry.get('language')
                    if lang:
                        languages.add(lang)
        except:
            continue
    
    return sorted(list(languages))

def get_available_languages_for_glossary():
    """Get a list of all available languages across all word files"""
    languages = set()
    files = find_word_files()
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                
            if 'proofreading' in data:
                for entry in data['proofreading']:
                    lang = entry.get('language')
                    if lang:
                        languages.add(lang)
        except:
            continue
    
    return sorted(list(languages))

def select_evaluation_type():
    """Prompt user to select between glossary and quiz evaluation"""
    print("Select evaluation type:")
    print("1. Glossary (word.yml files)")
    print("2. Quiz (question.yml files)")
    
    while True:
        try:
            user_input = input("\nEnter your choice (1 or 2): ").strip()
            
            if user_input == "1":
                return "glossary"
            elif user_input == "2":
                return "quiz"
            else:
                print("Invalid choice. Please enter 1 or 2.")
                continue
                
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
        except:
            print("Invalid input. Please try again.")

def select_course():
    """Prompt user to select a course"""
    available_courses = get_available_courses()
    
    if not available_courses:
        print("No courses with quizz folders found in ../../courses/")
        return None
    
    print(f"Available courses ({len(available_courses)}):")
    for i, course in enumerate(available_courses, 1):
        print(f"{i:2d}. {course}")
    
    while True:
        try:
            print(f"\nEnter the course code you want to analyze:")
            print("(You can type the code directly or enter a number from the list above)")
            user_input = input("Course: ").strip()
            
            # Check if user entered a number
            if user_input.isdigit():
                index = int(user_input) - 1
                if 0 <= index < len(available_courses):
                    return available_courses[index]
                else:
                    print("Invalid number. Please try again.")
                    continue
            else:
                # Check if the entered course code exists
                if user_input in available_courses:
                    return user_input
                else:
                    print(f"Course '{user_input}' not found. Please try again.")
                    continue
                    
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
        except:
            print("Invalid input. Please try again.")

def select_language(available_languages, context=""):
    """Prompt user to select a language"""
    if not available_languages:
        print(f"No languages found{context}.")
        return None
    
    print(f"\nAvailable languages{context} ({len(available_languages)}):")
    for i, lang in enumerate(available_languages, 1):
        print(f"{i:2d}. {lang}")
    
    while True:
        try:
            print(f"\nEnter the language code you want to calculate rewards for:")
            print("(You can type the code directly or enter a number from the list above)")
            user_input = input("Language: ").strip()
            
            # Check if user entered a number
            if user_input.isdigit():
                index = int(user_input) - 1
                if 0 <= index < len(available_languages):
                    return available_languages[index]
                else:
                    print("Invalid number. Please try again.")
                    continue
            else:
                # Check if the entered language code exists
                if user_input in available_languages:
                    return user_input
                else:
                    print(f"Language '{user_input}' not found. Please try again.")
                    continue
                    
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
        except:
            print("Invalid input. Please try again.")

def evaluate_glossary_rewards():
    """Evaluate rewards for glossary word files"""
    print(f"Glossary directory: {get_glossary_directory()}")
    
    # Find word files
    files = find_word_files()
    if not files:
        print("No word.yml files found in glossary directory.")
        return
    
    print(f"Found {len(files)} word.yml files in glossary")
    
    # Select language
    available_languages = get_available_languages_for_glossary()
    target_language = select_language(available_languages, " in glossary")
    if not target_language:
        return
    
    print(f"\nCalculating rewards for glossary, language: '{target_language}'")
    print("-" * 60)
    
    # Process files and calculate total reward
    total_reward = Decimal('0')
    processed_files = 0
    found_files = 0
    
    for file_path in files:
        # Show relative path from glossary folder for cleaner output
        glossary_dir = get_glossary_directory()
        relative_path = file_path.relative_to(glossary_dir)
        
        print(f"Processing file: ./{relative_path}")
        processed_files += 1
        
        reward = extract_reward_for_language(file_path, target_language)
        if reward is not None:
            print(f"Found reward: {reward}")
            total_reward += reward
            found_files += 1
    
    # Output results
    print("-" * 60)
    print(f"Evaluation type: Glossary")
    print(f"Language: {target_language}")
    print(f"Total files processed: {processed_files}")
    print(f"Files with {target_language} language: {found_files}")
    print(f"Total reward for language '{target_language}': {total_reward}")
    
    if found_files > 0:
        print(f"Average reward per file: {total_reward / found_files:.4f}")
        print(f"Total reward with extended precision: {total_reward}")
    else:
        print(f"No files found with language '{target_language}'")

def evaluate_quiz_rewards():
    """Evaluate rewards for quiz question files"""
    print(f"Courses directory: {get_courses_directory()}")
    
    # Select course
    course_code = select_course()
    if not course_code:
        return
    
    # Find question files for the selected course
    files = find_question_files(course_code)
    if not files:
        print(f"No question.yml files found in course '{course_code}' quizz folder.")
        return
    
    print(f"\nFound {len(files)} question.yml files in course '{course_code}'")
    
    # Select language
    available_languages = get_available_languages_for_course(course_code)
    target_language = select_language(available_languages, f" for course '{course_code}'")
    if not target_language:
        return
    
    print(f"\nCalculating rewards for course '{course_code}', language: '{target_language}'")
    print("-" * 60)
    
    # Process files and calculate total reward
    total_reward = Decimal('0')
    processed_files = 0
    found_files = 0
    
    for file_path in files:
        # Show relative path from quizz folder for cleaner output
        courses_dir = get_courses_directory()
        quizz_dir = courses_dir / course_code / "quizz"
        relative_path = file_path.relative_to(quizz_dir)
        
        print(f"Processing file: ./{relative_path}")
        processed_files += 1
        
        reward = extract_reward_for_language(file_path, target_language)
        if reward is not None:
            print(f"Found reward: {reward}")
            total_reward += reward
            found_files += 1
    
    # Output results
    print("-" * 60)
    print(f"Evaluation type: Quiz")
    print(f"Course: {course_code}")
    print(f"Language: {target_language}")
    print(f"Total files processed: {processed_files}")
    print(f"Files with {target_language} language: {found_files}")
    print(f"Total reward for language '{target_language}': {total_reward}")
    
    if found_files > 0:
        print(f"Average reward per file: {total_reward / found_files:.4f}")
        print(f"Total reward with extended precision: {total_reward}")
    else:
        print(f"No files found with language '{target_language}'")

def ask_continue():
    """Ask user if they want to calculate another reward"""
    while True:
        try:
            print("\n" + "=" * 60)
            user_input = input("Do you want to calculate another reward? (y/n): ").strip().lower()
            
            if user_input in ['y', 'yes']:
                return True
            elif user_input in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                continue
                
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return False
        except:
            print("Invalid input. Please try again.")

def main():
    print("=== Unified Language Reward Calculator ===")
    print(f"Working directory: {os.getcwd()}")
    
    while True:
        print()
        
        # Select evaluation type
        evaluation_type = select_evaluation_type()
        if not evaluation_type:
            break
        
        print()
        if evaluation_type == "glossary":
            evaluate_glossary_rewards()
        elif evaluation_type == "quiz":
            evaluate_quiz_rewards()
        
        # Ask if user wants to continue
        if not ask_continue():
            break
    
    print("\nThank you for using the Unified Language Reward Calculator!")

if __name__ == "__main__":
    main()