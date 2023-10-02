import math

def starMap(realm,xCentre,yCentre,viewSize):

    # Initialize variables
    currentRow = ""
    xCoord = xCentre - int(viewSize/2)
    yCoord = yCentre - int(viewSize/2)
    xQueue = []
    yQueue = []
    coordQ = [xQueue, yQueue]

    for i in range(viewSize):
        for j in range(viewSize):
            seed1 = xCoord*yCoord + yCoord + realm
            seed2 = xCoord*yCoord + xCoord + realm + 1
            seed3 = xCoord*yCoord + yCoord + realm + 2
            k1 = seed1 % 9
            k2 = seed2 % 11
            k3 = seed3 % 10
            if i == 0:
                if j == 0:
                    currentRow += "    "
                else:
                    if xCoord < -10: 
                        currentRow += "" + str(xCoord) + " "
                    elif xCoord < 0:
                        currentRow += " " + str(xCoord) + " "
                    elif xCoord < 10:
                        currentRow += "  " + str(xCoord) + " "
                    else:
                        currentRow += " " + str(xCoord) + " "
            elif j == 0:
                if yCoord < 0:
                    currentRow += " " + str(yCoord) + " "
                else:
                    currentRow += "  " + str(yCoord) + " "
            elif k1 >= 3 and k2 >= 4 and k3 >= 5:
                currentRow += "  + "
                xQueue.append(xCoord)
                yQueue.append(yCoord)
            else:
                currentRow += "    "
            xCoord += 1
        print(currentRow)
        currentRow = ""
        xCoord = xCentre - int(viewSize/2)
        yCoord += 1

    return coordQ