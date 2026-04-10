import sys
import json
from datetime import datetime
import numpy as np

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
        "map": map.tolist()
    }
    
    map_data['algorithm']['params'] = algorithm_params
    
    map_json = json.dumps(map_data)
    
    with open(f'{algorithm}-{time_str}.json', 'w') as f:
        print(map_json, file=f)