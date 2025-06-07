import numpy as np
import noise

def generateMap(shape = (1024, 1024), scale = 100, octaves = 1, persistence = 0.5, lacunarity = 2.0):
    map = np.zeros(shape)

    for i in range(shape[0]):
        for j in range(shape[1]):
            map[i][j] = noise.pnoise2(i/scale, 
                                        j/scale, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        base=0)        
    return map


