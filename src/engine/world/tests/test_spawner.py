import numpy as np 
import pytest

from engine.terrain import diamond_square as ds
from engine.terrain import perlin_noise as pn
from engine.world.spawner import Spawner, Vegetation_params

# data
map_empty_5x5 = np.zeros((5, 5))
corners_a = [0.5, 0.9, 0.6, 0.7]

# perlin noise dataset
TERRAIN_SIZE_PN = 64
TERRAIN_SCALE_PN = 100
TERRAIN_SEED_PN = 123

DISTANCE_PN = 8
VEGETATION_COVER_PN = 0.7
VEGETATION_PN = Vegetation_params(DISTANCE_PN, VEGETATION_COVER_PN)
SPAWN_SEED_PN = 321
NOISE_MAP_SHAPE_PN = (8, 8)

terrain_pn_64_a, _ = pn.generate_perlin_map(shape=(TERRAIN_SIZE_PN, TERRAIN_SIZE_PN), scale=TERRAIN_SCALE_PN, seed=TERRAIN_SEED_PN)
spawner_pn = Spawner(terrain_pn_64_a, VEGETATION_PN, SPAWN_SEED_PN)

# diamond-square dataset
TERRAIN_N = 6
TERRAIN_SIZE_DS = 2**TERRAIN_N - 1
TERRAIN_SCALE_DS = 100
TERRAIN_SEED_DS = 456

DISTANCE_DS = 8
VEGETATION_COVER_DS = 0.7
VEGETATION_DS = Vegetation_params(DISTANCE_DS, VEGETATION_COVER_DS)
SPAWN_SEED_DS = 321
NOISE_MAP_SHAPE_DS = (7, 7)

terrain_ds_64_a, _ = pn.generate_perlin_map(shape=(TERRAIN_SIZE_DS, TERRAIN_SIZE_DS), scale=TERRAIN_SCALE_DS, seed=TERRAIN_SEED_DS)
spawner_ds = Spawner(terrain_ds_64_a, VEGETATION_DS, SPAWN_SEED_DS)

# check noise map
@pytest.mark.parametrize("spawner, noise_map_shape", [(spawner_pn, NOISE_MAP_SHAPE_PN), (spawner_ds, NOISE_MAP_SHAPE_DS)])
def test_noise_map(spawner, noise_map_shape):
    output_noise_map_shape = spawner.noise_map.shape
    assert np.array_equal(output_noise_map_shape, noise_map_shape)