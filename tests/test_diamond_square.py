import numpy as np 
import pytest
from src import diamond_square as ds

# data
rng_no_seed = np.random.default_rng()
map_empty_5 = np.zeros((5, 5))

# diamond step dataset
map_a = np.array([[0.5, 0.0, 0.0, 0.0, 0.9],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.6, 0.0, 0.0, 0.0, 0.7]]) 
chunk_size_a = 5
x_a, y_a = (0, 0)
points_a = [(2, 2)]

map_b = np.array([[0.5, 0.0, 0.1, 0.0, 0.9],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.3, 0.0, 0.2, 0.0, 0.4],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.5, 0.0, 0.2, 0.0, 0.7]])
chunk_size_b = 3
x_b, y_b = (2, 0) 
points_b = [(1, 1), (1, 3), (3, 1), (3, 3)]

# square step dataset
map_c = np.array([[0.5, 0.0, 0.1, 0.0, 0.9],
                 [0.0, 0.5, 0.0, 0.5, 0.0],
                 [0.3, 0.0, 0.2, 0.0, 0.4],
                 [0.0, 0.5, 0.0, 0.5, 0.0],
                 [0.5, 0.0, 0.2, 0.0, 0.7]])
chunk_size_c = 3

# for first point (0, 1), second point (0, 3), third point (1, 0)
points_c = [
    (0, 1), (0, 3),
    (1, 0), (1, 2), (1, 4),
    (2, 1), (2, 3),
    (3, 0), (3, 2), (3, 4),
    (4, 1), (4, 3)
]
neighbor_values_c = [
    [0.5, 0.1, 0.5],         # (0, 1)
    [0.1, 0.5, 0.9],         # (0, 3)
    [0.5, 0.3, 0.5],         # (1, 0)
    [0.5, 0.2, 0.5, 0.1],    # (1, 2)
    [0.9, 0.5, 0.4],         # (1, 4)
    [0.3, 0.2, 0.5, 0.5],    # (2, 1)
    [0.2, 0.4, 0.5, 0.5],    # (2, 3)
    [0.5, 0.5, 0.3],         # (3, 0)
    [0.5, 0.5, 0.2, 0.2],    # (3, 2)
    [0.5, 0.7, 0.4],         # (3, 4)
    [0.5, 0.2, 0.5],         # (4, 1)
    [0.2, 0.7, 0.5]          # (4, 3)
]

def test_set_corners():
    # set initialization with a given corner set
    corners = [0.5, 0.9, 0.6, 0.7]
    new_map = ds.set_corners(map_empty_5, rng_no_seed, corners)
    assert np.array_equal(new_map, map_a)
    
    # set initialization when no corner set is provided
    new_map = ds.set_corners(map_empty_5, rng_no_seed)
    corner_pos = [(0, 4), (0, 4), (4, 0), (4, 4)]
    for p in corner_pos:
        px, py = p
        assert new_map[(py, px)] != 0

@pytest.mark.parametrize("map, chunk_size, rng, points", [(map_a, chunk_size_a, rng_no_seed, points_a), 
                                                           (map_b, chunk_size_b, rng_no_seed, points_b)])
def test_diamond_step(map, chunk_size, rng, points):
    new_map = ds.diamond_step(map, chunk_size, rng)
    for p in points:
        px, py = p
        assert new_map[(py, px)] != 0

@pytest.mark.parametrize("point, neighbor_values", list(zip(points_c, neighbor_values_c)))
def test_get_square_neighbor_values(point, neighbor_values):
    y, x = point
    result = ds.get_square_neighbor_values(map_c, x, y, chunk_size_c)
    assert sorted(result) == sorted(neighbor_values)

@pytest.mark.parametrize("map, points, chunk_size, rng", [(map_c, points_c, chunk_size_c, rng_no_seed)])
def test_square_step(map, points, chunk_size, rng):
    new_map = ds.square_step(map, chunk_size, rng)
    for p in points:
        y, x = p
        assert new_map[(y, x)] != 0

@pytest.mark.parametrize("n, size, roughness, seed, corners", [(3, 9, 1, None, [0.2, 0.5, 0.1, 0.9]), (4, 17, 1, None, None), (5, 33, 1, None, None)])
def test_diamond_square(n, size, roughness, seed, corners):
    map = ds.diamond_square(n, roughness, seed, corners)
    # check map size
    assert map.shape[0] == size

    # check seed if given
    if corners is not None:
        corners = [map[0, 0], map[0, size-1], map[size-1, 0], map[size-1, size-1]]
        assert corners == corners
        
    # check if matrix is completelly populated
    for row in map:
        for p in row:
            assert p != 0.0
            
def test_diamond_square_seed():
    # check map reproductibility given same seed
    map1 = ds.diamond_square(n=4, roughness=1, seed=123)
    map2 = ds.diamond_square(n=4, roughness=1, seed=123)
    assert np.array_equal(map1, map2)
    
    # check map variation given different seed
    map3 = ds.diamond_square(n=4, roughness=1, seed=456)
    assert not np.array_equal(map1, map3)
    
    # check map variation given same seed but changing other parameters
    # corners
    map3 = ds.diamond_square(n=4, roughness=1, seed=123, corners=[0.5, 0.3, 0.2, 0.9])
    assert not np.array_equal(map1, map3)
    
    # roughness
    map3 = ds.diamond_square(n=4, roughness=0.5, seed=123)
    assert not np.array_equal(map1, map3)
    
    # n
    map3 = ds.diamond_square(n=3, roughness=1, seed=123)
    assert not np.array_equal(map1, map3)
    
    
    
    

    