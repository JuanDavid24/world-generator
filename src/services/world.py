from engine.terrain.diamond_square import diamond_square as ds
from engine.world.spawner import SpawnParams, Spawner
from engine.world.vegetation_assembler import VegetationAssembler
from engine.world.vegetation_prototyper import VegetationPrototyper
from services.terrain import get_perlin_map, process_perlin_terrain, process_diamond_square_terrain
from schemas.world import VegetationParams
from src.utils.logger import format_terrain_data

def process_world(terrain_args, vegetation_args, debug=False):
    terrain, terrain_data = process_world_terrain(terrain_args)
    
    vegetation_data = process_world_vegetation(terrain, vegetation_args)
    world_data = {
        "world": {
            "terrain": terrain_data,
            "vegetation": vegetation_data
        }
    }
    return world_data

def process_world_terrain(terrain_args):
    # ----- terrain creation -----
    t_algorithm = terrain_args.pop("algorithm")
    
    if t_algorithm == "perlin_noise":
        terrain, seed = get_perlin_map(**terrain_args["params"])
    elif t_algorithm == "diamond_square":
        terrain, seed, cs = ds(**terrain_args["params"])
        # update terrain params
        terrain_args["params"]["size"] = 2 ** terrain_args["params"]["n"] + 1
        terrain_args["params"]["initial_corners"] = cs
    else: 
        raise ValueError(f"Algoritmo de terreno inválido: '{t_algorithm}'") 
    
    terrain_args["params"]["seed"] = seed # ensure seed is updated
    
    terrain_data = format_terrain_data(map=terrain, algorithm=t_algorithm, **terrain_args["params"])
    return terrain, terrain_data
    
def process_world_vegetation(terrain, vegetation_params):
    # vegetation spawner
    spawner = Spawner(terrain, vegetation_params.spawn)
    spawner.create_spawn_map()
    spawner.get_spawn_positions()
        
    # vegetation prototyper and pool
    prototyper = VegetationPrototyper(vegetation_params.genes)
    prototyper.generate_pool()
    pool = prototyper.pool
    
    # vegetation assembler 
    vegetation_assembler = VegetationAssembler(spawner, pool)
    vegetation_data = {
        "prototypes": vegetation_assembler.prototypes_payload,
        "instances": vegetation_assembler.instances_payload
    }
    return vegetation_data
    