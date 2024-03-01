from PIL import Image, ImageDraw
import numpy as np

# Define image dimensions
width = 1000
height = 1000

# Create a blank image
img = Image.new('L', (width, height), color=0)  # 'L' for grayscale
draw = ImageDraw.Draw(img)

# Define parameters for spiral arms
num_arms = 40  # Number of spiral arms
num_rotations = 4  # Number of rotations for the spiral arms
arm_length = min(width, height) / 10  # Length of each arm

# Function to calculate spiral arm coordinates
def spiral_coordinates(theta):
    radius = arm_length * theta / (2 * np.pi)
    x = width / 2 + radius * np.cos(theta)
    y = height / 2 + radius * np.sin(theta)
    return x, y

# Define Gaussian distribution parameters for central concentration
center_x = width / 2
center_y = height / 2
sigma = min(width, height) / 8  # Adjust the sigma parameter to control the distribution spread

# Generate stars with more stars closer to the center
num_stars = 5000
x_dist = np.random.normal(center_x, sigma, num_stars)
y_dist = np.random.normal(center_y, sigma, num_stars)

# Clip coordinates to image bounds
x_dist = np.clip(x_dist, 0, width - 1)
y_dist = np.clip(y_dist, 0, height - 1)

# Draw stars along spiral arms
for i in range(num_stars):
    x, y = map(int, (x_dist[i], y_dist[i]))
    theta = np.arctan2(y - center_y, x - center_x)
    arm_theta = (theta + np.pi) % (2 * np.pi)  # Normalize to [0, 2*pi]
    for j in range(num_arms):
        arm_start = j * (2 * np.pi / num_arms)
        arm_end = (j + 1) * (2 * np.pi / num_arms)
        if arm_start <= arm_theta < arm_end:
            draw.point((x, y), fill=255)  # Draw single pixel
            break  # Exit loop once the arm is found

# Save the image
img.save('spiral_galaxy.png')
