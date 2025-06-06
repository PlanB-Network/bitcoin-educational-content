Python app designed to create resources locally on your clone of the Plan ₿ Network data repo. It automatically generates and correctly places all the files and necessary metadata, following the latest guidelines from the data team.

Supports adding:
- A new tutorial;
- A new professor profile;
- A new project.

App maintained by Loïc Morel.

## Features

- Allows easy customization of the metadata for the new tutorial.
- Automatically generates `tutorial.yml`, `professor.yml`, `project.yml` and `.md` files with a new UUID.
- Creates the correct folder structure automatically.
- Saves recurring inputs (local path, language, GitHub ID, professor ID) in a JSON file so you don’t need to re-enter them next time.
- Function to search for the project, prof and tags by name and automatically return the correct `UUID` or tag.
- A modern GUI built with CustomTkinter.

I have integrated the `appdirs` library to manage user-specific configuration. In practice, the JSON settings file (which stores recurring inputs like your local path, language, GitHub ID, and professor ID) is saved in a directory dedicated to the user, outside of the repository clone (for example, under `%LOCALAPPDATA%` or `%APPDATA%` on Windows, and in `~/.config/` on Linux). This ensures that even if you execute the script directly from your repository clone, your personal configuration is not tracked by Git. And you will also be able to get my script updates directly by updating your clone.

## Requirements

- Python 3.8+
- Install the dependencies :

```bash
pip install -r requirements.txt
````

## How to Use

1. Go to the script's directory.
2. Run the script:

```bash
python3 main.py
```

3. Fill in the required fields on the homepage, then click on a button corresponding to the resource you want to create.  

4. Fill in the specific fields requested for your resource, then click the "Create..." button to generate the necessary files and structure.  

For projects and professors, there’s nothing else to do. Everything is created by the app, so you can proceed with a PR. For tutorials, only the document templates are created. You will need to write the tutorial and place the images in the appropriate folder before making the PR.

Upon closing, the software automatically saves your recurring inputs (local path, language, GitHub ID, professor ID) in a JSON file.