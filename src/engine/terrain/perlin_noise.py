import numpy as np
import noise

def generate_perlin_map(shape=(1024, 1024), scale=100, octaves=1, persistence=0.5, lacunarity=2, seed=None):
    if seed is None:
        # Create a random seed between 0 and 2^31
        seed = np.random.randint(0, 2**31)
    rng = np.random.default_rng(seed) 
    offset_x = rng.uniform(-10000, 10000)
    offset_y = rng.uniform(-10000, 10000)

    map = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):            
            map[i][j] = noise.pnoise2(i/scale + offset_x, 
                                        j/scale + offset_y, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        base=0)
    return map, seed