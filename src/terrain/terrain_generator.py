import numpy as np
import noise
from utils.map_logger import log_terrain_to_json
from diamond_square import diamond_square as ds

def perlin_map(shape=(1024, 1024), scale=100, octaves=1, persistence=0.5, lacunarity=2, seed=None, normalized=False, debug=False):
    if seed is None:
        # Create a random seed between 0 and 2^31
        seed = np.random.randint(0, 2**31)
    rng = np.random.default_rng(seed) 
    offset_x = rng.uniform(-10000, 10000)
    offset_y = rng.uniform(-10000, 10000)

    map = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):            
            map[i][j] = noise.pnoise2(i/scale + offset_x, 
                                        j/scale + offset_y, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        base=0)
    if normalized:
        return normalize_map(map, -1, 1), seed
    if debug:
        log_terrain_to_json('perlin_noise', shape[0], seed, map, scale=scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)

    return map, seed

def diamond_square_map(n, roughness=1, seed=None, corners=None, wrap=False, debug=False):
    map, seed, corners = ds(n, roughness, seed, corners, wrap)
        
    if debug:
        log_terrain_to_json('diamond_square', 2**n+1, seed, map, n=n, roughness=roughness, initial_corners=corners.tolist(), wrap=wrap)
    
    return map, seed, corners

def normalize_map(map, min, max):
    """ Normalizes a map to a given range [min, max]"""
    return (map - map.min()) / (map.max() - map.min()) * (max - min) + min