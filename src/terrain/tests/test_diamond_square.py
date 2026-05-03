import numpy as np 
import pytest
from terrain import diamond_square as ds

# data
map_empty_5x5 = np.zeros((5, 5))
corners_a = [0.5, 0.9, 0.6, 0.7]

# diamond step dataset
input_map_a = np.array([[0.5, 0.0, 0.0, 0.0, 0.9],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.6, 0.0, 0.0, 0.0, 0.7]]) 
chunk_size_a = 5
x_a, y_a = (0, 0)
points_a = [(2, 2)]
seed_a = 123

output_map_a = np.array([[0.5, 0.0, 0.0, 0.0, 0.9],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.85735186, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.6, 0.0, 0.0, 0.0, 0.7]]) 

input_map_b = np.array([[0.5, 0.0, 0.1, 0.0, 0.9],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.3, 0.0, 0.2, 0.0, 0.4],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.5, 0.0, 0.2, 0.0, 0.7]])
chunk_size_b = 3
x_b, y_b = (2, 0) 
points_b = [(1, 1), (1, 3), (3, 1), (3, 3)]
seed_b = 456

output_map_b = np.array([[0.5, 0., 0.1, 0., 0.9],
                         [0.,  0.24467324, 0., 0.02405681, 0.],
                         [0.3, 0., 0.2, 0., 0.4],
                         [0.,  0.2476553,  0., 0.62984998, 0.],
                         [0.5, 0., 0.2, 0., 0.7]])

# square step dataset
input_map_c = np.array([[0.5, 0.0, 0.1, 0.0, 0.9],
                        [0.0, 0.5, 0.0, 0.5, 0.0],
                        [0.3, 0.0, 0.2, 0.0, 0.4],
                        [0.0, 0.5, 0.0, 0.5, 0.0],
                        [0.5, 0.0, 0.2, 0.0, 0.7]])
chunk_size_c = 3
seed_c = 789
seec_c_sqr_step_no_zeros = 123
output_map_c = np.array([[0.5, 0.3, 0.1, 0.21414402, 0.9],
                         [0.56517943, 0.5, 0.4, 0.5, 0.10350159],
                         [0.3, 0.48553013, 0.2, 0.2 , 0.4],
                         [0.37589717, 0.5, 0.62346283, 0.5, 0.1139135 ],
                         [0.5, 0.49245978, 0.2, 0.74488143, 0.7]])

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
neighbor_values_c_wrap = [
    [0.5, 0.1, 0.5, 0.5],   # (0, 1)
    [0.1, 0.5, 0.5, 0.9],   # (0, 3)
    [0.5, 0.3, 0.5, 0.5],   # (1, 0)
    [0.5, 0.2, 0.5, 0.1],   # (1, 2)
    [0.9, 0.5, 0.5, 0.4],   # (1, 4)
    [0.3, 0.2, 0.5, 0.5],   # (2, 1)
    [0.2, 0.4, 0.5, 0.5],   # (2, 3)
    [0.5, 0.5, 0.5, 0.3],   # (3, 0)
    [0.5, 0.5, 0.2, 0.2],   # (3, 2)
    [0.5, 0.5, 0.7, 0.4],   # (3, 4)
    [0.5, 0.2, 0.5, 0.5],   # (4, 1)
    [0.2, 0.7, 0.5, 0.5]    # (4, 3)
]

# check map corner setting up
def test_set_corners():
    new_map = ds.set_corners(map_empty_5x5, corners_a)
    assert np.array_equal(new_map, input_map_a)

# check new_map has same zeros than output example map
@pytest.mark.parametrize("map, chunk_size, seed, output_map", [(input_map_a, chunk_size_a, seed_a, output_map_a), (input_map_b, chunk_size_b, seed_b, output_map_b)])
def test_diamond_step(map, chunk_size, seed, output_map):
    rng = np.random.default_rng(seed)
    new_map = ds.diamond_step(map, chunk_size, rng)
    assert np.array_equal(new_map == 0, output_map == 0) # compare masks with positions equal to zero    

# check diamond step output to be equal when same input map and seed is given
@pytest.mark.parametrize("map, chunk_size, seed", [(input_map_a, chunk_size_a, seed_a), (input_map_b, chunk_size_b, seed_b)])
def test_diamond_step_seed(map, chunk_size, seed):
    rng = np.random.default_rng(seed)  
    new_map1 = ds.diamond_step(map, chunk_size, rng)
    new_map2 = ds.diamond_step(map, chunk_size, rng)
    assert np.array_equal(new_map1, new_map2)

@pytest.mark.parametrize("point, neighbor_values", list(zip(points_c, neighbor_values_c)))
def test_get_square_neighbor_values(point, neighbor_values):
    y, x = point
    result = ds.get_square_neighbor_values(input_map_c, x, y, chunk_size_c)
    assert sorted(result) == sorted(neighbor_values)

@pytest.mark.parametrize("point, neighbor_values", list(zip(points_c, neighbor_values_c_wrap)))
def test_get_square_neighbor_values_wrap(point, neighbor_values):
    y, x = point
    result = ds.get_square_neighbor_values(input_map_c, x, y, chunk_size_c, wrap=True)
    assert sorted(result) == sorted(neighbor_values)
    
# check new_map has populated points with non-zero values given particular seed
@pytest.mark.parametrize("map, chunk_size, seed", [(input_map_c, chunk_size_c, seec_c_sqr_step_no_zeros)])
def test_square_step(map, chunk_size, seed):
    rng = np.random.default_rng(seed)  
    new_map = ds.square_step(map, chunk_size, rng)
    assert not (new_map == 0).any() 

# check square step output to be equal when same input map and seed is given
@pytest.mark.parametrize("map, chunk_size, seed", [(input_map_c, chunk_size_c, seed_c)])
def test_square_step_seed(map, chunk_size, seed):
    rng = np.random.default_rng(seed) 
    new_map1 = ds.square_step(map, chunk_size, rng)
    new_map2 = ds.square_step(map, chunk_size, rng)
    assert np.array_equal(new_map1, new_map2)

@pytest.mark.parametrize("n, size, roughness, seed, corners", [(3, 9, 1, None, [0.2, 0.5, 0.1, 0.9]), (4, 17, 1, None, None), (5, 33, 1, None, None)])
def test_diamond_square(n, size, roughness, seed, corners):
    map, _, _ = ds.diamond_square(n, roughness, seed, corners)
    # check map size
    assert map.shape[0] == size

    # check corners if given
    if corners is not None:
        corners = [map[0, 0], map[0, size-1], map[size-1, 0], map[size-1, size-1]]
        assert corners == corners
            
def test_diamond_square_seed():
    # check map reproductibility given same seed
    map1, _, _ = ds.diamond_square(n=4, roughness=1, seed=123, corners=[0.5, 0.5, -0.5, -0.5])
    map2, _, _ = ds.diamond_square(n=4, roughness=1, seed=123, corners=[0.5, 0.5, -0.5, -0.5])
    assert np.array_equal(map1, map2)
    
    # check map variation given different seed
    map3 = ds.diamond_square(n=4, roughness=1, seed=456, corners=[0.5, 0.5, -0.5, -0.5])
    assert not np.array_equal(map1, map3)
    
    # check map variation given same seed but changing other parameters
    # corners
    map3 = ds.diamond_square(n=4, roughness=1, seed=123, corners=[-0.2, 0.3, 0.2, 0.9])
    assert not np.array_equal(map1, map3)
    
    # roughness
    map3 = ds.diamond_square(n=4, roughness=0.5, seed=123, corners=[0.5, 0.5, -0.5, -0.5])
    assert not np.array_equal(map1, map3)
    
    # n
    map3 = ds.diamond_square(n=3, roughness=1, seed=123, corners=[0.5, 0.5, -0.5, -0.5])
    assert not np.array_equal(map1, map3)

def test_diamond_square_seed_wrap():
    # check map reproductibility given same seed
    map1, _, _ = ds.diamond_square(n=4, roughness=1, seed=123, corners=[0.5, 0.5, 0.5, 0.5], wrap=True)
    map2, _, _ = ds.diamond_square(n=4, roughness=1, seed=123, corners=[0.5, 0.5, 0.5, 0.5], wrap=True)
    assert np.array_equal(map1, map2)