import customtkinter as ctk
from config import load_settings, save_settings
from gui.home import HomePage

def on_closing(root, settings):
    # If the active page has an update_settings method, call it
    if hasattr(root, "active_page") and callable(getattr(root.active_page, "update_settings", None)):
        root.active_page.update_settings()
    # Remove temporary data from resource pages before saving
    settings.pop("tutorial_data", None)
    settings.pop("professor_data", None)
    settings.pop("project_data", None)
    save_settings(settings)
    root.destroy()

def main():
    settings = load_settings()
    # Apply the saved theme
    ctk.set_appearance_mode(settings.get("theme", "Light"))
    
    root = ctk.CTk()
    root.title("Resource Creator")
    
    # Use a default window size (768x576) at startup
    default_width, default_height = 768, 576
    root.geometry(f"{default_width}x{default_height}")
    root.resizable(True, True)
    
    home_page = HomePage(root, settings)
    home_page.pack(fill="both", expand=True)
    root.active_page = home_page
    
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, settings))
    root.mainloop()

if __name__ == "__main__":
    main()
