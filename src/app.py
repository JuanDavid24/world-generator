import map_generator as mg
import map_plotter as mp

scales = [500, 250, 125, 60]
octaves = [1, 2, 3, 4]

# mapSetScales = [mg.generateMap(scale=s, octaves=1) for s in scales]
# mapSetOctaves = [mg.generateMap(scale=200, octaves=o) for o in octaves]

# mp.plotMaps(mapSetScales, ('scale', scales))
# mp.plotMaps(mapSetOctaves, ('octaves', octaves))

# ----- diamond-square -----

ns = [3, 5, 7, 10]
rs = [2, 1, 0.5, 0.125] 
cs = [1.0, 1.0, 0.0, 0.0]
sd = 123

# single map plot
# ds_map = mg.diamond_square_map(n=7)
# mp.plot_map(ds_map)

# variating n
""" ds_maps_n = [mg.diamond_square_map(n) for n in ns]
mp.plot_maps(ds_maps_n, ('N', ns))"""

# variating roughhness
ds_maps_rg = [mg.diamond_square_map(5, roughness=r, corners=cs, seed=sd ) for r in rs]
mp.plot_maps(ds_maps_rg, ('roughness', rs)) 

# creating map with seed and fixed corners
""" 
ds_maps_cr = []
ds_maps_cr.append(mg.diamond_square_map(n=4, roughness=1, seed=123, corners=None))
ds_maps_cr.append(mg.diamond_square_map(n=4, roughness=1, seed=123, corners=None))
ds_maps_cr.append(mg.diamond_square_map(n=4, roughness=1, seed=123, corners=cs))
ds_maps_cr.append(mg.diamond_square_map(n=4, roughness=1, seed=123, corners=cs))
mp.plot_maps(ds_maps_cr, ('seed/corners', [(123, None), (123, None), (123, cs), (456, cs)])) """