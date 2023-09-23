import art
from colorama import Fore,Back,Style
import os
import tabulate

def separator():
    print(Style.RESET_ALL + "--------------------------------------------------------")

def head():
    print(Style.RESET_ALL)
    os.system("cls||clear")
    art.tprint("Starforge")
    separator()

def mainOptions():
    print(Fore.YELLOW + "(n)ew star (a)dd star " + Fore.BLUE + "(e)xport " + Fore.WHITE + "(m)enu " + Fore.RED + "(q)uit" + Style.RESET_ALL)