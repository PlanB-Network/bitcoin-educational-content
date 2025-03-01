import customtkinter as ctk
from tkinter import filedialog
from gui.tutorial_page import TutorialPage
from gui.professor_page import ProfessorPage
from gui.project_page import ProjectPage

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        
        # Base path selection
        self.base_path_var = ctk.StringVar(value=self.settings.get("base_path", ""))
        ctk.CTkLabel(self, text="Chemin local vers le dépôt:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.base_path_entry = ctk.CTkEntry(self, textvariable=self.base_path_var, width=300)
        self.base_path_entry.grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkButton(self, text="Parcourir", command=self.select_base_path).grid(row=0, column=2, padx=10, pady=5)
        
        # Resource type buttons
        ctk.CTkButton(self, text="Nouveau Tutoriel", command=self.open_tutorial_page).grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkButton(self, text="Nouveau Professeur", command=self.open_professor_page).grid(row=1, column=1, padx=10, pady=10)
        ctk.CTkButton(self, text="Nouveau Projet", command=self.open_project_page).grid(row=1, column=2, padx=10, pady=10)
    
    def select_base_path(self):
        path = filedialog.askdirectory()
        if path:
            self.base_path_var.set(path)
            self.settings["base_path"] = path
    
    def open_tutorial_page(self):
        self.destroy()
        tutorial_page = TutorialPage(self.parent, self.settings)
        tutorial_page.pack(fill="both", expand=True)
    
    def open_professor_page(self):
        self.destroy()
        professor_page = ProfessorPage(self.parent, self.settings)
        professor_page.pack(fill="both", expand=True)
    
    def open_project_page(self):
        self.destroy()
        project_page = ProjectPage(self.parent, self.settings)
        project_page.pack(fill="both", expand=True)
