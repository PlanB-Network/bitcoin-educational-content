import os
import shutil
import sys
import subprocess
from pathlib import Path

# Define base paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent

def get_supported_languages():
    """Get list of supported languages from btc101 course directory."""
    directory = PROJECT_ROOT / "courses" / "btc101"
    supported_languages = []
    
    if directory.exists():
        for filename in os.listdir(directory):
            if filename.endswith(".md") and filename != "en.md":
                supported_languages.append(filename.split(".")[0])
    return supported_languages

def content_exist(filenames, lang):
    """Check if content exists for a specific language in given filenames."""
    return any(f.endswith(f"{lang}.md") or f.endswith(f"{lang}.yml") for f in filenames)

def create_txt_to_en_from(lang):
    """Create a list of files that need translation from given language to English."""
    base_dir = PROJECT_ROOT / "tutorials"
    output_file = SCRIPT_DIR / "translate-to-en" / f"{lang}.txt"
    file_written = False

    with open(output_file, "w") as yml_file:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.startswith(f"{lang}.") and not content_exist(filenames, 'en'): 
                    file_path = Path(dirpath) / filename
                    relative_path = os.path.relpath(file_path, SCRIPT_DIR)
                    yml_file.write(f"{relative_path}\n")
                    file_written = True

    if not file_written:
        output_file.unlink(missing_ok=True)
        print(f"No need to translate from {lang}")

def create_txt_from_en_to(lang):
    """Create a list of files that need translation from English to given language."""
    base_dir = PROJECT_ROOT / "tutorials"
    output_file = SCRIPT_DIR / "translate-from-en" / f"{lang}.txt"
    file_written = False

    with open(output_file, "w") as yml_file:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.startswith(f"en.") and not content_exist(filenames, lang): 
                    file_path = Path(dirpath) / filename
                    relative_path = os.path.relpath(file_path, SCRIPT_DIR)
                    yml_file.write(f"{relative_path}\n")
                    file_written = True

    if not file_written:
        output_file.unlink(missing_ok=True)
        print(f"No need to translate from en to {lang}")

def translate_file(input_file, target_lang):
    """Translate a single file using translation_controller."""
    try:
        translation_controller = SCRIPT_DIR.parent / "translation_controller.py"
        command = ["python3", str(translation_controller), input_file, target_lang]
        subprocess.run(command, check=True)
        print(f"Translated {input_file} to {target_lang}")
    except subprocess.CalledProcessError as e:
        print(f"Error translating {input_file}: {e}")

def process_translation_list(list_file):
    """Process a list of files for translation."""
    list_path = Path(list_file)
    if not list_path.exists():
        return

    with open(list_path, 'r') as f:
        files = f.readlines()
        
    for file_path in files:
        file_path = file_path.strip()
        if file_path:
            if "translate-to-en" in str(list_path):
                translate_file(file_path, 'en')
            else:
                lang = list_path.stem
                translate_file(file_path, lang)

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    directory_path = Path(directory)
    if not directory_path.exists():
        directory_path.mkdir(parents=True, exist_ok=True)

def cleanup_temp_directories():
    """Remove temporary translation directories."""
    temp_dirs = [
        SCRIPT_DIR / "translate-to-en",
        SCRIPT_DIR / "translate-from-en"
    ]
    for dir_path in temp_dirs:
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"Removed temporary directory: {dir_path}")

def main():
    """Execute the translation workflow."""
    languages = get_supported_languages()
    ensure_directory_exists(SCRIPT_DIR / "translate-to-en")
    ensure_directory_exists(SCRIPT_DIR / "translate-from-en")

    # First pass: translate all non-English content to English
    for lang in sorted(languages):
        create_txt_to_en_from(lang)
        to_en_list = SCRIPT_DIR / "translate-to-en" / f"{lang}.txt"
        
        if to_en_list.exists():
            print(f"\nProcessing translations from {lang} to English")
            process_translation_list(str(to_en_list))

    # Second pass: translate English content to other languages
    for lang in sorted(languages):
        create_txt_from_en_to(lang)
        from_en_list = SCRIPT_DIR / "translate-from-en" / f"{lang}.txt"
        
        if from_en_list.exists():
            print(f"\nProcessing translations from English to {lang}")
            process_translation_list(str(from_en_list))

    print("Translation process completed!")

if __name__ == "__main__":
    main()

