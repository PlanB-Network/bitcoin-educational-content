import os

def rename_and_modify_files(directory):
    # Language to code mapping
    language_codes = {
        'English': 'en',
        'Spanish': 'es',
        'German': 'de',
        'Italian': 'it',
        'Portuguese': 'pt'
    }

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            new_filename = None
            # Determine the new file name based on language suffix
            for language, code in language_codes.items():
                if filename.endswith(f'_{language}.md'):
                    new_filename = f'{code}.md'
                    break

            if new_filename:
                new_path = os.path.join(directory, new_filename)
                old_path = os.path.join(directory, filename)

                # Read the old file's content and replace '/fr/' with the new code
                with open(old_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                new_content = content.replace('/fr/', f'/{new_filename[:-3]}/')

                # Write the modified content to the new file
                with open(new_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)

                # Remove the old file if it's not the same as new file
                if new_path != old_path:
                    os.remove(old_path)
                print(f"Renamed and modified '{filename}' to '{new_filename}'")


directory_path = '../../LLM-Translator/output/test/'
rename_and_modify_files(directory_path)

