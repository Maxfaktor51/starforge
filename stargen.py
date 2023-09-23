from colorama import Fore,Back,Style
from tabulate import tabulate

import fancymaker

def getPlanets(life):
    fancymaker.separator()
    print("Damn, all the planets are hiding somewhere!")
    if life >= 1:
        print(Fore.LIGHTGREEN_EX + "This system might be able to support life.")

def getStarData(mode):
    if mode == "n":
        fancymaker.head()

    # Get star coordinates
    Xcoord = int(input("Enter the X coordinate of your star:" + Fore.YELLOW + " "))
    Ycoord = int(input(Fore.RESET + "Enter the Y coordinate of your star:" + Fore.YELLOW + " "))
    fancymaker.separator()

    # Seed generation
    seed = Xcoord*Ycoord + Ycoord
    s_lvl = seed % 9

    # Define star age in percent
    s_age = seed % 100
    match s_age:
        case 0:
            s_type = "PD"       # Protostellar Disk
            s_temp = "unknown"
            s_mass = "unknown"
            s_rads = "unknown"
        case 1:
            s_type = "R"        # Rogue Gas Giant
            s_temp = "unknown"
            s_mass = "unknown"
            s_rads = "unknown"
        case _:                 # Further classification of Main Sequence Star
            match seed % 29:
                case 0:
                    s_type = "O" + str(s_lvl)
                    s_temp = 40000 + 40000 * (s_lvl/10)
                    s_mass = 50 + 20 * (s_lvl/10)
                    s_rads = 10 + 20 * (s_lvl/10)
                case 1|7:
                    s_type = "B" + str(s_lvl)
                    s_temp = 20000 + 20000 * (s_lvl/10)
                    s_mass = 10 + 40 * (s_lvl/10)
                    s_rads = 5 + 5 * (s_lvl/10)
                case 2|8|13:
                    s_type = "A" + str(s_lvl)
                    s_temp = 8500 + 11500 * (s_lvl/10)
                    s_mass = 2.0 + 8 * (s_lvl/10)
                    s_rads = 1.7 + 3.3 * (s_lvl/10)
                case 3|9|14|19:
                    s_type = "F" + str(s_lvl)
                    s_temp = 6500 + 1500 * (s_lvl/10)
                    s_mass = 1.5 + 0.5 * (s_lvl/10)
                    s_rads = 1.3 + 0.4 * (s_lvl/10)
                case 4|10|15|20|23:
                    s_type = "G" + str(s_lvl)
                    s_temp = 5700 + 800 * (s_lvl/10)
                    s_mass = 1.0 + 0.5 * (s_lvl/10)
                    s_rads = 1 + 0.3 * (s_lvl/10)
                case 5|11|16|21|24|26:
                    s_type = "K" + str(s_lvl)
                    s_temp = 4500 + 1200 * (s_lvl/10)
                    s_mass = 0.7 + 0.3 * (s_lvl/10)
                    s_rads = 0.8 + 0.2 * (s_lvl/10)
                case 6|12|17|22|25|27|28:
                    s_type = "M" + str(s_lvl)
                    s_temp = 3200 + 1300 * (s_lvl/10)
                    s_mass = 0.2 + 0.5 * (s_lvl/10)
                    s_rads = 0.3 + 0.5 * (s_lvl/10)
                case _:
                    print("classification error")
    
    # Specify Luminosity Class
    match s_type[0]:
        case "O":
            if s_age >= 75:
                s_type = s_type + "I"
                s_lumen = 1000 + 99000 * (s_lvl/10)
            else:
                s_type = s_type + "II"
                s_lumen = 20 + 980 * (s_lvl/10)
        case "B":
            if s_age >= 80:
                s_type = s_type + "II"
                s_lumen = 20 + 980 * (s_lvl/10)
            else:
                s_type = s_type + "III"
                s_lumen = 4 + 16 * (s_lvl/10)
        case "A"|"F"|"G":
            if s_age >= 95:
                s_type = s_type + "III"
                s_lumen = 4 + 16 * (s_lvl/10)
            else:
                s_type = s_type + "IV"
                s_lumen = 1 + 3 * (s_lvl/10)
        case "K"|"M":
            if s_age >= 90:
                s_type = s_type + "IV"
                s_lumen = 1 + 3 * (s_lvl/10)
            else:
                s_type = s_type + "V"
                s_lumen = 0.2 + 0.8 * (s_lvl/10)
        case "P":
            s_type = s_type + "VII"
            s_lumen = 0.01 + 0.19 * (s_lvl/10)
        case _:
            s_type = s_type + ""
            s_lumen = round(0.1 * (s_lvl/10), 2)
    
    # Check wether the star is old enough to support life
    match s_type[0]:
        case "G":
            if s_age >= 30 and s_age < 95:
                life = 2
            elif s_age >= 15 and s_age < 95:
                life = 1
            else:
                life = 0
        case "K":
            if s_age >= 6 and s_age < 90:
                life = 2
            elif s_age >= 3 and s_age < 90:
                life = 1
            else:
                life = 0
        case "M":
            if s_age >= 2 and s_age < 90:
                life = 2
            elif s_age >= 1 and s_age < 90:
                life = 1
            else:
                life = 0
        case _:    
            life = 0
    
    # Formulate star name
    s_name = s_type + "." + str(Xcoord) + "." + str(Ycoord)
        # add possibility to save aliases

    # Print star data
    if s_mass != "unknown":
        s_mass = str(round(s_mass, 2)) + " x Solar Mass"
        s_rads = str(round(s_rads, 2)) + " x Solar Radius"
        s_temp = str(int(s_temp)) + " Kelvin"
        s_lumen = str(round(s_lumen, 2)) + " x Solar Luminosity"
    print(tabulate([["Name",s_name],["Mass",s_mass],["Radius",s_rads],["Temperature",s_temp],["Luminosity",s_lumen]], tablefmt="presto"))

    # Generate Planets for this star
    getPlanets(life)
