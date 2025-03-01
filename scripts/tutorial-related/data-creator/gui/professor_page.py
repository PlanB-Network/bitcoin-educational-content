import customtkinter as ctk
from tkinter import messagebox

class ProfessorPage(ctk.CTkFrame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings
        self.base_path = self.settings.get("base_path", "")
        
        # Simple form for adding a new professor
        self.professor_name_var = ctk.StringVar()
        self.professor_id_var = ctk.StringVar(value=self.settings.get("professor_id", ""))
        self.department_var = ctk.StringVar()
        
        row = 0
        ctk.CTkLabel(self, text=f"Base path: {self.base_path}").grid(row=row, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="Nom du professeur:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.professor_name_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="ID du professeur:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.professor_id_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="w")
        row += 1
        
        ctk.CTkLabel(self, text="Département:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(self, textvariable=self.department_var, width=300).grid(row=row, column=1, padx=10, pady=5, sticky="w")
        row += 1
        
        # Buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=row, column=0, columnspan=2, pady=20)
        ctk.CTkButton(button_frame, text="Create Professor", command=self.create_professor).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Back", command=self.go_back).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Toggle Theme", command=self.toggle_theme).pack(side="left", padx=10)
    
    def create_professor(self):
        # Stub: Implement the logic for creating a professor in the repository
        professor_name = self.professor_name_var.get().strip()
        professor_id = self.professor_id_var.get().strip()
        department = self.department_var.get().strip()
        if not professor_name or not professor_id:
            messagebox.showerror("Error", "Please fill in all required fields (name and ID).")
            return
        
        # Here, add logic to create the professor resource in the repository.
        # For now, we simulate success.
        messagebox.showinfo("Success", f"Professor '{professor_name}' created successfully.")
    
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
