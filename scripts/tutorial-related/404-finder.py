import os
import re
import yaml
from urllib.parse import urlparse
import glob

base_dir = input("Enter the base directory path to DATA repo: ").strip().strip('"').strip("'")
report_path = os.path.join(base_dir, "broken_links_report.md")

link_pattern = re.compile(r'https?://[^\s)]+', re.IGNORECASE)

allowed_domain = "planb.network"

broken_links = []

uuid_pattern = re.compile(
    r'^(?P<name>.+)-(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$'
)

def check_tutorial_link(link, source_file):
    parsed = urlparse(link)
    if parsed.netloc != allowed_domain:
        return

    path_parts = [p for p in parsed.path.split('/') if p]

    if 'tutorials' not in path_parts:
        return

    t_index = path_parts.index('tutorials')
    segments_after = len(path_parts) - (t_index + 1)

    if segments_after == 0:
        return

    if segments_after == 1:
        return

    if segments_after == 2:
        category = path_parts[t_index + 1]
        something = path_parts[t_index + 2]

        m = uuid_pattern.match(something)
        if m:
            tutorial_name = m.group('name')
            tutorial_uuid = m.group('uuid')

            tutorial_dir = os.path.join(base_dir, "tutorials", category, tutorial_name)
            if not os.path.isdir(tutorial_dir):
                broken_links.append((link, source_file, f"Tutorial directory not found: {tutorial_dir}"))
                return

            tutorial_yml_path = os.path.join(tutorial_dir, "tutorial.yml")
            if not os.path.isfile(tutorial_yml_path):
                broken_links.append((link, source_file, f"tutorial.yml file not found: {tutorial_yml_path}"))
                return

            with open(tutorial_yml_path, 'r', encoding='utf-8') as yf:
                try:
                    data = yaml.safe_load(yf)
                except yaml.YAMLError:
                    broken_links.append((link, source_file, f"Unable to read YAML file: {tutorial_yml_path}"))
                    return

            if 'id' not in data or data['id'] != tutorial_uuid:
                broken_links.append((link, source_file, f"UUID does not match (URL: {tutorial_uuid}, YAML: {data.get('id')})"))
                return

            if 'category' not in data:
                broken_links.append((link, source_file, "No category defined in YAML"))
                return
            broken_links.append((link, source_file, "Incomplete link (missing subcategory)"))
        else:
            broken_links.append((link, source_file, "Incomplete link (missing UUID)"))
        return

    category = path_parts[t_index + 1]
    subcategory = path_parts[t_index + 2]
    last_part = path_parts[t_index + 3]

    m = uuid_pattern.match(last_part)
    if not m:
        broken_links.append((link, source_file, "Unable to parse tutorial name and UUID"))
        return

    tutorial_name = m.group('name')
    tutorial_uuid = m.group('uuid')

    tutorial_dir = os.path.join(base_dir, "tutorials", category, tutorial_name)
    if not os.path.isdir(tutorial_dir):
        broken_links.append((link, source_file, f"Tutorial directory not found: {tutorial_dir}"))
        return

    tutorial_yml_path = os.path.join(tutorial_dir, "tutorial.yml")
    if not os.path.isfile(tutorial_yml_path):
        broken_links.append((link, source_file, f"tutorial.yml file not found: {tutorial_yml_path}"))
        return

    with open(tutorial_yml_path, 'r', encoding='utf-8') as yf:
        try:
            data = yaml.safe_load(yf)
        except yaml.YAMLError:
            broken_links.append((link, source_file, f"Unable to read YAML file: {tutorial_yml_path}"))
            return

    if 'id' not in data or data['id'] != tutorial_uuid:
        broken_links.append((link, source_file, f"UUID does not match (URL: {tutorial_uuid}, YAML: {data.get('id')})"))
        return

    if 'category' not in data or data['category'] != subcategory:
        broken_links.append((link, source_file, f"Subcategory does not match (URL: {subcategory}, YAML: {data.get('category')})"))
        return

for md_file in glob.glob(os.path.join(base_dir, '**', '*.md'), recursive=True):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    links = link_pattern.findall(content)
    for link in links:
        if "tutorials" in link:
            check_tutorial_link(link, md_file)

print(f"Broken links: {len(broken_links)}")

with open(report_path, 'w', encoding='utf-8') as rf:
    rf.write("# Broken Links Report\n\n")
    if not broken_links:
        rf.write("No broken links were found.\n")
    else:
        rf.write("| Broken Link | Source File | Reason |\n")
        rf.write("|-------------|-------------|--------|\n")
        for b_link, b_file, b_reason in broken_links:
            rf.write(f"| {b_link} | {b_file} | {b_reason} |\n")
