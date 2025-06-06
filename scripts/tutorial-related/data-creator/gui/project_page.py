import os
import re
import uuid
import datetime
import customtkinter as ctk
from tkinter import messagebox, filedialog
from gui.footer import create_footer
from utils.data_loader import load_allowed_tags, load_all_builders
from utils.file_ops import (
    create_directory,
    write_file,
    process_profile_image,
    create_project_yaml,
    create_project_language_yaml
)
from utils.constants import PROJECT_CATEGORIES

class ProjectPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = settings.get("base_path", "")
        
        # Set this page as active
        self.master.active_page = self
        
        # Retrieve previously saved project data, if any
        project_data = self.settings.get("project_data", {})
        
        # Configure grid layout
        for i in range(12):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)
        
        row = 0
        ctk.CTkLabel(self, text="New Project Creation", font=("Arial", 20, "bold")).grid(row=row, column=0, columnspan=4, pady=10)
        row += 1
        
        # Folder name input
        ctk.CTkLabel(self, text="Folder name:", font=("Arial", 14)).grid(
            row=row, column=0, sticky="w", padx=10
        )
        self.folder_name_var = ctk.StringVar(value=project_data.get("folder_name", ""))
        ctk.CTkEntry(self, textvariable=self.folder_name_var, width=200, font=("Arial", 14, "bold")).grid(
            row=row, column=1, padx=10, pady=5, sticky="ew"
        )
        row += 1
        
        # Project name input (required)
        ctk.CTkLabel(self, text="Project Name:", font=("Arial", 14)).grid(
            row=row, column=0, sticky="w", padx=10
        )
        self.project_name_var = ctk.StringVar(value=project_data.get("project_name", ""))
        ctk.CTkEntry(self, textvariable=self.project_name_var, width=200, font=("Arial", 14, "bold")).grid(
            row=row, column=1, padx=10, pady=5, sticky="ew"
        )
        row += 1
        
        # Optional website and Twitter inputs
        ctk.CTkLabel(self, text="Website (optional):", font=("Arial", 14)).grid(
            row=row, column=0, sticky="w", padx=10
        )
        self.website_var = ctk.StringVar(value=project_data.get("website", ""))
        ctk.CTkEntry(self, textvariable=self.website_var, width=200, font=("Arial", 14, "bold")).grid(
            row=row, column=1, padx=10, pady=5, sticky="ew"
        )
        ctk.CTkLabel(self, text="Twitter / X (optional):", font=("Arial", 14)).grid(
            row=row, column=2, sticky="w", padx=10
        )
        self.twitter_var = ctk.StringVar(value=project_data.get("twitter", ""))
        ctk.CTkEntry(self, textvariable=self.twitter_var, width=200, font=("Arial", 14, "bold")).grid(
            row=row, column=3, padx=10, pady=5, sticky="ew"
        )
        row += 1
        
        # Category dropdown
        ctk.CTkLabel(self, text="Category:", font=("Arial", 14)).grid(
            row=row, column=0, sticky="w", padx=10
        )
        self.category_var = ctk.StringVar(value=project_data.get("category", PROJECT_CATEGORIES[0]))
        self.category_menu = ctk.CTkOptionMenu(self, values=PROJECT_CATEGORIES, variable=self.category_var, width=200, font=("Arial", 14, "bold"))
        self.category_menu.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Tags input and suggestions (minimum 2 tags required)
        ctk.CTkLabel(self, text="Tags (min. 2):", font=("Arial", 14)).grid(
            row=row, column=0, sticky="w", padx=10
        )
        tag_frame = ctk.CTkFrame(self, width=300)
        tag_frame.grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        num_tags = 3
        gap_width = 5
        tag_field_width = int((300 - (num_tags - 1) * gap_width) / num_tags * 1.8)
        self.tag1_var = ctk.StringVar(value=project_data.get("tag1", ""))
        self.tag2_var = ctk.StringVar(value=project_data.get("tag2", ""))
        self.tag3_var = ctk.StringVar(value=project_data.get("tag3", ""))
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
        
        ctk.CTkLabel(self, text="Tag Suggestions:", font=("Arial", 14)).grid(
            row=row, column=0, sticky="w", padx=10
        )
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
        
        # Logo image input
        ctk.CTkLabel(self, text="Logo Image:", font=("Arial", 14)).grid(
            row=row, column=0, sticky="w", padx=10
        )
        self.image_path_var = ctk.StringVar(value=project_data.get("image_path", ""))
        ctk.CTkEntry(self, textvariable=self.image_path_var, width=200, font=("Arial", 14, "bold")).grid(
            row=row, column=1, padx=10, pady=5, sticky="ew"
        )
        ctk.CTkButton(self, text="Select Image", command=self.select_image, width=120, font=("Arial", 14, "bold")).grid(
            row=row, column=2, padx=10, pady=5
        )
        row += 1
        
        # Description input (multiline)
        ctk.CTkLabel(self, text="Description:", font=("Arial", 14)).grid(
            row=row, column=0, sticky="nw", padx=10
        )
        self.description_textbox = ctk.CTkTextbox(self, width=400, height=100)
        self.description_textbox.grid(row=row, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        if "description" in project_data:
            self.description_textbox.insert("1.0", project_data.get("description"))
        row += 1
        
        # Buttons for creating project and going back
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=4, pady=20, sticky="ew")
        ctk.CTkButton(button_frame, text="Create Project", command=self.create_project, font=("Arial", 14, "bold")).pack(side="left", padx=10, expand=True)
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
        self.settings["project_data"] = {
            "folder_name": self.folder_name_var.get(),
            "project_name": self.project_name_var.get(),
            "website": self.website_var.get(),
            "twitter": self.twitter_var.get(),
            "category": self.category_var.get(),
            "tag1": self.tag1_var.get(),
            "tag2": self.tag2_var.get(),
            "tag3": self.tag3_var.get(),
            "image_path": self.image_path_var.get(),
            "description": self.description_textbox.get("1.0", "end").strip()
        }
    
    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Logo Image", 
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp")]
        )
        if file_path:
            self.image_path_var.set(file_path)
    
    def create_project(self):
        folder_name = self.folder_name_var.get().strip()
        if not folder_name or not re.match(r'^[a-z0-9\-]+$', folder_name):
            messagebox.showerror("Error", "Invalid folder name. Use only lowercase letters, digits, and dashes.")
            return
        
        project_name = self.project_name_var.get().strip()
        if not project_name:
            messagebox.showerror("Error", "Please enter the project name.")
            return
        
        projects_dir = os.path.join(self.base_path, "resources", "projects")
        create_directory(projects_dir)
        new_folder = os.path.join(projects_dir, folder_name)
        if os.path.exists(new_folder):
            counter = 2
            while os.path.exists(f"{new_folder}-{counter}"):
                counter += 1
            folder_name = f"{folder_name}-{counter}"
            new_folder = os.path.join(projects_dir, folder_name)
        
        tags = [t.strip() for t in [self.tag1_var.get(), self.tag2_var.get(), self.tag3_var.get()] if t.strip()]
        if len(tags) < 2:
            messagebox.showerror("Error", "Please enter at least two tags for the project.")
            return
        allowed_tags = load_allowed_tags(self.base_path)
        for tag in tags:
            if tag not in allowed_tags:
                messagebox.showerror("Error", f"Tag '{tag}' is not valid. Please select a valid tag from the suggestions.")
                return
        
        if not self.image_path_var.get().strip():
            messagebox.showerror("Error", "Please select a logo image.")
            return
        
        description = self.description_textbox.get("1.0", "end").strip()
        if not description:
            messagebox.showerror("Error", "Please enter a project description.")
            return
        
        try:
            create_directory(new_folder)
            assets_dir = os.path.join(new_folder, "assets")
            create_directory(assets_dir)
            logo_source = self.image_path_var.get().strip()
            if logo_source and os.path.exists(logo_source):
                dest_logo = os.path.join(assets_dir, "logo.webp")
                process_profile_image(logo_source, dest_logo)
            
            project_uuid = str(uuid.uuid4())
            
            website = self.website_var.get().strip()
            twitter = self.twitter_var.get().strip()
            category = self.category_var.get().strip()
            language_code = self.settings.get("language", "en").split(" ")[0]
            current_date = datetime.date.today().strftime("%Y-%m-%d")
            global_contributor = self.settings.get("contributor_id", "").strip()
            
            project_yaml_content = create_project_yaml(
                project_uuid,
                project_name,
                website,
                twitter,
                category,
                tags,
                language_code,
                current_date,
                global_contributor
            )
            project_yaml_path = os.path.join(new_folder, "project.yml")
            write_file(project_yaml_path, project_yaml_content)
            
            professor_global = self.settings.get("professor_id", "").strip()
            lang_yaml_content = create_project_language_yaml(
                language_code,
                description,
                professor_global
            )
            lang_yaml_path = os.path.join(new_folder, f"{language_code}.yml")
            write_file(lang_yaml_path, lang_yaml_content)
            
            messagebox.showinfo("Success", f"Project created successfully in:\n{new_folder}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def update_local_state(self):
        self.settings["project_data"] = {
            "folder_name": self.folder_name_var.get(),
            "project_name": self.project_name_var.get(),
            "website": self.website_var.get(),
            "twitter": self.twitter_var.get(),
            "category": self.category_var.get(),
            "tag1": self.tag1_var.get(),
            "tag2": self.tag2_var.get(),
            "tag3": self.tag3_var.get(),
            "image_path": self.image_path_var.get(),
            "description": self.description_textbox.get("1.0", "end").strip()
        }
    
    def go_back(self):
        self.update_local_state()
        from gui.home import HomePage
        self.destroy()
        home_page = HomePage(self.parent, self.settings)
        home_page.pack(fill="both", expand=True)
