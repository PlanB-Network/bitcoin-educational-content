import os
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
    
def create_yml_to_en_from(lang):
    base_dirs = ["../../courses", "../../resources", "../../tutorials"]
    output_file = f"./translate-to-en/{lang}.yml"
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
        print(f"No need to translate from {lang}")


def main():
    # prepare_git_branch()
    languages = get_supported_languages()
    print(languages)
    create_yml_to_en_from("fr")
    output_file_path = "./translate-to-en/fr.yml"
    if os.path.exists(output_file_path):
        with open(output_file_path, 'r') as file:
            content = file.read()
            print(content)
    else:
        print("No need to translate from fr or no entries found in 'fr.yml'.") 

    print("So far so good!")


if __name__ == "__main__":
    main()
