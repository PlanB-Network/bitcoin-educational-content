import customtkinter as ctk
from tkinter import filedialog
from gui.footer import create_footer
from gui.tutorial_page import TutorialPage
from gui.professor_page import ProfessorPage
from gui.project_page import ProjectPage
from utils.constants import MAIN_LANGUAGE_OPTIONS, OTHER_LANGUAGE_OPTIONS

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings

        # Distribute space across rows/columns for a modern layout
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        # Row 0: Local repository path
        self.base_path_var = ctk.StringVar(value=self.settings.get("base_path", ""))
        ctk.CTkLabel(
            self,
            text="Local repository path:",
            font=("Arial", 14)
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.base_path_entry = ctk.CTkEntry(
            self,
            textvariable=self.base_path_var,
            width=320
        )
        self.base_path_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkButton(
            self,
            text="Browse",
            command=self.select_base_path,
            width=120,
            height=40,
            font=("Arial", 14, "bold")
        ).grid(row=0, column=2, padx=10, pady=5)

        # Row 1: Language option (Main vs Other)
        self.language_option_var = ctk.IntVar(value=self.settings.get("language_option", 1))
        self.language_option_var.trace_add("write", lambda *args: self.update_language_options())

        ctk.CTkLabel(
            self,
            text="Language Option:",
            font=("Arial", 14)
        ).grid(row=1, column=0, padx=10, pady=5, sticky="w")

        language_frame = ctk.CTkFrame(self, fg_color="transparent")
        language_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        ctk.CTkRadioButton(
            language_frame,
            text="Main Languages",
            variable=self.language_option_var,
            value=1,
            font=("Arial", 12, "bold")
        ).pack(side="left", padx=5)

        ctk.CTkRadioButton(
            language_frame,
            text="Other Languages",
            variable=self.language_option_var,
            value=2,
            font=("Arial", 12, "bold")
        ).pack(side="left", padx=5)

        # Row 2: Language selection dropdown
        self.language_var = ctk.StringVar(value=self.settings.get("language", MAIN_LANGUAGE_OPTIONS[0]))
        ctk.CTkLabel(
            self,
            text="Language Selection:",
            font=("Arial", 14)
        ).grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.language_menu = ctk.CTkOptionMenu(
            self,
            values=MAIN_LANGUAGE_OPTIONS,
            variable=self.language_var,
            width=320,
            font=("Arial", 14, "bold")
        )
        self.language_menu.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.update_language_options()

        # Row 3: Contributor's GitHub ID
        self.contributor_id_var = ctk.StringVar(value=self.settings.get("contributor_id", ""))
        ctk.CTkLabel(
            self,
            text="Contributor's GitHub ID:",
            font=("Arial", 14)
        ).grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.contributor_entry = ctk.CTkEntry(
            self,
            textvariable=self.contributor_id_var,
            width=320,
            font=("Arial", 14, "bold")
        )
        self.contributor_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        # Row 4: PBN Professor's ID
        self.professor_id_var = ctk.StringVar(value=self.settings.get("professor_id", ""))
        ctk.CTkLabel(
            self,
            text="PBN Professor's ID:",
            font=("Arial", 14)
        ).grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.professor_entry = ctk.CTkEntry(
            self,
            textvariable=self.professor_id_var,
            width=320,
            font=("Arial", 14, "bold")
        )
        self.professor_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        # Row 5: Control buttons for resource creation (Tutorial, Professor, Project)
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")
        button_frame.grid_rowconfigure(0, weight=1)
        for j in range(3):
            button_frame.grid_columnconfigure(j, weight=1)

        # Reduce button height by about 40% (from 70 to ~42)
        self.tutorial_button = ctk.CTkButton(
            button_frame,
            text="New Tutorial",
            command=self.open_tutorial_page,
            width=220,
            height=42,
            font=("Arial", 16, "bold")
        )
        self.tutorial_button.grid(row=0, column=0, padx=20, pady=20)

        self.professor_button = ctk.CTkButton(
            button_frame,
            text="New Professor",
            command=self.open_professor_page,
            width=220,
            height=42,
            font=("Arial", 16, "bold")
        )
        self.professor_button.grid(row=0, column=1, padx=20, pady=20)

        self.project_button = ctk.CTkButton(
            button_frame,
            text="New Project",
            command=self.open_project_page,
            width=220,
            height=42,
            font=("Arial", 16, "bold")
        )
        self.project_button.grid(row=0, column=2, padx=20, pady=20)

        create_footer(self)

        # Set this page as the active page
        self.master.active_page = self

    def update_language_options(self):
        if self.language_option_var.get() == 1:
            self.language_menu.configure(values=MAIN_LANGUAGE_OPTIONS)
            if self.language_var.get() not in MAIN_LANGUAGE_OPTIONS:
                self.language_var.set(MAIN_LANGUAGE_OPTIONS[0])
        else:
            self.language_menu.configure(values=OTHER_LANGUAGE_OPTIONS)
            if self.language_var.get() not in OTHER_LANGUAGE_OPTIONS:
                self.language_var.set(OTHER_LANGUAGE_OPTIONS[0])

    def select_base_path(self):
        path = filedialog.askdirectory()
        if path:
            self.base_path_var.set(path)
            self.settings["base_path"] = path

    def update_settings(self):
        """Updates the global settings with current page values."""
        self.settings["base_path"] = self.base_path_var.get()
        self.settings["language_option"] = self.language_option_var.get()
        self.settings["language"] = self.language_var.get()
        self.settings["contributor_id"] = self.contributor_id_var.get()
        self.settings["professor_id"] = self.professor_id_var.get()

    def open_tutorial_page(self):
        self.update_settings()
        self.destroy()
        tutorial_page = TutorialPage(self.parent, self.settings)
        tutorial_page.pack(fill="both", expand=True)
        self.master.active_page = tutorial_page

    def open_professor_page(self):
        self.update_settings()
        self.destroy()
        from gui.professor_page import ProfessorPage
        professor_page = ProfessorPage(self.parent, self.settings)
        professor_page.pack(fill="both", expand=True)
        self.master.active_page = professor_page

    def open_project_page(self):
        self.update_settings()
        self.destroy()
        from gui.project_page import ProjectPage
        project_page = ProjectPage(self.parent, self.settings)
        project_page.pack(fill="both", expand=True)
        self.master.active_page = project_page
