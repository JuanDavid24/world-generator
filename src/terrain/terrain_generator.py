import numpy as np
import noise
from diamond_square import diamond_square as ds

def perlin_map(shape=(1024, 1024), scale=100, octaves=1, persistence=0.5, lacunarity=2, seed=None, normalized=False):
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
        return normalize_map(map, -1, 1)
    return map

def diamond_square_map(n, roughness=1, seed=None, corners=None):
    map = ds(n, roughness, seed, corners)
    return map

def normalize_map(map, min, max):
    """ Normalizes a map to a given range [min, max]"""
    return (map - map.min()) / (map.max() - map.min()) * (max - min) + min