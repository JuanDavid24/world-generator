from engine.terrain.diamond_square import diamond_square as ds
from engine.terrain.perlin_noise import generate_perlin_map
from engine.world.spawner import Spawner, Vegetation_params
from engine.terrain.terrain_plotter import Map_plotter

# ----- spawner -----
TERRAIN_SIZE = TERRAIN_SIZE = 256
TERRAIN_SCALE = 100
TERRAIN_SEED = 1
DISTANCE = 8
VEGETATION_COVER = 0.7
MIN_HEIGHT = -0.2
MAX_HEIGHT = 0.55
MAX_JITTER = 1.5
VARIANCE = 0.35
VEGETATION = Vegetation_params(DISTANCE, VEGETATION_COVER, MAX_JITTER, VARIANCE, MIN_HEIGHT, MAX_HEIGHT)
SPAWN_SEED = 3

terrain_plt = Map_plotter()
terrain, seed = generate_perlin_map(shape=(TERRAIN_SIZE, TERRAIN_SIZE), scale=TERRAIN_SCALE, seed=TERRAIN_SEED)
terrain_plt.plot_map(terrain, min=-1, max=1, title=f"Perlin Map Terrain, seed={TERRAIN_SEED}") 

spawner = Spawner(terrain, VEGETATION, SPAWN_SEED)
spawner.create_spawn_map()
spawner.get_spawn_positions()

terrain_plt.plot_map(spawner.noise_map, min=-1, max=1, title=f"Perlin Map Vegetation Spawner, noise_map with seed={spawner.seed}") 

spawn_plotter = Map_plotter(["black", "yellowgreen"], [0, 1])
spawn_plotter.plot_map(spawner.spawn_map, min=-0, max=2, title=f"Vegetation spawn map, seed={spawner.seed}, vegetation cover={spawner.vegetation.cover}")

terrain_plt.plot_map_with_spawn_points(map=spawner.terrain, 
                                       spawn_points_x=spawner.spawn_positions_x,
                                       spawn_points_y=spawner.spawn_positions_y,
                                       title=f"Vegetation terrain with vegetation spawning points, seed={spawner.seed}, vegetation params={spawner.vegetation}")
