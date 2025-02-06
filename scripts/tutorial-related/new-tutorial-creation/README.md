This Python script runs a GUI where the tutorial writer can easily select the parameters for a new tutorial and then automatically generate all the required folders and files, allowing him to focus solely on what matters: writing the tutorial.

## Features

- Allows easy customization of the metadata for the new tutorial.
- Automatically generates `tutorial.yml` and `.md` files with a new UUID.
- Creates the correct folder structure automatically.
- Saves recurring inputs (local path, language, GitHub ID, professor ID) in a JSON file so you don’t need to re-enter them next time.
- **Note:** The builder's information is now handled differently. Instead of entering a builder's name, you must enter the builder's **Project ID** (UUID). The script will verify this UUID in the `resources/builders` folder and, if found, display the builder’s name for confirmation.
- From now on, there is a function to search for the builder by name and automatically return the correct `projectId`.
- A modern GUI built with CustomTkinter.

I have integrated the `appdirs` library to manage user-specific configuration. In practice, the JSON settings file (which stores recurring inputs like your local path, language, GitHub ID, and professor ID) is saved in a directory dedicated to the user, outside of the repository clone (for example, under `%LOCALAPPDATA%` or `%APPDATA%` on Windows, and in `~/.config/` on Linux). This ensures that even if you execute the script directly from your repository clone, your personal configuration is not tracked by Git. And you will also be able to get my script updates directly by updating your clone.

## Requirements

- Python 3.8+
- `CustomTkinter` and `appdirs` libraries. Install with:

```bash
pip install customtkinter appdirs
````

## How to Use

1. Go to the script's directory.
2. Run the script:

```bash
python new-tutorial-creation.py
```

3. Fill in the fields in the GUI:
    
    - **Local path:** Your local path to the `/tutorials` folder (e.g., `.../bitcoin-educational-content/tutorials/`).
    - **Language:** Select the language in which you will write the tutorial. Use "_Main languages_" for English, French, Italian, or Spanish; otherwise, select "_Other languages_".
    - **Category/Subcategory/Difficulty:** Choose the category, subcategory, and difficulty level for your tutorial.
    - **Folder name:** Enter the folder name for your tutorial. This will also form part of the tutorial's URL, so use only lowercase letters, numbers, and hyphens.
    - **Builder name:** Type the beginning of the builder's name to search for it and select it from the dropdown menu. Its `projectId` will automatically be filled in the field below. You can also enter it manually.
    - **Project ID:** **Enter the builder's Project ID (UUID).** The application will search in the `resources/builders` folder (located at the same level as your `/tutorials` folder) for a builder with this UUID.
        - If found, the builder’s name will be displayed for confirmation.
        - If not found, you will receive a warning and can choose to continue anyway or cancel.
    - **Tags:** Choose 2 or 3 tags.
    - **Contributor's GitHub ID and PBN professor's ID:** Enter your GitHub ID and your internal professor ID.

4. Click **"Create Tutorial"** to generate the folder structure and files.

Upon closing, the software automatically saves your recurring inputs (local path, language, GitHub ID, professor ID) in a JSON file.

The GUI uses the default light and blue theme of CustomTkinter. You can switch to dark mode by clicking the "_Toggle Theme_" button.

## Files Generated

```
local_tutorials_path/
├── category_name/
    ├── tutorial_name/
        ├── assets/
        │   └── [language_code]/
        ├── tutorial.yml
        └── [language_code].md
```
