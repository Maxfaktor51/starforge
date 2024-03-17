import tkinter as tk
import customtkinter as ctk
import ringermacherMead as rM
from customtkinter import CTkSlider
from PIL import Image, ImageTk


window = ctk.CTk()
window.geometry(f"{1200}x{600}")
window.title("Starforge v0.9")

title = ctk.CTkImage(dark_image=Image.open("./assets/starforgelogo.png"), size=(200,80))
title_label = ctk.CTkLabel(master=window, image=title, text="")
title_label.grid(row=0, column=0)



window.mainloop()