import mapGenerator as mg
import mapPlotter as mp

scales = [500, 250, 125, 60]
octaves = [1, 2, 3, 4]

# mapSetScales = [mg.generateMap(scale=s, octaves=1) for s in scales]
# mapSetOctaves = [mg.generateMap(scale=200, octaves=o) for o in octaves]

# mp.plotMaps(mapSetScales, ('scale', scales))
# mp.plotMaps(mapSetOctaves, ('octaves', octaves))

# ----- diamond-square -----

ns = [3, 5, 7, 10]
rs = [2, 1, 0.5, 0.125] 

# single map plot
# ds_map = mg.diamond_square_map(n=7)
# mp.plot_map(ds_map)

# variating n
ds_maps = [mg.diamond_square_map(n) for n in ns]
mp.plot_maps(ds_maps, ('N', ns))

# variating roughhness
# ds_maps = [mg.diamond_square_map(5, roughness=r) for r in rs]
# mp.plot_maps(ds_maps, ('roughness', rs))