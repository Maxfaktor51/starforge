from PIL import Image
import random
import numpy as np

# Dimensions of the image
width = 1000
height = 1000

# Create a blank image
img = Image.new('L', (width, height), color=0)  # 'L' for grayscale

# Generate galaxy-like structure with more stars closer to the center
num_stars = 25000

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
    img.putpixel((x, y), 255)  # 255 represents white (star)

# Save the image
img.save('galaxy.png')
