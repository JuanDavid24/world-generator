import random as rnd
import numpy as np

def diamondSquare(n, roughness=1, seed=None):
    size = 2 ** n + 1
    map = np.zeros((size, size))
    
    # Initialize the corners of the grid with the given seed values
    setInitialCorners(map, seed)
    diamondStep(map, 0, 0, size)
    return map

def setInitialCorners(map, seed=None):
    if seed is None:
        seed = np.random.rand(4)       
    last_index = map.shape[0] - 1
    map[0, 0] = seed[0]
    map[0, last_index] = seed[1]
    map[last_index, 0] = seed[2]
    map[last_index, last_index] = seed[3]
    
    """  print("Initial corners set:")
    print(map) """
    return map

def diamondStep(map, x, y, size, roughness=1): 
    half = size // 2
    avg = (map[x, y] + map[x, size-1] + map[size-1, y] + map[size-1, size-1]) / 4

    """ print(f"Diamond step at ({x}, {y}) with size {size}, average: {avg}")
    print(f"point {x, y} = {map[x, y]}")
    print(f"point {x, size-1} = {map[x, size-1]}")
    print(f"point {size-1, y} = {map[size-1, y]}")
    print(f"point {size-1, size-1} = {map[size-1, size-1]}") """

    # calculate the midpoint value
    randomValue = np.random.uniform(-1, 1) * roughness # random value scaled by roughness
    value = min(1, max(0, randomValue + avg)) # ensure value is between 0 and 1
    map[x + half, y + half] = value

    """ print(f"random value {randomValue}")
    print(f"midpoint {x + half, y + half} = {map[x + half, y + half]}") """

    return map

map = diamondSquare(2)
print(map)