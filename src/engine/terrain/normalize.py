import numpy as np

""" Normalizes a map to a given range [min, max]"""
def normalize_map(map, min_val=0, max_val=1):
    map_range = map.max() - map.min()
    desired_range =  max_val - min_val
    
    if map_range == 0:
        # single element map case
        normalized_zero = min_val + desired_range / 2
        normalized_map = np.array([[normalized_zero]]) # single element matrix with normalized zero
    else:
        normalized_map = (map - map.min()) / map_range * (max_val - min_val) + min_val
    
    return normalized_map