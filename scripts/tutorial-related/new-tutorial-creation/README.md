
This Python script runs a GUI where the tutorial writer can easily select the parameters for a new tutorial and then automatically generate all the required folders and files, to allow him to focus solely on the essential: writing the tutorial.

## Features
- Allows easy customization of the metadata for the new tutorial;  
- Automatically generates `tutorial.yml` and `.md` files;  
- Automatically creates the correct structure for these files along with a UUID;  
- Saves recurring inputs in a JSON file so the user doesn’t need to re-enter them during the next use (local path, language, GitHub ID, professor ID);  
- A modern GUI built with CustomTkinter.

## Requirements

- Python 3.8+
- `CustomTkinter` library. Install with:

```bash
pip install customtkinter
```

## How to Use

Before starting, **I suggest copying the script folder to a local directory outside your PBN repo clone**, as the JSON settings file that saves your personal inputs should not be pushed to the source repository.

1. Go to the script's directory.

2. Run the script:

```bash
python new-tutorial-creation.py
```

3. Fill in the fields in the GUI:
	- Your local path to the `/tutorials` folder (`.../bitcoin-educational-content/tutorials/`).
	- Select the language in which you will write the tutorial. If it’s in English, French, Italian, or Spanish, select the "*Main languages*" button. For any other language, select "*Other languages*".
	- Choose the category, subcategory, and difficulty level of your tutorial.  
	- Enter the folder name for your tutorial. Note: this folder name will also become your tutorial's URL path, so use only lowercase letters, numbers, and hyphens. Avoid using spaces.
	- Enter the builder's name.
	- Choose 2 or 3 tags.
	- Provide your GitHub ID and your internal professor ID (the two words from the BIP39 list).

4. Click **"*Create Tutorial*"** to generate the folder structure and files.

Upon closing, the software will automatically generate a JSON file that saves your local path, language, and IDs, so you won’t have to enter them manually each time you use it. To modify these settings, click the "Clear" button.

The GUI uses the default light and blue theme of CustomTkinter. You can switch to dark mode by clicking the "*Toggle Theme*" button.

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

