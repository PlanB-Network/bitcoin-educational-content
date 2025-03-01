import customtkinter as ctk
from config import load_settings, save_settings
from gui.home import HomePage

def on_closing(root, settings):
    save_settings(settings)
    root.destroy()

def main():
    # Initialize the main window
    root = ctk.CTk()
    root.title("Resource Creator")
    
    # Load user settings from configuration file
    settings = load_settings()
    
    # Create and pack the HomePage
    home_page = HomePage(root, settings)
    home_page.pack(fill="both", expand=True)
    
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, settings))
    root.mainloop()

if __name__ == "__main__":
    main()
