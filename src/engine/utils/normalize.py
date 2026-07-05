def normalize_map(map, min, max):
    """ Normalizes a map to a given range [min, max]"""
    return (map - map.min()) / (map.max() - map.min()) * (max - min) + min