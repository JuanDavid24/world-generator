import mapGenerator as mg
import matplotlib.pyplot as plt

maps = [mg.generateMap(),
mg.generateMap(octaves=2),
mg.generateMap(octaves=3),
mg.generateMap(octaves=4)]

for i, map in enumerate(maps):
    plt.subplot(2, 2, i + 1)
    plt.title("octaves = " + str(i + 1))
    plt.imshow(map, cmap='gray')
    plt.colorbar()

plt.show()