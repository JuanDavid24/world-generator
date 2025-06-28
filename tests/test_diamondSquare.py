import numpy as np 
import pytest
from src import diamondSquare as ds

# data
# diamond step dataset
mapA = np.array([[0.5, 0.0, 0.0, 0.0, 0.9],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.5, 0.0, 0.0, 0.0, 0.7]]) 
chunkSizeA = 5
xA, yA = (0, 0)
pointsA = [(2, 2)]

mapB = np.array([[0.5, 0.0, 0.1, 0.0, 0.9],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.3, 0.0, 0.2, 0.0, 0.4],
                 [0.0, 0.0, 0.0, 0.0, 0.0],
                 [0.5, 0.0, 0.2, 0.0, 0.7]])
chunkSizeB = 3
xB, yB = (2, 0) 
pointsB = [(1, 1), (1, 3), (3, 1), (3, 3)]

# square step dataset
mapC = np.array([[0.5, 0.0, 0.1, 0.0, 0.9],
                 [0.0, 0.5, 0.0, 0.5, 0.0],
                 [0.3, 0.0, 0.2, 0.0, 0.4],
                 [0.0, 0.5, 0.0, 0.5, 0.0],
                 [0.5, 0.0, 0.2, 0.0, 0.7]])
chunkSizeC = 3
# pointsC = [(1, 0), (3, 0), (0, 1), (2, 1), (4, 1), (1, 2), (3, 2), (0, 3), (2, 3), (4, 3), (1, 4), (3, 4)]
# neighborsValuesC = [[0.5, 0.3, 0.5], [0.3, 0.5, 0.5], [0.5, 0.1, 0.5], [0.5, 0.5, 0.2, 0.3], [0.5, 0.2, 0.5], 
#                     [0.1, 0.2, 0.5, 0.5], [0.2, 0.2, 0.5, 0.5], [0.5, 0.9, 0.1], [0.5, 0.5, 0.4, 0.2], [0.5, 0.7, 0.2],
#                      [0.9, 0.4, 0.5], [0.4, 0.7, 0.5]]

# for first point (0, 1), second point (0, 3), third point (1, 0)
pointsC = [
    (0, 1), (0, 3),
    (1, 0), (1, 2), (1, 4),
    (2, 1), (2, 3),
    (3, 0), (3, 2), (3, 4),
    (4, 1), (4, 3)
]
neighborsValuesC = [
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

@pytest.mark.parametrize("map, x , y, chunkSize, points", [(mapA, xA, yA, chunkSizeA, pointsA), 
                                                           (mapB, xB, yB, chunkSizeB, pointsB)])
def test_diamondStep(map, x, y, chunkSize, points):
    newMap = ds.diamondStep(map, x, y, chunkSize)
    for p in points:
        px, py = p
        assert newMap[(py, px)] != 0

@pytest.mark.parametrize("point, neighborsValues", list(zip(pointsC, neighborsValuesC)))
def test_getSquareNeighborsValues(point, neighborsValues):
    y, x = point
    result = ds.getSquareNeighborsValues(mapC, x, y, chunkSizeC)
    assert sorted(result) == sorted(neighborsValues)

# @pytest.mark.parametrize("map, x , y, chunkSize", [(mapC, xC, yC, chunkSizeC)])
# def test_calculateSquareValue(map, x, y, chunkSize):
#     newMap = ds.calculateSquareValue(map, x, y, chunkSize)
#     assert newMap[(x, y)] != 0

@pytest.mark.parametrize("map, points, chunkSize", [(mapC, pointsC, chunkSizeC)])
def test_calculateSquareStep(map, points, chunkSize):
    newMap = ds.squareStep(map, chunkSize)
    for p in points:
        y, x = p
        assert newMap[(y, x)] != 0

