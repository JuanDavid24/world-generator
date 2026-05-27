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

def log_terrain_to_json(algorithm, size, seed, map, **algorithm_params):
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d-%H%M%S')
    
    np.set_printoptions(threshold=sys.maxsize) # print all matrix
    map_data = {
        'date': time_str,
        'algorithm': {
            'name': algorithm,
            'params': {}
        },
        "seed": seed, 
        "size": size,
        "min": map.min(),
        "max": map.max(),
        "map": map.tolist()
    }
    
    if algorithm == "diamond_square":
        algorithm_params["initial_corners"] = algorithm_params["initial_corners"].tolist()
        
    map_data['algorithm']['params'] = algorithm_params
    
    map_json = json.dumps(map_data)
    filename = f'{algorithm}-{time_str}.json'
    
    with open(TERRAIN_MOCK_DIR / filename, 'w') as f:
        print(map_json, file=f)
        
def save_terrain_as_png(algorithm, map):
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d-%H%M%S')
    filename = f'{algorithm}-{time_str}.png'
    plt.imsave(TERRAIN_MOCK_DIR / filename, map, cmap='gray', vmin=-1, vmax=1)
    
def log_plant_to_json(lsys, iterations, seed, output_sentence):
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d-%H%M%S')
    
    mapped_ruleset = map_lsystem_ruleset(lsys["ruleset"])
    mapped_lsys = {
        "ruleset": mapped_ruleset,
        "axiom": lsys["axiom"]
    }
    plant_data = {
        "date": time_str,
        "l_system": mapped_lsys,
        "iterations": iterations,
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