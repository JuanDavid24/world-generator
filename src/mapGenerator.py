import numpy as np
import noise
from diamondSquare import diamondSquare as ds

def perlin_map(shape = (1024, 1024), scale = 100, octaves = 1, persistence = 0.5, lacunarity = 2.0):
    map = np.zeros(shape)

    for i in range(shape[0]):
        for j in range(shape[1]):
            map[i][j] = noise.pnoise2(i/scale, 
                                        j/scale, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        base=0)        
    return map

def diamond_square_map(n, roughness=1, seed=None):
    map = ds(n, roughness, seed)
    return normalize_map(map)

def normalize_map(map):
    return (map - map.min()) / (map.max() - map.min())