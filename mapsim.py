import numpy as np
from PIL import Image

# Constants
G = 6.67430e-11  # gravitational constant
width = 1000
height = 1000
num_particles = 100
num_iterations = 10

# Create a blank image
img = Image.new('L', (width, height), color=0)  # 'L' for grayscale
pixels = img.load()

# Initialize particles with random positions and velocities
particles = np.random.rand(num_particles, 4)  # [x, y, vx, vy]

# Define gravitational force calculation function
def calculate_gravity(particles):
    for i in range(num_particles):
        for j in range(i+1, num_particles):
            dx = particles[j, 0] - particles[i, 0]
            dy = particles[j, 1] - particles[i, 1]
            r_squared = dx**2 + dy**2
            if r_squared > 1e-3:  # avoid division by zero
                r = np.sqrt(r_squared)
                force = G / r_squared
                particles[i, 2] += force * dx / r
                particles[i, 3] += force * dy / r
                particles[j, 2] -= force * dx / r
                particles[j, 3] -= force * dy / r

# Simulation loop
for i in range(num_iterations):
    calculate_gravity(particles)
    particles[:, :2] += particles[:, 2:]  # update positions

# Map particle positions to image grid
for particle in particles:
    x, y = int(particle[0] * width), int(particle[1] * height)
    if 0 <= x < width and 0 <= y < height:
        pixels[x, y] = 255  # white (star)

# Save the image
img.save('galaxy2.png')
