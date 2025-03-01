import os
import re
import customtkinter as ctk
from tkinter import messagebox
from utils.constants import SECTIONS, LEVELS, MAIN_LANGUAGE_OPTIONS, OTHER_LANGUAGE_OPTIONS
from utils.data_loader import load_allowed_tags, load_all_builders
from utils.file_ops import create_tutorial_files

class TutorialPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = self.settings.get("base_path", "")
        
        # Variables
        self.language_option_var = ctk.IntVar(value=self.settings.get("language_option", 1))
        self.language_var = ctk.StringVar(value=self.settings.get("language", ""))
        self.section_var = ctk.StringVar()
        self.category_var = ctk.StringVar()
        self.level_var = ctk.StringVar()
        self.tutorial_name_var = ctk.StringVar()
        self.builder_search_var = ctk.StringVar()
        self.project_id_var = ctk.StringVar()
        self.tag1_var = ctk.StringVar()
        self.tag2_var = ctk.StringVar()
        self.tag3_var = ctk.StringVar()
        self.contributor_id_var = ctk.StringVar(value=self.settings.get("contributor_id", ""))
        self.professor_id_var = ctk.StringVar(value=self.settings.get("professor_id", ""))
        
        # Global mapping for builders
        self.builders_mapping = {}
        
        # Layout construction
        row = 0
        ctk.CTkLabel(self, text=f"Base path: {self.base_path}").grid(row=row, column=0, columnspan=3, padx=10, pady=5, sticky="w")
        row += 1
        
        # Language selection
        ctk.CTkLabel(self, text="Language:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        language_frame = ctk.CTkFrame(self, fg_color="transparent")
        language_frame.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        ctk.CTkRadioButton(language_frame, text="Main languages", variable=self.language_option_var, value=1, command=self.update_language_options).pack(side="left", padx=5)
        ctk.CTkRadioButton(language_frame, text="Other languages", variable=self.language_option_var, value=2, command=self.update_language_options).pack(side="left", padx=5)
        row += 1
        
        # Language menu
        ctk.CTkLabel(self, text="Language selection:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.language_menu = ctk.CTkOptionMenu(self, values=[], variable=self.language_var, width=300)
        self.language_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        self.update_language_options()
        row += 1
        
        # Category selection
        ctk.CTkLabel(self, text="Category:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.section_menu = ctk.CTkOptionMenu(self, values=list(SECTIONS.keys()), variable=self.section_var, command=self.update_categories, width=300)
        self.section_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="Subcategory:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.category_menu = ctk.CTkOptionMenu(self, values=[], variable=self.category_var, width=300)
        self.category_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        # Difficulty level
        ctk.CTkLabel(self, text="Difficulty level:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.level_menu = ctk.CTkOptionMenu(self, values=LEVELS, variable=self.level_var, width=300)
        self.level_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        # Folder name for tutorial
        ctk.CTkLabel(self, text="Folder name:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.tutorial_name_var, width=300).grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        # Project Name (search)
        ctk.CTkLabel(self, text="Project Name:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.builder_search_entry = ctk.CTkEntry(self, textvariable=self.builder_search_var, width=300, placeholder_text="Find the project ID")
        self.builder_search_entry.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        self.builder_search_entry.bind("<KeyRelease>", self.update_builder_suggestions)
        row += 1
        
        # Project Suggestions
        ctk.CTkLabel(self, text="Project Suggestions:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.builder_suggestions_menu = ctk.CTkOptionMenu(self, values=[], command=self.on_builder_selected, width=300)
        self.builder_suggestions_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        self.update_builder_suggestions()
        row += 1
        
        # Project ID
        ctk.CTkLabel(self, text="Project ID:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.project_id_var, width=300).grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        # Tags input
        ctk.CTkLabel(self, text="Tags (2 ou 3):").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        tag_frame = ctk.CTkFrame(self, width=300)
        tag_frame.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        num_tags = 3
        gap_width = 5
        total_gaps = (num_tags - 1) * gap_width
        tag_field_width = int((300 - total_gaps) / num_tags)
        
        self.tag1_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag1_var, width=tag_field_width)
        self.tag1_entry.grid(row=0, column=0, padx=(0, gap_width), sticky="w")
        self.tag1_entry.bind("<KeyRelease>", self.update_tag1_suggestions)
        
        self.tag2_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag2_var, width=tag_field_width)
        self.tag2_entry.grid(row=0, column=1, padx=(0, gap_width), sticky="w")
        self.tag2_entry.bind("<KeyRelease>", self.update_tag2_suggestions)
        
        self.tag3_entry = ctk.CTkEntry(tag_frame, textvariable=self.tag3_var, width=tag_field_width)
        self.tag3_entry.grid(row=0, column=2, sticky="w")
        self.tag3_entry.bind("<KeyRelease>", self.update_tag3_suggestions)
        row += 1
        
        # Tag suggestions menus
        ctk.CTkLabel(self, text="Tag Suggestions:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        tag_suggestion_frame = ctk.CTkFrame(self, width=300)
        tag_suggestion_frame.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        self.tag1_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag1_selected, width=tag_field_width)
        self.tag1_suggestions_menu.grid(row=0, column=0, padx=(0, gap_width), sticky="w")
        self.tag2_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag2_selected, width=tag_field_width)
        self.tag2_suggestions_menu.grid(row=0, column=1, padx=(0, gap_width), sticky="w")
        self.tag3_suggestions_menu = ctk.CTkOptionMenu(tag_suggestion_frame, values=[], command=self.on_tag3_selected, width=tag_field_width)
        self.tag3_suggestions_menu.grid(row=0, column=2, sticky="w")
        self.update_tag1_suggestions()
        self.update_tag2_suggestions()
        self.update_tag3_suggestions()
        row += 1
        
        # Contributor and professor IDs
        ctk.CTkLabel(self, text="Contributor's GitHub ID:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.contributor_id_var, width=300).grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="PBN professor's ID:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.professor_id_var, width=300).grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        # Buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=3, pady=20)
        ctk.CTkButton(button_frame, text="Create Tutorial", command=self.create_tutorial).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Clear", command=self.clear_fields).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Back", command=self.go_back).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Toggle Theme", command=self.toggle_theme).pack(side="left", padx=10)
    
    def update_language_options(self):
        if self.language_option_var.get() == 1:
            self.language_menu.configure(values=MAIN_LANGUAGE_OPTIONS)
            if self.language_var.get() not in MAIN_LANGUAGE_OPTIONS:
                self.language_var.set(MAIN_LANGUAGE_OPTIONS[0])
        else:
            self.language_menu.configure(values=OTHER_LANGUAGE_OPTIONS)
            if self.language_var.get() not in OTHER_LANGUAGE_OPTIONS:
                self.language_var.set(OTHER_LANGUAGE_OPTIONS[0])
    
    def update_categories(self, *args):
        section = self.section_var.get()
        categories = SECTIONS.get(section, [])
        self.category_menu.configure(values=categories)
        if categories:
            self.category_var.set(categories[0])
        else:
            self.category_var.set("")
    
    def update_builder_suggestions(self, event=None):
        search_text = self.builder_search_var.get().lower()
        self.builders_mapping = load_all_builders(self.base_path)
        suggestions = [name for name in self.builders_mapping.keys() if search_text in name.lower()]
        if suggestions:
            self.builder_suggestions_menu.configure(values=suggestions)
            self.builder_suggestions_menu.set(suggestions[0])
        else:
            self.builder_suggestions_menu.configure(values=["No match"])
            self.builder_suggestions_menu.set("No match")
    
    def on_builder_selected(self, selected_name):
        if selected_name in self.builders_mapping:
            self.project_id_var.set(self.builders_mapping[selected_name])
            self.builder_search_var.set(selected_name)
    
    def update_tag1_suggestions(self, event=None):
        text = self.tag1_var.get().lower()
        allowed = load_allowed_tags(self.base_path)
        suggestions = [t for t in allowed if text in t.lower()]
        if suggestions:
            self.tag1_suggestions_menu.configure(values=suggestions)
            self.tag1_suggestions_menu.set(suggestions[0])
        else:
            self.tag1_suggestions_menu.configure(values=["No match"])
            self.tag1_suggestions_menu.set("No match")
    
    def update_tag2_suggestions(self, event=None):
        text = self.tag2_var.get().lower()
        allowed = load_allowed_tags(self.base_path)
        suggestions = [t for t in allowed if text in t.lower()]
        if suggestions:
            self.tag2_suggestions_menu.configure(values=suggestions)
            self.tag2_suggestions_menu.set(suggestions[0])
        else:
            self.tag2_suggestions_menu.configure(values=["No match"])
            self.tag2_suggestions_menu.set("No match")
    
    def update_tag3_suggestions(self, event=None):
        text = self.tag3_var.get().lower()
        allowed = load_allowed_tags(self.base_path)
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
    
    def create_tutorial(self):
        # Validate inputs
        if not self.base_path:
            messagebox.showerror("Error", "Please select the local base path for the repository.")
            return
        if not self.language_var.get():
            messagebox.showerror("Error", "Please select a language.")
            return
        language_code = self.language_var.get().split(" ")[0]
        if not self.section_var.get():
            messagebox.showerror("Error", "Please select the tutorial section.")
            return
        if not self.tutorial_name_var.get():
            messagebox.showerror("Error", "Please enter the folder name for the tutorial.")
            return
        project_id = self.project_id_var.get().strip()
        if not project_id:
            messagebox.showerror("Error", "Please enter the project's ID (UUID).")
            return
        
        # Validate project existence
        parent_dir = os.path.dirname(self.base_path)
        builders_dir = os.path.join(parent_dir, "resources", "projects")
        if not os.path.exists(builders_dir):
            messagebox.showerror("Error", f"The projects directory does not exist at:\n{builders_dir}")
            return
        found = False
        builder_display_name = None
        for d in os.listdir(builders_dir):
            sub_dir = os.path.join(builders_dir, d)
            if os.path.isdir(sub_dir):
                builder_file = os.path.join(sub_dir, "project.yml")
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
            answer = messagebox.askyesno("Confirm Project",
                                         f"The project with ID {project_id} is named '{builder_display_name}'.\nDo you want to continue?")
            if not answer:
                return
        else:
            answer = messagebox.askyesno("Project Not Found",
                                         f"No project with ID {project_id} was found.\nDo you want to continue anyway?")
            if not answer:
                return
        
        if not self.level_var.get():
            messagebox.showerror("Error", "Please select the tutorial's difficulty level.")
            return
        
        tags = [tag.strip() for tag in [self.tag1_var.get(), self.tag2_var.get(), self.tag3_var.get()] if tag.strip()]
        if len(tags) < 2:
            messagebox.showerror("Error", "Please enter at least two tags for the tutorial.")
            return
        if len(set(tags)) != len(tags):
            messagebox.showerror("Error", "Duplicate tags detected. Please ensure all tags are unique.")
            return
        allowed_tags = load_allowed_tags(self.base_path)
        for tag in tags:
            if tag not in allowed_tags:
                messagebox.showerror("Error", f"Tag '{tag}' is not valid. Please select a valid tag from the suggestions.")
                return
        
        if not self.category_var.get():
            messagebox.showerror("Error", "Please select the subcategory.")
            return
        if not self.contributor_id_var.get().strip():
            messagebox.showerror("Error", "Please enter the contributor's GitHub ID.")
            return
        if not self.professor_id_var.get().strip():
            messagebox.showerror("Error", "Please enter the PBN professor's ID.")
            return
        
        # Save updated settings
        self.settings["language_option"] = self.language_option_var.get()
        self.settings["language"] = self.language_var.get()
        self.settings["contributor_id"] = self.contributor_id_var.get()
        self.settings["professor_id"] = self.professor_id_var.get()
        
        try:
            tutorial_path = create_tutorial_files(
                base=self.base_path,
                section_name=self.section_var.get(),
                tutorial_name=self.tutorial_name_var.get(),
                language_code=language_code,
                project_id=project_id,
                tags=tags,
                category_value=self.category_var.get(),
                level_value=self.level_var.get(),
                professor_id=self.professor_id_var.get(),
                contributor_id=self.contributor_id_var.get()
            )
            messagebox.showinfo("Success", f"Tutorial successfully created in the folder:\n{tutorial_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def clear_fields(self):
        answer = messagebox.askyesno("Confirmation", "Are you sure you want to erase all data?")
        if answer:
            self.language_option_var.set(1)
            self.update_language_options()
            self.language_var.set("")
            self.section_var.set("")
            self.category_var.set("")
            self.level_var.set("")
            self.tutorial_name_var.set("")
            self.builder_search_var.set("")
            self.builder_suggestions_menu.set("")
            self.project_id_var.set("")
            self.tag1_var.set("")
            self.tag2_var.set("")
            self.tag3_var.set("")
            self.contributor_id_var.set("")
            self.professor_id_var.set("")
    
    def go_back(self):
        from gui.home import HomePage
        self.destroy()
        home_page = HomePage(self.parent, self.settings)
        home_page.pack(fill="both", expand=True)
    
    def toggle_theme(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        self.settings["theme"] = new_mode
