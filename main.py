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

# Main loop
while mode != "q":
    match mode:
        case "i": # Initialise / Change Map
            fancymaker.head("i")
        case "m": # Main Menu
            fancymaker.head("m")
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
                            case "p" | "c": # preview or create map
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
                            case "p" | "c": # preview or create map
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
                            case "p" | "c": # preview or create map
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
                            case "p" | "c": # preview or create map
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
                        userInput = input("All set! Would you like to " + Fore.YELLOW + "(c)reate " + Style.RESET_ALL + "or " + Fore.YELLOW + "(p)review" + Style.RESET_ALL + "? ")
                        match userInput:
                            case "p" | "c": # preview or create map
                                mapgen.map(galaxyName, galaxySize, galaxyArms, galaxyAge, userInput)
                            case "b": # go back
                                i -= 1
                            case "m": # quit to main menu
                                mode = "m"
                                skip2Menu = 1
                            case _:   # error message
                                print("Error: invalid input")
        case "l": # Load Map
            fancymaker.head("l")
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