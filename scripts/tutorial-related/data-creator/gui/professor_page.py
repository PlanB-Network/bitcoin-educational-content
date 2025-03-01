import customtkinter as ctk
from tkinter import messagebox

class ProfessorPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = self.settings.get("base_path", "")
        
        # Enregistrer cette page comme active
        self.master.active_page = self

        # Récupérer les données sauvegardées si elles existent
        professor_data = self.settings.get("professor_data", {})

        # Initialiser les variables avec les données sauvegardées
        self.professor_name_var = ctk.StringVar(value=professor_data.get("professor_name", ""))
        # On conserve l'ID général s'il n'est pas renseigné localement
        self.professor_id_var = ctk.StringVar(value=professor_data.get("professor_id", self.settings.get("professor_id", "")))
        self.department_var = ctk.StringVar(value=professor_data.get("department", ""))

        # Configure grid
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.grid_columnconfigure(j, weight=1)
        
        row = 0
        ctk.CTkLabel(self, text=f"Base path: {self.base_path}").grid(row=row, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="Professor Name:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.professor_name_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        ctk.CTkLabel(self, text="Professor ID:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.professor_id_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        ctk.CTkLabel(self, text="Department:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.department_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        row += 1
        
        # Boutons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=2, pady=20, sticky="ew")
        ctk.CTkButton(button_frame, text="Create Professor", command=self.create_professor).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(button_frame, text="Back", command=self.go_back).pack(side="left", padx=10, expand=True)
    
    def update_local_state(self):
        """Sauvegarder les données saisies dans settings sous 'professor_data'."""
        self.settings["professor_data"] = {
            "professor_name": self.professor_name_var.get(),
            "professor_id": self.professor_id_var.get(),
            "department": self.department_var.get()
        }
    
    def create_professor(self):
        professor_name = self.professor_name_var.get().strip()
        professor_id = self.professor_id_var.get().strip()
        department = self.department_var.get().strip()
        if not professor_name or not professor_id:
            messagebox.showerror("Error", "Please fill in all required fields (name and ID).")
            return
        
        # Logique de création du professeur
        messagebox.showinfo("Success", f"Professor '{professor_name}' created successfully.")
    
    def go_back(self):
        # Sauvegarder l'état local avant de quitter
        self.update_local_state()
        from gui.home import HomePage
        self.destroy()
        home_page = HomePage(self.parent, self.settings)
        home_page.pack(fill="both", expand=True)
