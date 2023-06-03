import os
import yaml

def process_book_yaml(file_path):
    """
    Process a book.yaml file:
    - Look for lines that start with "-"
    - Add a double space to these lines
    """

    with open(file_path, 'r') as f:
        lines = f.readlines()

    lines = ['  ' + line if line.startswith('-') else line for line in lines]

    with open(file_path, 'w') as f:
        f.writelines(lines)


def process_language_file(folder_path, language_code):
    """
    Process a {language_code}.yml file according to the provided instructions.
    """

    no_pub_date = []
    file_path = os.path.join(folder_path, f'{language_code}.yml')

    if not os.path.exists(file_path):
        return no_pub_date

    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    with open('tmp.yml', 'w') as tmp:
        title = data.get('title', 'N/A')
        tmp.write(f'title: "{title}"\n')

        publication_year = data.get('publication_year')
        if publication_year:
            tmp.write(f"publication_year: {publication_year}\n")
        else:
            tmp.write("publication_year:\n")
            no_pub_date.append(title)

        cover = data.get('cover')
        if cover:
            tmp.write(f"cover: {cover}\n")
        else:
            # Check if there's a file named "cover_{language_code}.jpeg" in the assets folder
            assets_folder = os.path.join(folder_path, 'assets')
            cover_file = f"cover_{language_code}.jpeg"
            if cover_file in os.listdir(assets_folder):
                tmp.write(f"cover: {cover_file}\n")
            else:
                tmp.write("cover:\n")

        original = data.get('original', 'N/A')
        tmp.write(f"original: {original}\n")

        description = data.get('description', 'N/A').strip().replace('\n', ' ').replace('  ', ' ')
        tmp.write("description: |\n")
        tmp.write(f"  {description}\n")

        tmp.write("contributors:\n")
        tmp.write("  - rabbit-hole\n")

    os.replace('tmp.yml', file_path)

    return no_pub_date

def update_pub_year(folder_path, language_code, title):
    """
    Function to update the publication year of a book by asking for input.
    """

    # Ask the user for the publication year
    print(f"Please enter the publication year for the book '{title}' in {language_code}: ")
    publication_year = input()

    file_path = os.path.join(folder_path, f'{language_code}.yml')

    # Open the yaml file and load its data
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    # Update the publication year
    data['publication_year'] = publication_year

    # Write the data back to the file
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


def main():
    """
    Main function to traverse each directory under "../resources/books/"
    """

    base_dir = "../resources/books/"
    language_codes = ["fr", "en"]  # Add more language codes if necessary

    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)

        if os.path.isdir(folder_path):
            # Process book.yaml
            book_yaml_path = os.path.join(folder_path, 'book.yaml')
            if os.path.exists(book_yaml_path):
                process_book_yaml(book_yaml_path)

            # Process {language_code}.yml for each language
            for language_code in language_codes:
                no_pub_date_books = process_language_file(folder_path, language_code)

                # For each book without a publication date, ask for the year and update it
                for book in no_pub_date_books:
                    update_pub_year(folder_path, language_code, book)

if __name__ == "__main__":
    main()
