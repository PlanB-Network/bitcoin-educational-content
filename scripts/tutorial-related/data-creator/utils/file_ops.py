import os
import shutil
import uuid
from PIL import Image
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
        f"professor_id: {professor_id}",
        "",
        "# Proofreading metadata",
        "",
        f"original_language: {language_code}",
        "proofreading:",
        f"  - language: {language_code}",
        f"    last_contribution_date: {current_date}",
        "    urgency: 1",
        "    contributor_names:",
        f"      - {contributor_id}",
        "    reward: 0"
    ])
    yaml_content = "\n".join(lines)
    write_file(os.path.join(tutorial_path, "tutorial.yml"), yaml_content)
    
    return tutorial_path

def create_professor_yaml(full_name, website=None, twitter=None, lightning=None, tags=None):
    prof_uuid = str(uuid.uuid4())
    lines = [
        f"id: {prof_uuid}",
        f"name: {full_name}",
        "",
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
    lines.append("contributor_names:")
    lines.append(f"  - {global_contributor}")
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
    lines.append("    contributor_names:")
    lines.append(f"      - {global_contributor}")
    lines.append("    reward: 0")
    lines.append("")
    return "\n".join(lines)

def create_project_language_yaml(language_code, description, professor_global):
    lines = [
        f"description: |",
        f"  {description}",
    ]
    return "\n".join(lines)
