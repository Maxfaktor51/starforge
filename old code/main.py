import os, sys
import numpy as np
import mapgen, fancymaker

from colorama import Fore, Style

# Cleanup
os.system("cls||clear")

# Initialise
mode = "i"
skip2Menu = 0
n = 0
starQX = [0]
starQY = [0]
starQ = [starQX, starQY]
galaxyName = "-"
galaxyArms = 0
galaxySize = "M"
galaxyAge = 0

# Main loop
while mode != "q":
    match mode:
        case "i" | "c": # Initialise / Change Map
            fancymaker.head("i")
        case "m": # Main Menu
            fancymaker.head("m")
            if galaxyName == "-":
                print(Fore.RED + "Error loading map\n" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW, galaxyName, Style.RESET_ALL + "selected\n")
            fancymaker.options("m")
            fancymaker.separator("m")
        case "n": # New Map
            # Reset Edtor
            i = 0
            galaxyName = "-"
            galaxyArms = 0
            galaxySize = "M"
            galaxyAge = 0
            
            # loop until happy
            while mode != "m":
                fancymaker.head("n")
                print("   Name:   " + Fore.YELLOW + galaxyName)
                print(Style.RESET_ALL + "   Size:   " + Fore.YELLOW + galaxySize)
                print(Style.RESET_ALL + "   Arms:  " + Fore.YELLOW, galaxyArms)
                print(Style.RESET_ALL + "    Age:  " + Fore.YELLOW, galaxyAge)
                print("\n")
                fancymaker.options("n")
                fancymaker.separator("n")
                match i:
                    case 0: # galaxyName
                        userInput = input("Please enter a name for your galaxy:" + Fore.YELLOW + " ")
                        match userInput:
                            case "r": # random name
                                galaxyName = "G" + str(np.random.randint(0, 1000)) + "-" + str(np.random.randint(0, 1000))
                                i += 1
                            case "p": # preview or create map
                                mapgen.map(galaxyName, galaxySize, galaxyArms, galaxyAge, userInput)
                            case "m": # quit to main menu
                                mode = "m"
                                skip2Menu = 1
                            case "":  # jump to next
                                i += 1
                            case _:   # set galaxyName
                                galaxyName = userInput
                                i += 1
                    case 1: # galaxySize
                        userInput = input("Please enter the size of your map (s/m/l):" + Fore.YELLOW + " ")
                        match userInput:
                            case "r": # random size
                                size = np.random.randint(0, 2)
                                if size == 0:
                                    galaxySize = "S"
                                elif size == 1:
                                    galaxySize = "M"
                                else:
                                    galaxySize = "L"
                                i += 1
                            case "b": # go back
                                i -= 1
                            case "p": # preview or create map
                                mapgen.map(galaxyName, galaxySize, galaxyArms, galaxyAge, userInput)
                            case "":  # jump to next
                                i += 1
                            case _:   # set galaxySize
                                match userInput:
                                    case "s" | "S":
                                        galaxySize = "S"
                                    case "l" | "L":
                                        galaxySize = "L"
                                    case _:
                                        galaxySize = "M"
                                i += 1
                    case 2: # galaxyArms
                        userInput = input("Please choose the number of spiral arms:" + Fore.YELLOW + " ")
                        match userInput:
                            case "r": # random number of arms
                                galaxyArms = np.random.randint(1, 24)
                                i += 1
                            case "b": # go back
                                i -= 1
                            case "p": # preview or create map
                                mapgen.map(galaxyName, galaxySize, galaxyArms, galaxyAge, userInput)
                            case "m": # quit to main menu
                                mode = "m"
                                skip2Menu = 1
                            case "":  # jump to next
                                i += 1
                            case _:   # set galaxyArms
                                galaxyArms = int(userInput)
                                i += 1
                    case 3: # galaxyAge
                        userInput = input("Please enter the age of your galaxy (1 - 10):" + Fore.YELLOW + " ")
                        match userInput:
                            case "r": # random age
                                galaxyAge = np.random.randint(1, 10)
                                i += 1
                            case "b": # go back
                                i -= 1
                            case "p": # preview or create map
                                mapgen.map(galaxyName, galaxySize, galaxyArms, galaxyAge, userInput)
                            case "m": # quit to main menu
                                mode = "m"
                                skip2Menu = 1
                            case "":  # jump to next
                                i += 1
                            case _:   # set galaxyAge
                                galaxyAge = int(userInput)
                                i += 1
                    case 4: # Done
                        userInput = input("All set! You can now " + Fore.YELLOW + "(c)reate " + Style.RESET_ALL + "the map. ")
                        match userInput:
                            case "c": # preview or create map
                                mapgen.map(galaxyName, galaxySize, galaxyArms, galaxyAge, userInput)
                                print("\n" + Fore.YELLOW, galaxyName, Style.RESET_ALL + " has been successfully created!")
                                mode = "m"
                                skip2Menu = 1
                            case "p":
                                mapgen.map(galaxyName, galaxySize, galaxyArms, galaxyAge, userInput)
                            case "b": # go back
                                i -= 1
                            case "m": # quit to main menu
                                mode = "m"
                                skip2Menu = 1
                            case _:   # error message
                                print("Error: invalid input")
        case "l": # Load Map
            check = 0
            fancymaker.head("l")
            files = os.listdir('./galaxies')
            for file_name in files:
                print(file_name)
            fancymaker.separator("l")
            galaxyName = input("Which map would you like to load?" + Fore.BLUE + " ")
            for file_name in files:
                if galaxyName+".png" == file_name:
                    check += 1
            while check != 1:
                fancymaker.head("l")
                files = os.listdir('./galaxies')
                for file_name in files:
                    print(file_name)
                fancymaker.separator("l")
                if check > 1 or check == 0:
                    print(Fore.RED + "Input Error. Pleasy try again." + Style.RESET_ALL)
                galaxyName = input("Which map would you like to load?" + Fore.BLUE + " ")
                for file_name in files:
                    if galaxyName+".png" == file_name:
                        check += 1            
            skip2Menu = 1
        case "v": # View Star
            fancymaker.head("v")
        case "p": # Print ALL stars
            fancymaker.head("p")
        case "s": # SETI Mode
            fancymaker.head("s")
        case _:
            print("Error: invalid input")
    
    if skip2Menu == 1:
        mode = "m"
        skip2Menu = 0
    else:
        mode = input()