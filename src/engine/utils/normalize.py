def normalize_map(map, min_val, max_val):
    """ Normalizes a map to a given range [min, max]"""
    return (map - map.min()) / (map.max() - map.min()) * (max_val - min_val) + min_val