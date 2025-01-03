import os
import shutil
import sys
import subprocess
from pathlib import Path

def get_supported_languages():
    directory = "../../../courses/btc101"
    supported_languages = []
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".md") and filename != "en.md":
                supported_languages.append(filename.split(".")[0])
    return supported_languages

def content_exist(filenames, lang):
    return any(f.endswith(f"{lang}.md") or f.endswith(f"{lang}.yml") for f in filenames)

def create_txt_to_en_from(lang):
    base_dir = "../../../tutorials/"
    output_file = f"./translate-to-en/{lang}.txt"
    file_written = False

    with open(output_file, "w") as yml_file:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.startswith(f"{lang}.") and not content_exist(filenames, 'en'): 
                    # Calculate path relative to script's parent directory
                    abs_path = Path(dirpath) / filename
                    relative_path = "../" + os.path.relpath(abs_path, start=os.path.dirname(os.getcwd()))
                    yml_file.write(f"{relative_path}\n")
                    file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from {lang}")

def create_txt_from_en_to(lang):
    base_dir = "../../../tutorials/"
    output_file = f"./translate-from-en/{lang}.txt"
    file_written = False

    with open(output_file, "w") as yml_file:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.startswith(f"en.") and not content_exist(filenames, lang): 
                    # Calculate path relative to script's parent directory
                    abs_path = Path(dirpath) / filename
                    relative_path = "../" + os.path.relpath(abs_path, start=os.path.dirname(os.getcwd()))
                    yml_file.write(f"{relative_path}\n")
                    file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from en to {lang}")

def translate_file(input_file, target_lang):
    try:
        command = ["python3", "../translation_controller.py", input_file, target_lang]
        subprocess.run(command, check=True)
        print(f"Translated {input_file} to {target_lang}")
    except subprocess.CalledProcessError as e:
        print(f"Error translating {input_file}: {e}")

def process_translation_list(list_file):
    if not os.path.exists(list_file):
        return

    with open(list_file, 'r') as f:
        files = f.readlines()
        
    for file_path in files:
        file_path = file_path.strip()
        if file_path:
            base_name = Path(list_file).name
            lang = base_name.split('.')[0]
            
            if list_file.startswith('./translate-to-en/'):
                translate_file(file_path, 'en')
            else:
                translate_file(file_path, lang)

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    languages = get_supported_languages()
    ensure_directory_exists("./translate-to-en")
    ensure_directory_exists("./translate-from-en")

    for lang in sorted(languages):
        create_txt_to_en_from(lang)
        
        to_en_list = f"./translate-to-en/{lang}.txt"
        if os.path.exists(to_en_list):
            print(f"\nProcessing translations from {lang} to English")
            process_translation_list(to_en_list)
    for lang in sorted(languages):
        create_txt_from_en_to(lang)
        from_en_list = f"./translate-from-en/{lang}.txt"
        
            
        if os.path.exists(from_en_list):
            print(f"\nProcessing translations from English to {lang}")
            process_translation_list(from_en_list)

    print("Translation process completed!")

if __name__ == "__main__":
    main()
