import os
from proofreading import * 

def ask_which_content_type(specific_files):
    content_types = [file_name.replace('.yml', '') for file_name in specific_files]

    print("Please choose a content type by entering the corresponding number:")
    for index, content_type in enumerate(content_types, start=1):
        print(f"{index}. {content_type}")

    while True:
        try:
            choice = input("Enter the number of your choice: ")
            choice = int(choice)
            if 1 <= choice <= len(content_types):
                selected_content_type = content_types[choice - 1]
                print(f"You selected: {selected_content_type}")
                return selected_content_type
            else:
                print("Please enter a valid number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_folder_content(subfolders_path, selected_content_type):
    
# Example usage
selected_content_type = ask_which_content_type(specific_files)
