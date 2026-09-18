import numpy as np

from dataclasses import dataclass
from engine.terrain.perlin_noise import generate_perlin_map
from engine.terrain.normalize import normalize_map

@dataclass
class Vegetation_params:
    distance: int
    cover: float = 0.5
    max_jitter: float | None = None
    
    def __post_init__(self):
        if self.max_jitter is None:
            self.max_jitter = self.distance // 4
    
class Spawner:
    def __init__(self, terrain, vegetation: Vegetation_params, seed=None):
        self.terrain = terrain
        self.terrain_size = self.terrain.shape[0]
        self.vegetation = vegetation
        self.seed = seed
        self.rng = np.random.default_rng(seed) # Initialize random number generator with seed
        self.noise_map_threshold = 1 - self.vegetation.cover
        self.create_noise_map()
        # self.create_jitter()
        self.sample_terrain_heights()
        
        
    def create_noise_map(self):
        self.noise_map_size = self.terrain_size // self.vegetation.distance
        SIZE_SCALE_FACTOR = 2.56    # size/scale factor for perlin maps, calculed as map_side_size/scale. Default ratio defined as: 256/100
        
        perlin_scale = self.noise_map_size / SIZE_SCALE_FACTOR
        noise_map, seed = generate_perlin_map(shape=(self.noise_map_size, self.noise_map_size), 
                                        scale=perlin_scale, 
                                        seed=self.seed)
        self.noise_map = normalize_map(noise_map, 0, 1)
        self.seed = seed
        
    def create_jitter_matrix(self):
        random_matrix = self.rng.uniform(-self.vegetation.max_jitter, self.vegetation.max_jitter, 
                                         size=(self.noise_map_size, self.noise_map_size))
        jitter = np.where(self.noise_map >= self.noise_map_threshold, random_matrix, 0)
        # jitter = jitter.astype(int) # cast to int
        return jitter
        
    def create_jittered_positions(self):        
        base_x, base_y = self.create_base_axes()
        
        # jitter matrices for plant displacement
        jitter_x = self.create_jitter_matrix()
        jitter_y = self.create_jitter_matrix()
        
        # jitter-displaced x and y spawn coordinates on the terrain
        jittered_x = jitter_x + base_x
        jittered_y = jitter_y + base_y
        
        # round and cast values to int
        jittered_x = np.round(jittered_x).astype(int)
        jittered_y = np.round(jittered_y).astype(int)
        
        # clip values so they keep inside terrain limits
        max_index = self.terrain_size - 1
        jittered_x = np.clip(jittered_x, 0, max_index)
        jittered_y = np.clip(jittered_y, 0, max_index)
        
        return jittered_x, jittered_y
        
    def create_base_axes(self):
        # each cell of terrain where a plant could spawn
        CELL_COUNT = self.noise_map_size
        CELL_CENTER_OFFSET = self.vegetation.distance / 2.0 # preserve decimals for not losing precision early
        
        # base axis coordinates for plant spawning (center point of each possible spawn cell on the terrain)
        base_x = np.arange(CELL_COUNT)[None, :] * self.vegetation.distance + CELL_CENTER_OFFSET # row vector 
        base_y = base_x.T   # col vector
        return base_x, base_y
    
    def sample_terrain_heights(self):
        positions_x, positions_y = self.create_jittered_positions()
        self.real_heightmap = self.terrain[positions_y, positions_x]
        
    # def create_spawn_map(self):
    #     NOISE_MAP_THRESHOLD = 1 - self.vegetation.cover
        
    #     spawn_map = np.zeros((self.noise_map_size, self.noise_map_size))
    #     self.fitness() # create random spawn matrix for randomize tree spawn
        
    #     spawn_map = np.where(self.noise_map + self.fitness_matrix > NOISE_MAP_THRESHOLD, 1, 0)
    #     self.spawn_map = spawn_map
        
    # def fitness(self):
    #     self.fitness_matrix = self.rng.uniform(-0.15, 0.15, size=(self.noise_map.shape[0], self.noise_map.shape[0]))