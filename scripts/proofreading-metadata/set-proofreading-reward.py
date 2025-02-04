import os
from math import floor
from ruamel.yaml import YAML

BASE_FEE = .1
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

def compute_reward(words, difficulty_factor, language_factor, urgency, base_fee, proofread_iteration):
    euros_per_word = 0.0006
    reward = (urgency * (euros_per_word * words * difficulty_factor * language_factor) + base_fee) * 2**(-proofread_iteration)
    reward = round(reward, 2)
    return reward

def update_reward_property(file_path, language, reward):
    data = get_yml_content(file_path)
    # Update the reward property for the specified language
    data['proofreading'][language]['reward'] = reward
    
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def get_proofread_iteration(reviewers_id):
    if reviewers_id == None:
        proofread_iteration = 0
    else:
        proofread_iteration = len(reviewers_id)
    return proofread_iteration

def get_words(file_path):
    data = get_yml_content(file_path)
    original = get_orignal(data)
    if not original:
        raise ValueError(f"The 'original' property is not found in {file_path}.")
    
    directory = os.path.dirname(file_path)
    md_file = os.path.join(directory, f"{original}.md")
    yml_file = os.path.join(directory, f"{original}.yml")
    
    if os.path.exists(md_file):
        file_to_check = md_file
    elif os.path.exists(yml_file):
        file_to_check = yml_file
    else:
        raise FileNotFoundError(f"Neither {md_file} nor {yml_file} exists.")
    
    with open(file_to_check, 'r', encoding='utf-8') as file:
        content = file.read()
        word_count = len(content.split())
    
    return word_count

def get_orignal(data):
    original = data.get('original_language')
    return original


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

def get_yml_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    return data

    
    

def is_original(data, language)
    return data['original_language'] == language

def get_data_languages(data):
    data_languages = list(data['proofreading'].keys())
    return data_languages


root_directory = '../../'
subfolders = ["courses", "tutorials", "resources"]

print("let's start the reward computation!")
for subfolder in subfolders:
    full_path = os.path.join(root_directory, subfolder)
    if os.path.exists(full_path):
        for root, dirs, files in os.walk(full_path):
            for file in files:
                if file in specific_files:
                    file_path = os.path.join(root, file)
                    # print(file_path)
                    data = get_yml_content(file_path)
                    if data.get('proofreading'):
                        words = get_words(file_path)
                        difficulty_factor = get_difficulty_factor(data)
                        data_languages = get_data_languages(data)
                        for language in data_languages:
                            language_factor = language_factors[language]
                            reviewers_id = data['proofreading'][language]['contributors_id']
                            proofread_iteration = get_proofread_iteration(reviewers_id)
                            urgency = data['proofreading'][language]['urgency']
                            original = is_original(data, language)
                            reward = compute_reward(words, difficulty_factor, language_factor, urgency, BASE_FEE, proofread_iteration, original)
                            update_reward_property(file_path, language, reward)
                            # print(f"{file_path} reward updated in {language} to {reward}")
    print(f"rewards set for {subfolder}")
print("reward update process finished!")


