import os
from proofreading import *

specific_files = {"course.yml",
                  "question.yml",
                  "tutorial.yml",
                  "book.yml",
                  # "podcast.yml",
                  "word.yml",
                  "bet.yml",
                  "builder.yml",
                  "conference.yml"
                  }


root_directory = '../../'
subfolders = ["courses", "tutorials", "resources"]
subfolders = ["courses/btc101/"]

test_pathfile = "../../courses/btc101/course.yml"
# print(file_path)
data = get_yml_content(test_pathfile)
if data.get('proofreading'):
    words = get_words(test_pathfile)
    difficulty_factor = get_difficulty_factor(data)
    data_languages = get_data_languages(data)
    for proofreading_item in data_languages:
        if proofreading_item["language"] == "vi":
            print(proofreading_item["contributors_id"])
            print(proofreading_item["reward"])
            proofreading_item["reward"] = 100000
            print(proofreading_item["reward"])

# print("let's start the reward computation!")
# for subfolder in subfolders:
#     full_path = os.path.join(root_directory, subfolder)
#     if os.path.exists(full_path):
#         for root, dirs, files in os.walk(full_path):
#             for file in files:
#                 if file in specific_files:
#                     file_path = os.path.join(root, file)
#                     # print(file_path)
#                     data = get_yml_content(file_path)
#                     if data.get('proofreading'):
#                         words = get_words(file_path)
#                         difficulty_factor = get_difficulty_factor(data)
#                         data_languages = get_data_languages(data)
#                         print(data_languages)
