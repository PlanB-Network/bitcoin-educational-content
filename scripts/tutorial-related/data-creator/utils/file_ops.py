import os
import uuid
import datetime

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_tutorial_files(base, section_name, tutorial_name, language_code, project_id, tags, category_value, level_value, professor_id, contributor_id):
    """
    Create the necessary files for a new tutorial.
    """
    tutorial_path = os.path.join(base, section_name, tutorial_name)
    create_directory(tutorial_path)
    assets_path = os.path.join(tutorial_path, "assets")
    create_directory(assets_path)
    assets_lang_path = os.path.join(assets_path, language_code)
    create_directory(assets_lang_path)
    
    # Create markdown file
    md_filename = f"{language_code}.md"
    md_content = """---
name: 
description: 
---
![cover](assets/cover.webp)
"""
    write_file(os.path.join(tutorial_path, md_filename), md_content)
    
    # Create YAML file with tutorial metadata
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
