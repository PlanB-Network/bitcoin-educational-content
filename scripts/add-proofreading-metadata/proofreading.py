import os
from math import floor
from ruamel.yaml import YAML
from datetime import date

BASE_FEE = 2500
yaml = YAML()
yaml.preserve_quotes = True

specific_files = {"course.yml",
def load_supported_languages():
    with open('./supported_languages.yml', 'r') as file:
        languages_dict = yaml.load(file)
    return languages_dict

def get_languages_list(languages_dict):
    return list(languages_dict.keys())


def load_difficulty_dict():
    with open('./content_difficulty.yml', 'r') as file:
        difficulty_dict = yaml.load(file)
    return difficulty_dict


def compute_reward(words, difficulty_factor, language_factor, urgency, base_fee, proofread_iteration):
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
        difficulty_factors = load_difficulty_dict()
        difficulty_factor = difficulty_factors[level]
    return difficulty_factor 

def is_from_glossary(data):
    is_term = data.get('en_word')
    if not is_term:
        glossary = False
    else:
        glossary = True
    return glossary

def get_proofreading_data(data):
    proofreading_data = list(data['proofreading'])
    return proofreading_data

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

def update_proofreading_inline_property(data, language, property_name, property_value):
    # TODO: add check for type of input depending of the property name
    # date or interger
    for entry in data['proofreading']:
        if entry['language'] == language:
            entry[property_name] = property_value
            break

def update_yml_data(file_path, data):
    current_data = get_yml_content(file_path)
    current_data.update(data)
    with open(file_path, 'w') as file:
        yaml.dump(current_data, file)

def get_proofreading_property(data, language, property_name):
    for entry in data['proofreading']:
        if entry['language'] == language:
            return entry[property_name]
    
def get_proofreading_state(data, language):
    contributors_id = get_proofreading_property(data, language, 'contributors_id')
    if contributors_id == None:
        return 0
    else:
        return round(len(contributors_id)/3, 2)
  
def add_proofreading_contributor(data, language, contributor_id):
    for entry in data['proofreading']:
        if entry['language'] == language:
            if entry['contributors_id'] is None:
                entry['contributors_id'] = []

            entry['contributors_id'].append(contributor_id)
            print('added')
            break
    

