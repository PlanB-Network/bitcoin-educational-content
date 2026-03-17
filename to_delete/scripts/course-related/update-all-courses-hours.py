import os
import re
import math
from colorama import Fore, Style, init

init(autoreset=True)

def select_md_file(folder_path):
    en_md_path = os.path.join(folder_path, 'en.md')
    fr_md_path = os.path.join(folder_path, 'fr.md')
    if os.path.exists(en_md_path):
        return en_md_path
    elif os.path.exists(fr_md_path):
        return fr_md_path
    else:
        md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
        if not md_files:
            print(Fore.RED + "No .md file found in the folder.")
            return None
        else:
            print(Fore.CYAN + "Multiple .md files found:")
            for idx, md_file in enumerate(md_files):
                print(f"{idx + 1}. {md_file}")
            while True:
                choice = input("Enter the number of the .md file to use: ")
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(md_files):
                        return os.path.join(folder_path, md_files[choice - 1])
                    else:
                        print("Invalid selection. Please enter a number from the list.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

def count_words_images_and_tutorial_links(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        words = len(re.findall(r'\b\w+\b', content))

        images = len(re.findall(r'!\[.*?\]\(.*?\)', content))

        urls = re.findall(r'https?://[^\s\)"]+', content)

        tutorial_links = sum('/tutorials/' in url for url in urls)

        return words, images, tutorial_links
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        return None, None, None

def get_difficulty_factor(level):
    difficulty_mapping = {
        'beginner': 1,
        'intermediate': 1.5,
        'advanced': 2,
        'wizard': 2.5
    }
    return difficulty_mapping.get(level.lower(), 1)

def calculate_hours(words, images, tutorial_links, difficulty):
    base_time_seconds = words * 0.75 + images * 30
    tutorial_time_seconds = tutorial_links * 600
    total_time_seconds = (base_time_seconds + tutorial_time_seconds) * difficulty
    return total_time_seconds / 3600

def format_duration_in_hours_and_minutes(total_hours):
    hours = int(total_hours)
    minutes = int(round((total_hours - hours) * 60))
    return hours, minutes

def update_hours_in_yaml(course_yaml_path, new_hours):
    try:
        with open(course_yaml_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(course_yaml_path, 'w', encoding='utf-8') as file:
            for line in lines:
                if line.strip().startswith('hours:'):
                    indentation = line[:line.index('hours:')]
                    line = f"{indentation}hours: {new_hours}\n"
                file.write(line)
        print(Fore.GREEN + f"The 'hours' value has been updated to {new_hours} in {course_yaml_path}")
    except Exception as e:
        print(Fore.RED + f"Error updating {course_yaml_path}: {e}")

def main():
    base_path = input("Please enter the path to the 'courses' folder: ").strip()

    if (base_path.startswith('"') and base_path.endswith('"')) or (base_path.startswith("'") and base_path.endswith("'")):
        base_path = base_path[1:-1]

    base_path = os.path.normpath(base_path)

    if not os.path.isdir(base_path):
        print(Fore.RED + "The base directory does not exist. Please check the path.")
        return

    course_folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

    for course_folder in course_folders:
        folder_path = os.path.join(base_path, course_folder)
        while True:
            print(Fore.CYAN + f"\nDo you want to process the course '{course_folder}'? (y/n): ", end="")
            choice = input().strip().lower()
            if choice in ['y', 'n']:
                break
            else:
                print(Fore.RED + "Please enter 'y' for yes or 'n' for no.")

        if choice != 'y':
            continue

        course_yaml_path = os.path.join(folder_path, 'course.yml')
        if not os.path.exists(course_yaml_path):
            print(Fore.RED + f"course.yml not found in {folder_path}. Course skipped.")
            continue

        try:
            with open(course_yaml_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                level = 'beginner'
                for line in lines:
                    if line.strip().startswith('level:'):
                        level = line.strip().split(':', 1)[1].strip()
                        break
        except Exception as e:
            print(Fore.RED + f"Error reading {course_yaml_path}: {e}")
            continue

        difficulty = get_difficulty_factor(level)

        md_file_path = select_md_file(folder_path)
        if md_file_path is None:
            print(Fore.RED + "No appropriate .md file found. Course skipped.")
            continue

        total_words, total_images, total_tutorial_links = count_words_images_and_tutorial_links(md_file_path)
        if total_words is None or total_images is None or total_tutorial_links is None:
            print(Fore.RED + "Error analyzing markdown content. Course skipped.")
            continue

        total_hours = calculate_hours(total_words, total_images, total_tutorial_links, difficulty)
        rounded_hours = math.ceil(total_hours)
        exact_hours, exact_minutes = format_duration_in_hours_and_minutes(total_hours)

        print(Fore.YELLOW + f"\nTotal words counted: {total_words}")
        print(Fore.YELLOW + f"Total images found: {total_images}")
        print(Fore.YELLOW + f"Total tutorial links found: {total_tutorial_links}")
        print(Fore.BLUE + f"Exact duration: {exact_hours} hours and {exact_minutes} minutes")
        print(Fore.GREEN + f"Rounded duration: {rounded_hours} hours")

        update_hours_in_yaml(course_yaml_path, rounded_hours)

if __name__ == "__main__":
    main()
