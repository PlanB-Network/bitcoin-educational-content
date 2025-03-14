import os
import shutil
import uuid
from PIL import Image
import random
import re
import datetime

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def process_profile_image(source_path, dest_path):
    """
    Convert and copy the profile image to WEBP.
    """
    if source_path and os.path.exists(source_path):
        _, ext = os.path.splitext(source_path)
        ext = ext.lower()
        if ext in [".png", ".jpg", ".jpeg"]:
            img = Image.open(source_path)
            img.save(dest_path, "WEBP")
        else:
            shutil.copy(source_path, dest_path)

def generate_random_contributor_id():
    from utils.constants import BIP39_WORDS
    words = random.sample(BIP39_WORDS, 2)
    return f"{words[0]}-{words[1]}"

def check_contributor_id(base_path, contributor_id):
    """
    Verify that the contributor ID consists of two BIP39 words and is unique.
    """
    parts = contributor_id.split('-')
    from utils.constants import BIP39_WORDS
    if len(parts) != 2:
        return False, "Contributor ID must consist of two words separated by a hyphen."
    for word in parts:
        if word not in BIP39_WORDS:
            return False, f"The word '{word}' is not in the BIP39 list."
    professors_dir = os.path.join(base_path, "professors")
    if os.path.exists(professors_dir):
        for folder in os.listdir(professors_dir):
            folder_path = os.path.join(professors_dir, folder)
            if os.path.isdir(folder_path):
                yaml_path = os.path.join(folder_path, "professor.yml")
                if os.path.exists(yaml_path):
                    with open(yaml_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    match = re.search(r'^contributor_id:\s*(\S+)', content, re.MULTILINE)
                    if match:
                        existing_id = match.group(1).strip()
                        if existing_id == contributor_id:
                            return False, f"Contributor ID '{contributor_id}' is already used."
    return True, ""

def create_tutorial_files(base, section_name, tutorial_name, language_code, project_id, tags, category_value, level_value, professor_id, contributor_id):
    """
    Create files required for a new tutorial.
    """
    tutorial_path = os.path.join(base, "tutorials", section_name, tutorial_name)
    create_directory(tutorial_path)
    assets_path = os.path.join(tutorial_path, "assets")
    create_directory(assets_path)
    assets_lang_path = os.path.join(assets_path, language_code)
    create_directory(assets_lang_path)
    
    md_filename = f"{language_code}.md"
    md_content = """---
name: 
description: 
---
![cover](assets/cover.webp)
"""
    write_file(os.path.join(tutorial_path, md_filename), md_content)
    
    uuid_value = str(uuid.uuid4())
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    lines = [
        f"id: {uuid_value}",
        "",
        f"project_id: {project_id}",
        "",
        "tags:"
    ]
    for tag in tags:
        lines.append(f"  - {tag}")
    lines.extend([
        "",
        f"category: {category_value}",
        "",
        f"level: {level_value}",
        "",
        "credits:",
        f"  professor: {professor_id}",
        "",
        "# Proofreading metadata",
        "",
        f"original_language: {language_code}",
        "proofreading:",
        f"  - language: {language_code}",
        f"    last_contribution_date: {current_date}",
        "    urgency: 1",
        "    contributors_id:",
        f"      - {contributor_id}",
        "    reward: 0"
    ])
    yaml_content = "\n".join(lines)
    write_file(os.path.join(tutorial_path, "tutorial.yml"), yaml_content)
    
    return tutorial_path

def create_professor_yaml(full_name, contributor_id, website=None, twitter=None, lightning=None, tags=None):
    """
    Generate YAML content for a new professor.
    """
    prof_uuid = str(uuid.uuid4())
    lines = [
        f"id: {prof_uuid}",
        f"name: {full_name}",
        "",
        f"contributor_id: {contributor_id}",
        ""
    ]
    if website or twitter:
        lines.append("links:")
        if website:
            lines.append(f"  website: {website}")
        if twitter:
            lines.append(f"  twitter: {twitter}")
        lines.append("")
    if lightning:
        lines.append("tips:")
        lines.append(f"  lightning_address: {lightning}")
        lines.append("")
    if tags:
        lines.append("tags:")
        for t in tags:
            lines.append(f"  - {t}")
        lines.append("")
    return "\n".join(lines)

def create_language_yaml(language_code, bio, short_bio):
    """
    Generate YAML content for language-specific project information.
    """
    lines = [
        "bio: |",
        f"  {bio}",
        "",
        "short_bio:" + (f" {short_bio}" if short_bio else "")
    ]
    return "\n".join(lines)

def create_project_yaml(project_uuid, project_name, website, twitter, category, tags, language_code, current_date, global_contributor):
    """
    Generate the content for project.yml.
    'global_contributor' is the GitHub Contributor's ID from HOME.
    """
    lines = [
        f"id: {project_uuid}",
        f"name: {project_name}",
        "",
    ]
    if website or twitter:
        lines.append("links:")
        if website:
            lines.append(f"  website: {website}")
        if twitter:
            lines.append(f"  twitter: {twitter}")
        lines.append("")
    lines.append(f"category: {category}")
    lines.append("")
    lines.append("tags:")
    for t in tags:
        lines.append(f"  - {t}")
    lines.append("")
    lines.append("# Proofreading metadata")
    lines.append(f"original_language: {language_code}")
    lines.append("proofreading:")
    lines.append(f"  - language: {language_code}")
    lines.append(f"    last_contribution_date: {current_date}")
    lines.append("    urgency: 1")
    lines.append("    contributors_id:")
    lines.append(f"      - {global_contributor}")
    lines.append("    reward: 0")
    lines.append("")
    return "\n".join(lines)

def create_project_language_yaml(language_code, description, professor_global):
    """
    Generate the content for the language YAML file for a project.
    'description' is mandatory and 'professor_global' is the PBN Professor's ID from HOME.
    """
    lines = [
        f"description: |",
        f"  {description}",
        "contributors:",
        f"  - {professor_global}"
    ]
    return "\n".join(lines)
