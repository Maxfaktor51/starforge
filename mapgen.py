from PIL import Image
import numpy as np

# Colour Definitions
cO_color = (146, 181, 255)
cB_color = (162, 192, 255)
cA_color = (213, 224, 255)
cF_color = (249, 245, 255)
cG_color = (255, 237, 227)
cK_color = (255, 218, 181)
cM_color = (255, 182, 108) 

# Functions
def getSeed(gName):
    # reset seed
    seed = 0
    # get seed by adding up ASCII values
    for i in range(len(gName)):
        seed += (ord(gName[i])*i+1)
    return seed

def pol2cart(rho, theta):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x,y

def addSpiral(seed, parameters, width, height, map, j):
    # set seed
    np.random.seed(seed)
    # adjust number of stars
    parameters[2] = round(parameters[2]*parameters[3]*0.1)
    # get center coordinates
    centerX = width / 2
    centerY = height / 2
    # create spiral
    for i in range(parameters[2]):
        arm       = np.random.randint(0, parameters[0] - j)
        angle     = np.random.uniform(0, parameters[4] * np.pi)
        distance  = np.random.uniform(0, parameters[1])
        armOffset = parameters[5] * np.pi / parameters[0] * arm
        # get pixel coordinates
        rho = np.sqrt(distance) * np.exp(angle / parameters[6])
        theta = (angle * parameters[7]) + (armOffset*parameters[8])
        x, y = pol2cart(rho, theta)
        x = round(x+centerX)
        y = round(y+centerY)
        # assign color to pixel
        if 1 <= x < width-1 and 1 <= y < height-1:
            starClass = np.random.rand() * 100
            if starClass < 0.1:
                map.putpixel((x, y), cO_color)
            elif starClass < 0.4:
                map.putpixel((x, y), cB_color)
            elif starClass < 1.0:
                map.putpixel((x, y), cA_color)
            elif starClass < 4.0:
                map.putpixel((x, y), cF_color)
            elif starClass < 12.0:
                map.putpixel((x, y), cG_color)
            elif starClass < 24.0:
                map.putpixel((x, y), cK_color)
            else:
                map.putpixel((x, y), cM_color)
    return map

def addGauss(seed, parameters, width, height, map, j):
    # set seed
    np.random.seed(seed)
    # adjust number of stars
    parameters[2] = round(parameters[2]*(1-parameters[3]*0.1))
    # get center coordinates
    centerX = width / 2
    centerY = height / 2
    # get gaussian distribution
    sigma = min(width, height) / parameters[9] * (j+1)
    x_dist = np.random.normal(centerX, sigma, parameters[2])
    y_dist = np.random.normal(centerY, sigma, parameters[2])
    # create point cloud
    for i in range(parameters[2]):
        x = round(x_dist[i])
        y = round(y_dist[i])
        # assign color to pixel
        if 1 <= x < width-1 and 1 <= y < height-1:
            starClass = np.random.rand() * 100
            if starClass < 0.1:
                map.putpixel((x, y), cO_color)
            elif starClass < 0.4:
                map.putpixel((x, y), cB_color)
            elif starClass < 1.0:
                map.putpixel((x, y), cA_color)
            elif starClass < 4.0:
                map.putpixel((x, y), cF_color)
            elif starClass < 12.0:
                map.putpixel((x, y), cG_color)
            elif starClass < 24.0:
                map.putpixel((x, y), cK_color)
            else:
                map.putpixel((x, y), cM_color)
    return map

def addFrame(seed, parameters, width, height, map):
    # set seed
    np.random.seed(seed)
    # get background
    blank = Image.new('RGB', map.size, (0,0,0))
    # create mask using gaussian distribution
    mask = Image.new('L', map.size, 0)
    centerX = width / 2
    centerY = height / 2
    sigma = min(width, height) / 6
    x_dist = np.random.normal(centerX, sigma, parameters[2]*69)
    y_dist = np.random.normal(centerY, sigma, parameters[2]*69)
    for i in range(parameters[2]*69):
        x = round(x_dist[i])
        y = round(y_dist[i])
        if 20 <= x < width-20 and 20 <= y < height-20:
            mask.putpixel((x,y), 255)
    # blend map onto background using the mask
    map = Image.composite(map, blank, mask)
    return map

def removeClusters(width, height, map):
    px = map.load()
    for y in range(height):
        for x in range(width):
            if px[x,y] != (0,0,0):
                px[x-1,y-1] = (0,0,0)
                px[x  ,y-1] = (0,0,0)
                px[x+1,y-1] = (0,0,0)
                px[x-1,y  ] = (0,0,0)
                px[x+1,y  ] = (0,0,0)
                px[x-1,y+1] = (0,0,0)
                px[x  ,y+1] = (0,0,0)
                px[x+1,y+1] = (0,0,0)
    return map

def map(gName, gSize, nArms, gAge, mode):
    # create blank map
    match gSize:
        case "S":
            width  = 750
        case "M":
            width  = 1250
        case "L":
            width  = 1500
    height = width
    map = Image.new('RGB', (width, height), (0,0,0))
    # get seed
    seed = getSeed(gName)
    # initialise parameters
    parameters = [nArms,                          # 0 - number of spiral arms
                  round(width*nArms*0.1),         # 1 - length of spiral arms
                  round((nArms*width*width)/50),  # 2 - number of stars (some may get covered up by the frame in the final map)
                  gAge,                           # 3 - age of galaxy (cloud to spiral ratio)
                  np.pi*nArms,                    # 4 - angle scalar
                  1.66+nArms*0.01,                # 5 - armOffset scalar
                  10/(nArms*2),                   # 6 - rho
                  nArms*0.075+gAge*0.075,         # 7 - theta 1
                  1+nArms*0.1,                    # 8 - theta 2
                  3*gAge                          # 9 - sigma (gaussian distribution modifier)
                 ]
    # create stars
    j = 0
    for j in range(2):
        if parameters[0] - j > 0:
            map = addSpiral(seed+j, parameters, width, height, map, j)
            map = addGauss(seed+j, parameters, width, height, map, j)
    if mode == "c":
        map = addFrame(seed, parameters, width, height, map)
        map = removeClusters(width, height, map)
        map.save('./galaxies/'+gName+'.png')
        map.show(gName+".png")
    else:
        map.show()
    return
