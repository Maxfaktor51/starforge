from PIL import Image

# Dimensions of the image
width = 1000
height = 1000

# Create a blank image
img = Image.new('L', (width, height), color=0)  # 'L' for grayscale

# Generate galaxy-like structure
# You can implement your own algorithm or use libraries like numpy
# Here's a simple example of randomly placing stars
import random
num_stars = 5000
for _ in range(num_stars):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    img.putpixel((x, y), 255)  # 255 represents white (star)

# Save the image
img.save('galaxy.png')
