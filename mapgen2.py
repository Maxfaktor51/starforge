from PIL import Image
import random
import numpy as np

# Dimensions of the image
width = 1000
height = 1000

# Create a blank image
img = Image.new('RGB', (width, height), color=0)  # 'L' for grayscale

cO_color = (146, 181, 255)
cB_color = (162, 192, 255)
cA_color = (213, 224, 255)
cF_color = (249, 245, 255)
cG_color = (255, 237, 227)
cK_color = (255, 218, 181)
cM_color = (255, 182, 108)


# Generate galaxy-like structure with more stars closer to the center
num_stars = 10000

# Define a Gaussian distribution centered at the image center
center_x = width / 2
center_y = height / 2
sigma = min(width, height) / 10  # Adjust the sigma parameter to control the distribution spread
x_dist = np.random.normal(center_x, sigma, num_stars)
y_dist = np.random.normal(center_y, sigma, num_stars)

# Clip coordinates to image bounds
x_dist = np.clip(x_dist, 0, width - 1)
y_dist = np.clip(y_dist, 0, height - 1)

for i in range(num_stars):
    x = int(round(x_dist[i]))
    y = int(round(y_dist[i]))
    starClass = i % 6
    match starClass:
        case 0:
            img.putpixel((x, y), cO_color)  # 255 represents white (star)
        case 1:
            img.putpixel((x, y), cB_color)
        case 2:
            img.putpixel((x, y), cA_color)
        case 3:
            img.putpixel((x, y), cF_color)
        case 4:
            img.putpixel((x, y), cG_color)
        case 5:
            img.putpixel((x, y), cK_color)
        case _:
            img.putpixel((x, y), cM_color)
# Save the image
img.save('galaxy.png')
