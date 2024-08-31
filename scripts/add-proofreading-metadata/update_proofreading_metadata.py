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

def select_language_to_update(content_path):
    content_languages = get_language_list_for_content(content_path)
    question = [
        inquirer.List('language_choice',
                      message="Select the language to update",
                      choices=sorted(content_languages),
                      carousel=True)
    ]
    
    selected_language = inquirer.prompt(question)['language_choice']
    print(f"You selected to update the content for: {selected_language}")
    return selected_language

def add_new_contribution_to(content_path):
    selected_language = select_language_to_update(content_path)    
    file_path = get_existing_file_path(content_path, specific_files)
    data = get_yml_content(file_path)
    content_name = os.path.basename(content_path)

    question_contributor = f"Do you want to add a new contributor to {content_name} in {selected_language}?"
    new_contribution = ask_yes_no_question(question_contributor)
    print()
    if new_contribution == 'y':
        contributor_id = input("Enter the github username of the contributor: ")
        add_proofreading_contributor(data, selected_language, contributor_id) 
        update_yml_data(content_path, data)
        print(f"{contributor_id} added a new proofreader of {content_name} in {selected_language}")
        reward = get_proofreading_property(data, selected_language, 'reward')
        print(f"{contributor_id} has won {reward} sats for that proofreading")
    
    question_urgency = f"Do you want to change the urgency of the proofreading of {content_name} in {selected_language}"
    change_urgency = ask_yes_no_question(question_urgency)
    if change_urgency == 'y':
        current_urgency = get_proofreading_property(data, selected_language, 'urgency')
        print(f"Current urgency is: {current_urgency}")

        while True:
            new_urgency = input("Enter the new urgency value (integer): ")
            try:
                new_urgency = int(new_urgency)
                break  # Exit the loop if conversion to int was successful
            except ValueError:
                print("Please enter a valid integer.")
        update_proofreading_inline_property(data, selected_language, 'urgency', new_urgency)    

    update_proofreading_reward(file_path, selected_language)

    data = get_yml_content(file_path)
    reward = get_proofreading_property(data, selected_language, 'reward')
    state = get_proofreading_state(data, selected_language)
    if state < 3: 
        left = 3-state
        print(f"{content_name} requires {left} proofreading(s) in {selected_language}")
        print(f"Next reward for this proofreading is {reward} sats!")
        
    else:
        print(f"Congrats! {content_name} requires no more proofreading in {selected_language}")


    # update reward for this content for this language
    # tell the state of that proofreading language and the next reward
    # associated to it
def ask_yes_no_question(question):
    while True:
        response = input(question+" [y/n]: ").strip().lower()
        if response in ['y', 'n']:
            return response
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def update_proofreading(root_dir, specific_files):
    print('Automatic Update for Proofreading section in progress...')

    for dirpath, dirnames, filenames in os.walk(root_dir):
        
        dirnames[:] = [d for d in dirnames if d != 'docs']
        translated_content = [f for f in filenames if f in specific_files]
        
        if translated_content:
            print()
            print(f"Checking for {dirpath}")
            missing_proofreading_section = False
            yml_filepath = get_existing_file_path(dirpath, specific_files)
            print(yml_filepath)
            data = get_yml_content(yml_filepath)  
            existing_languages = get_language_list_for_content(dirpath)

            for language in existing_languages:
                language_file_yml = f'{language}.yml'
                language_file_md = f'{language}.md'

                language_file_path_yml = os.path.join(dirpath, language_file_yml)
                language_file_path_md = os.path.join(dirpath, language_file_md)
                
                if os.path.isfile(language_file_path_yml) or os.path.isfile(language_file_path_md):
                    if not check_language_existence(data, language):
                        print(f"Proofreading section missing for {language}")
                        missing_proofreading_section = True
                        # Add the proofreading section at the end of the YAML file
                        proofreading_section = (
                            f"  - language: {language}\n"
                            f"    last_contribution_date:\n"
                            f"    urgency: 1\n"
                            f"    contributors_id:\n"
                            f"    reward:\n"
                        )

                        with open(yml_filepath, 'a', encoding='utf-8') as file:
                            file.write(proofreading_section)
                        
                        print(f"Proofreading section added for {language}")
                        print()

                    current_reward = get_proofreading_property(data, language, 'reward')
                    evaluated_reward = evaluate_proofreading_reward(yml_filepath, language)
                    if current_reward != evaluated_reward:
                        update_proofreading_reward(yml_filepath, language, evaluated_reward)

            if not missing_proofreading_section:
                print(f"Everything updated in {dirpath}")

    print('Automatic update done!')


def add_new_supported_language(code_language, language_difficulty):
    try:
        # Ensure language_difficulty is a float with two decimal places
        language_difficulty = round(float(language_difficulty), 2)
    except ValueError:
        print("Language difficulty must be a numeric value.")
        return

    languages_dict = load_supported_languages()

    if code_language in languages_dict:
        print(f"{code_language} is already in the list of supported languages.")
    else:
        # Adding new entry with validated and formatted difficulty
        languages_dict[code_language] = language_difficulty
        save_supported_languages(languages_dict)
        print(f"Added {code_language} with difficulty {language_difficulty:.2f} to the list of supported languages.")

def main():
    print("Let's update proofreading data!")
    root_directory = '../../'
    while True:
        question_language = "Do you want to add a new supported language?"
        new_language = ask_yes_no_question(question_language)
        if new_language == 'y':
            code_language = input("Enter the code language:")
            language_difficulty = input(f"Enter the difficulty of {code_language}:")
            add_new_supported_language(code_language, language_difficulty)
        else:
            break

    update_proofreading(root_directory, specific_files)
    # while True:
    #     question = "Do you want to modify a proofreading section of a content? (new contributor or urgency change)"
    #     user_response = ask_yes_no_question(question)
    #     if user_response == 'y':
    #         selected_subfolder_path = ask_for_subfolder(root_directory, specific_files)
    #         if selected_subfolder_path:
    #             print(f"Selected subfolder: {selected_subfolder_path}")
    #             add_new_contribution_to(selected_subfolder_path)
    #         else:
    #             print("No valid subfolder with specific files was found.")
    #     elif user_response == 'n':
    #         print("Exiting the contribution loop. No more contributions to add.")
    #         break

if __name__ == "__main__":
    main()

