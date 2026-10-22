import numpy as np
import noise

from engine.terrain.diamond_square import diamond_square as ds
from engine.terrain.perlin_noise import generate_perlin_map as pn
from engine.terrain.normalize import normalize_map
from src.utils.logger import log_terrain_to_json_file, save_terrain_as_png, format_terrain_data

def process_perlin_terrain(size, scale, octaves, persistence, lacunarity, seed, normalized, debug=False):
    heightmap, seed = get_perlin_map(size, scale, octaves, persistence, lacunarity, seed, normalized)
    
    if debug:
        log_terrain_to_json_file('perlin_noise', shape[0], seed, heightmap, scale=scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
        save_terrain_as_png('perlin_noise', heightmap)
        
    terrain_data = format_terrain_data(algorithm="perlin_noise", size=size, seed=seed, map=heightmap, scale=scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
    return terrain_data

def get_perlin_map(size=256, scale=100, octaves=1, persistence=0.5, lacunarity=2, seed=None, normalized=False):
    shape = (size, size)    
    heightmap, seed = pn(shape, scale, octaves, persistence, lacunarity, seed)
    
    if normalized:
        heightmap = normalize_map(heightmap, -1, 1)
    
    return heightmap, seed

def process_diamond_square_terrain(n, roughness=1, seed=None, initial_corners=None, wrap=False, debug=False):
    heightmap, seed, initial_corners = ds(n, roughness, seed, initial_corners, wrap)
    size = 2**n + 1
        
    if debug:
        log_terrain_to_json_file('diamond_square', size, seed, heightmap, n=n, roughness=roughness, initial_corners=initial_corners, wrap=wrap)
        save_terrain_as_png('diamond_square', heightmap)
    
    terrain_data = format_terrain_data(algorithm="diamond_square", size=size, seed=seed, map=heightmap, n=n, roughness=roughness, initial_corners=initial_corners, wrap=wrap)
    return terrain_data

