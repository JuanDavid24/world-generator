import numpy as np

MAX_AMPLITUDE = 1.0
MAX_RANDOM_DISPLACEMENT = 1.0
    
def diamond_square(n, roughness=1.0, seed=None, initial_corners=None, wrap=False):
    size = 2**n + 1
    map = np.zeros((size, size))
    
    if seed is None:
        # Create a random seed between 0 and 2^31
        seed = np.random.randint(0, 2**31)
        
    # Initialize random number generator with seed
    rng = np.random.default_rng(seed)

    # Initialize the corners of the grid 
    if initial_corners is None:
        initial_corners = np.random.uniform(-MAX_AMPLITUDE, MAX_AMPLITUDE, size=4)
    else:
        # ensure corners is a numpy float array
        initial_corners = np.asarray(initial_corners, dtype=float)
        
    map = set_corners(map, initial_corners)

    chunk_size = size
    while n > 0:
        map = diamond_step(map, chunk_size, rng, roughness)
        map = square_step(map, chunk_size, rng, roughness, wrap)
        n -= 1
        chunk_size = 2**n + 1
        roughness /= 2
    return map, seed, initial_corners

def set_corners(map, corners):   
    last_index = map.shape[0] - 1
    map[0, 0] = corners[0]                     # top-left
    map[0, last_index] = corners[1]            # top-right
    map[last_index, 0] = corners[2]            # bottom-left
    map[last_index, last_index] = corners[3]   # bottom-right
    return map

def diamond_step(map, chunk_size, rng, roughness=1.0): 
    NEIGHBOR_COUNT = 4
    map_size = map.shape[0]
    half = chunk_size // 2

    '''x, y: top-left corner of first chunk'''
    for x in range(0, map_size-1, chunk_size-1):
        for y in range(0, map_size-1, chunk_size-1):
            # calculate the diamond midpoint value
            avg = (
                map[y, x] + 
                map[y + chunk_size - 1, x] + 
                map[y, x + chunk_size - 1] + 
                map[y + chunk_size - 1, x + chunk_size - 1]
                ) / NEIGHBOR_COUNT
            value = rng.uniform(-MAX_RANDOM_DISPLACEMENT, MAX_RANDOM_DISPLACEMENT) * roughness # random value scaled by roughness
            map[y + half, x + half] = np.clip(avg + value, -MAX_AMPLITUDE, MAX_AMPLITUDE)
    return map

def square_step(map, chunk_size, rng, roughness=1.0, wrap=False):
    size = map.shape[0]
    half = chunk_size // 2
    for y in range(0, size, half):
        x0 = (y + half) % (chunk_size -1)
        for x in range(x0, size, chunk_size-1):
            map = calculate_square_value(map, x, y, chunk_size, rng, roughness, wrap)
    return map

def calculate_square_value(map, x, y, chunk_size, rng, roughness=1.0, wrap=False):
    neighbor_values = get_square_neighbor_values(map, x, y, chunk_size, wrap)
    avg = sum(neighbor_values) / len(neighbor_values)
    value = rng.uniform(-MAX_RANDOM_DISPLACEMENT, MAX_RANDOM_DISPLACEMENT) * roughness # random value scaled by roughness
    map[y, x] = np.clip(avg + value, -MAX_AMPLITUDE, MAX_AMPLITUDE)
    return map

def get_square_neighbor_values(map, x, y, chunk_size, wrap=False):
    map_size = map.shape[0]
    half = chunk_size // 2

    # Orthogonal neighbors of point (x,y)
    top = (y-half, x)
    bottom = (y+half, x)
    left = (y, x-half)
    right = (y, x+half)
    
    neighbors = [p for p in [top, bottom, left, right] if is_within_bounds(p[1], p[0], map_size)]  # extract map values for neighbour points, discard points that fall outside the grid
    
    if wrap and len(neighbors) < 4:
        if x == 0:
            neighbors.append((y, map_size-half-1))
        if x == map_size-1:
            neighbors.append((y, half))
        if y == 0:
            neighbors.append((map_size-half-1, x))
        if y == map_size-1:
            neighbors.append((half, x))
               
    neighbor_values = [map[p] for p in neighbors]
    return neighbor_values

def is_within_bounds(x, y, map_size):
    # checks if point (x, y) is within map bounds
    return 0 <= x <= map_size-1 and 0 <= y <= map_size-1