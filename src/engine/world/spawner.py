import numpy as np

from dataclasses import dataclass
from engine.terrain.perlin_noise import generate_perlin_map
from engine.terrain.normalize import normalize_map

@dataclass
class Vegetation_params:
    distance: int
    cover: float = 0.5
    max_jitter: float | None = None
    variance: float | None = None
    min_height: float = -0.25
    max_height: float = 0.8
    
    def __post_init__(self):
        if self.max_jitter is None:
            self.max_jitter = 1.0
        if self.variance is None:
            self.variance = 0.15
    
class Spawner:
    def __init__(self, terrain, vegetation: Vegetation_params, seed=None):
        self.terrain = terrain
        self.terrain_size = self.terrain.shape[0]
        self.vegetation = vegetation
        self.seed = seed
        self.rng = np.random.default_rng(seed) # Initialize random number generator with seed
        self.spawn_threshold = 1 - self.vegetation.cover
        
    def create_spawn_map(self):
        self.create_noise_map()
        self.create_base_axes()
        self.create_jittered_positions()
        self.sample_terrain_heights()
        self.create_fitness_map()
        
        self.spawn_map = self.fitness_map > self.spawn_threshold
        
    def create_noise_map(self):
        self.noise_map_size = self.terrain_size // self.vegetation.distance
        SIZE_SCALE_FACTOR = 2.56    # size/scale factor for perlin maps, calculed as map_side_size/scale. Default ratio defined as: 256/100
        
        perlin_scale = self.noise_map_size / SIZE_SCALE_FACTOR
        noise_map, seed = generate_perlin_map(shape=(self.noise_map_size, self.noise_map_size), 
                                        scale=perlin_scale, 
                                        seed=self.seed)
        self.noise_map = normalize_map(noise_map)
        self.seed = seed
                
    def create_jitter_matrix(self):
        jitter = self.rng.uniform(-self.vegetation.max_jitter, self.vegetation.max_jitter, 
                                         size=(self.noise_map_size, self.noise_map_size))
        # jitter = np.where(self.noise_map >= self.spawn_threshold, random_matrix, 0)
        # jitter = jitter.astype(int) # cast to int
        return jitter
        
    def create_jittered_positions(self):        
        # jitter matrices for plant displacement
        jitter_x = self.create_jitter_matrix()
        jitter_y = self.create_jitter_matrix()
        
        # jitter-displaced x and y spawn coordinates on the terrain
        jittered_x = jitter_x + self.base_x
        jittered_y = jitter_y + self.base_y
        
        # round and cast values to int
        jittered_x = np.round(jittered_x).astype(int)
        jittered_y = np.round(jittered_y).astype(int)
        
        # clip values so they keep inside terrain limits
        max_index = self.terrain_size - 1
        jittered_x = np.clip(jittered_x, 0, max_index)
        jittered_y = np.clip(jittered_y, 0, max_index)
        
        self.positions_x = jittered_x 
        self.positions_y = jittered_y
        
        return jittered_x, jittered_y
        
    def create_base_axes(self):
        # each cell of terrain where a plant could spawn
        CELL_COUNT = self.noise_map_size
        CELL_CENTER_OFFSET = self.vegetation.distance / 2.0 # preserve decimals for not losing precision early
        
        # base axis coordinates for plant spawning (center point of each possible spawn cell on the terrain)
        base_x = np.arange(CELL_COUNT)[None, :] * self.vegetation.distance + CELL_CENTER_OFFSET # row vector 
        base_y = base_x.T   # col vector
        
        self.base_x = base_x
        self.base_y = base_y
        
        return base_x, base_y
    
    def sample_terrain_heights(self):
        self.spawn_points_heightmap = self.terrain[self.positions_y, self.positions_x]
        
    def create_valid_height_mask(self):
        return (self.spawn_points_heightmap >= self.vegetation.min_height) & (self.spawn_points_heightmap <= self.vegetation.max_height)
    
    def create_random_variance(self):
        return self.rng.uniform(-self.vegetation.variance, self.vegetation.variance, size=self.noise_map.shape)
        
    def create_fitness_map(self):
        INVALID_HEIGHT_PENALTY = -1.0 # for positions with out-of-bounds height values
        
        # filter valid height values
        valid_height_mask = self.create_valid_height_mask()
        
        # random variaton matrix
        random_variance = self.create_random_variance()
        
        # fitness map generation
        base_fitness = self.noise_map + random_variance 
        self.fitness_map = np.where(valid_height_mask, base_fitness, INVALID_HEIGHT_PENALTY)    # strict penalty applied to out-of-range heights
        
    def get_spawn_positions(self):
        self.spawn_positions_x = self.positions_x[self.spawn_map]
        self.spawn_positions_y = self.positions_y[self.spawn_map]