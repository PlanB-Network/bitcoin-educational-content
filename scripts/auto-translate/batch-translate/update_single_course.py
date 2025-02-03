import os
import sys
import shutil
import subprocess
from pathlib import Path
from functools import wraps
from typing import List, Callable, Any, Optional

def redirect_output_to_file(filepath: str) -> Callable:
    """Decorator to redirect function output to a file."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            original_stdout = sys.stdout
            with open(filepath, 'w') as f:
                sys.stdout = f
                result = func(*args, **kwargs)
            sys.stdout = original_stdout
            return result
        return wrapper
    return decorator

def get_supported_languages() -> List[str]:
    """Get list of supported languages from btc101 course directory."""
    directory = "../../../courses/btc101"
    supported_languages = []

    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".md") and filename != "en.md":
                supported_languages.append(filename.split(".")[0])
    else:
        print("Directory does not exist.")

    return supported_languages

def content_exist(filenames: List[str], lang: str) -> bool:
    """Check if content exists for a specific language in given filenames."""
    return any(f.endswith(f"{lang}.md") or f.endswith(f"{lang}.yml") for f in filenames)

def create_txt_to_en_from(lang: str, base_dir) -> None:
    """Create a list of files that need translation from given language to English."""
    # base_dir = "../../../courses"
    output_file = f"./translate-to-en/{lang}.txt"
    file_written = False

    with open(output_file, "w") as yml_file:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.startswith(f"{lang}.") and not content_exist(filenames, 'en'): 
                    relative_path = os.path.relpath(Path(dirpath) / filename, start=".")
                    yml_file.write(f"{relative_path}\n")
                    file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from {lang}")

def create_txt_from_en_to(lang: str, base_dir) -> None:
    """Create a list of files that need translation from English to given language."""
    # base_dir = "../../../courses"
    output_file = f"./translate-from-en/{lang}.txt"
    file_written = False

    with open(output_file, "w") as yml_file:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.startswith(f"en.") and not content_exist(filenames, lang): 
                    relative_path = os.path.relpath(Path(dirpath) / filename, start=".")
                    yml_file.write(f"{relative_path}\n")
                    file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from en to {lang}")

def translate_file(input_file: str, target_lang: str) -> None:
    """Translate a single file using translation_controller."""
    try:
        command = ["python3", "../translation_controller.py", input_file, target_lang]
        subprocess.run(command, check=True)
        print(f"Translated {input_file} to {target_lang}")
    except subprocess.CalledProcessError as e:
        print(f"Error translating {input_file}: {e}")

def process_translation_list(list_file: str) -> None:
    """Process a list of files for translation."""
    if not os.path.exists(list_file):
        return

    with open(list_file, 'r') as f:
        files = f.readlines()
        
    for file_path in files:
        file_path = file_path.strip()
        if file_path:
            if list_file.startswith('./translate-to-en/'):
                translate_file(file_path, 'en')
            else:
                lang = Path(list_file).stem
                translate_file(file_path, lang)

def ensure_directory_exists(directory: str) -> None:
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def cleanup_temp_directories() -> None:
    """Remove temporary translation directories."""
    temp_dirs = ["./translate-to-en", "./translate-from-en"]
    for dir_path in temp_dirs:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"Removed temporary directory: {dir_path}")

def select_course_folder():
    """
    Presents a CLI interface for selecting a folder from ../../../courses/
    Returns the selected folder's path as a string
    """
    # Get the absolute path for ../../../courses/
    current_dir = Path(__file__).parent
    courses_path = (current_dir / '../../../courses/').resolve()
    
    # Check if the directory exists
    if not courses_path.exists():
        print(f"Error: Directory {courses_path} does not exist")
        return None
    
    # Get list of folders
    try:
        folders = [f for f in os.listdir(courses_path) 
                  if os.path.isdir(os.path.join(courses_path, f))]
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return None
    
    # If no folders found
    if not folders:
        print("No folders found in the specified directory")
        return None
    
    # Present folders to user
    folders = sorted(folders)
    print("\nAvailable folders:")
    for idx, folder in enumerate(folders, 1):
        print(f"{idx}. {folder}")
    
    # Get user selection
    while True:
        try:
            selection = input("\nSelect a folder number (or 'q' to quit): ")
            
            # Check for quit
            if selection.lower() == 'q':
                return None
            
            # Convert to integer and validate
            selection_idx = int(selection) - 1
            if 0 <= selection_idx < len(folders):
                selected_folder = folders[selection_idx]
                return str(courses_path / selected_folder)
            else:
                print(f"Please enter a number between 1 and {len(folders)}")
        except ValueError:
            print("Please enter a valid number")

def main() -> None:
    """Execute the course translation workflow."""
    languages = get_supported_languages()
    ensure_directory_exists("./translate-to-en")
    ensure_directory_exists("./translate-from-en")
    base_dir = select_course_folder()
    
    # First pass: translate all non-English content to English
    for lang in languages:
        create_txt_to_en_from(lang, base_dir)
        to_en_list = f"./translate-to-en/{lang}.txt"
        if os.path.exists(to_en_list):
            print(f"\nProcessing translations from {lang} to English")
            process_translation_list(to_en_list)

    # Second pass: translate English content to other languages
    for lang in languages:
        create_txt_from_en_to(lang, base_dir)
        from_en_list = f"./translate-from-en/{lang}.txt"
        if os.path.exists(from_en_list):
            print(f"\nProcessing translations from English to {lang}")
            process_translation_list(from_en_list)

    cleanup_temp_directories()
    print("Course translation process completed!")

if __name__ == "__main__":
    main() 

