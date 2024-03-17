# This is the main code of Starforge.
import gui
import tkinter       as tk
import customtkinter as ctk

version = "0.9"
galaxy  = ""
mode = "n"

root = ctk.CTk()

if galaxy == "":
    file_path = gui.getGalaxy(root)
    print(file_path)

gui.mainWindow(root, version, galaxy)

root.mainloop()