import os
import shutil

# Define the origin and destination directory paths
script_directory = os.path.dirname(os.path.abspath(__file__))
origin_path = os.path.join(script_directory, './../../sovereign-university-data/')
destination_path = os.path.join(script_directory, '../../LLM-Translator/inputs/planb-content/')


# Ensure the destination directory exists
os.makedirs(destination_path, exist_ok=True)

# Define the subfolders and their corresponding file types
subfolders = {
    'courses': 'en.md',
    'tutorials': 'en.md',
    'resources': 'en.yml',
    'professors': 'en.yml',
}

# Initialize counters for files and words
file_counts = {key: 0 for key in subfolders.keys()}
word_counts = {key: 0 for key in subfolders.keys()}
total_files = 0
total_words = 0

# Function to process each subfolder
def process_subfolder(subfolder, file_type):
    global total_files, total_words
    path = os.path.join(origin_path, subfolder)
    print(path)
    for root, dirs, files in os.walk(path):
        print(root)
        for file in files:
            if file.endswith(file_type):
                src_file_path = os.path.join(root, file)
                # Construct the new filename and its path
                new_filename = root.replace(origin_path, '').replace(os.sep, '_') + "_English" + os.path.splitext(file)[1]
                dst_file_path = os.path.join(destination_path, new_filename)
                # Copy and rename the file
                shutil.copy2(src_file_path, dst_file_path)
                file_counts[subfolder] += 1
                total_files += 1
                # Count the words in the current file
                with open(src_file_path, 'r', encoding='utf-8') as file:
                    words = file.read().split()
                    word_counts[subfolder] += len(words)
                    total_words += len(words)

# Process each subfolder
for subfolder, file_type in subfolders.items():
    process_subfolder(subfolder, file_type)

# Output the number of each content type, the total number of files, and word counts
for subfolder in subfolders.keys():
    print(f"{subfolder}: {file_counts[subfolder]} files, {word_counts[subfolder]} words")
print(f"Total files: {total_files}, Total words: {total_words}")

