import os
import re
import uuid
import random
import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image
from gui.footer import create_footer
from utils.data_loader import load_allowed_tags
from utils.file_ops import (
    create_directory,
    write_file,
    process_profile_image,
    create_professor_yaml,
    create_language_yaml
)

class ProfessorPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = self.settings.get("base_path", "")
        
        # Set this page as the active page in the master
        self.master.active_page = self
        
        # Retrieve any previously saved professor data
        professor_data = self.settings.get("professor_data", {})
        
        # Configure the grid layout
        for i in range(15):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)
        
        row = 0
        ctk.CTkLabel(self, text="New Professor Creation", font=("Arial", 20, "bold")).grid(row=row, column=0, columnspan=4, pady=10)
        row += 1
        
        # Folder name input
        ctk.CTkLabel(self, text="Folder name:", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=10)
        self.folder_name_var = ctk.StringVar(value=professor_data.get("folder_name", ""))
        ctk.CTkEntry(self, textvariable=self.folder_name_var, width=200, font=("Arial", 14, "bold")).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        # First and last name inputs
        ctk.CTkLabel(self, text="First Name:", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=10)
        self.first_name_var = ctk.StringVar(value=professor_data.get("first_name", ""))
        ctk.CTkEntry(self, textvariable=self.first_name_var, width=200, font=("Arial", 14, "bold")).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkLabel(self, text="Last Name (optional):", font=("Arial", 14)).grid(row=row, column=2, sticky="w", padx=10)
        self.last_name_var = ctk.StringVar(value=professor_data.get("last_name", ""))
        ctk.CTkEntry(self, textvariable=self.last_name_var, width=200, font=("Arial", 14, "bold")).grid(row=row, column=3, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Optional website and Twitter inputs
        ctk.CTkLabel(self, text="Website (optional):", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=10)
        self.website_var = ctk.StringVar(value=professor_data.get("website", ""))
        ctk.CTkEntry(self, textvariable=self.website_var, width=200, font=("Arial", 14, "bold")).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkLabel(self, text="Twitter / X (optional):", font=("Arial", 14)).grid(row=row, column=2, sticky="w", padx=10)
        self.twitter_var = ctk.StringVar(value=professor_data.get("twitter", ""))
        ctk.CTkEntry(self, textvariable=self.twitter_var, width=200, font=("Arial", 14, "bold")).grid(row=row, column=3, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Optional lightning address input
        ctk.CTkLabel(self, text="Lightning Address (optional):", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=10)
        self.lightning_var = ctk.StringVar(value=professor_data.get("lightning", ""))
        ctk.CTkEntry(self, textvariable=self.lightning_var, width=200, font=("Arial", 14, "bold")).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Tags input and suggestions (minimum 2 required)
        ctk.CTkLabel(self, text="Tags (min. 2):", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=10)
        tag_frame = ctk.CTkFrame(self, width=300)
        tag_frame.grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        num_tags = 3
        gap_width = 5
        tag_field_width = int((300 - (num_tags - 1) * gap_width) / num_tags * 1.8)
        self.tag1_var = ctk.StringVar(value=professor_data.get("tag1", ""))
        self.tag2_var = ctk.StringVar(value=professor_data.get("tag2", ""))
        self.tag3_var = ctk.StringVar(value=professor_data.get("tag3", ""))
        self.tag1_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag1_var, width=tag_field_width, font=("Arial", 14, "bold"))
        self.tag1_entry.grid(row=0, column=0, padx=(0, gap_width), sticky="ew")
        self.tag1_entry.bind("<KeyRelease>", self.update_tag1_suggestions)
        self.tag2_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag2_var, width=tag_field_width, font=("Arial", 14, "bold"))
        self.tag2_entry.grid(row=0, column=1, padx=(0, gap_width), sticky="ew")
        self.tag2_entry.bind("<KeyRelease>", self.update_tag2_suggestions)
        self.tag3_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag3_var, width=tag_field_width, font=("Arial", 14, "bold"))
        self.tag3_entry.grid(row=0, column=2, sticky="ew")
        self.tag3_entry.bind("<KeyRelease>", self.update_tag3_suggestions)
        row += 1
        
        ctk.CTkLabel(self, text="Tag Suggestions:", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=10)
        tag_suggestion_frame = ctk.CTkFrame(self, width=300)
        tag_suggestion_frame.grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        self.tag1_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag1_selected, width=tag_field_width, font=("Arial", 14, "bold"))
        self.tag1_suggestions_menu.grid(row=0, column=0, padx=(0, gap_width), sticky="ew")
        self.tag2_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag2_selected, width=tag_field_width, font=("Arial", 14, "bold"))
        self.tag2_suggestions_menu.grid(row=0, column=1, padx=(0, gap_width), sticky="ew")
        self.tag3_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag3_selected, width=tag_field_width, font=("Arial", 14, "bold"))
        self.tag3_suggestions_menu.grid(row=0, column=2, sticky="ew")
        self.update_tag1_suggestions()
        self.update_tag2_suggestions()
        self.update_tag3_suggestions()
        row += 1
        
        # Profile image input
        ctk.CTkLabel(self, text="Profile Image:", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=10)
        self.image_path_var = ctk.StringVar(value=professor_data.get("image_path", ""))
        ctk.CTkEntry(self, textvariable=self.image_path_var, width=200, font=("Arial", 14, "bold")).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(self, text="Select Image", command=self.select_image, width=120, font=("Arial", 14, "bold")).grid(row=row, column=2, padx=10, pady=5)
        row += 1
        
        # Biography and Short bio inputs
        ctk.CTkLabel(self, text="Biography:", font=("Arial", 14)).grid(row=row, column=0, sticky="nw", padx=10)
        self.bio_textbox = ctk.CTkTextbox(self, width=400, height=100)
        self.bio_textbox.grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        if "bio" in professor_data:
            self.bio_textbox.insert("1.0", professor_data.get("bio"))
        row += 1
        
        ctk.CTkLabel(self, text="Short bio:", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=10)
        self.short_bio_var = ctk.StringVar(value=professor_data.get("short_bio", ""))
        ctk.CTkEntry(self, textvariable=self.short_bio_var, width=400, font=("Arial", 14, "bold")).grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Buttons for creating the professor and going back
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=4, pady=20, sticky="ew")
        ctk.CTkButton(button_frame, text="Create Professor", command=self.create_professor, font=("Arial", 14, "bold")).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(button_frame, text="Back", command=self.go_back, font=("Arial", 14, "bold")).pack(side="left", padx=10, expand=True)
   
        create_footer(self)

   
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
        self.settings["professor_data"] = {
            "folder_name": self.folder_name_var.get(),
            "first_name": self.first_name_var.get(),
            "last_name": self.last_name_var.get(),
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
        file_path = filedialog.askopenfilename(
            title="Select Profile Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp")]
        )
        if file_path:
            self.image_path_var.set(file_path)
   
    def create_professor(self):
        folder_name = self.folder_name_var.get().strip()
        if not folder_name or not re.match(r'^[a-z0-9\-]+$', folder_name):
            messagebox.showerror("Error", "Invalid folder name. Use only lowercase letters, digits, and dashes.")
            return
       
        if not self.first_name_var.get().strip():
            messagebox.showerror("Error", "Please enter a first name or a pseudo.")
            return
       
        tags = [t.strip() for t in [self.tag1_var.get(), self.tag2_var.get(), self.tag3_var.get()] if t.strip()]
        if len(tags) < 2:
            messagebox.showerror("Error", "Please enter at least two tags.")
            return
        allowed_tags = load_allowed_tags(self.base_path)
        for tag in tags:
            if tag not in allowed_tags:
                messagebox.showerror("Error", f"Tag '{tag}' is not valid. Please select a valid tag from the suggestions.")
                return
       
        if not self.image_path_var.get().strip():
            messagebox.showerror("Error", "Please select a profile image.")
            return
       
        if not self.bio_textbox.get("1.0", "end").strip():
            messagebox.showerror("Error", "Please enter a biography for the professor.")
            return
       
        professors_dir = os.path.join(self.base_path, "professors")
        create_directory(professors_dir)
        new_folder = os.path.join(professors_dir, folder_name)
        if os.path.exists(new_folder):
            counter = 2
            while os.path.exists(f"{new_folder}-{counter}"):
                counter += 1
            folder_name = f"{folder_name}-{counter}"
            new_folder = os.path.join(professors_dir, folder_name)
       
        try:
            create_directory(new_folder)
            assets_dir = os.path.join(new_folder, "assets")
            create_directory(assets_dir)
           
            image_path = self.image_path_var.get().strip()
            if image_path and os.path.exists(image_path):
                dest_image = os.path.join(assets_dir, "profile.webp")
                process_profile_image(image_path, dest_image)
           
            first_name = self.first_name_var.get().strip()
            last_name = self.last_name_var.get().strip()
            full_name = first_name if not last_name else f"{first_name} {last_name}"

            yaml_content = create_professor_yaml(
                full_name,
                website=self.website_var.get().strip(),
                twitter=self.twitter_var.get().strip(),
                lightning=self.lightning_var.get().strip(),
                tags=tags
            )
            yaml_file_path = os.path.join(new_folder, "professor.yml")
            write_file(yaml_file_path, yaml_content)
           
            language = self.settings.get("language", "en").split(" ")[0]
            lang_yaml_content = create_language_yaml(
                language,
                self.bio_textbox.get("1.0", "end").strip(),
                self.short_bio_var.get().strip()
            )
            lang_yaml_path = os.path.join(new_folder, f"{language}.yml")
            write_file(lang_yaml_path, lang_yaml_content)
           
            messagebox.showinfo("Success", f"Professor created successfully in:\n{new_folder}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
   
    def go_back(self):
        self.update_local_state()
        from gui.home import HomePage
        self.destroy()
        home_page = HomePage(self.parent, self.settings)
        home_page.pack(fill="both", expand=True)
