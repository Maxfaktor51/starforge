from PIL import Image
import random
import numpy as np

def polar_to_cartesian(rho, theta):
    """Convert polar coordinates to Cartesian coordinates."""
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y

def generate_logarithmic_spiral(width, height, num_arms, arm_length, num_stars):
    """Generate stars along a logarithmic spiral with adjustable arms and arm lengths."""
    img = Image.new('RGB', (width, height), color=0)
    center_x = width / 2
    center_y = height / 2
    
    # Create a Gaussian distribution centered at the image center
    sigma = min(width, height) / 10
    x_dist = np.random.normal(center_x, sigma, num_stars)
    y_dist = np.random.normal(center_y, sigma, num_stars)
    
    for i in range(num_stars):
        arm = random.randint(0, num_arms - 1)
        angle = random.uniform(0, 2*np.pi)
        distance = random.uniform(0, arm_length)
        arm_offset = 2*np.pi / num_arms * arm
        
        rho = distance * np.exp(angle)
        theta = angle + arm_offset
        x, y = polar_to_cartesian(rho, theta)
        
        x += center_x
        y += center_y
        
        x = int(round(x))
        y = int(round(y))
        
        # Ensure the star is within the image bounds
        if 0 <= x < width and 0 <= y < height:
            img.putpixel((x, y), (255, 255, 255))  # White pixel for star
    
    # Add stars according to Gaussian distribution
    for i in range(num_stars):
        x = int(round(x_dist[i]))
        y = int(round(y_dist[i]))
        
        # Ensure the star is within the image bounds
        if 0 <= x < width and 0 <= y < height:
            img.putpixel((x, y), (255, 255, 255))  # White pixel for star
            
    return img

def addGauss(width, height, img):
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
        img.putpixel((x,y), (255, 255, 255))
    # Save the image
    return img

# Define parameters
width = 1000
height = 1000
num_arms = 4  # Number of spiral arms
arm_length = 0.90  # Length of each spiral arm
num_stars = 1000

# Generate galaxy-like structure
galaxy_img = generate_logarithmic_spiral(width, height, num_arms, arm_length, num_stars)
galaxy_img = addGauss(width, height, galaxy_img)
# Save the image
galaxy_img.save('galaxy.png')