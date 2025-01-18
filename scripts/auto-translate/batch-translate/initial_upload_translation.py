import json
import os
from pathlib import Path
import sys
import subprocess
from typing import List, Dict
from tqdm import tqdm
import readline

def load_supported_languages() -> Dict:
    lang_file_path = Path(__file__).parent.parent / 'translation_logic' / 'supported_languages.json'
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
        command = ["python3", "../translation_controller.py", input_file, target_lang]
        subprocess.run(command, check=True)
        print(f"Translated {input_file} to {target_lang}")
    except subprocess.CalledProcessError as e:
        print(f"Error translating {input_file}: {e}")
 
def should_skip_file(file_path: str) -> bool:
    """Check if file should be skipped based on path."""
    return "courses/btc101" in file_path
 
def find_english_files(base_directories: List[str]) -> List[Path]:
    english_files = []
    script_dir = Path(os.path.dirname(os.getcwd()))
    
    for directory in base_directories:
        base_dir = Path(directory)
        if not os.path.exists(base_dir):
            print(f"Warning: Directory not found: {base_dir}")
            continue
            
        for ext in ['.md', '.yml']:
            for path in base_dir.rglob(f'en{ext}'):
                if path.is_file():
                    relative_path = "../" + os.path.relpath(path, start=script_dir)
                    if not should_skip_file(str(relative_path)):
                        english_files.append(relative_path)
    
    return sorted(english_files)
 
def main():
    base_directories = [
        "../../../courses",
        "../../../professors",
        "../../../resources/builders",
        "../../../resources/bet",
        "../../../resources/books",
        "../../../tutorials"
    ]
    
    supported_langs = load_supported_languages()
    target_lang = get_target_language(supported_langs)
    
    english_files = find_english_files(base_directories)
    
    if not english_files:
        print("No English files found in the specified directories.")
        return
    
    print(f"\nFound {len(english_files)} English files to translate.")
    print("Note: Files in courses/btc101/ will be skipped")
    files_list = "\n".join(english_files)
    print(f"\nFiles to be translated:\n{files_list}")
    
    if get_input("\nProceed with translation? (y/n): ").lower() != 'y':
        print("Translation cancelled.")
        return
    
    success_count = 0
    error_count = 0
    
    total_files = len(english_files)
    progress_bar = tqdm(english_files, desc="Translating files", unit="file", total=total_files)
    
    for file_path in progress_bar:
        folder_name = Path(file_path).parent.name
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
