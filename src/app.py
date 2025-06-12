import mapGenerator as mg
import mapPlotter as mp

scales = [500, 250, 125, 60]
octaves = [1, 2, 3, 4]

mapSetScales = [mg.generateMap(scale=s, octaves=1) for s in scales]
mapSetOctaves = [mg.generateMap(scale=200, octaves=o) for o in octaves]

mp.plotMaps(mapSetScales, ('scale', scales))
# mp.plotMaps(mapSetOctaves, ('octaves', octaves))