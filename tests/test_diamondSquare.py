import numpy as np 
import pytest
from src import diamond_square as ds

# data
# diamond step dataset
map_a = np.array([[0.5, 0.0, 0.0, 0.0, 0.9],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.5, 0.0, 0.0, 0.0, 0.7]]) 
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

@pytest.mark.parametrize("map, chunk_size, points", [(map_a, chunk_size_a, points_a), 
                                                           (map_b, chunk_size_b, points_b)])
def test_diamond_step(map, chunk_size, points):
    new_map = ds.diamond_step(map, chunk_size)
    for p in points:
        px, py = p
        assert new_map[(py, px)] != 0

@pytest.mark.parametrize("point, neighbor_values", list(zip(points_c, neighbor_values_c)))
def test_get_square_neighbor_values(point, neighbor_values):
    y, x = point
    result = ds.get_square_neighbor_values(map_c, x, y, chunk_size_c)
    assert sorted(result) == sorted(neighbor_values)

@pytest.mark.parametrize("map, points, chunk_size", [(map_c, points_c, chunk_size_c)])
def test_square_step(map, points, chunk_size):
    new_map = ds.square_step(map, chunk_size)
    for p in points:
        y, x = p
        assert new_map[(y, x)] != 0

@pytest.mark.parametrize("n, size, roughness, seed", [(3, 9, 1, [0.2, 0.5, 0.1, 0.9]), (4, 17, 1, None), (5, 33, 1, None)])
def test_diamond_square(n, size, roughness, seed):
    map = ds.diamond_square(n, roughness, seed)
    # check map size
    assert map.shape[0] == size
    
    # check seed if given
    if seed is not None:
        corners = [map[0, 0], map[0, size-1], map[size-1, 0], map[size-1, size-1]]
        assert corners == seed
        
    # check if matrix is completelly populated
    for row in map:
        for p in row:
            assert p != 0.0
    