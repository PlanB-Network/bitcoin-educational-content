import customtkinter as ctk
from tkinter import messagebox

class ProjectPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = self.settings.get("base_path", "")
        
        # Simple form for creating a new project (company)
        self.project_name_var = ctk.StringVar()
        self.project_id_var = ctk.StringVar()
        self.description_var = ctk.StringVar()
        
        row = 0
        ctk.CTkLabel(self, text=f"Base path: {self.base_path}").grid(row=row, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="Nom du projet:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.project_name_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="ID du projet:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.project_id_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="Description:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.description_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="w")
        row += 1
        
        # Buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=2, pady=20)
        ctk.CTkButton(button_frame, text="Create Project", command=self.create_project).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Back", command=self.go_back).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Toggle Theme", command=self.toggle_theme).pack(side="left", padx=10)
    
    def create_project(self):
        project_name = self.project_name_var.get().strip()
        project_id = self.project_id_var.get().strip()
        description = self.description_var.get().strip()
        if not project_name or not project_id:
            messagebox.showerror("Error", "Please fill in all required fields (project name and ID).")
            return
        
        # Here, add logic to create the project resource in the repository.
        # For now, we simulate success.
        messagebox.showinfo("Success", f"Project '{project_name}' created successfully.")
    
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
