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

def select_language(course_code):
    """Prompt user to select a language for the given course"""
    available_languages = get_available_languages_for_course(course_code)
    
    if not available_languages:
        print(f"No languages found for course '{course_code}'.")
        return None
    
    print(f"\nAvailable languages for course '{course_code}' ({len(available_languages)}):")
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
                    print(f"Language '{user_input}' not found for this course. Please try again.")
                    continue
                    
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
        except:
            print("Invalid input. Please try again.")

def main():
    print("=== Course Language Reward Calculator ===")
    print(f"Working directory: {os.getcwd()}")
    print(f"Courses directory: {get_courses_directory()}")
    print()
    
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
    target_language = select_language(course_code)
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

if __name__ == "__main__":
    main()