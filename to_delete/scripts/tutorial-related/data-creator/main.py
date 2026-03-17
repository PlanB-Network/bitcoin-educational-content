import sys

# ── Check dependencies ──────────────────────────────────────────────────────────
missing = []
for pkg in ("customtkinter", "PIL", "appdirs", "darkdetect", "packaging"):
    try:
        __import__(pkg.split(".")[0])
    except ImportError:
        missing.append(pkg)

if missing:
    print("\n[Erreur] Missing dependencies:", ", ".join(missing))
    print("Please execute:  python3 -m pip install -r requirements.txt\n")
    sys.exit(1)
# ────────────────────────────────────────────────────────────────────────────────

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
    
    # Use only the custom theme. We do not store or toggle appearance mode in config anymore.
    ctk.set_default_color_theme("theme.json")
    
    # Force dark appearance mode
    ctk.set_appearance_mode("dark")
    
    root = ctk.CTk()
    root.title("Data Creator - Plan ₿ Network")
    
    try:
        root.iconbitmap("favicon.ico")
    except Exception as e:
        print(f"Impossible to charge icon favicon.ico: {e}")
    
    # Default window size
    default_width, default_height = 870, 690
    root.geometry(f"{default_width}x{default_height}")
    root.resizable(True, True)
    
    home_page = HomePage(root, settings)
    home_page.pack(fill="both", expand=True)
    root.active_page = home_page
    
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, settings))
    root.mainloop()

if __name__ == "__main__":
    main()