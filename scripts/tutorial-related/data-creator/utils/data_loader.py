import os
import re

def load_allowed_tags(base_path):
    """
    Load allowed tags from the markdown file located at 'docs/50-planb-tags.md'
    relative to the repository root.
    """
    tags = []
    if base_path:
        file_path = os.path.join(base_path, "docs", "50-planb-tags.md")
    else:
        file_path = os.path.join("docs", "50-planb-tags.md")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^\s*\d+\.\s+(.+?):", line)
                if m:
                    tags.append(m.group(1).strip())
    return tags

def load_all_builders(base_path):
    """
    Load all builders (projects) from the 'resources/projects' directory relative to the repository root.
    Returns a dictionary mapping builder names to their IDs.
    """
    builders = {}
    if not base_path:
        return builders
    builders_dir = os.path.join(base_path, "resources", "projects")
    if not os.path.exists(builders_dir):
        return builders
    for d in os.listdir(builders_dir):
        sub_dir = os.path.join(builders_dir, d)
        if os.path.isdir(sub_dir):
            builder_file = os.path.join(sub_dir, "project.yml")
            if os.path.exists(builder_file):
                with open(builder_file, "r", encoding="utf-8") as bf:
                    lines = bf.readlines()
                b_id = None
                b_name = None
                for line in lines:
                    if line.startswith("id:"):
                        b_id = line.split(":", 1)[1].strip()
                    elif line.startswith("name:"):
                        b_name = line.split(":", 1)[1].strip()
                if b_id and b_name:
                    builders[b_name] = b_id
    return builders
