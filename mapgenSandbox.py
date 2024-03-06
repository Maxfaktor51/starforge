from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

# Parameters
# Presets 
# [0 nArms, 
#  1 armLength, 
#  2 nStars, 
#  3 age, 
#  4 angle scale
#  5 armOffset scale
#  6 rho
#  7 theta 1
#  8 theta 2
#  9 sigma (gaussian distribution)]

seed = np.random.randint(0, 1000)
width  = 1000
height = width
nArms = 4
armLength = round(width*nArms*0.01)
nStars = round((nArms*width*width)/100)
age = 7

preset1 = [0, 0, 0, 0, np.pi*nArms, 1.66+nArms*0.01, 10/(nArms*2), nArms*0.075+age*0.075, 1+nArms*0.1, 3*age]

parameters = preset1

cO_color = (146, 181, 255, 255)
cB_color = (162, 192, 255, 255)
cA_color = (213, 224, 255, 255)
cF_color = (249, 245, 255, 255)
cG_color = (255, 237, 227, 255)
cK_color = (255, 218, 181, 255)
cM_color = (255, 182, 108, 255) 

# Functions
def pol2cart(rho, theta):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x,y

def addSpiral(seed, parameters, width, height, nArms, armLength, nStars, img):

    np.random.seed(seed)

    centerX = width / 2
    centerY = height / 2

    for i in range(nStars):
        arm       = np.random.randint(0, nArms)
        angle     = np.random.uniform(0, parameters[4] * np.pi)
        distance  = np.random.uniform(0, armLength)
        armOffset = parameters[5] * np.pi / nArms * arm

        rho = np.sqrt(distance) * np.exp(angle / parameters[6])
        theta = (angle * parameters[7]) + (armOffset*parameters[8])
        x, y = pol2cart(rho, theta)
        
        x = round(x+centerX)
        y = round(y+centerY)

        if 1 <= x < width-1 and 1 <= y < height-1:
            starClass = np.random.rand() * 100
            if starClass < 0.1:
                img.putpixel((x, y), cO_color)
            elif starClass < 0.4:
                img.putpixel((x, y), cB_color)
            elif starClass < 1.0:
                img.putpixel((x, y), cA_color)
            elif starClass < 4.0:
                img.putpixel((x, y), cF_color)
            elif starClass < 12.0:
                img.putpixel((x, y), cG_color)
            elif starClass < 24.0:
                img.putpixel((x, y), cK_color)
            else:
                img.putpixel((x, y), cM_color)
    return img

def addGauss(seed, parameters, width, height, nStars, img):

    np.random.seed(seed)
    
    centerX = width / 2
    centerY = height / 2

    sigma = min(width, height) / parameters[9]
    x_dist = np.random.normal(centerX, sigma, nStars)
    y_dist = np.random.normal(centerY, sigma, nStars)

    # Clip coordinates to image bounds
    x_dist = np.clip(x_dist, 0, width - 1)
    y_dist = np.clip(y_dist, 0, height - 1)

    for i in range(nStars):
        x = int(round(x_dist[i]))
        y = int(round(y_dist[i]))
        if 1 <= x < width-1 and 1 <= y < height-1:
            starClass = np.random.rand() * 100
            if starClass < 0.1:
                img.putpixel((x, y), cO_color)
            elif starClass < 0.4:
                img.putpixel((x, y), cB_color)
            elif starClass < 1.0:
                img.putpixel((x, y), cA_color)
            elif starClass < 4.0:
                img.putpixel((x, y), cF_color)
            elif starClass < 12.0:
                img.putpixel((x, y), cG_color)
            elif starClass < 24.0:
                img.putpixel((x, y), cK_color)
            else:
                img.putpixel((x, y), cM_color)
    return img

def addFrame(seed, width, height, nStars, img):
    np.random.seed(seed)
    blank = Image.new('RGBA', img.size, (0,0,0,0))
    mask = Image.new('L', img.size, 0)
    centerX = width / 2
    centerY = height / 2

    sigma = min(width, height) / 6
    x_dist = np.random.normal(centerX, sigma, nStars*69)
    y_dist = np.random.normal(centerY, sigma, nStars*69)

    for i in range(nStars*69):
        x = round(x_dist[i])
        y = round(y_dist[i])
        if 20 <= x < width-20 and 20 <= y < height-20:
            mask.putpixel((x,y), 255)

    img = Image.composite(img, blank, mask)
    return img

def removeClusters(width, height, img):
    px = img.load()
    for y in range(height-1):
        for x in range(width-1):
            if px[x,y] != (0,0,0,0):
                px[x-1,y-1] = (0,0,0,0)
                px[x  ,y-1] = (0,0,0,0)
                px[x+1,y-1] = (0,0,0,0)
                px[x-1,y  ] = (0,0,0,0)
                px[x+1,y  ] = (0,0,0,0)
                px[x-1,y+1] = (0,0,0,0)
                px[x  ,y+1] = (0,0,0,0)
                px[x+1,y+1] = (0,0,0,0)
    return img


# Main
img = Image.new('RGBA', (width, height), (0,0,0,0))
for i in range(2):
    if nArms-i > 0:
        img = addSpiral(seed+i, parameters, width, height, nArms-i, armLength, round(nStars*(age*0.1)), img)
img = addGauss(seed, parameters, width, height, round(nStars*(1-age*0.1)*0.5), img)
img = addFrame(seed, width, height, round(nStars), img)
img = removeClusters(width, height, img)
blur = img.filter(ImageFilter.GaussianBlur(3))
blank = Image.new('RGB', img.size, (0,0,0))
mask = Image.new('L', img.size, 255)
postP = Image.composite(blur, blank, mask)
postP = Image.composite(img, postP, mask)
postP.save('newGalaxyFX.png')
img.save('newGalaxy.png')