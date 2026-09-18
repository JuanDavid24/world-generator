import numpy as np 
import pytest

from engine.terrain import diamond_square as ds
from engine.terrain import perlin_noise as pn
from engine.world.spawner import Spawner, Vegetation_params

# --- dataset ---
TERRAIN_DATA_DUMMY = [      # mock terrain of zeros
    np.zeros((16, 16)),     # pair
    np.zeros((15, 15))      # odd
]

TERRAIN_DATA = [
    np.array([[-0.5, 0.1, 0.3, 0.1, 0.1],
              [0.5, -0.1, 0.3, 0.9, 0.9],
              [0.5, 0.1, -0.3, 0.1, 0.1],
              [0.5, 0.1, -0.3, 0.1, 0.1],
              [-0.9, 0.1, 0.3, -0.1, -0.1]]),
    np.array([[-0.5, 0.1, 0.3, 0.1, 0.1, -0.2],
              [0.5, -0.1, 0.3, 0.9, 0.9, 0.2],
              [0.5, 0.1, -0.3, 0.1, 0.1, 0.7],
              [0.5, 0.1, -0.3, 0.1, 0.1, 0.2],
              [0.3, 0.2, -0.1, 0.4, 0.8, 0.2],
              [-0.9, 0.1, 0.3, -0.1, -0.1, 0.1]])
]
DISTANCE_DATA = [3, 2]

# --- fixtures ---
@pytest.fixture(params=TERRAIN_DATA_DUMMY)
def multi_terrain_dummy(request):
    return request.param

@pytest.fixture(params=TERRAIN_DATA)
def multi_terrain(request):
    return request.param

@pytest.fixture(params=DISTANCE_DATA)
def multi_vegetation(request):
    return Vegetation_params(distance=request.param, cover=0.7)

@pytest.fixture
def dynamic_spawner_dummy(multi_terrain_dummy, multi_vegetation):
    return Spawner(terrain=multi_terrain_dummy, vegetation=multi_vegetation, seed=123)

@pytest.fixture
def dynamic_spawner(multi_terrain, multi_vegetation):
    return Spawner(terrain=multi_terrain, vegetation=multi_vegetation, seed=123)

# --- tests ---
def test_noise_map_shape(dynamic_spawner_dummy):
    terrain_size = dynamic_spawner_dummy.terrain_size
    distance = dynamic_spawner_dummy.vegetation.distance
    
    # calculaate expected values
    expected_noise_size = terrain_size // distance
    expected_noise_shape = (expected_noise_size, expected_noise_size)
    
    assert dynamic_spawner_dummy.noise_map.shape == expected_noise_shape

def test_base_axes(dynamic_spawner_dummy):
    # generate base axes
    base_x, base_y = dynamic_spawner_dummy.create_base_axes()
    
    # calculate expected base axes
    distance = dynamic_spawner_dummy.vegetation.distance
    terrain_size = dynamic_spawner_dummy.terrain_size
    
    cell_count = terrain_size // distance
    cell_offset = distance / 2.0
    
    expected_centers = [cell_offset + i * distance for i in range(cell_count)]   # list of cell centers 
    expected_base_x = np.array(expected_centers, dtype=np.float64)[None, :]      # transformed to row vector and numpy array  
    expected_base_y = expected_base_x.T
    
    assert np.allclose(base_x, expected_base_x)
    assert np.allclose(base_y, expected_base_y)
    
def test_jittered_positions(dynamic_spawner_dummy):
    # generate jittered x and y matrix
    jittered_positions_x, jittered_positions_y = dynamic_spawner_dummy.create_jittered_positions()
    
    # assert same shape as noise map
    noise_map_shape = dynamic_spawner_dummy.noise_map.shape
    assert(noise_map_shape == jittered_positions_x.shape)
    assert(noise_map_shape == jittered_positions_y.shape)
    
    # check positions be inside terrain
    terrain_size = dynamic_spawner_dummy.terrain_size
    positions_x_in_bound = np.all((0 <= jittered_positions_x) & 
                                  (jittered_positions_x < terrain_size))
    positions_y_in_bound = np.all((0 <= jittered_positions_y) & 
                                      (jittered_positions_y < terrain_size))
    assert positions_x_in_bound
    assert positions_y_in_bound
    
def test_fitness_map(dynamic_spawner):
    # generate fitness
    dynamic_spawner.create_fitness_map()
    fitness_map = dynamic_spawner.fitness_map
    fitness_shape = fitness_map.shape

    # assert same shape as noise map
    noise_map_shape = dynamic_spawner.noise_map.shape
    assert fitness_shape == noise_map_shape
    
    # check values
    noise_map = dynamic_spawner.noise_map
    real_heightmap = dynamic_spawner.real_heightmap
    min_h = dynamic_spawner.vegetation.min_height
    max_h = dynamic_spawner.vegetation.max_height
    var = dynamic_spawner.vegetation.variance
    INVALID_HEIGHT_PENALTY = -1.0
    
    for y in range(noise_map_shape[0]):
        for x in range(noise_map_shape[1]):
            if min_h <= real_heightmap[y, x] < max_h:
                assert(is_valid_fitness(fitness_map[y, x], 
                                        noise_map[y, x],
                                        var))
            else:
                assert(fitness_map[y, x] == INVALID_HEIGHT_PENALTY)
    
def is_valid_fitness(f, base_f, variance):
    return base_f - variance <= f <= base_f + variance