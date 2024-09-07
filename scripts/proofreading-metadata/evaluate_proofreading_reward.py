import os
import inquirer
from tqdm import tqdm
from proofreading import *
from update_proofreading_metadata import *


def get_subfolder_choices(root_directory):
    subfolders = [
        dirname for dirname in os.listdir(root_directory)
        if os.path.isdir(os.path.join(root_directory, dirname)) and not dirname.startswith('.')
    ]
    return sorted(subfolders)

def has_specific_file(subfolder_path, specific_files):
    for file_name in os.listdir(subfolder_path):
        if file_name in specific_files:
            return True
    return False

def ask_for_subfolder(root_directory, specific_files):
    while True:
       subfolders = get_subfolder_choices(root_directory)
        if not subfolders:
            print(f"No subfolders found in {root_directory}.")
            return None
        question = [
            inquirer.List('subfolder',
                          message=f"Select a subfolder in {root_directory}",
                          choices=subfolders,
                          carousel=True,
                          ),
        ]
        answers = inquirer.prompt(question)
        selected_subfolder = answers['subfolder']
        selected_subfolder_path = os.path.join(root_directory, selected_subfolder)
        if has_specific_file(selected_subfolder_path, specific_files):
            print(f"The subfolder '{selected_subfolder}' contains a specific file.")
            return selected_subfolder_path
        else:
            print(f"Recursing into subfolder: {selected_subfolder}")
            return ask_for_subfolder(selected_subfolder_path, specific_files)

def select_language(content_path):
    content_languages = get_language_list_for_content(content_path)
    question = [
        inquirer.List('language_choice',
                      message="Select the language to update",
                      choices=sorted(content_languages),
                      carousel=True)
    ]
    
    selected_language = inquirer.prompt(question)['language_choice']
    print(f"You have selected: {selected_language}")
    return selected_language


def main():
    print("Let's update proofreading data!")
    root_directory = '../../'

    while True:
        selected_subfolder_path = ask_for_subfolder(root_directory, specific_files)
        if selected_subfolder_path:
            print(f"Selected subfolder: {selected_subfolder_path}")
            add_new_contribution_to(selected_subfolder_path)
        else:
            print("No valid subfolder with specific files was found.")
        
        ask_yes_no_question()
        select_language(selected_subfolder_path)
        

if __name__ == "__main__":
    main()


