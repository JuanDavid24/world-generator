import sys
from pathlib import Path
import json
from datetime import datetime
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MOCK_DIR = BASE_DIR / "data" / "mock_responses"
MOCK_DIR.mkdir(parents=True, exist_ok=True)

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
    
    with open(MOCK_DIR / filename, 'w') as f:
        print(map_json, file=f)