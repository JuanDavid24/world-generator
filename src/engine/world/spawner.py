import numpy as np

from engine.terrain.perlin_noise import generate_perlin_map
from engine.utils.normalize import normalize_map

class Spawner:
    def __init__(self, terrain, spawn_distance, coverage=0.5, seed=None):
        self.terrain = terrain
        self.terrain_size = self.terrain.shape[0]
        self.spawn_distance = spawn_distance
        self.coverage = coverage
        self.seed = seed
        self.create_noise_map()

    def create_noise_map(self):
        VEGETATION_MATRIX_ROWS = VEGETATION_MATRIX_COLS = self.terrain_size // self.spawn_distance
        SIZE_SCALE_FACTOR = 2.56    # size/scale factor for perlin maps, calculed as map_side_size/scale. efault ratio defined as: 256/100
        
        perlin_scale = VEGETATION_MATRIX_ROWS / SIZE_SCALE_FACTOR
        
        noise_map, seed = generate_perlin_map(shape=(VEGETATION_MATRIX_ROWS, VEGETATION_MATRIX_COLS), 
                                        scale=perlin_scale, 
                                        seed=self.seed)
        self.noise_map = normalize_map(noise_map, -1, 1)
        self.seed = seed
        
    def create_spawn_map(self):
        NOISE_MAP_THRESHOLD = 1 - self.coverage
        NOISE_MAP_SIZE = self.noise_map.shape[0]
        
        spawn_map = np.zeros((NOISE_MAP_SIZE, NOISE_MAP_SIZE))
        spawn_map = np.where(self.noise_map > NOISE_MAP_THRESHOLD, 1, 0)
        self.spawn_map = spawn_map