import os
import yaml
from collections import defaultdict

# Initialize a dictionary to store tags and their occurrence count
tag_counts = defaultdict(int)

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk("."):
    for file in files:
        # Check if the file is a .yml file
        if file.endswith(".yml"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as ymlfile:
                try:
                    # Load the content of the .yml file
                    content = yaml.safe_load(ymlfile)
                    if content and 'tags' in content:
                        # Increment the count for each tag
                        for tag in content['tags']:
                            tag_counts[tag] += 1
                except yaml.YAMLError as exc:
                    print(f"Error parsing YAML file: {file_path}", exc)

# Sort tags alphabetically and then by their occurrence count
sorted_tags_alphabetically = sorted(tag_counts.items())
sorted_tags_by_occurrence = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)

# Write the sorted tags alphabetically to tags.md
with open("planb-tags.md", "w") as mdfile:
    for tag, count in sorted_tags_alphabetically:
        mdfile.write(f"- {tag}: {count}\n")

# Write the sorted tags by occurrence to tag-occurrence-sorted.md
with open("planb-tag-occurrence-sorted.md", "w") as mdfile_occ:
    for tag, count in sorted_tags_by_occurrence:
        mdfile_occ.write(f"- {tag}: {count}\n")

print("planb-tags.md file has been created with sorted tags alphabetically.")
print("planb-tag-occurrence-sorted.md file has been created with tags sorted by their occurrences.")

