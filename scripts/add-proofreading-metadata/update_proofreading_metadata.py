import os
import inquirer
from proofreading import *

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
                          message=f"Select a subfolder in {root_directory}:",
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

def select_language_to_update(content_path):
    content_languages = get_language_list_for_content(content_path)
    question = [
        inquirer.List('language_choice',
                      message="Select the language to update:",
                      choices=sorted(content_languages),
                      carousel=True)
    ]
    
    selected_language = inquirer.prompt(question)['language_choice']
    print(f"You selected to update the content for: {selected_language}")
    return selected_language

def update_content_proofreading(content_path):
    selected_language = select_language_to_update(content_path)    
    # ask if they want to add contributor
      # if so add new contributor
    # ask if they want to update the urgency for next proofreading 
      # print current urgency before and if they want update it
    # update reward for this content for this language
    # tell the state of that proofreading language and the next reward
    # associated to it


def main():
    print("Let's update proofreading data!")
    
    root_directory = '../../'
    specific_files = {
        "course.yml",
        "question.yml",
        "tutorial.yml",
        "book.yml",
        "word.yml",
        "bet.yml",
        "builder.yml",
        "conference.yml"
    }
    
    selected_subfolder_path = ask_for_subfolder(root_directory, specific_files)
    
    if selected_subfolder_path:
        print(f"Final selected subfolder: {selected_subfolder_path}")
    else:
        print("No valid subfolder with specific files was found.")
    update_content_proofreading(selected_subfolder_path)

    # update the proofreading section in case of new translation
    # ask if a new proofreading contribution has to be added
    # if so ask for which content 
    # then for which languaguage
    # ask if another contribution need to be add (loop 2 steps ahead)
    # 
if __name__ == "__main__":
    main()

