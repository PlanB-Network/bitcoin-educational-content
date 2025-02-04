import os
import uuid
import datetime
import json
from appdirs import user_config_dir
import customtkinter as ctk
from tkinter import messagebox, filedialog

root = ctk.CTk()
root.title("Tutorial Creation")

base_path_var = ctk.StringVar(master=root)
language_option_var = ctk.IntVar(master=root, value=1)
language_var = ctk.StringVar(master=root)
section_var = ctk.StringVar(master=root)
category_var = ctk.StringVar(master=root)
level_var = ctk.StringVar(master=root)
tutorial_name_var = ctk.StringVar(master=root)
builder_search_var = ctk.StringVar(master=root)
project_id_var = ctk.StringVar(master=root)
tag1_var = ctk.StringVar(master=root)
tag2_var = ctk.StringVar(master=root)
tag3_var = ctk.StringVar(master=root)
contributor_id_var = ctk.StringVar(master=root)
professor_id_var = ctk.StringVar(master=root)

APP_NAME = "Tutorial Creator GUI"
APP_AUTHOR = "Plan B Network"

CONFIG_DIR = user_config_dir(APP_NAME, APP_AUTHOR)
os.makedirs(CONFIG_DIR, exist_ok=True)
SETTINGS_FILE = os.path.join(CONFIG_DIR, 'settings.json')

def select_base_path():
    path = filedialog.askdirectory()
    base_path_var.set(path)

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            settings = json.load(f)
            if 'theme' in settings:
                ctk.set_appearance_mode(settings['theme'])
            else:
                ctk.set_appearance_mode("Light")
            if 'base_path' in settings:
                base_path_var.set(settings['base_path'])
            if 'language_option' in settings:
                language_option_var.set(settings['language_option'])
            if 'language' in settings:
                language_var.set(settings['language'])
            if 'contributor_id' in settings:
                contributor_id_var.set(settings['contributor_id'])
            if 'professor_id' in settings:
                professor_id_var.set(settings['professor_id'])
            return settings
    else:
        ctk.set_appearance_mode("Light")
        return {}

def save_settings():
    settings = {
        'base_path': base_path_var.get(),
        'language_option': language_option_var.get(),
        'language': language_var.get(),
        'contributor_id': contributor_id_var.get(),
        'professor_id': professor_id_var.get(),
        'theme': ctk.get_appearance_mode()
    }
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)

def load_all_builders():
    builders = {}
    base_path = base_path_var.get()
    if not base_path:
        return builders
    parent_dir = os.path.dirname(base_path)
    builders_dir = os.path.join(parent_dir, "resources", "builders")
    if not os.path.exists(builders_dir):
        return builders

    for d in os.listdir(builders_dir):
        sub_dir = os.path.join(builders_dir, d)
        if os.path.isdir(sub_dir):
            builder_file = os.path.join(sub_dir, "builder.yml")
            if os.path.exists(builder_file):
                with open(builder_file, "r", encoding="utf-8") as bf:
                    lines = bf.readlines()
                b_id = None
                b_name = None
                for line in lines:
                    if line.startswith("id:"):
                        b_id = line.split(":", 1)[1].strip()
                    elif line.startswith("name:"):
                        b_name = line.split(":", 1)[1].strip()
                if b_name and b_id:
                    builders[b_name] = b_id
    return builders

def update_categories(*args):
    section = section_var.get()
    categories = sections.get(section, [])
    category_menu.configure(values=categories)
    if categories:
        category_var.set(categories[0])
    else:
        category_var.set('')

builders_mapping = {}

def update_builder_suggestions(event=None):
    search_text = builder_search_var.get().lower()
    global builders_mapping
    builders_mapping = load_all_builders()
    suggestions = [name for name in builders_mapping.keys() if search_text in name.lower()]
    if suggestions:
        builder_suggestions_menu.configure(values=suggestions)
        builder_suggestions_menu.set(suggestions[0])
    else:
        builder_suggestions_menu.configure(values=["No match"])
        builder_suggestions_menu.set("No match")

def on_builder_selected(selected_name):
    if selected_name in builders_mapping:
        project_id_var.set(builders_mapping[selected_name])

def create_tutorial():
    base_path = base_path_var.get()
    if not base_path:
        messagebox.showerror("Error", "Please select the local base path for the BEC/tutorials/ folder.")
        return

    selected_language = language_var.get()
    if not selected_language:
        messagebox.showerror("Error", "Please select a language.")
        return
    language_code = selected_language.split(' ')[0]

    section_name = section_var.get()
    if not section_name:
        messagebox.showerror("Error", "Please select the tutorial section.")
        return

    tutorial_name = tutorial_name_var.get()
    if not tutorial_name:
        messagebox.showerror("Error", "Please enter the folder name for the tutorial.")
        return

    project_id = project_id_var.get().strip()
    if not project_id:
        messagebox.showerror("Error", "Please enter the builder's project ID (UUID).")
        return

    parent_dir = os.path.dirname(base_path)
    builders_dir = os.path.join(parent_dir, "resources", "builders")
    if not os.path.exists(builders_dir):
        messagebox.showerror("Error", f"The builders directory does not exist at:\n{builders_dir}")
        return

    found = False
    builder_display_name = None
    for d in os.listdir(builders_dir):
        sub_dir = os.path.join(builders_dir, d)
        if os.path.isdir(sub_dir):
            builder_file = os.path.join(sub_dir, "builder.yml")
            if os.path.exists(builder_file):
                with open(builder_file, "r", encoding="utf-8") as bf:
                    lines = bf.readlines()
                b_id = None
                b_name = None
                for line in lines:
                    if line.startswith("id:"):
                        b_id = line.split(":", 1)[1].strip()
                    elif line.startswith("name:"):
                        b_name = line.split(":", 1)[1].strip()
                if b_id and b_id.lower() == project_id.lower():
                    found = True
                    builder_display_name = b_name
                    break

    if found:
        answer = messagebox.askyesno("Confirm Builder",
            f"The builder with project ID {project_id} is named '{builder_display_name}'.\nDo you want to continue?")
        if not answer:
            return
    else:
        answer = messagebox.askyesno("Builder Not Found",
            f"No builder with project ID {project_id} was found.\nDo you want to continue anyway?")
        if not answer:
            return

    level_value = level_var.get()
    if not level_value:
        messagebox.showerror("Error", "Please select the tutorial's difficulty level.")
        return

    tags = []
    for tag_var in [tag1_var, tag2_var, tag3_var]:
        tag = tag_var.get().strip()
        if tag:
            tags.append(tag)
    if not tags:
        messagebox.showerror("Error", "Please enter at least one tag for the tutorial.")
        return

    category_value = category_var.get()
    if not category_value:
        messagebox.showerror("Error", "Please select the subcategory.")
        return

    contributor_id = contributor_id_var.get().strip()
    if not contributor_id:
        messagebox.showerror("Error", "Please enter the contributor's GitHub ID.")
        return

    professor_id = professor_id_var.get().strip()
    if not professor_id:
        messagebox.showerror("Error", "Please enter the PBN professor's ID.")
        return

    save_settings()

    try:
        tutorial_path = os.path.join(base_path, section_name, tutorial_name)
        os.makedirs(tutorial_path, exist_ok=True)
        assets_path = os.path.join(tutorial_path, "assets")
        os.makedirs(assets_path, exist_ok=True)
        assets_lang_path = os.path.join(assets_path, language_code)
        os.makedirs(assets_lang_path, exist_ok=True)

        md_filename = f"{language_code}.md"
        md_content = """---
name: 
description: 
---
![cover](assets/cover.webp)
"""
        with open(os.path.join(tutorial_path, md_filename), "w", encoding="utf-8") as md_file:
            md_file.write(md_content)

        uuid_value = str(uuid.uuid4())
        current_date = datetime.date.today().strftime("%Y-%m-%d")

        lines = [
            f"id: {uuid_value}",
            "",
            f"project_id: {project_id}",
            "",
            "tags:"
        ]
        for tag in tags:
            lines.append(f"  - {tag}")
        lines.extend([
            "",
            f"category: {category_value}",
            "",
            f"level: {level_value}",
            "",
            "credits:",
            f"  professor: {professor_id}",
            "",
            "# Proofreading metadata",
            "",
            f"original_language: {language_code}",
            "proofreading:",
            f"  - language: {language_code}",
            f"    last_contribution_date: {current_date}",
            "    urgency:",
            "    contributors_id:",
            f"      - {contributor_id}",
            "    reward:"
        ])
        yaml_content = "\n".join(lines)

        with open(os.path.join(tutorial_path, "tutorial.yml"), "w", encoding="utf-8") as yaml_file:
            yaml_file.write(yaml_content)

        messagebox.showinfo("Success", f"Tutorial successfully created in the folder:\n{tutorial_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def clear_fields():
    base_path_var.set('')
    language_option_var.set(1)
    update_language_options()
    language_var.set('')
    section_var.set('')
    category_var.set('')
    level_var.set('')
    tutorial_name_var.set('')
    builder_search_var.set('')
    builder_suggestions_menu.set('')
    project_id_var.set('')
    tag1_var.set('')
    tag2_var.set('')
    tag3_var.set('')
    contributor_id_var.set('')
    professor_id_var.set('')

def update_language_options():
    if language_option_var.get() == 1:
        language_menu.configure(values=main_language_options)
        if language_var.get() not in main_language_options:
            language_var.set(main_language_options[0])
    elif language_option_var.get() == 2:
        language_menu.configure(values=other_language_options)
        if language_var.get() not in other_language_options:
            language_var.set(other_language_options[0])

def on_closing():
    save_settings()
    root.destroy()

def toggle_theme():
    current_mode = ctk.get_appearance_mode()
    new_mode = "Light" if current_mode == "Dark" else "Dark"
    ctk.set_appearance_mode(new_mode)
    save_settings()

ctk.set_default_color_theme("blue")

sections = {
    "exchange": ["centralized", "peer-to-peer"],
    "merchant": ["merchant"],
    "mining": ["hardware", "software"],
    "node": ["bitcoin", "lightning-network", "rgb"],
    "others": ["contribution", "general"],
    "privacy": ["analysis", "bitcoin", "general"],
    "wallet": ["desktop", "hardware", "mobile", "backup"]
}

levels = ["beginner", "intermediate", "advanced", "expert"]

main_language_codes = {
    'en': 'English',
    'es': 'Español',
    'fr': 'Français',
    'it': 'Italiano'
}
main_language_options = [f"{code} ({main_language_codes[code]})" for code in main_language_codes]

other_language_codes = {
    'af': 'Afrikaans',
    'am': 'አማርኛ',
    'ar': 'العربية',
    'as': 'অসমীয়া',
    'az': 'Azərbaycanca',
    'be': 'Беларуская',
    'bg': 'Български',
    'bn': 'বাংলা',
    'bo': 'བོད་སྐད་',
    'bs': 'Bosanski',
    'ca': 'Català',
    'ceb': 'Cebuano',
    'co': 'Corsu',
    'cs': 'Čeština',
    'cy': 'Cymraeg',
    'da': 'Dansk',
    'de': 'Deutsch',
    'dv': 'ދިވެހިބަސް',
    'dz': 'རྫོང་ཁ',
    'ee': 'Eʋegbe',
    'el': 'Ελληνικά',
    'eo': 'Esperanto',
    'et': 'Eesti',
    'eu': 'Euskara',
    'fa': 'فارسی',
    'fi': 'Suomi',
    'fil': 'Filipino',
    'fj': 'Na Vosa Vakaviti',
    'fo': 'Føroyskt',
    'fy': 'Frysk',
    'ga': 'Gaeilge',
    'gd': 'Gàidhlig',
    'gl': 'Galego',
    'gn': "Avañe'ẽ",
    'gu': 'ગુજરાતી',
    'ha': 'Hausa',
    'he': 'עברית',
    'hi': 'हिन्दी',
    'hmn': 'Hmoob',
    'hr': 'Hrvatski',
    'ht': 'Kreyòl Ayisyen',
    'hu': 'Magyar',
    'hy': 'Հայերեն',
    'id': 'Bahasa Indonesia',
    'ig': 'Igbo',
    'is': 'Íslenska',
    'ja': '日本語',
    'jv': 'Basa Jawa',
    'ka': 'ქართული',
    'kk': 'Қазақша',
    'kl': 'Kalaallisut',
    'km': 'ខ្មែរ',
    'kn': 'ಕನ್ನಡ',
    'ko': '한국어',
    'ku': 'Kurdî',
    'ky': 'Кыргызча',
    'la': 'Latina',
    'lb': 'Lëtzebuergesch',
    'lo': 'ລາວ',
    'lt': 'Lietuvių',
    'lv': 'Latviešu',
    'mg': 'Malagasy',
    'mi': 'Māori',
    'mk': 'Македонски',
    'ml': 'മലയാളം',
    'mn': 'Монгол',
    'mr': 'मराठी',
    'ms': 'Bahasa Melayu',
    'mt': 'Malti',
    'my': 'မြန်မာစာ',
    'nb': 'Norsk Bokmål',
    'ne': 'नेपाली',
    'nl': 'Nederlands',
    'nn': 'Norsk Nynorsk',
    'no': 'Norsk',
    'ny': 'Chichewa',
    'oc': 'Occitan',
    'om': 'Afaan Oromoo',
    'or': 'ଓଡ଼ିଆ',
    'pa': 'ਪੰਜਾਬੀ',
    'pl': 'Polski',
    'ps': 'پښتو',
    'pt': 'Português',
    'ro': 'Română',
    'ru': 'Русский',
    'rw': 'Kinyarwanda',
    'sd': 'سنڌي',
    'si': 'සිංහල',
    'sk': 'Slovenčina',
    'sl': 'Slovenščina',
    'sm': 'Gagana Samoa',
    'sn': 'ChiShona',
    'so': 'Soomaali',
    'sq': 'Shqip',
    'sr': 'Српски',
    'ss': 'SiSwati',
    'st': 'Sesotho',
    'su': 'Basa Sunda',
    'sv': 'Svenska',
    'sw': 'Kiswahili',
    'ta': 'தமிழ்',
    'te': 'తెలుగు',
    'tg': 'Тоҷикӣ',
    'th': 'ไทย',
    'ti': 'ትግርኛ',
    'tk': 'Türkmençe',
    'tl': 'Tagalog',
    'tn': 'Setswana',
    'tr': 'Türkçe',
    'ts': 'Xitsonga',
    'uk': 'Українська',
    'ur': 'اردو',
    'uz': "Oʻzbekcha",
    'vi': 'Tiếng Việt',
    'xh': 'isiXhosa',
    'yi': 'ייִדיש',
    'yo': 'Yorùbá',
    'zh': '中文',
    'zh-Hans': '简体中文',
    'zh-Hant': '繁體中文',
    'zu': 'isiZulu'
}
sorted_other_languages = sorted(other_language_codes)
other_language_options = [f"{code} ({other_language_codes[code]})" for code in sorted_other_languages]

settings = load_settings()

# GUI

# --- Ligne 0 : Chemin local ---
ctk.CTkLabel(root, text="Local path to /tutorials:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
base_path_entry = ctk.CTkEntry(root, textvariable=base_path_var, width=300)
base_path_entry.grid(row=0, column=1, sticky='w', padx=10, pady=5)
ctk.CTkButton(root, text="Browse", command=select_base_path).grid(row=0, column=2, sticky='w', padx=10, pady=5)

# --- Ligne 1 : Language ---
ctk.CTkLabel(root, text="Language:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
language_frame = ctk.CTkFrame(root, fg_color="transparent")
language_frame.grid(row=1, column=1, columnspan=2, sticky='w', padx=10, pady=5)
ctk.CTkRadioButton(language_frame, text="Main languages", variable=language_option_var, value=1, command=update_language_options).pack(side='left', padx=5)
ctk.CTkRadioButton(language_frame, text="Other languages", variable=language_option_var, value=2, command=update_language_options).pack(side='left', padx=5)

# --- Ligne 2 : Menu de sélection de langue ---
language_menu = ctk.CTkOptionMenu(root, values=[], variable=language_var, width=300)
language_menu.grid(row=2, column=1, columnspan=2, sticky='w', padx=10, pady=5)
update_language_options()

# --- Ligne 3 : Catégorie ---
ctk.CTkLabel(root, text="Category:").grid(row=3, column=0, sticky='w', padx=10, pady=5)
section_menu = ctk.CTkOptionMenu(root, values=list(sections.keys()), variable=section_var, command=lambda _: update_categories(), width=300)
section_menu.grid(row=3, column=1, columnspan=2, sticky='w', padx=10, pady=5)

# --- Ligne 4 : Sous-catégorie ---
ctk.CTkLabel(root, text="Subcategory:").grid(row=4, column=0, sticky='w', padx=10, pady=5)
category_menu = ctk.CTkOptionMenu(root, values=[], variable=category_var, width=300)
category_menu.grid(row=4, column=1, columnspan=2, sticky='w', padx=10, pady=5)

# --- Ligne 5 : Niveau de difficulté ---
ctk.CTkLabel(root, text="Difficulty level:").grid(row=5, column=0, sticky='w', padx=10, pady=5)
level_menu = ctk.CTkOptionMenu(root, values=levels, variable=level_var, width=300)
level_menu.grid(row=5, column=1, columnspan=2, sticky='w', padx=10, pady=5)

# --- Ligne 6 : Folder name ---
ctk.CTkLabel(root, text="Folder name:").grid(row=6, column=0, sticky='w', padx=10, pady=5)
ctk.CTkEntry(root, textvariable=tutorial_name_var, width=300).grid(row=6, column=1, columnspan=2, sticky='w', padx=10, pady=5)

# --- Ligne 7 : Builder Name (avec texte indicatif) ---
ctk.CTkLabel(root, text="Builder Name:").grid(row=7, column=0, sticky='w', padx=10, pady=5)
builder_search_entry = ctk.CTkEntry(root, textvariable=builder_search_var, width=300, placeholder_text="Find the builder ID")
builder_search_entry.grid(row=7, column=1, columnspan=2, sticky='w', padx=10, pady=5)
builder_search_entry.bind("<KeyRelease>", update_builder_suggestions)

# --- Ligne 8 : Suggestions de builder ---
ctk.CTkLabel(root, text="Builder Suggestions:").grid(row=8, column=0, sticky='w', padx=10, pady=5)
builder_suggestions_menu = ctk.CTkOptionMenu(root, values=[], command=on_builder_selected, width=300)
builder_suggestions_menu.grid(row=8, column=1, columnspan=2, sticky='w', padx=10, pady=5)

# --- Ligne 9 : Project ID ---
ctk.CTkLabel(root, text="Project ID:").grid(row=9, column=0, sticky='w', padx=10, pady=5)
ctk.CTkEntry(root, textvariable=project_id_var, width=300).grid(row=9, column=1, columnspan=2, sticky='w', padx=10, pady=5)

# --- Ligne 10 : Tags ---
ctk.CTkLabel(root, text="Tags (2 or 3):").grid(row=10, column=0, sticky='w', padx=10, pady=5)
tag_frame = ctk.CTkFrame(root, width=300)
tag_frame.grid(row=10, column=1, columnspan=2, sticky='w', padx=10, pady=5)
for i in range(3):
    tag_frame.grid_columnconfigure(i, weight=1)
num_tags = 3
gap_width = 5
total_gaps = (num_tags - 1) * gap_width
tag_field_width = int((300 - total_gaps) / num_tags)
for i, tag_var in enumerate([tag1_var, tag2_var, tag3_var]):
    entry = ctk.CTkEntry(tag_frame, textvariable=tag_var, width=tag_field_width)
    padx = (0, gap_width) if i < num_tags - 1 else (0, 0)
    entry.grid(row=0, column=i, padx=padx, sticky='w')

# --- Ligne 11 : Contributor's GitHub ID ---
ctk.CTkLabel(root, text="Contributor's GitHub ID:").grid(row=11, column=0, sticky='w', padx=10, pady=5)
ctk.CTkEntry(root, textvariable=contributor_id_var, width=300).grid(row=11, column=1, columnspan=2, sticky='w', padx=10, pady=5)

# --- Ligne 12 : PBN professor's ID ---
ctk.CTkLabel(root, text="PBN professor's ID:").grid(row=12, column=0, sticky='w', padx=10, pady=5)
ctk.CTkEntry(root, textvariable=professor_id_var, width=300).grid(row=12, column=1, columnspan=2, sticky='w', padx=10, pady=5)

# --- Ligne 13 : Boutons ---
button_frame = ctk.CTkFrame(root, fg_color="transparent", border_width=0)
button_frame.grid(row=13, column=0, columnspan=3, pady=20)
create_button = ctk.CTkButton(button_frame, text="Create Tutorial", command=create_tutorial)
create_button.pack(side='left', padx=10)
clear_button = ctk.CTkButton(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side='left', padx=10)
cancel_button = ctk.CTkButton(button_frame, text="Close", command=on_closing)
cancel_button.pack(side='left', padx=10)
theme_switch = ctk.CTkButton(button_frame, text="Toggle Theme", command=toggle_theme)
theme_switch.pack(side='left', padx=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
