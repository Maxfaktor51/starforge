from colorama import Fore,Back,Style
import os
import sys

import stargen
import fancymaker

os.system ("cls||clear")
mode = "m"
n = 0
starQueueX = [0]
starQueueY = [0]

while mode != "q":
    match mode:
        case "m":
            fancymaker.head("m")
            print("Welcome to Starforge v0.5\n")
            realm = int(input("Please enter a Realm ID:" + Fore.YELLOW + " "))
            print(Fore.GREEN + "(n)ew Star " + Fore.RED + "(q)uit")
            print(Style.RESET_ALL)
        case "n":
            print("Realm ID: " + str(realm))
            fancymaker.head("n")
            starQueueX[n] = int(input("Enter the X coordinate of your star:" + Fore.YELLOW + " "))
            starQueueY[n] = int(input(Fore.RESET + "Enter the Y coordinate of your star:" + Fore.YELLOW + " "))
            n += 1
            fancymaker.separator("n")
            newStar = stargen.getStarData("n",starQueueX[0],starQueueY[0],realm)
            fancymaker.separator("n")
            fancymaker.mainOptions()
        case "a": 
            starQueueX.append(int(input("Enter the X coordinate of your star:" + Fore.YELLOW + " ")))
            starQueueY.append(int(input(Fore.RESET + "Enter the Y coordinate of your star:" + Fore.YELLOW + " ")))
            stargen.getStarData("a",starQueueX[n],starQueueY[n],realm)
            n += 1
            fancymaker.separator("a")
            fancymaker.mainOptions()
        case "e":
            #Setup
            fileName = newStar + ".txt"
            stdout_fileno = sys.stdout
            sys.stdout = open(fileName, "w")
            fancymaker.head(mode)
            print("Realm ID: " + str(realm))
            fancymaker.separator(mode)
            n = 0
            # Regenerate systems from memory but print to file
            while n < len(starQueueX):
                stargen.getStarData("e",starQueueX[n],starQueueY[n],realm)
                fancymaker.separator(mode)
                n += 1
                if n < len(starQueueX):
                    fancymaker.separator(mode)
            # Clear memory, reset and close file
            n = 0
            starQueueX = [0]
            starQueueY = [0]
            sys.stdout.close()
            sys.stdout = stdout_fileno
            print(Fore.GREEN + "Success!")
            print(Fore.GREEN + "(n)ew Star " + Fore.YELLOW + "(m)enu " + Fore.RED + "(q)uit")
            print(Style.RESET_ALL)
 
    mode = input()
    fancymaker.separator(mode)
