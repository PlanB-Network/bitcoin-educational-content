import os
import re
import uuid
import shutil
import random
import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image  # requires Pillow
from utils.constants import BIP39_WORDS  # Liste complète BIP39 dans constants.py
from utils.data_loader import load_allowed_tags  # pour la gestion des tags

class ProfessorPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = self.settings.get("base_path", "")
       
        # Enregistrer cette page comme active dans le master
        self.master.active_page = self

        # Charger les données temporaires enregistrées (si elles existent)
        professor_data = self.settings.get("professor_data", {})

        # Configurer la grille pour occuper tout l'espace
        for i in range(15):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)
       
        row = 0
        ctk.CTkLabel(self, text="New Professor Creation", font=("Arial", 20)).grid(row=row, column=0, columnspan=4, pady=10)
        row += 1
       
        # Folder name (for new professor)
        ctk.CTkLabel(self, text="Folder name:").grid(row=row, column=0, sticky="w", padx=10)
        self.folder_name_var = ctk.StringVar(value=professor_data.get("folder_name", ""))
        ctk.CTkEntry(self, textvariable=self.folder_name_var, width=200).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
       
        # First Name and Last Name
        ctk.CTkLabel(self, text="First Name:").grid(row=row, column=0, sticky="w", padx=10)
        self.first_name_var = ctk.StringVar(value=professor_data.get("first_name", ""))
        ctk.CTkEntry(self, textvariable=self.first_name_var, width=200).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkLabel(self, text="Last Name:").grid(row=row, column=2, sticky="w", padx=10)
        self.last_name_var = ctk.StringVar(value=professor_data.get("last_name", ""))
        ctk.CTkEntry(self, textvariable=self.last_name_var, width=200).grid(row=row, column=3, padx=10, pady=5, sticky="ew")
        row += 1
       
        # Random Contributor ID with re-roll button
        ctk.CTkLabel(self, text="Random Contributor ID:").grid(row=row, column=0, sticky="w", padx=10)
        initial_contrib = professor_data.get("prof_contrib", self.generate_random_contributor_id())
        self.prof_contrib_var = ctk.StringVar(value=initial_contrib)
        ctk.CTkEntry(self, textvariable=self.prof_contrib_var, width=200).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(self, text="Re-roll", command=self.roll_contributor_id, width=100).grid(row=row, column=2, padx=10, pady=5)
        row += 1
       
        # Links: Website and Twitter (optionnels)
        ctk.CTkLabel(self, text="Website (optional):").grid(row=row, column=0, sticky="w", padx=10)
        self.website_var = ctk.StringVar(value=professor_data.get("website", ""))
        ctk.CTkEntry(self, textvariable=self.website_var, width=200).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkLabel(self, text="Twitter (optional):").grid(row=row, column=2, sticky="w", padx=10)
        self.twitter_var = ctk.StringVar(value=professor_data.get("twitter", ""))
        ctk.CTkEntry(self, textvariable=self.twitter_var, width=200).grid(row=row, column=3, padx=10, pady=5, sticky="ew")
        row += 1
       
        # Tips: Lightning address (optionnel)
        ctk.CTkLabel(self, text="Lightning Address (optional):").grid(row=row, column=0, sticky="w", padx=10)
        self.lightning_var = ctk.StringVar(value=professor_data.get("lightning", ""))
        ctk.CTkEntry(self, textvariable=self.lightning_var, width=200).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
       
        # Tags (obligatoires) : minimum 2 tags et doivent être valides
        ctk.CTkLabel(self, text="Tags (min. 2):").grid(row=row, column=0, sticky="w", padx=10)
        tag_frame = ctk.CTkFrame(self, width=300)
        tag_frame.grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        num_tags = 3
        gap_width = 5
        tag_field_width = int((300 - (num_tags - 1) * gap_width) / num_tags)
        self.tag1_var = ctk.StringVar(value=professor_data.get("tag1", ""))
        self.tag2_var = ctk.StringVar(value=professor_data.get("tag2", ""))
        self.tag3_var = ctk.StringVar(value=professor_data.get("tag3", ""))
        self.tag1_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag1_var, width=tag_field_width)
        self.tag1_entry.grid(row=0, column=0, padx=(0, gap_width), sticky="ew")
        self.tag1_entry.bind("<KeyRelease>", self.update_tag1_suggestions)
        self.tag2_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag2_var, width=tag_field_width)
        self.tag2_entry.grid(row=0, column=1, padx=(0, gap_width), sticky="ew")
        self.tag2_entry.bind("<KeyRelease>", self.update_tag2_suggestions)
        self.tag3_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag3_var, width=tag_field_width)
        self.tag3_entry.grid(row=0, column=2, sticky="ew")
        self.tag3_entry.bind("<KeyRelease>", self.update_tag3_suggestions)
        row += 1
       
        ctk.CTkLabel(self, text="Tag Suggestions:").grid(row=row, column=0, sticky="w", padx=10)
        tag_suggestion_frame = ctk.CTkFrame(self, width=300)
        tag_suggestion_frame.grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        self.tag1_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag1_selected, width=tag_field_width)
        self.tag1_suggestions_menu.grid(row=0, column=0, padx=(0, gap_width), sticky="ew")
        self.tag2_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag2_selected, width=tag_field_width)
        self.tag2_suggestions_menu.grid(row=0, column=1, padx=(0, gap_width), sticky="ew")
        self.tag3_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag3_selected, width=tag_field_width)
        self.tag3_suggestions_menu.grid(row=0, column=2, sticky="ew")
        self.update_tag1_suggestions()
        self.update_tag2_suggestions()
        self.update_tag3_suggestions()
        row += 1
       
        # Profile image (obligatoire)
        ctk.CTkLabel(self, text="Profile Image:").grid(row=row, column=0, sticky="w", padx=10)
        self.image_path_var = ctk.StringVar(value=professor_data.get("image_path", ""))
        ctk.CTkEntry(self, textvariable=self.image_path_var, width=200).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(self, text="Select Image", command=self.select_image, width=120).grid(row=row, column=2, padx=10, pady=5)
        row += 1
       
        # Biography (multilines) et Short Bio (obligatoire mais peut être vide)
        ctk.CTkLabel(self, text="Biography:").grid(row=row, column=0, sticky="nw", padx=10)
        self.bio_textbox = ctk.CTkTextbox(self, width=400, height=100)
        self.bio_textbox.grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        if "bio" in professor_data:
            self.bio_textbox.insert("1.0", professor_data.get("bio"))
        row += 1
       
        ctk.CTkLabel(self, text="Short bio:").grid(row=row, column=0, sticky="w", padx=10)
        self.short_bio_var = ctk.StringVar(value=professor_data.get("short_bio", ""))
        ctk.CTkEntry(self, textvariable=self.short_bio_var, width=400).grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        row += 1
       
        # Boutons : Create Professor et Back
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=4, pady=20, sticky="ew")
        ctk.CTkButton(button_frame, text="Create Professor", command=self.create_professor).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(button_frame, text="Back", command=self.go_back).pack(side="left", padx=10, expand=True)
   
    def generate_random_contributor_id(self):
        # Choisir 2 mots aléatoires dans BIP39_WORDS et les joindre par un tiret
        words = random.sample(BIP39_WORDS, 2)
        return f"{words[0]}-{words[1]}"
   
    def roll_contributor_id(self):
        self.prof_contrib_var.set(self.generate_random_contributor_id())
   
    def check_contributor_id(self, contributor_id):
        """
        Vérifie que le contributor_id est composé de 2 mots séparés par un tiret,
        que ces mots sont dans la liste BIP39, et qu'ils ne sont pas déjà utilisés.
        """
        parts = contributor_id.split('-')
        if len(parts) != 2:
            return False, "Contributor ID must consist of two words separated by a hyphen."
        from utils.constants import BIP39_WORDS
        for word in parts:
            if word not in BIP39_WORDS:
                return False, f"The word '{word}' is not in the BIP39 list."
        # Vérifier qu'aucun professor.yml existant n'utilise ce contributor_id
        professors_dir = os.path.join(self.base_path, "professors")
        if os.path.exists(professors_dir):
            for folder in os.listdir(professors_dir):
                folder_path = os.path.join(professors_dir, folder)
                if os.path.isdir(folder_path):
                    yaml_path = os.path.join(folder_path, "professor.yml")
                    if os.path.exists(yaml_path):
                        with open(yaml_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        match = re.search(r'^contributor_id:\s*(\S+)', content, re.MULTILINE)
                        if match:
                            existing_id = match.group(1).strip()
                            if existing_id == contributor_id:
                                return False, f"Contributor ID '{contributor_id}' is already used."
        return True, ""
   
    def update_tag1_suggestions(self, event=None):
        allowed = load_allowed_tags(self.base_path)
        text = self.tag1_var.get().lower()
        suggestions = [t for t in allowed if text in t.lower()]
        if suggestions:
            self.tag1_suggestions_menu.configure(values=suggestions)
            self.tag1_suggestions_menu.set(suggestions[0])
        else:
            self.tag1_suggestions_menu.configure(values=["No match"])
            self.tag1_suggestions_menu.set("No match")
   
    def update_tag2_suggestions(self, event=None):
        allowed = load_allowed_tags(self.base_path)
        text = self.tag2_var.get().lower()
        suggestions = [t for t in allowed if text in t.lower()]
        if suggestions:
            self.tag2_suggestions_menu.configure(values=suggestions)
            self.tag2_suggestions_menu.set(suggestions[0])
        else:
            self.tag2_suggestions_menu.configure(values=["No match"])
            self.tag2_suggestions_menu.set("No match")
   
    def update_tag3_suggestions(self, event=None):
        allowed = load_allowed_tags(self.base_path)
        text = self.tag3_var.get().lower()
        suggestions = [t for t in allowed if text in t.lower()]
        if suggestions:
            self.tag3_suggestions_menu.configure(values=suggestions)
            self.tag3_suggestions_menu.set(suggestions[0])
        else:
            self.tag3_suggestions_menu.configure(values=["No match"])
            self.tag3_suggestions_menu.set("No match")
   
    def on_tag1_selected(self, selected_tag):
        self.tag1_var.set(selected_tag)
   
    def on_tag2_selected(self, selected_tag):
        self.tag2_var.set(selected_tag)
   
    def on_tag3_selected(self, selected_tag):
        self.tag3_var.set(selected_tag)
   
    def update_local_state(self):
        """Sauvegarder les valeurs de la page professor dans settings."""
        self.settings["professor_data"] = {
            "folder_name": self.folder_name_var.get(),
            "first_name": self.first_name_var.get(),
            "last_name": self.last_name_var.get(),
            "prof_contrib": self.prof_contrib_var.get(),
            "website": self.website_var.get(),
            "twitter": self.twitter_var.get(),
            "lightning": self.lightning_var.get(),
            "tag1": self.tag1_var.get(),
            "tag2": self.tag2_var.get(),
            "tag3": self.tag3_var.get(),
            "image_path": self.image_path_var.get(),
            "bio": self.bio_textbox.get("1.0", "end").strip(),
            "short_bio": self.short_bio_var.get()
        }
   
    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select Profile Image", 
                                               filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp")])
        if file_path:
            self.image_path_var.set(file_path)
   
    def create_professor(self):
        # Validation des champs obligatoires
        folder_name = self.folder_name_var.get().strip()
        if not folder_name or not re.match(r'^[a-z0-9\-]+$', folder_name):
            messagebox.showerror("Error", "Invalid folder name. Use only lowercase letters, digits, and dashes.")
            return
       
        if not self.first_name_var.get().strip() or not self.last_name_var.get().strip():
            messagebox.showerror("Error", "Please enter both first and last names.")
            return
       
        # Vérifier que le contributor ID est valide et unique
        contributor_id = self.prof_contrib_var.get().strip()
        valid, error_msg = self.check_contributor_id(contributor_id)
        if not valid:
            messagebox.showerror("Error", error_msg)
            return
       
        # Vérifier que les tags sont renseignés (au moins 2) et valides
        tags = [t.strip() for t in [self.tag1_var.get(), self.tag2_var.get(), self.tag3_var.get()] if t.strip()]
        if len(tags) < 2:
            messagebox.showerror("Error", "Please enter at least two tags.")
            return
        allowed_tags = load_allowed_tags(self.base_path)
        for tag in tags:
            if tag not in allowed_tags:
                messagebox.showerror("Error", f"Tag '{tag}' is not valid. Please select a valid tag from the suggestions.")
                return
       
        # Vérifier que l'image de profil est renseignée
        if not self.image_path_var.get().strip():
            messagebox.showerror("Error", "Please select a profile image.")
            return
       
        # Vérifier que la bio n'est pas vide
        if not self.bio_textbox.get("1.0", "end").strip():
            messagebox.showerror("Error", "Please enter a biography for the professor.")
            return
       
        # Vérifier l'unicité du dossier dans [base_path]/professors/
        professors_dir = os.path.join(self.base_path, "professors")
        os.makedirs(professors_dir, exist_ok=True)
        new_folder = os.path.join(professors_dir, folder_name)
        if os.path.exists(new_folder):
            counter = 2
            while os.path.exists(f"{new_folder}-{counter}"):
                counter += 1
            folder_name = f"{folder_name}-{counter}"
            new_folder = os.path.join(professors_dir, folder_name)
       
        try:
            os.makedirs(new_folder, exist_ok=True)
            # Créer le dossier assets dans le dossier du professeur
            assets_dir = os.path.join(new_folder, "assets")
            os.makedirs(assets_dir, exist_ok=True)
           
            # Gérer l'image de profil
            image_path = self.image_path_var.get().strip()
            if image_path and os.path.exists(image_path):
                _, ext = os.path.splitext(image_path)
                ext = ext.lower()
                dest_image = os.path.join(assets_dir, "profile.webp")
                if ext in [".png", ".jpg", ".jpeg"]:
                    img = Image.open(image_path)
                    img.save(dest_image, "WEBP")
                else:
                    shutil.copy(image_path, dest_image)
           
            # Générer un UUID pour le professeur
            prof_uuid = str(uuid.uuid4())
            full_name = f"{self.first_name_var.get().strip()} {self.last_name_var.get().strip()}"
           
            # Préparer le contenu YAML pour professor.yml
            yaml_lines = [
                f"id: {prof_uuid}",
                f"name: {full_name}",
                "",
                f"contributor_id: {contributor_id}",
                ""
            ]
            # Liens (optionnels)
            links = {}
            if self.website_var.get().strip():
                links["website"] = self.website_var.get().strip()
            if self.twitter_var.get().strip():
                links["twitter"] = self.twitter_var.get().strip()
            if links:
                yaml_lines.append("links:")
                for key, value in links.items():
                    yaml_lines.append(f"  {key}: {value}")
                yaml_lines.append("")
            # Tips
            if self.lightning_var.get().strip():
                yaml_lines.append("tips:")
                yaml_lines.append(f"  lightning_address: {self.lightning_var.get().strip()}")
                yaml_lines.append("")
            # Tags
            yaml_lines.append("tags:")
            for t in tags:
                yaml_lines.append(f"  - {t}")
            yaml_lines.append("")
           
            yaml_content = "\n".join(yaml_lines)
            yaml_file_path = os.path.join(new_folder, "professor.yml")
            with open(yaml_file_path, "w", encoding="utf-8") as f:
                f.write(yaml_content)
           
            # Créer le fichier de langue, par exemple "fr.yml"
            language = self.settings.get("language", "en").split(" ")[0]
            lang_yaml_path = os.path.join(new_folder, f"{language}.yml")
            lang_yaml_lines = [
                "bio: |",
                f"  {self.bio_textbox.get('1.0', 'end').strip()}",
                "",
                "short_bio:"  # Doit être présente, même si vide
            ]
            short_bio = self.short_bio_var.get().strip()
            if short_bio:
                lang_yaml_lines[-1] += f" {short_bio}"
            lang_yaml_content = "\n".join(lang_yaml_lines)
            with open(lang_yaml_path, "w", encoding="utf-8") as f:
                f.write(lang_yaml_content)
           
            messagebox.showinfo("Success", f"Professor created successfully in:\n{new_folder}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
   
    def go_back(self):
        self.update_local_state()
        from gui.home import HomePage
        self.destroy()
        home_page = HomePage(self.parent, self.settings)
        home_page.pack(fill="both", expand=True)
