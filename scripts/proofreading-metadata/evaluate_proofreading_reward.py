import os
import inquirer
from tqdm import tqdm
from proofreading import *
from update_proofreading_metadata import *


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
        question = "Do you want to know the proofreading reward of a content? "
        user_response = ask_yes_no_question(question)
        if user_response == 'y':
            selected_subfolder_path = ask_for_subfolder(root_directory, specific_files)
            if selected_subfolder_path:
                print(f"Selected subfolder: {selected_subfolder_path}")
                
                file_path = get_existing_file_path(selected_subfolder_path,
                                                   specific_files) 
                content_name = os.path.basename(selected_subfolder_path)
                data = get_yml_content(file_path)
                custom_language_question = "Do you want to evaluate for custom language factors?"
                custom_language = ask_yes_no_question(custom_language_question)
                if custom_language == 'y':
                    selected_language = "Custom language"
                    language_factor = float(input("What's the language factor? "))
                    urgency = float(input("What's the urgency? "))

                    words = get_words(file_path)
                    difficulty_factor = get_difficulty_factor(data)


                    proofread_iteration = 0
                    reward = compute_reward(words, difficulty_factor, language_factor, urgency, BASE_FEE, proofread_iteration)
                    
                else:
                    selected_language = select_language(selected_subfolder_path)
                    proofread_iteration = get_proofreading_state(data, selected_language)  
                    reward = evaluate_proofreading_reward(file_path, selected_language)
                print()
                print(f"For {content_name}:")
                print(f"The proofreading reward is: {reward} sats")
                left = 3 - proofread_iteration
                print(f"{left} proofreading(s) are/is missing for {selected_language}")
                print()

                    
            else:
                print("No valid subfolder with specific files was found.")
        elif user_response == 'n':
            break
        
        
            
        

if __name__ == "__main__":
    main()


