# This code runs the GUI windows
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog

def mainWindow(root, version, galaxy):
    
    # Setup
    root.geometry("800x500")
    root.title("Starforge v" + version)

    # Add tabs
    tabs = ctk.CTkTabview(master=root)
    home    = tabs.add("Home")
    viewSys = tabs.add("View System")
    seti    = tabs.add("SETI")

    tabs.set("Home")

    # Button Functions
    def switchGalaxy():
        print("switch galaxy")
        getGalaxy(root)
    
    # Elements
    switchGalaxy_button = ctk.CTkButton(master=home, text="Switch Galaxy", command=switchGalaxy)

    # Assembly
    tabs.grid(row=0)
    switchGalaxy_button.grid(row=1)

def getGalaxy(root):
    # Clean up
    file_path = ""

    # Set up pop-up window
    getGalaxyWindow = ctk.CTkToplevel(root)
    getGalaxyWindow.title("Get Galaxy")

    # Button commands
    def loadGalaxy():
        global file_path
        file_path = filedialog.askopenfilename()
        print(file_path)

    def newGalaxy():
        global file_path
        print("PLACEHOLDER - new galaxy editor")
        # open new galaxy editor

    # Elements
    info  = ctk.CTkLabel(getGalaxyWindow, text="ERROR - no map loaded.\nPlease load or create a galaxy.")
    loadGalaxy_button = ctk.CTkButton(getGalaxyWindow, text="Load Galaxy", command=loadGalaxy)
    newGalaxy_button  = ctk.CTkButton(getGalaxyWindow, text="New Galaxy", command=newGalaxy)

    # Assembly
    info.grid(row=0, padx=10, pady=10, columnspan=2)
    loadGalaxy_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    newGalaxy_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    # Close window when done
    if file_path != "":
        getGalaxyWindow.destroy()