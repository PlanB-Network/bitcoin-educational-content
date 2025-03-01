import customtkinter as ctk
from config import load_settings, save_settings
from gui.home import HomePage

def on_closing(root, settings):
    # Récupère update_settings si elle existe, sinon retourne None
    update_func = getattr(root.active_page, "update_settings", None)
    if callable(update_func):
        update_func()
    save_settings(settings)
    root.destroy()


def main():
    settings = load_settings()
    # Appliquer le thème sauvegardé
    ctk.set_appearance_mode(settings.get("theme", "Light"))
    
    root = ctk.CTk()
    root.title("Resource Creator")
    
    # Utiliser une taille par défaut à chaque démarrage (768x576)
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
