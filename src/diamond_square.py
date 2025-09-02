import numpy as np

def diamond_square(n, roughness=1, seed=None, corners=None):
    size = 2**n + 1
    map = np.zeros((size, size))
    
    # Create a random number generator with provided seed (if seed is None, it will use a random seed)
    rng = np.random.default_rng(seed)

    # Initialize the corners of the grid with the given seed values
    map = set_corners(map, rng, corners)

    chunk_size = size
    while n > 0:
        map = diamond_step(map, chunk_size, rng, roughness)
        map = square_step(map, chunk_size, rng, roughness)
        n -= 1
        chunk_size = 2**n + 1
        roughness /= 2
    return map

def set_corners(map, rng, corners=None):
    if corners is None:
        corners = rng.random(4)   
    last_index = map.shape[0] - 1
    map[0, 0] = corners[0]                     # top-left
    map[0, last_index] = corners[1]            # top-right
    map[last_index, 0] = corners[2]            # bottom-left
    map[last_index, last_index] = corners[3]   # bottom-right
    return map

def diamond_step(map, chunk_size, rng, roughness=1): 
    '''x, y: top-left corner of first chunk'''
    map_size = map.shape[0]
    half = chunk_size // 2

    for x in range(0, map_size-1, chunk_size-1):
        for y in range(0, map_size-1, chunk_size-1):
            # calculate the diamond midpoint value
            avg = (
                map[y, x] + 
                map[y + chunk_size - 1, x] + 
                map[y, x + chunk_size - 1] + 
                map[y + chunk_size - 1, x + chunk_size - 1]
                ) / 4
            value = rng.uniform(-1,1) * roughness # random value scaled by roughness
            map[y + half, x + half] = avg + value
    return map

def square_step(map, chunk_size, rng, roughness=1):
    size = map.shape[0]
    half = chunk_size // 2
    for y in range(0, size, half):
        x0 = int(((y / half + 1) % 2) * half)
        for x in range(x0, size, chunk_size-1):
            map = calculate_square_value(map, x, y, chunk_size, rng, roughness)
    return map

def calculate_square_value(map, x, y, chunk_size, rng, roughness=1):
    neighbor_values = get_square_neighbor_values(map, x, y, chunk_size)
    avg = sum(neighbor_values) / len(neighbor_values)
    value = rng.uniform(-1,1) * roughness # random value scaled by roughness
    map[y, x] = avg + value
    return map

def get_square_neighbor_values(map, x, y, chunk_size):
    map_size = map.shape[0]
    half = chunk_size // 2

    # Orthogonal neighbors of point (x,y)
    top = (y-half, x)
    bottom = (y+half, x)
    left = (y, x-half)
    right = (y, x+half)

    neighbors = [p for p in [top, bottom, left, right] if is_within_bounds(p[1], p[0], map_size)]  # extract map values for neighbour points, discard points that fall outside the grid
    neighbor_values = [map[p] for p in neighbors]
    return neighbor_values

def is_within_bounds(x, y, map_size):
    # checks if point (x, y) is within map bounds
    return 0 <= x <= map_size-1 and 0 <= y <= map_size-1