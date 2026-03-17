# gui/footer.py
import customtkinter as ctk
from PIL import Image

def create_footer(parent):
    logo = Image.open("./pbn_logo.png")
    logo_image = ctk.CTkImage(light_image=logo, size=(200, 36))
    footer = ctk.CTkLabel(parent, text="", image=logo_image, compound="left")
    footer.grid(row=999, column=0, columnspan=parent.grid_size()[0], sticky="s", pady=10)
    return footer
