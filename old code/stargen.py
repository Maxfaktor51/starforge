from colorama import Fore,Back,Style
from tabulate import tabulate

import math
import fancymaker

def getPlanets(mode,life,seed,s_type,s_lumen,s_temp,s_name):
    fancymaker.separator(mode)

    # Check if and how many planets the star can host
    match s_type[0]:
        case "M" | "K" | "B":
            n_planets = 1 + seed % 2
        case "G" | "A":
            n_planets = 2 + seed % 4
        case "F":
            n_planets = 3 + seed % 6
        case _:
            n_planets = 0
            development = "None"
    
    # Iterate through number of Planets and print their details 
    i = 0

    while n_planets > 0:
        p_name = s_name + "-" + fancymaker.write_roman(i + 1)
        p_rads = round(0.1 + ((seed * n_planets) % 10)/10 + (0.1 + (seed % 5)/10) * math.pow(2 + (seed % 2), i), 2)
        p_prid = round(math.sqrt(math.pow(p_rads, 3)), 2)
        p_mass = round(0.1 + i / n_planets + p_rads * 0.25, 2)
        p_grav = round(p_mass * (0.7 + ((seed + n_planets * seed) % 7) / 10), 2)

        # Check wether planet has an atmosphere
        if p_mass >= 0.6 and p_rads >= 0.7:
            atmo = 1
        else:
            atmo = 0

        # Determine surface temperature
        heat_rad = (s_temp / (p_rads + 10)) * (0.4 + (seed % 3)/10)
        heat_int = p_mass * (seed % 50) * 0.5
        p_temp = round((heat_rad + heat_int) * 1 + (((seed % 10)/10) * atmo))
        if p_temp <= 20:
            atmo = 0

        # Check wether planet is in the habitable zone
        habitable_zone = s_lumen/(math.pow(p_rads, 2))
        if habitable_zone >= 0.9 and habitable_zone <= 1.1:
            match life + seed % 9:
                case 6 | 7:
                    development = "Primitive"
                case 8:
                    development = "Complex"
                case 9:
                    development = "Intelligent"
                case 10:
                    development = "Spacefaring"
                case _:
                    development = "Molecular"
        else:
            development = "None"
        
        # Draw conclusions
        if atmo == 1:
            if seed % 10 >= 7:
                atmo = "Breathable"
            else:
                atmo = "Poisonous"
        else:
            atmo = "Nonexistent"

        # Define type of planet
        if p_mass >= 0.5 and p_mass <= 10:
            if p_temp >= 400:
                p_type = "Scorched World"
                if p_temp >= 1000:
                    p_type = "Hellworld"
            elif p_temp >= 250 and p_temp <= 350:
                p_type = "Earthlike World"
            else:
                p_type = "Barren World"
        elif p_mass > 10:
            p_type = "Gas Giant"
        else:
            p_type = "Dwarf Planet"


        # Print planetary data
        p_name = p_name + " " + p_type
        p_rads = str(p_rads) + " AU"
        p_prid = str(p_prid) + " Terran Years"
        p_mass = str(p_mass) + " Terran Masses"
        p_grav = str(p_grav) + " G"
        p_temp = str(p_temp) + " K"
        
        print(tabulate([["Name",p_name],["Semi Major Axis",p_rads],["Orbital Period",p_prid],["Mass",p_mass],["Surface Gravity",p_grav],["Surface Temperature",p_temp],["Atmosphere",atmo],["Life",development]], tablefmt="presto"))
        

        if n_planets != 1:
            fancymaker.semi_separator(mode)
        
        i += 1
        n_planets -= 1
    return development

def getStarData(mode,Xcoord,Ycoord,realm):
    # Seed generation
    seed = Xcoord*Ycoord + Ycoord + realm
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
            match seed % 28:
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
                case 3|9|14|18:
                    s_type = "F" + str(s_lvl)
                    s_temp = 6500 + 1500 * (s_lvl/10)
                    s_mass = 1.5 + 0.5 * (s_lvl/10)
                    s_rads = 1.3 + 0.4 * (s_lvl/10)
                case 4|10|15|19|22:
                    s_type = "G" + str(s_lvl)
                    s_temp = 5700 + 800 * (s_lvl/10)
                    s_mass = 1.0 + 0.5 * (s_lvl/10)
                    s_rads = 1 + 0.3 * (s_lvl/10)
                case 5|11|16|20|23|25:
                    s_type = "K" + str(s_lvl)
                    s_temp = 4500 + 1200 * (s_lvl/10)
                    s_mass = 0.7 + 0.3 * (s_lvl/10)
                    s_rads = 0.8 + 0.2 * (s_lvl/10)
                case 6|12|17|21|24|26|27:
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
            s_lumen = round(0.01 + 0.19 * (s_lvl/10), 2)
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

    # Conserve numerical values for passing to functions
    luminosity = s_lumen
    temperature = s_temp

    # Print star data
    if s_mass != "unknown":
        s_mass = str(round(s_mass, 2)) + " Solar Masses"
        s_rads = str(round(s_rads, 2)) + " Solar Radii"
        s_temp = str(int(s_temp)) + " K"
        s_lumen = str(round(s_lumen, 2)) + " x Solar Luminosity"
    if mode == "e":
        print(tabulate([["Name",s_name],["Mass",s_mass],["Radius",s_rads],["Temperature",s_temp],["Luminosity",s_lumen]], tablefmt="presto"))
    else:
        print(Fore.YELLOW + tabulate([["Star",s_name],["Mass",s_mass],["Radius",s_rads],["Temperature",s_temp],["Luminosity",s_lumen]], tablefmt="presto"))

    # Generate Planets for this star
    if mode == "s":
        development = getPlanets(mode,life,seed,s_type,luminosity,temperature,s_name)
        return development
    else:
        development = getPlanets(mode,life,seed,s_type,luminosity,temperature,s_name)
        return s_name