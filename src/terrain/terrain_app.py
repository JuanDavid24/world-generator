import terrain_generator as mg
import terrain_plotter as mp
from utils.timer import Timer
# ----- perlin noise -----
scales = [100, 200, 400, 800]
octaves = [1, 2, 3, 4]
seeds = [1, 2, 3, 4]
persistences = [0.3, 0.5, 0.7, 0.9]
lacunarities = [2, 4, 6, 8]
timer = Timer()
    
# single map plot, random seed, normalized vs not
# timer.run()
# pn_map, seed = mg.perlin_map(scale=400, octaves=7, normalized=False)
# timer.stop("Perlin map sin normalizar generado")
# mp.plot_map(pn_map, min=-1, max=1, title=f"Perlin Map without normalization, seed={seed}")

# timer.run()
# pn_map_norm, _ = mg.perlin_map(scale=400, octaves=7, seed=seed, normalized=True)
# timer.stop("Perlin map normalizado generado")
# mp.plot_map(pn_map_norm, min=-1, max=1, title=f"Perlin Map, normalized, same seed={seed}")

# variating scale
# pn_maps_scales = [mg.perlin_map(scale=s, seed=seeds[0])[0] for s in scales]
# mp.plot_maps(pn_maps_scales, ('scale', scales), min=-1, max=1)

# variating octaves
# normalized vs non-normalized
# pn_maps_octaves = [mg.perlin_map(scale=400, octaves=o, seed=seeds[0], normalized=False)[0] for o in octaves]
# mp.plot_maps(pn_maps_octaves, ('octaves', octaves), min=-1, max=1, title="Maps variating octaves, with same seed, non-normalized")
# pn_maps_octaves = [mg.perlin_map(scale=400, octaves=o, seed=seeds[0], normalized=True)[0] for o in octaves]
# mp.plot_maps(pn_maps_octaves, ('octaves', octaves), min=-1, max=1, title="Maps variating octaves, with same seed, normalized")

# variating persistence
# pn_maps_persistence = [mg.perlin_map(scale=400, octaves=6, persistence=p, seed=seeds[1], normalized=True)[0] for p in persistences]
# mp.plot_maps(pn_maps_persistence, ('persistence', persistences), min=-1, max=1)

# variating lacunarity
# pn_maps_lacunarity = [mg.perlin_map(scale=400, octaves= 6, lacunarity=l, seed=seeds[2], normalized=True)[0] for l in lacunarities]
# mp.plot_maps(pn_maps_lacunarity, ('lacunarity', lacunarities), min=-1, max=1)

# variating seed
# pn_maps_seed = [mg.perlin_map(scale=400, octaves=3, seed=s, normalized=True)[0] for s in seeds]
# mp.plot_maps(pn_maps_seed, ('seed', seeds), min=-1, max=1)

# ----- diamond-square -----
ns = [3, 5, 7, 10]
rs = [2, 1, 0.5, 0.125] 
cs = [0.2, 0.2, 0.2, 0.2]
ss = [123, 456, 789, 101112]

# single map plot, random seed and corners
timer.run()
ds_map, seed, corners = (mg.diamond_square_map(n=10, roughness=1))
timer.stop("Diamond-square map generado")
corners_str = ",".join([str(c) for c in corners])
mp.plot_map(ds_map, title=f"Map with seed {seed} and corners {corners_str}")

# variating n
# ds_maps_n = [mg.diamond_square_map(n, seed=ss[0], corners=cs)[0] for n in ns]
# mp.plot_maps(ds_maps_n, ('N', ns), title="Maps variating N, with same seed and corners")

# variating roughhness
# ds_maps_rg = [mg.diamond_square_map(7, roughness=r, seed=ss[0], corners=cs)[0] for r in rs]
# mp.plot_maps(ds_maps_rg, ('roughness', rs), title="Maps variating roughness, with same seed and corners") 

# variating seed
# ds_maps_sd = [mg.diamond_square_map(6, roughness=1, seed=s, corners=cs)[0] for s in ss]
# mp.plot_maps(ds_maps_sd, ('seed', ss), title="Maps variating seed")

# creating map with seed and fixed corners
# ds_maps_cr = []
# ds_maps_cr.append(mg.diamond_square_map(n=5, roughness=1, seed=123, corners=None)[0])
# ds_maps_cr.append(mg.diamond_square_map(n=5, roughness=1, seed=123, corners=None)[0])
# ds_maps_cr.append(mg.diamond_square_map(n=5, roughness=1, seed=123, corners=cs)[0])
# ds_maps_cr.append(mg.diamond_square_map(n=5, roughness=1, seed=456, corners=cs)[0])
# mp.plot_maps(ds_maps_cr, ('seed/corners', [(123, None), (123, None), (123, cs), (456, cs)]), title="Maps variating seed and corners")