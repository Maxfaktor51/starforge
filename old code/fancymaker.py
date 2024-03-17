import art
from colorama import Fore,Style
from collections import OrderedDict
import os

def head(mode):
    match mode:
        case "e":
            os.system("cls||clear")
            art.tprint("Starforge")
        case "i":
            print(Style.RESET_ALL)
            os.system("cls||clear")
            art.tprint("Starforge")
            separator(mode)
            print("Welcome to Starforge v0.8\nby Maximilian Kaulfuss  -  https://maxfaktor51.github.io\n\n\n\n\n\n")
            options(mode)
            separator(mode)
        case "l":
            print(Style.RESET_ALL)
            os.system("cls||clear")
            art.tprint("Starforge")
            separator(mode)
            print(Fore.BLUE + "Load Galaxy Map")
            separator(mode)
        case "m":
            print(Style.RESET_ALL)
            os.system("cls||clear")
            art.tprint("Starforge")
            separator(mode)
            print("Welcome to Starforge v0.8  https://maxfaktor51.github.io\n\n\n\n\n")
        case "n":
            print(Style.RESET_ALL)
            os.system("cls||clear")
            art.tprint("Starforge")
            separator(mode)
            print(Fore.YELLOW + "New Galaxy Map Editor")
            separator(mode)
        case _:
            print(Style.RESET_ALL)
            os.system("cls||clear")
            art.tprint("Starforge")
            separator(mode)

def separator(mode):
    if mode == "e":
        print("--------------------------------------------------------")
    else:
        print(Style.RESET_ALL + "--------------------------------------------------------")

def semi_separator(mode):
    if mode == "e":
        print("----- ---- --- -- -")
    else:
        print(Style.RESET_ALL + "----- ---- --- -- -")

def options(type):
    match type:
        case "i": #initial
            print(Fore.YELLOW + "(n)ew map  " 
                  + Fore.BLUE + "(l)oad map  " 
                  + Fore.RED + "(q)uit" + Style.RESET_ALL)
        case "m": #main options
            print(Fore.YELLOW + "(c)hange map  " 
                  + Fore.BLUE + "(v)iew star  (p)rint  (s)eti  " 
                  + Fore.RED + "(q)uit" + Style.RESET_ALL)
        case "n": #new map options
            print(Fore.YELLOW + "(r)andom  "
                  + Fore.RED + "(b)ack  " 
                  + Fore.BLUE + "(p)review  "
                  + Fore.WHITE + "(m)enu" + Style.RESET_ALL)

def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])