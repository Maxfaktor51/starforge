from colorama import Fore,Back,Style
import os

import stargen
import fancymaker

os.system ("cls||clear")
mode = "m"
while mode != "q":
    match mode:
        case "m":
            fancymaker.head()
            print("Welcome to Starforge v0.3\n\nWhat would you like to do?")
            print(Fore.GREEN + "(n) - New Star")
            print(Fore.RED + "(q) - Quit")
            print(Style.RESET_ALL)
        case "n":
            fancymaker.head()
            stargen.getStarData("n")
            fancymaker.separator()
            fancymaker.mainOptions()
        case "a":
            stargen.getStarData("a")
            fancymaker.separator()
            fancymaker.mainOptions()
        case "e":
            print("This feature has not been implemented yet!")
            print(Fore.YELLOW + "(m) - Return To Menu")
            print(Fore.RED + "(q) - Quit")
            print(Style.RESET_ALL)   
    mode = input()
    fancymaker.separator()
