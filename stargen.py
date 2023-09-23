from colorama import Fore,Back,Style

import fancymaker

def getStarData(mode):
    if mode == "n":
        fancymaker.head()

    # Get star coordinates
    Xcoord = int(input("Enter the X coordinate of your star:" + Fore.YELLOW + " "))
    Ycoord = int(input(Fore.RESET + "Enter the Y coordinate of your star:" + Fore.YELLOW + " "))
    fancymaker.separator()

    # Seed generation
    seed = Xcoord*Ycoord + Ycoord
    print ("using seed: " + str(seed))

    # Define star age
    match seed % 100:
        case 0:
            s_type = "PD"       # Protostellar Disk
        case 1:
            s_type = "R"        # Rogue Planet
        case _:                 # Further classification of Main Sequence Star
            match seed % 29:
                case 0:
                    s_type = "O" + str(seed % 9)
                case 1|7:
                    s_type = "B" + str(seed % 9)
                case 2|8|13:
                    s_type = "A" + str(seed % 9)
                case 3|9|14|19:
                    s_type = "F" + str(seed % 9)
                case 4|10|15|20|23:
                    s_type = "G" + str(seed % 9)
                case 5|11|16|21|24|26:
                    s_type = "K" + str(seed % 9)
                case 6|12|17|22|25|27|28:
                    s_type = "M" + str(seed % 9)
                case _:
                    print("classification error")
    
    # Specify Luminosity Class
    match s_type[0]:
        case "O":
            if seed % 100 >= 75:
                s_type = s_type + "I"
            else:
                s_type = s_type + "II"
        case "B":
            if seed % 100 >= 80:
                s_type = s_type + "II"
            else:
                s_type = s_type + "III"
        case "A"|"F"|"G":
            if seed % 100 >= 95:
                s_type = s_type + "III"
            else:
                s_type = s_type + "IV"
        case "K"|"M":
            if seed % 100 >= 90:
                s_type = s_type + "IV"
            else:
                s_type = s_type + "V"
        case "P":
            s_type = s_type + "VII"
        case _:
            s_type = s_type + ""
    
    s_name = s_type + "." + str(Xcoord) + "." + str(Ycoord)
    print("Name: " + s_name)