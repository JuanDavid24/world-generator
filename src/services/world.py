from engine.world.spawner import Spawn_params, Spawner
from engine.world.vegetation_assembler import Vegetation_assembler
from engine.world.vegetation_prototyper import Vegetation_prototyper
from services.terrain import get_perlin_map, process_perlin_terrain, process_diamond_square_terrain
from src.utils.logger import format_terrain_data

def process_world(terrain_args, vegetation_args, debug=False):
    # terrain creation
    if terrain["algorithm"] == "perlin_noise":
        terrain, terrain_args["params"]["seed"] = get_perlin_map(**terrain_args["params"])  
    else: 
        terrain, terrain_args["params"]["seed"] = process_diamond_square_terrain(**terrain_args["params"])
        terrain_args["params"]["size"] = 2 ** terrain_args["params"]["n"] + 1
    
    terrain_data = format_terrain_data(algorithm=terrain["algorithm"], map=terrain, **terrain_args)
    
    DISTANCE = 8
    VEGETATION_COVER = 0.7
    MIN_HEIGHT = -0.2
    MAX_HEIGHT = 0.55
    MAX_JITTER = 1.5
    VARIANCE = 0.35
    VEGETATION = Spawn_params(DISTANCE, VEGETATION_COVER, MAX_JITTER, VARIANCE, MIN_HEIGHT, MAX_HEIGHT)
    # SPAWN_SEED # --> pasar en el req
    
    # # ----- vegetation spawner -----
    spawner = Spawner(terrain, VEGETATION)
    spawner.create_spawn_map()
    spawner.get_spawn_positions()
        
    # # ----- vegetation prototyper -----

    prototyper = Vegetation_prototyper(vegetation_args.genes)

    prototyper.generate_pool()
    pool = prototyper.pool
    
    # # ----- vegetation assembler -----
    vegetation_assembler = Vegetation_assembler(spawner, pool)
    
    vegetation_data = {
        "prototypes": vegetation_assembler.prototypes_payload,
        "instances": vegetation_assembler.instances_payload
    }
    world_data = {
        "world": {
            "terrain": terrain_data,
            "vegetation": vegetation_data
        }
    }
    return world_data