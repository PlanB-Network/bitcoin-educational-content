import customtkinter as ctk
from tkinter import filedialog, messagebox

from gui.footer import create_footer
from gui.tutorial_page import TutorialPage
from gui.professor_page import ProfessorPage
from gui.project_page import ProjectPage

from utils.constants import MAIN_LANGUAGE_OPTIONS, OTHER_LANGUAGE_OPTIONS
from utils.data_loader import load_all_professors

from utils.path_utils import normalize_base_path
from utils.repo_validator import validate_repo_root


class HomePage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.repo_ok = False
        self.last_validation = {"ok": False, "path": "", "issues": ["No repository path selected."]}

        # Rows: 0..8 (we added a status row)
        for i in range(9):
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

        # Normalize on Enter / when leaving the field (no cursor jump while typing)
        self.base_path_entry.bind("<Return>", lambda _e: self.commit_base_path())
        self.base_path_entry.bind("<FocusOut>", lambda _e: self.commit_base_path())

        ctk.CTkButton(
            self,
            text="Browse",
            command=self.select_base_path,
            width=120,
            height=40,
            font=("Arial", 14, "bold")
        ).grid(row=0, column=2, padx=10, pady=5)

        # Row 1: Blocking repo status message (hidden when OK)
        self.repo_status_frame = ctk.CTkFrame(self, corner_radius=10)
        self.repo_status_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="ew")

        self.repo_status_title = ctk.CTkLabel(
            self.repo_status_frame,
            text="Repository check failed",
            font=("Arial", 14, "bold"),
            anchor="w",
            justify="left"
        )
        self.repo_status_title.grid(row=0, column=0, padx=12, pady=(10, 2), sticky="ew")

        self.repo_status_details = ctk.CTkLabel(
            self.repo_status_frame,
            text="",
            font=("Arial", 12),
            anchor="w",
            justify="left",
            wraplength=800
        )
        self.repo_status_details.grid(row=1, column=0, padx=12, pady=(0, 10), sticky="ew")

        self.repo_status_frame.grid_columnconfigure(0, weight=1)

        # Row 2: Language option (Main vs Other)
        self.language_option_var = ctk.IntVar(value=self.settings.get("language_option", 1))
        self.language_option_var.trace_add("write", lambda *args: self.update_language_options())

        ctk.CTkLabel(
            self,
            text="Language Option:",
            font=("Arial", 14)
        ).grid(row=2, column=0, padx=10, pady=5, sticky="w")

        language_frame = ctk.CTkFrame(self, fg_color="transparent")
        language_frame.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

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

        # Row 3: Language selection dropdown
        self.language_var = ctk.StringVar(value=self.settings.get("language", MAIN_LANGUAGE_OPTIONS[0]))
        ctk.CTkLabel(
            self,
            text="Language Selection:",
            font=("Arial", 14)
        ).grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.language_menu = ctk.CTkOptionMenu(
            self,
            values=MAIN_LANGUAGE_OPTIONS,
            variable=self.language_var,
            width=320,
            font=("Arial", 14, "bold")
        )
        self.language_menu.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.update_language_options()

        # Row 4: Contributor's GitHub ID
        self.contributor_id_var = ctk.StringVar(value=self.settings.get("contributor_id", ""))
        ctk.CTkLabel(
            self,
            text="Contributor's GitHub ID:",
            font=("Arial", 14)
        ).grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.contributor_entry = ctk.CTkEntry(
            self,
            textvariable=self.contributor_id_var,
            width=320,
            font=("Arial", 14, "bold")
        )
        self.contributor_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        # Row 5: Professor Name
        self.professor_search_var = ctk.StringVar(value=self.settings.get("professor_name", ""))

        ctk.CTkLabel(
            self,
            text="Professor Name:",
            font=("Arial", 14)
        ).grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.professor_search_entry = ctk.CTkEntry(
            self,
            textvariable=self.professor_search_var,
            width=100,
            font=("Arial", 14, "bold"),
            placeholder_text="Search by name"
        )
        self.professor_search_entry.grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.professor_search_entry.bind("<KeyRelease>", self.update_professor_suggestions)

        ctk.CTkLabel(
            self,
            text="Prof. Suggestions:",
            font=("Arial", 14)
        ).grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.professor_suggestions_menu = ctk.CTkOptionMenu(
            self,
            values=[],
            command=self.on_professor_selected,
            width=180,
            font=("Arial", 14, "bold")
        )
        self.professor_suggestions_menu.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        # Row 7: Professor’s UUID
        self.professor_id_var = ctk.StringVar(value=self.settings.get("professor_id", ""))

        ctk.CTkLabel(
            self,
            text="Professor's UUID:",
            font=("Arial", 14)
        ).grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.professor_id_entry = ctk.CTkEntry(
            self,
            textvariable=self.professor_id_var,
            width=320,
            font=("Arial", 14, "bold")
        )
        self.professor_id_entry.grid(row=7, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        # Row 8: Control buttons
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=8, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")
        button_frame.grid_rowconfigure(0, weight=1)
        for j in range(3):
            button_frame.grid_columnconfigure(j, weight=1)

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

        # Live validation while user edits (non-destructive)
        self.base_path_var.trace_add("write", lambda *_: self.refresh_repo_status(live=True))

        # First normalization + validation
        self.commit_base_path()
        self.refresh_repo_status(live=False)
        self.update_professor_suggestions()

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
            # Browse should work as before; we simply normalize afterward.
            self.base_path_var.set(path)
            self.commit_base_path()

    def commit_base_path(self):
        """
        Normalize and persist base_path without breaking Browse.
        Triggered on Enter / FocusOut, and after Browse.
        """
        raw = self.base_path_var.get()
        normalized = normalize_base_path(raw)

        if normalized != raw:
            # Setting var will trigger refresh_repo_status() via trace_add
            self.base_path_var.set(normalized)

        self.settings["base_path"] = normalized

    def refresh_repo_status(self, live: bool = False):
        """
        Validate repository structure and update UI.
        """
        status = validate_repo_root(self.base_path_var.get())
        self.last_validation = status
        self.repo_ok = bool(status.get("ok"))

        if self.repo_ok:
            # Hide blocking message
            self.repo_status_frame.grid_remove()
        else:
            # Show blocking message
            self.repo_status_frame.grid()
            path = status.get("path", "") or self.base_path_var.get().strip()
            issues = status.get("issues", [])

            details = (
                "The app could not detect a valid repository root.\n"
                "Please select the cloned repository root folder (it must contain docs/, tutorials/, professors/ and resources/).\n\n"
                f"Selected path: {path}\n\n"
                "Detected issues:\n"
                + "\n".join([f"- {i}" for i in issues])
            )
            self.repo_status_details.configure(text=details)

        # Disable / enable creation buttons
        state = "normal" if self.repo_ok else "disabled"
        self.tutorial_button.configure(state=state)
        self.professor_button.configure(state=state)
        self.project_button.configure(state=state)

    def update_settings(self):
        """
        Updates the global settings with current page values.
        Ensures base_path is normalized before saving.
        """
        self.commit_base_path()
        self.settings["base_path"] = self.base_path_var.get()
        self.settings["language_option"] = self.language_option_var.get()
        self.settings["language"] = self.language_var.get()
        self.settings["contributor_id"] = self.contributor_id_var.get()
        self.settings["professor_id"] = self.professor_id_var.get()
        self.settings["professor_name"] = self.professor_search_var.get()

    def ensure_repo_ready_or_block(self) -> bool:
        """
        Hard block navigation if repo is not valid.
        """
        self.refresh_repo_status(live=False)
        if self.repo_ok:
            return True

        path = self.last_validation.get("path", "") or self.base_path_var.get().strip()
        issues = self.last_validation.get("issues", [])

        msg = (
            "Cannot continue: invalid repository path.\n\n"
            f"Selected path: {path}\n\n"
            "Please select the repository root folder.\n\n"
            "Detected issues:\n" + "\n".join([f"- {i}" for i in issues])
        )
        messagebox.showerror("Repository Error", msg)
        return False

    def open_tutorial_page(self):
        self.update_settings()
        if not self.ensure_repo_ready_or_block():
            return
        self.destroy()
        tutorial_page = TutorialPage(self.parent, self.settings)
        tutorial_page.pack(fill="both", expand=True)
        self.master.active_page = tutorial_page

    def open_professor_page(self):
        self.update_settings()
        if not self.ensure_repo_ready_or_block():
            return
        self.destroy()
        professor_page = ProfessorPage(self.parent, self.settings)
        professor_page.pack(fill="both", expand=True)
        self.master.active_page = professor_page

    def open_project_page(self):
        self.update_settings()
        if not self.ensure_repo_ready_or_block():
            return
        self.destroy()
        project_page = ProjectPage(self.parent, self.settings)
        project_page.pack(fill="both", expand=True)
        self.master.active_page = project_page

    def update_professor_suggestions(self, event=None):
        # If repo is invalid, keep UX explicit
        if not self.repo_ok:
            self.professor_suggestions_menu.configure(values=["Repository not ready"])
            self.professor_suggestions_menu.set("Repository not ready")
            return

        search_text = self.professor_search_var.get().lower()
        professors_mapping = load_all_professors(self.base_path_var.get())

        if not search_text:
            suggestions = list(professors_mapping.keys())
        else:
            suggestions = [name for name in professors_mapping.keys() if search_text in name.lower()]

        if suggestions:
            self.professor_suggestions_menu.configure(values=suggestions)
            self.professor_suggestions_menu.set(suggestions[0])
        else:
            self.professor_suggestions_menu.configure(values=["No match"])
            self.professor_suggestions_menu.set("No match")

    def on_professor_selected(self, selected_name):
        if not self.repo_ok:
            return
        professors_mapping = load_all_professors(self.base_path_var.get())
        if selected_name in professors_mapping:
            self.professor_id_var.set(professors_mapping[selected_name])
            self.professor_search_var.set(selected_name)
