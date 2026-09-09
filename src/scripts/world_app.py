from engine.terrain.diamond_square import diamond_square as ds
from engine.terrain.perlin_noise import generate_perlin_map
from engine.world.spawner import Spawner
import engine.terrain.terrain_plotter as tp

# ----- spawner -----
TERRAIN_SIZE = TERRAIN_SIZE = 256
TERRAIN_SCALE = 100
TERRAIN_SEED = 1
DISTANCE = 8
COVERAGE = 0.7
SPAWN_SEED = 3

terrain, seed = generate_perlin_map(shape=(TERRAIN_SIZE, TERRAIN_SIZE), scale=TERRAIN_SCALE, seed=TERRAIN_SEED)
tp.plot_map(terrain, min=-1, max=1, title=f"Perlin Map Terrain, seed={TERRAIN_SEED}") 

spawner = Spawner(terrain, DISTANCE, COVERAGE, SPAWN_SEED)
tp.plot_map(spawner.noise_map, min=-1, max=1, title=f"Perlin Map Vegetation Spawner, seed={spawner.seed}") 

spawner.create_spawn_map()
tp.plot_map(spawner.spawn_map, min=-0, max=2, title=f"Vegetation spawn map, seed={spawner.seed}") 