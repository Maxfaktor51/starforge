# Inspired by https://arxiv.org/ftp/arxiv/papers/0908/0908.0892.pdf

import numpy as np
from PIL import Image, ImageDraw

# define colours
cO_color = (146, 181, 255, 255)
cB_color = (162, 192, 255, 255)
cA_color = (213, 224, 255, 255)
cF_color = (249, 245, 255, 255)
cG_color = (255, 237, 227, 255)
cK_color = (255, 218, 181, 255)
cM_color = (255, 182, 108, 255)

width  = 1000
height = 1000

def addSpiral(map, tMax, A, B, N, angO, decay):
    centerX = map.size[0] / 2
    centerY = map.size[1] / 2
    t = 1
    while t <= tMax:
        theta = t/100
        theta = np.tan(theta/(2*N))
        r = A / (np.log(B * theta))
        dX = r * np.cos(angO+t/100)
        dY = r * np.sin(angO+t/100)
        x = round(centerX + dX)
        y = round(centerY - dY)
        if t == 2 and decay <= 2:
            ImageDraw.Draw(map).line((x,y,centerX,centerY), cK_color)
        if 1 <= x <= width-1 and 1 <= y <= height-1:
            starClass = np.random.rand() * 100
            if starClass < 0.1/decay:
                map.putpixel((x,y), cO_color)
            elif starClass < 0.4/decay:
                map.putpixel((x,y), cB_color)
            elif starClass < 1.0/decay:
                map.putpixel((x,y), cA_color)
            elif starClass < 4.0/decay:
                map.putpixel((x,y), cF_color)
            elif starClass < 12.0/decay:
                map.putpixel((x,y), cG_color)
            elif starClass < 24.0/decay:
                map.putpixel((x,y), cK_color)
            elif starClass < 70.0/decay:
                map.putpixel((x,y), cM_color)
        else:
            break
        t += 1
    return map

def addGauss(map, sigma, nStars):
    nStars = round(nStars)
    centerX = map.size[0] / 2
    centerY = map.size[1] / 2
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

def addFrame(map, sigma, nStars):
    blank = Image.new('RGBA', map.size, (0,0,0,255))
    mask = Image.new('L', map.size, 0)

    centerX = round(map.size[0] / 2)
    centerY = round(map.size[1] / 2)
    nStars = round(nStars)
    x_dist = np.random.normal(centerX, sigma, nStars*30)
    y_dist = np.random.normal(centerY, sigma, nStars*30)

    for i in range(nStars*30):

        x = round(x_dist[i])
        y = round(y_dist[i])
        if 20 <= x < width-20 and 20 <= y < height-20:
            mask.putpixel((x,y), 255)

    map = Image.composite(map, blank, mask)
    return map

def removeClusters(map):
    px = map.load()
    for y in range(map.size[1]-1):
        for x in range(map.size[0]-1):
            if px[x,y] != (0,0,0,255):
                px[x-1,y-1] = (0,0,0,255)
                px[x  ,y-1] = (0,0,0,255)
                px[x+1,y-1] = (0,0,0,255)
                px[x-1,y  ] = (0,0,0,255)
                px[x+1,y  ] = (0,0,0,255)
                px[x-1,y+1] = (0,0,0,255)
                px[x  ,y+1] = (0,0,0,255)
                px[x+1,y+1] = (0,0,0,255)
    return map

def runRM():
    # create empty map
    map = Image.new('RGBA', (width, height), (0,0,0,255))

    # Formula:   r(phi) = A / log(B * tan(phi / 2*N))
    # using paramaters
    A = width/10            # scale
    B = 2                   # arm sweep
    N = 11                   # tightness

    # additional parameters
    nArms = 2               # number of arms
    decay = 200             # how slowly an arm will vanish               
    chaos = 0               # how chaotic the galaxy looks (set 0 if undesired)

    # derived parameters
    tMax   = width*2          # steps per arm
    angO   = (2*3.14)/nArms   # angular offset between arms
    sigma  = 100                # Gaussian distribution modifier
    sigma2 = 100                # Frame modifier
    nStars = (width*width)/64 # Number of rogue stars

    # create galaxy
    if chaos == 0:
        for i in range(round(decay)):
            for j in range(nArms):
                    map = addSpiral(map, tMax, A, B, N, angO*j+(i*0.01), (i+1)*0.1)
    else:
        nArms = nArms+chaos
        for k in range(nArms):
            for i in range(round(decay*(k+1))):
                for j in range(nArms):
                        angO  = ((2*3.14)/nArms)+(k*j)
                        map = addSpiral(map, tMax, A, B+(chaos*0.01), N+(chaos*0.01), angO*j+(i*0.01), (i+1)*0.1)
        print("Adding spirals ", k, "of", nArms)
        nArms -= 1
    print("Spirals complete")

    # add rogue stars
    map = addGauss(map, sigma, nStars)
    map = addGauss(map, sigma/3, nStars/2)
    map = addGauss(map, sigma/6, nStars/4)
    print("Gauss complete")

    # add frame
    map = addFrame(map, sigma2, nStars)
    print("Frame complete")
    map.save('ringermacher.png')

    # decluster
    map = removeClusters(map)
    map.save('loose_ringermacher.png')
