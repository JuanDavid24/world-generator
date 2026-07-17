import sys
from pathlib import Path
import json
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TERRAIN_MOCK_DIR = BASE_DIR / "data" / "mock_responses" / "terrain"
VEGETATION_MOCK_DIR = BASE_DIR / "data" / "mock_responses" / "vegetation"
TERRAIN_MOCK_DIR.mkdir(parents=True, exist_ok=True)
VEGETATION_MOCK_DIR.mkdir(parents=True, exist_ok=True)

def log_terrain_to_json_file(algorithm, size, seed, map, **algorithm_params):
    terrain_data = format_terrain_data(algorithm, size, seed, map, **algorithm_params)
    
    terrain_json = json.dumps(terrain_data)
    filename = f'{algorithm}-{terrain_data["date"]}.json'
    
    with open(TERRAIN_MOCK_DIR / filename, 'w') as f:
        print(terrain_json, file=f)
        
def format_terrain_data(algorithm, size, seed, map, **algorithm_params):
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d-%H%M%S')
    
    np.set_printoptions(threshold=sys.maxsize) # print all matrix
    terrain_data = {
        'date': time_str,
        'algorithm': {
            'name': algorithm,
            'params': {}
        },
        "seed": seed, 
        "size": size,
        "min": float(map.min()),
        "max": float(map.max()),
        "map": map.tolist()
    }
    
    if algorithm == "diamond_square":
        algorithm_params["initial_corners"] = algorithm_params["initial_corners"].tolist()
    
    terrain_data['algorithm']['params'] = algorithm_params
    
    return terrain_data
    
def save_terrain_as_png(algorithm, map):
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d-%H%M%S')
    filename = f'{algorithm}-{time_str}.png'
    plt.imsave(TERRAIN_MOCK_DIR / filename, map, cmap='gray', vmin=-1, vmax=1)
    
def log_plant_to_json_file(lsys, iterations, seed, output_sentence):
    plant_data = format_plant_data(lsys, iterations, seed, output_sentence)
    
    plant_json = json.dumps(plant_data)
    filename = f'{plant_data["date"]}.json'
    
    with open(VEGETATION_MOCK_DIR / filename, 'w') as f:
        print(plant_json, file=f)
        
def format_plant_data(lsys, iterations, seed, output_sentence, id=None):
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d-%H%M%S')
    
    mapped_ruleset = map_lsystem_ruleset(lsys["ruleset"])
    algorithm_data = {
        "name": "l_system",
        "ruleset": mapped_ruleset,
        "axiom": lsys["axiom"],
        "iterations": iterations
    }
    plant_data = {
        "date": time_str,
        "name": id,
        "algorithm": algorithm_data,
        "seed": seed, 
        "default_angle": lsys["default_angle"],
        "size": len(output_sentence),
        "sentence": output_sentence
    }
    
    return plant_data
    
def log_plant_to_json(lsys, iterations, seed, output_sentence):
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d-%H%M%S')
    
    mapped_ruleset = map_lsystem_ruleset(lsys["ruleset"])
    algorithm_data = {
        "name": "l_system",
        "ruleset": mapped_ruleset,
        "axiom": lsys["axiom"],
        "iterations": iterations
    }
    plant_data = {
        "date": time_str,
        "algorithm": algorithm_data,
        "seed": seed, 
        "size": len(output_sentence),
        "sentence": output_sentence
    }
    
    plant_json = json.dumps(plant_data)
    filename = f'lsystem-{time_str}.json'
    with open(VEGETATION_MOCK_DIR / filename, 'w') as f:
        print(plant_json, file=f)

def map_lsystem_ruleset(lsys_ruleset):
    mapped_ruleset = {}
    for symbol, symbol_ruleset in lsys_ruleset.items():
        mapped_ruleset[symbol] = [] # define ruleset array for each symbol
        for rule in symbol_ruleset:
            mapped_rule = {
                "sucessor": rule[0],
                "probability": rule[1]
            }
            mapped_ruleset[symbol].append(mapped_rule)
    return mapped_ruleset