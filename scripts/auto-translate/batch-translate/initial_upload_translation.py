import json
import os
import sys
import subprocess
from typing import List, Dict
from tqdm import tqdm
import readline

# Get the script's directory and root directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..'))

def load_supported_languages() -> Dict:
    lang_file_path = os.path.join(SCRIPT_DIR, '..', 'translation_logic', 'supported_languages.json')

    try:
        with open(lang_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading supported languages: {e}")
        sys.exit(1)
 
def display_current_languages(languages: List[Dict]) -> None:
    print("\n=== Current Supported Languages ===")
    print(f"Total languages: {len(languages)}\n")
    
    for idx, lang in enumerate(sorted(languages, key=lambda x: x['code'].lower()), 1):
        print(f"{idx}. {lang['name']} ({lang['code']:<8}) - {lang['translator']}")
    print()
 
def get_input(prompt: str) -> str:
    try:
        readline.parse_and_bind('set editing-mode emacs')
        return input(prompt)
    except EOFError:
        print("\nInput cancelled")
        sys.exit(1)
 
def get_target_language(supported_langs: Dict) -> str:
    display_current_languages(supported_langs['languages'])
    
    while True:
        try:
            choice = int(get_input("\nEnter the number of your target language: "))
            if 1 <= choice <= len(supported_langs['languages']):
                return supported_langs['languages'][choice-1]['code']
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
 
def translate_file(input_file: str, target_lang: str) -> None:
    try:
        # Just use relative path to translation_controller from current script
        translation_controller = "../translation_controller.py"
        adjusted_input_file = "../../../" + input_file
        command = ["python3", translation_controller, adjusted_input_file, target_lang]

        subprocess.run(command, check=True)
        print(f"Translated {input_file} to {target_lang}")
    except subprocess.CalledProcessError as e:
        print(f"Error translating {input_file}: {e}")


def should_skip_file(file_path: str) -> bool:
    """Check if file should be skipped based on path."""
    paths_to_skip = [
        "courses/btc101",
        "courses/biz224",
        "courses/btc204",
        # "courses/test",
        # "resources/draft",
    ]
    return any(skip_path in file_path for skip_path in paths_to_skip)


def find_english_files(base_directories: List[str], target_lang: str) -> List[str]:
    english_files = []
    
    for directory in base_directories:
        base_dir = os.path.join(ROOT_DIR, directory)
        if not os.path.exists(base_dir):
            print(f"Warning: Directory not found: {base_dir}")
            continue
            
        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.endswith(('en.md', 'en.yml')):
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, ROOT_DIR)
                    
                    # Check if translation already exists
                    target_file = relative_path.replace('en.', f'{target_lang}.')
                    target_full_path = os.path.join(ROOT_DIR, target_file)
                    
                    if os.path.exists(target_full_path):
                        print(f"Skipping {relative_path} - {target_lang} translation already exists")
                        continue
                        
                    if not should_skip_file(relative_path):
                        english_files.append(relative_path)
    
    return sorted(english_files)
 
def main():
    # Paths relative to root directory
    base_directories = [
        'courses',
        'professors',
        'resources/projects',
        'resources/bet',
        'resources/books',
        'tutorials'
    ]
    
    supported_langs = load_supported_languages()
    
    
    # Get target language first
    if len(sys.argv) > 1:
        target_lang = sys.argv[1]
        if target_lang not in [lang['code'] for lang in supported_langs['languages']]:
            print(f"Error: Language '{target_lang}' is not supported.")
            sys.exit(1)
    else:
        target_lang = get_target_language(supported_langs)
    
    # Now pass target_lang to find_english_files
    english_files = find_english_files(base_directories, target_lang)
    
    if not english_files:
        print("No English files found in the specified directories.")
        return
    
    print(f"\nFound {len(english_files)} English files to translate.")
    print("Note: Files in courses/btc101/ will be skipped")
    files_list = "\n".join(str(f) for f in english_files)
    
    
    success_count = 0
    error_count = 0
    
    total_files = len(english_files)
    progress_bar = tqdm(english_files, desc="Translating files", unit="file", total=total_files)
    
    for file_path in progress_bar:
        folder_name = os.path.basename(os.path.dirname(file_path))
        progress_bar.set_description(f"Processing {folder_name}")
        
        try:
            translate_file(file_path, target_lang)
            success_count += 1
        except Exception as e:
            error_count += 1
            error_msg = str(e).split('\n')[0]
            print(f"\nError translating {file_path}: {error_msg}")
    
    print(f"\nTranslation completed!")
    print(f"Successfully translated: {success_count} files")
    print(f"Failed translations: {error_count} files")
 
if __name__ == "__main__":
    main()


