import os
import shutil
import subprocess
from pathlib import Path


def prepare_git_branch():

    os.system("git checkout dev")
    os.system("git pull")
    os.system("git checkout -b auto-batch-translation")
    print("New branch updated and ready to proceed!")


def get_supported_languages():
    """Returns an array of strings with the names of all Markdown (*.md) files in the directory, excluding 'en.md'."""

    directory = "../../courses/btc101/"
    supported_languages = []

    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".md") and filename != "en.md":
                supported_languages.append(filename.split(".")[0])
    else:
        print("Directory does not exist.")

    return supported_languages

def content_exist(filenames, lang):
    return any(f.endswith(f"{lang}.md") or f.endswith(f"{lang}.yml") for f in filenames)
    
def create_txt_to_en_from(lang):
    base_dirs = ["../../courses", "../../resources", "../../tutorials"]
    output_file = f"./translate-to-en/{lang}.txt"
    skip_dirs = ["btc205",
                 ]
    file_written = False

    with open(output_file, "w") as yml_file:
        for base_dir in base_dirs:
            for dirpath, dirnames, filenames in os.walk(base_dir):
                if any(skip_dir in dirpath for skip_dir in skip_dirs):
                    continue
                for filename in filenames:
                    if filename.startswith(f"{lang}.") and content_exist(filenames, lang) and not content_exist(filenames, 'en'): 
                        relative_path = os.path.relpath(Path(dirpath) / filename, start=".")
                        yml_file.write(f"{relative_path}\n")
                        file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from {lang}")

def copy_from_repo_to_LLM_Translator(lang):
    input_list_path = f"./translate-to-en/{lang}.txt"
    destination_base_path = f"../../../LLM-Translator/inputs/pbn-from-{lang}-to-en/"

    if not os.path.exists(input_list_path):
        print(f"No file list found for language '{lang}'.")
    else:
        os.makedirs(destination_base_path, exist_ok=True)
        with open(input_list_path, 'r') as file:
            for line in file:
                source_path = line.strip()
                if not source_path:
                    continue
                new_filename = source_path.lstrip('./').replace('/', '_')
                new_filename = new_filename.rstrip('_')
                new_filename = new_filename.replace(f'_{lang}','')
                print(new_filename)
                destination_file_path = os.path.join(destination_base_path, new_filename)

                try:
                    shutil.copy(source_path, destination_file_path)
                    print(f"Copied and renamed '{source_path}' to '{destination_file_path}'")
                except Exception as e:
                    print(f"Error copying '{source_path}': {str(e)}")

def run_LLM_Translator(source_language, destination_language, folder_path):
    command = [
        "python3",
        "../../../LLM-Translator/scripts/main.py",
        "-l", destination_language,
        "-o", source_language,
        "-s", folder_path
    ]

    try:
        subprocess.run(command, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# def copy_from_LLM_Translator_to_repo(lang):


def main():
    # prepare_git_branch()
    languages = get_supported_languages()
    for lang in languages:
        create_txt_to_en_from(lang)
        translation_needed = os.path.exists(f"./translate-to-en/{lang}.txt")
        if translation_needed:
            copy_from_repo_to_LLM_Translator(lang)
            # translation_input_path = f"pbn-from-{lang}-to-en"
            # run_LLM_Translator(lang, 'en', translation_input_path)
            # copy_from_LLM_Translator_to_repo(lang)
    print("So far so good!")


if __name__ == "__main__":
    main()
