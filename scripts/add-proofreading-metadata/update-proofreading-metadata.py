import os
from math import floor
from ruamel.yaml import YAML

BASE_FEE = 2500
yaml = YAML()
yaml.preserve_quotes = True

language_factors = {
    'en': 1.00,  # English
    'fr': 1.00,  # French
    'de': 1.00,  # German
    'es': 1.50,  # Spanish
    'it': 1.50,  # Italian
    'cs': 2.00,  # Czech
    'vi': 3.00,  # Vietnamese
    'ja': 3.00,  # Japanese
    'pt': 1.00,  # Portuguese
    'ru': 2.00,  # Russian
    'fi': 2.00   # Finnish
}
languages = list(language_factors.keys())

# Dictionary mapping difficulty levels to their difficulty factors
difficulty_factors = {
    'beginner': 1,
    'intermediate': 2,
    'advanced': 3,
    'wizard': 4
}


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


def compute_reward(words, difficulty_factor, language_factor, urgency, base_fee, proofread_iteration, original):
    reward = (urgency * (words * difficulty_factor * language_factor * 2**(-proofread_iteration)) + base_fee)
    reward = floor(reward)
    return reward

def get_yml_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    return data

def get_difficulty_factor(data, is_from_glossary=False):
    level = data.get('level')

    if not level:
        # for all content without the mention of level
        # ie. all resources except those from glossary
        if is_from_glossary:
            difficulty_factor = 3.00
        else:
            difficulty_factor = 1.00
    else:
        difficulty_factor = difficulty_factors[level]
    return difficulty_factor 

def is_from_glossary(data):
    is_term = data.get('en_word')
    if not is_term:
        glossary = False
    else:
        glossary = True
    return glossary

def get_data_languages(data):
    data_languages = list(data['proofreading'])
    return data_languages

def get_words(file_path):
    data = get_yml_content(file_path)
    original = get_orignal(data)
    if not original:
        raise ValueError(f"The 'original' property is not found in {file_path}.")

def get_orignal(data):
    original = data.get('original_language')
    return original

def update_reward_property(file_path, language, reward):
    data = get_yml_content(file_path)
    ## TODO: write modification logic   
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

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
