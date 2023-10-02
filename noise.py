from perlin_noise import PerlinNoise

noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)

xpix, ypix = 10, 10
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 10 * noise2([i/xpix, j/ypix])
        noise_val += 12.5 * noise3([i/xpix, j/ypix])
        noise_val += 11.25 * noise4([i/xpix, j/ypix])

        row.append(int(noise_val))
    pic.append(row)

print(pic)