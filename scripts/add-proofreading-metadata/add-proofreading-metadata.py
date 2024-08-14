import os

# List of languages you might include in the YAML files
languages = ["fr", "en", "cs", "de", "es", "fi", "it", "ja", "pt", "vi", "ru"]
languages.sort()  # Sorts the language list alphabetically

# Part of the template that is always added
base_template = """
# Proofreading metadata
original:
translation_review:"""
def template_language_specific(lang):
    content = f"""
  - {lang}
      - last_reviewed: 
      - next_review_urgency: 
      - reviewer_id: 
      - reward: """
    return content

def append_to_yaml(file_path, content):
    """Append the specified content to a YAML file."""
    with open(file_path, 'a') as file:
        file.write(content)

def check_language_files(root, languages):
    """Check each language to see if there are files starting with '{lang}.'"""
    lang_presence = {}
    for lang in languages:
        lang_presence[lang] = any(f.startswith(lang + ".") for f in os.listdir(root) if os.path.isfile(os.path.join(root, f)))
    return lang_presence


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


def process_directory(root_dir, subfolders):
    """Process each YAML file in the specified subdirectories."""
    for subfolder in subfolders:
        full_path = os.path.join(root_dir, subfolder)
        if os.path.exists(full_path):
            for root, dirs, files in os.walk(full_path):
                for file in files:
                    if file in specific_files:
                        file_path = os.path.join(root, file)
                        lang_presence = check_language_files(root, languages)
                        content_to_append = base_template
                        # Check each language and append if relevant files are found
                        for lang in languages:
                            print(lang_presence[lang])
                            if lang_presence[lang]:
                                content_to_append += f"""
  - {lang}
      - last_reviewed: 
      - next_review_urgency: 
      - reviewer_id: 
      - reward: """
                        append_to_yaml(file_path, content_to_append)
                        print(f"Processed {file_path}")
        else:
            print(f"Subfolder {subfolder} does not exist in the root directory.")

# Root directory for the specific subfolders
root_directory = '../../'
# root_directory = '../../test-bec/'
subfolders = ["courses", "tutorials", "resources", "professors"]

# Call the function with the list of subfolders to process
process_directory(root_directory, subfolders)

