import os
import json
from appdirs import user_config_dir

APP_NAME = "Tutorial Creator GUI"
APP_AUTHOR = "Plan B Network"
CONFIG_DIR = user_config_dir(APP_NAME, APP_AUTHOR)
os.makedirs(CONFIG_DIR, exist_ok=True)
SETTINGS_FILE = os.path.join(CONFIG_DIR, "settings.json")

def load_settings():
    """Load user settings from JSON file."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
            return settings
    else:
        # Default settings if none exist
        return {
            "base_path": "",
            "language_option": 1,
            "language": "",
            "contributor_id": "",
            "professor_id": "",
            "theme": "Light"
        }

def save_settings(settings):
    """Save user settings to JSON file."""
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)
