import numpy as np

def diamondSquare(n, roughness=1, seed=None):
    size = 2**n + 1
    map = np.zeros((size, size))

    # Initialize the corners of the grid with the given seed values
    setInitialCorners(map, seed)

    chunk_size = size
    while n > 0:
        diamondStep(map, chunk_size, roughness)
        squareStep(map, chunk_size, roughness)
        n -= 1
        chunk_size = 2**n + 1
        roughness /= 2
    return map

def setInitialCorners(map, seed=None):
    if seed is None:
        seed = np.random.rand(4)       
    last_index = map.shape[0] - 1
    map[0, 0] = seed[0]                     # top-left
    map[0, last_index] = seed[1]            # top-right
    map[last_index, 0] = seed[2]            # bottom-left
    map[last_index, last_index] = seed[3]   # bottom-right
    return map

def diamondStep(map, chunkSize, roughness=1): 
    '''x, y: top-left corner of first chunk'''
    mapSize = map.shape[0]
    half = chunkSize // 2

    for x in range(0, mapSize-1, chunkSize-1):
        for y in range(0, mapSize-1, chunkSize-1):
            # calculate the diamond midpoint value
            avg = (map[y, x] + map[chunkSize-1, x] + map[y, chunkSize-1] + map[chunkSize-1, chunkSize-1]) / 4
            value = np.random.uniform(-1, 1) * roughness # random value scaled by roughness
            #value = min(1, max(0, random + avg)) # ensure value is between 0 and 1
            map[y + half, x + half] = avg + value
    return map

def squareStep(map, chunkSize, roughness=1):
    size = map.shape[0]
    half = chunkSize // 2
    for y in range(0, size, half):
        x0 = int(((y / half + 1) % 2) * half)
        for x in range(x0, size, chunkSize-1):
            map = calculateSquareValue(map, x, y, chunkSize, roughness )
    return map

def calculateSquareValue(map, x, y, chunkSize, roughness=1):
    neighborsValues = getSquareNeighborsValues(map, x, y, chunkSize)
    avg = sum(neighborsValues) / len(neighborsValues)
    value = np.random.uniform(-1, 1) * roughness # random value scaled by roughness
    #value = min(1, max(0, random + avg)) # ensure value is between 0 and 1
    map[y, x] = avg + value
    return map

def getSquareNeighborsValues(map, x, y, chunkSize):
    mapSize = map.shape[0]
    half = chunkSize // 2

    # Orthogonal neighbours of point (x,y)
    top = (y-half, x)
    bottom = (y+half, x)
    left = (y, x-half)
    right = (y, x+half)

    neighbors = [p for p in [top, bottom, left, right] if pointIsInMap(p[1], p[0], mapSize)]  # extract map values for neighbour points, discard points that fall outside the grid
    neighborsValues = [map[p] for p in neighbors]
    return neighborsValues

def pointIsInMap(x, y, mapSize):
    # checks if point (x, y) is within map bounds
    return 0 <= x <= mapSize-1 and 0 <= y <= mapSize-1