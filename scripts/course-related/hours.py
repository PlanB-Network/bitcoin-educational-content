import re
import os
from colorama import Fore, Style, init

init(autoreset=True)

def count_words_and_images(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        words = len(re.findall(r'\b\w+\b', content))

        images = len(re.findall(r'!\[.*?\]\(.*?\)', content))

        return words, images
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None, None

def get_difficulty_factor(choice):
    difficulty_mapping = {'A': 1, 'B': 1.5, 'C': 2, 'D': 2.5}
    return difficulty_mapping.get(choice.upper(), None)

def calculate_hours(words, images, difficulty):
    return (words * 0.25 + images * 30) * difficulty / 60 / 60

def format_duration_in_hours_and_minutes(total_hours):
    hours = int(total_hours)
    minutes = int((total_hours - hours) * 60)
    return hours, minutes

def main():
    print(Fore.CYAN + "Drop the .md file path here :", end=" ")
    file_path = input().strip().strip('"').strip("'")

    if not os.path.exists(file_path):
        print(Fore.RED + "The file does not exist. Please provide a valid file path.")
        return

    print(Fore.CYAN + "\nSelect the difficulty:")
    print(Fore.CYAN + "- A: Easy (1)")
    print(Fore.CYAN + "- B: Intermediate (1.5)")
    print(Fore.CYAN + "- C: Expert (2)")
    print(Fore.CYAN + "- D: Wizard (2.5)")

    difficulty_choice = input(Fore.CYAN + "Enter your choice (A, B, C, or D): ").upper()
    difficulty = get_difficulty_factor(difficulty_choice)

    if difficulty is None:
        print(Fore.RED + "Invalid difficulty choice. Please select A, B, C, or D.")
        return

    words, images = count_words_and_images(file_path)
    if words is None or images is None:
        return

    total_hours = calculate_hours(words, images, difficulty)
    rounded_hours = round(total_hours)
    exact_hours, exact_minutes = format_duration_in_hours_and_minutes(total_hours)

    print(Fore.YELLOW + f"\nTotal words counted: {words}")
    print(Fore.YELLOW + f"Total images found: {images}")
    print(Fore.BLUE + f"Exact duration: {exact_hours} hours and {exact_minutes} minutes")
    print(Fore.GREEN + f"Rounded duration: {rounded_hours} hours")

if __name__ == "__main__":
    main()
