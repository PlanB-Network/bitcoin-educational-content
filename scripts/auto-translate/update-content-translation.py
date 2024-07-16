import os
import shutil
import sys
import subprocess
from pathlib import Path
from functools import wraps


def redirect_output_to_file(filepath):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            original_stdout = sys.stdout
            with open(filepath, 'w') as f:
                sys.stdout = f
                result = func(*args, **kwargs)
            sys.stdout = original_stdout
            return result
        return wrapper
    return decorator

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
                 "econ102"
                 ]
    file_written = False

    with open(output_file, "w") as yml_file:
        for base_dir in base_dirs:
            for dirpath, dirnames, filenames in os.walk(base_dir):
                if any(skip_dir in dirpath for skip_dir in skip_dirs):
                    continue
                for filename in filenames:
                    if filename.startswith(f"{lang}.") and not content_exist(filenames, 'en'): 
                        relative_path = os.path.relpath(Path(dirpath) / filename, start=".")
                        yml_file.write(f"{relative_path}\n")
                        file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from {lang}")

def create_txt_from_en_to(lang):
    base_dirs = ["../../courses", "../../resources", "../../tutorials"]
    output_file = f"./translate-from-en/{lang}.txt"
    skip_dirs = ["crypto302",
                 "conference",
                 "podcasts"
                 ]
    file_written = False

    with open(output_file, "w") as yml_file:
        for base_dir in base_dirs:
            for dirpath, dirnames, filenames in os.walk(base_dir):
                if any(skip_dir in dirpath for skip_dir in skip_dirs):
                    continue
                for filename in filenames:
                    if filename.startswith(f"en.") and not content_exist(filenames, lang): 
                        relative_path = os.path.relpath(Path(dirpath) / filename, start=".")
                        yml_file.write(f"{relative_path}\n")
                        file_written = True

    if not file_written:
        os.remove(output_file)
        print(f"No need to translate from en to {lang}")

def copy_from_repo_to_LLM_Translator(lang, input_list_path, destination_base_path):
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

def copy_from_LLM_Translator_to_repo(lang, source_path):

    source_path = os.path.join('../../../LLM-Translator/outputs/', source_path)
    if not os.path.exists(source_path):
        print(f"No source directory found for language '{lang}'.")
        return

    files = os.listdir(source_path)
    for file in files:
        destination_file_path = os.path.join('../../', file.replace('_','/'))
        source_file_path = os.path.join(source_path, file)
        try:
            shutil.copy(source_file_path, destination_file_path)
            print(f"Copied '{source_file_path}' back to '{destination_file_path}'")
        except Exception as e:
            print(f"Error copying back to '{destination_file_path}': {str(e)}")


def git_commit(commit_message):
    try:
        subprocess.run(['git', 'add', '../../'], check=True)
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print("Changes committed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit changes: {e}")


def create_pull_request(target_branch, title, body=""):
    """Create a pull request to the specified target branch with a title and optional body description."""
    try:
        # Push the current branch to remote
        subprocess.run(['git', 'push', '--set-upstream', 'origin', 'HEAD'], check=True)
        # Create a pull request using hub
        subprocess.run(['hub', 'pull-request', '-b', target_branch, '-m', title, '-m', body], check=True)
        print("Pull request created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create pull request: {e}")


@redirect_output_to_file('../../../pbn-auto-translate-logs.txt')
def main():
    prepare_git_branch()
    languages = get_supported_languages()
    for lang in languages:
        create_txt_to_en_from(lang)

        translation_needed = os.path.exists(f"./translate-to-en/{lang}.txt")
        if translation_needed:
            input_list_path = f"./translate-to-en/{lang}.txt"
            destination_base_path = f"../../../LLM-Translator/inputs/pbn-from-{lang}-to-en/"
            copy_from_repo_to_LLM_Translator(lang, input_list_path, destination_base_path)

            source_path = f"pbn-from-{lang}-to-en"
            run_LLM_Translator(lang, 'en', source_path)
            print('llm translator from lang to en running')
            copy_from_LLM_Translator_to_repo(lang, source_path)

            message_commit = f"batch translation from {lang} to en"
            print(message_commit)
            git_commit(message_commit)
    for lang in languages:
        create_txt_from_en_to(lang)
        translation_needed = os.path.exists(f"./translate-from-en/{lang}.txt")
        if translation_needed:
            input_list_path = f"./translate-from-en/{lang}.txt"
            destination_base_path = f"../../../LLM-Translator/inputs/pbn-from-en-to-{lang}/"
            copy_from_repo_to_LLM_Translator('en', input_list_path, destination_base_path)

            source_path = f"pbn-from-en-to-{lang}"
            run_LLM_Translator('en', lang, source_path)
            print('llm runs from en to lang')
            copy_from_LLM_Translator_to_repo(lang, source_path)
            
            message_commit = f"batch translation from en to {lang}"
            print(message_commit)
            git_commit(message_commit)
    target_branch = 'dev'
    pr_title = '[Automated] upload batch translations'
    body = """ This PR was sent by the auto-translated script. It used LLM-Translator to translate the language-specific files in all supported languages. With the current version of this script and due to random behaviors of LLMs, there's a probability that some files did not respect PBN standard formats. If it's the case, the formatting error will be resolved before merging. """
    create_pull_request(target_branch, pr_title, body) 
    print("So far so good!")


if __name__ == "__main__":
    main()
