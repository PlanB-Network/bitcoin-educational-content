import customtkinter as ctk
from tkinter import messagebox

class ProjectPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = self.settings.get("base_path", "")
        
        self.master.active_page = self
        
        # Récupérer les données sauvegardées si elles existent
        project_data = self.settings.get("project_data", {})

        self.project_name_var = ctk.StringVar(value=project_data.get("project_name", ""))
        self.project_id_var = ctk.StringVar(value=project_data.get("project_id", ""))
        self.description_var = ctk.StringVar(value=project_data.get("description", ""))
        
        # Configure grid
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.grid_columnconfigure(j, weight=1)
        
        row = 0
        ctk.CTkLabel(self, text=f"Base path: {self.base_path}").grid(row=row, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="Project Name:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.project_name_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        ctk.CTkLabel(self, text="Project ID:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.project_id_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        ctk.CTkLabel(self, text="Description:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.description_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Boutons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=2, pady=20, sticky="ew")
        ctk.CTkButton(button_frame, text="Create Project", command=self.create_project).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(button_frame, text="Back", command=self.go_back).pack(side="left", padx=10, expand=True)
    
    def update_local_state(self):
        """Sauvegarder les données saisies dans settings sous 'project_data'."""
        self.settings["project_data"] = {
            "project_name": self.project_name_var.get(),
            "project_id": self.project_id_var.get(),
            "description": self.description_var.get()
        }
    
    def create_project(self):
        project_name = self.project_name_var.get().strip()
        project_id = self.project_id_var.get().strip()
        description = self.description_var.get().strip()
        if not project_name or not project_id:
            messagebox.showerror("Error", "Please fill in all required fields (project name and ID).")
            return
        
        # Logique de création du projet
        messagebox.showinfo("Success", f"Project '{project_name}' created successfully.")
    
    def go_back(self):
        self.update_local_state()
        from gui.home import HomePage
        self.destroy()
        home_page = HomePage(self.parent, self.settings)
        home_page.pack(fill="both", expand=True)
