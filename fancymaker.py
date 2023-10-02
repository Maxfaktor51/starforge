import art
from colorama import Fore,Back,Style
from collections import OrderedDict
import os

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

def head(mode):
    if mode == "e":
        os.system("cls||clear")
        art.tprint("Starforge")
    else:
        print(Style.RESET_ALL)
        os.system("cls||clear")
        art.tprint("Starforge")
        separator(mode)

def mainOptions():
    print(Fore.YELLOW + "(n)ew star (a)dd star " + Fore.BLUE + "(e)xport " + Fore.WHITE + "(m)enu " + Fore.RED + "(q)uit" + Style.RESET_ALL)

def reducedOptions():
    print(Fore.YELLOW + "(n)ew star " + Fore.BLUE + "(e)xport " + Fore.WHITE + "(m)enu " + Fore.RED + "(q)uit" + Style.RESET_ALL)

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