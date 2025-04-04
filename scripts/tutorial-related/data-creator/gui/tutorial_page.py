import customtkinter as ctk
from tkinter import messagebox, filedialog
from utils.constants import SECTIONS, LEVELS
from utils.data_loader import load_allowed_tags, load_all_builders
from utils.file_ops import create_tutorial_files
from gui.footer import create_footer


class TutorialPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = self.settings.get("base_path", "")
        
        # Set this page as the active page
        self.master.active_page = self

        # Retrieve saved tutorial data if available
        tutorial_data = self.settings.get("tutorial_data", {})

        # Initialize variables with saved values if present
        self.section_var = ctk.StringVar(value=tutorial_data.get("section", ""))
        self.category_var = ctk.StringVar(value=tutorial_data.get("subcategory", ""))
        self.level_var = ctk.StringVar(value=tutorial_data.get("difficulty", ""))
        self.tutorial_name_var = ctk.StringVar(value=tutorial_data.get("tutorial_name", ""))
        self.builder_search_var = ctk.StringVar(value=tutorial_data.get("builder_search", ""))
        self.project_id_var = ctk.StringVar(value=tutorial_data.get("project_id", ""))
        self.tag1_var = ctk.StringVar(value=tutorial_data.get("tag1", ""))
        self.tag2_var = ctk.StringVar(value=tutorial_data.get("tag2", ""))
        self.tag3_var = ctk.StringVar(value=tutorial_data.get("tag3", ""))
        
        # Set up grid layout
        total_rows = 12
        for i in range(total_rows):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)
        
        row = 0
        ctk.CTkLabel(self, text="New Tutorial Creation", font=("Arial", 20, "bold")).grid(row=row, column=0, columnspan=4, pady=10)
        row += 1
        
        # Category and subcategory selection
        ctk.CTkLabel(self, text="Category:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.section_menu = ctk.CTkOptionMenu(
            self,
            values=list(SECTIONS.keys()),
            variable=self.section_var,
            command=self.update_categories,
            width=300,
            font=("Arial", 14, "bold")
        )
        self.section_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        row += 1
        
        ctk.CTkLabel(self, text="Subcategory:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.category_menu = ctk.CTkOptionMenu(self, values=[], variable=self.category_var, width=300, font=("Arial", 14, "bold"))
        self.category_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Difficulty level selection
        ctk.CTkLabel(self, text="Difficulty level:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.level_menu = ctk.CTkOptionMenu(self, values=LEVELS, variable=self.level_var, width=300, font=("Arial", 14, "bold"))
        self.level_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Tutorial folder name entry
        ctk.CTkLabel(self, text="Folder name:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.tutorial_name_var, width=300, font=("Arial", 14, "bold")).grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Project search entry
        ctk.CTkLabel(self, text="Project Name:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.builder_search_entry = ctk.CTkEntry(self, textvariable=self.builder_search_var, width=300, placeholder_text="Find the project ID", font=("Arial", 14, "bold"))
        self.builder_search_entry.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.builder_search_entry.bind("<KeyRelease>", self.update_builder_suggestions)
        row += 1
        
        # Project suggestions dropdown
        ctk.CTkLabel(self, text="Project Suggestions:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.builder_suggestions_menu = ctk.CTkOptionMenu(self, values=[], command=self.on_builder_selected, width=300, font=("Arial", 14, "bold"))
        self.builder_suggestions_menu.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.update_builder_suggestions()
        row += 1
        
        # Project ID entry
        ctk.CTkLabel(self, text="Project ID:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.project_id_var, width=300, font=("Arial", 14, "bold")).grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Tags entry and suggestions with fixed width
        ctk.CTkLabel(self, text="Tags (2 or 3):").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        tag_frame = ctk.CTkFrame(self, width=300)
        tag_frame.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        num_tags = 3
        gap_width = 5
        tag_field_width = int((300 - (num_tags - 1) * gap_width) / num_tags * 1.8)
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
        
        ctk.CTkLabel(self, text="Tag Suggestions:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        tag_suggestion_frame = ctk.CTkFrame(self, width=300)
        tag_suggestion_frame.grid(row=row, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
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
        
        # Buttons for Create, Clear, and Back actions
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=3, pady=20, sticky="ew")
        ctk.CTkButton(button_frame, text="Create Tutorial", command=self.create_tutorial, font=("Arial", 14, "bold")).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(button_frame, text="Clear", command=self.clear_fields, font=("Arial", 14, "bold")).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(button_frame, text="Back", command=self.go_back, font=("Arial", 14, "bold")).pack(side="left", padx=10, expand=True)
    
        create_footer(self)

    def update_categories(self, *args):
        section = self.section_menu.get()
        categories = SECTIONS.get(section, [])
        self.category_menu.configure(values=categories)
        if categories:
            self.category_menu.set(categories[0])
        else:
            self.category_menu.set("")
    
    def update_builder_suggestions(self, event=None):
        search_text = self.builder_search_var.get().lower()
        builders_mapping = load_all_builders(self.base_path)
        suggestions = [name for name in builders_mapping.keys() if search_text in name.lower()]
        if suggestions:
            self.builder_suggestions_menu.configure(values=suggestions)
            self.builder_suggestions_menu.set(suggestions[0])
        else:
            self.builder_suggestions_menu.configure(values=["No match"])
            self.builder_suggestions_menu.set("No match")
    
    def on_builder_selected(self, selected_name):
        builders_mapping = load_all_builders(self.base_path)
        if selected_name in builders_mapping:
            self.project_id_var.set(builders_mapping[selected_name])
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
    
    def create_tutorial(self):
        if not self.base_path:
            messagebox.showerror("Error", "Please select the local base path for the repository.")
            return
        if not self.section_menu.get():
            messagebox.showerror("Error", "Please select the tutorial section.")
            return
        if not self.tutorial_name_var.get():
            messagebox.showerror("Error", "Please enter the folder name for the tutorial.")
            return
        project_id = self.project_id_var.get().strip()
        if not project_id:
            messagebox.showerror("Error", "Please enter the project's ID (UUID).")
            return
        
        # Validate tutorial difficulty selection
        if not self.level_menu.get():
            messagebox.showerror("Error", "Please select the tutorial's difficulty level.")
            return
        
        tags = [t.strip() for t in [self.tag1_var.get(), self.tag2_var.get(), self.tag3_var.get()] if t.strip()]
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
        if not self.category_menu.get():
            messagebox.showerror("Error", "Please select the subcategory.")
            return
        
        # Retrieve global settings
        language = self.settings.get("language", "")
        if not language:
            messagebox.showerror("Error", "Global language setting is missing.")
            return
        language_code = language.split(" ")[0]
        contributor_id = self.settings.get("contributor_id", "").strip()
        professor_id = self.settings.get("professor_id", "").strip()
        if not contributor_id:
            messagebox.showerror("Error", "Global contributor's GitHub ID is missing.")
            return
        if not professor_id:
            messagebox.showerror("Error", "Global PBN professor's ID is missing.")
            return
        
        try:
            tutorial_path = create_tutorial_files(
                base=self.base_path,
                section_name=self.section_menu.get(),
                tutorial_name=self.tutorial_name_var.get(),
                language_code=language_code,
                project_id=project_id,
                tags=tags,
                category_value=self.category_menu.get(),
                level_value=self.level_menu.get(),
                professor_id=professor_id,
                contributor_id=contributor_id
            )
            messagebox.showinfo("Success", f"Tutorial successfully created in the folder:\n{tutorial_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def clear_fields(self):
        answer = messagebox.askyesno("Confirmation", "Are you sure you want to erase all data?")
        if answer:
            self.section_menu.set("")
            self.category_menu.set("")
            self.level_menu.set("")
            self.tutorial_name_var.set("")
            self.builder_search_var.set("")
            self.builder_suggestions_menu.set("")
            self.project_id_var.set("")
            self.tag1_var.set("")
            self.tag2_var.set("")
            self.tag3_var.set("")
    
    def update_local_state(self):
        """Save current tutorial data for later reuse."""
        self.settings["tutorial_data"] = {
            "section": self.section_menu.get(),
            "subcategory": self.category_menu.get(),
            "difficulty": self.level_menu.get(),
            "tutorial_name": self.tutorial_name_var.get(),
            "builder_search": self.builder_search_var.get(),
            "project_id": self.project_id_var.get(),
            "tag1": self.tag1_var.get(),
            "tag2": self.tag2_var.get(),
            "tag3": self.tag3_var.get()
        }
    
    def go_back(self):
        # Save state before returning to home page
        self.update_local_state()
        from gui.home import HomePage
        self.destroy()
        home_page = HomePage(self.parent, self.settings)
        home_page.pack(fill="both", expand=True)
