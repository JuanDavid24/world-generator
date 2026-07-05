from diamond_square import diamond_square as ds
from perlin_noise import generate_perlin_map
import terrain_plotter as tp
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
# pn_map, seed = generate_perlin_map(shape=(256, 256), scale=100, octaves=7, normalized=False, debug=True)
# timer.stop("Perlin map sin normalizar generado")
# tp.plot_map(pn_map, min=-1, max=1, title=f"Perlin Map without normalization, seed={seed}")

# timer.run()
# pn_map_norm, _ = generate_perlin_map(scale=400, octaves=7, seed=seed, normalized=True)
# timer.stop("Perlin map normalizado generado")
# tp.plot_map(pn_map_norm, min=-1, max=1, title=f"Perlin Map, normalized, same seed={seed}")

# variating scale
# pn_maps_scales = [generate_perlin_map(scale=s, seed=seeds[0])[0] for s in scales]
# tp.plot_maps(pn_maps_scales, ('scale', scales), min=-1, max=1)

# variating octaves
# normalized vs non-normalized
# pn_maps_octaves = [generate_perlin_map(scale=400, octaves=o, seed=seeds[0], normalized=False)[0] for o in octaves]
# tp.plot_maps(pn_maps_octaves, ('octaves', octaves), min=-1, max=1, title="Maps variating octaves, with same seed, non-normalized")
# pn_maps_octaves = [generate_perlin_map(scale=400, octaves=o, seed=seeds[0], normalized=True)[0] for o in octaves]
# tp.plot_maps(pn_maps_octaves, ('octaves', octaves), min=-1, max=1, title="Maps variating octaves, with same seed, normalized")

# variating persistence
# pn_maps_persistence = [generate_perlin_map(scale=400, octaves=6, persistence=p, seed=seeds[1], normalized=True)[0] for p in persistences]
# tp.plot_maps(pn_maps_persistence, ('persistence', persistences), min=-1, max=1)

# variating lacunarity
# pn_maps_lacunarity = [generate_perlin_map(scale=400, octaves= 6, lacunarity=l, seed=seeds[2], normalized=True)[0] for l in lacunarities]
# tp.plot_maps(pn_maps_lacunarity, ('lacunarity', lacunarities), min=-1, max=1)

# variating seed
# pn_maps_seed = [generate_perlin_map(scale=400, octaves=3, seed=s, normalized=True)[0] for s in seeds]
# tp.plot_maps(pn_maps_seed, ('seed', seeds), min=-1, max=1)

# ----- diamond-square -----
ns = [3, 5, 7, 10]
rs = [2, 1, 0.5, 0.125] 
cs = [-0.2, 0.2, -0.2, 0.2]
ss = [123, 456, 789, 101112]

# single map plot, random seed and corners
# timer.run()
ds_map, seed, initial_corners = (ds(n=8, roughness=1, debug=True))
# timer.stop("Diamond-square map generado")
corners_str = ",".join([str(c) for c in initial_corners])
tp.plot_map(ds_map, title=f"Map with seed {seed} and corners {corners_str}")

# variating n
# ds_maps_n = [ds(n, seed=ss[0], initial_corners=cs)[0] for n in ns]
# tp.plot_maps(ds_maps_n, ('N', ns), title="Maps variating N, with same seed and corners")

# variating roughhness
# ds_maps_rg = [ds(7, roughness=r, seed=ss[0], initial_corners=cs)[0] for r in rs]
# tp.plot_maps(ds_maps_rg, ('roughness', rs), title="Maps variating roughness, with same seed and corners") 

# variating seed
# ds_maps_sd = [ds(6, roughness=1, seed=s, initial_corners=cs)[0] for s in ss]
# tp.plot_maps(ds_maps_sd, ('seed', ss), title="Maps variating seed")

# creating map with seed and fixed corners
# ds_maps_cr = []
# map1, seed1, corners1 = ds(n=5, roughness=1, seed=None, initial_corners=None) # all random
# ds_maps_cr.append(map1)
# ds_maps_cr.append(ds(n=5, roughness=1, seed=seed1, initial_corners=corners1)[0]) # same seed and corners
# ds_maps_cr.append(ds(n=5, roughness=1, seed=seed1, initial_corners=None)[0]) # random corners
# ds_maps_cr.append(ds(n=5, roughness=1, seed=None, initial_corners=corners1)[0]) # random seed

# tp.plot_maps(ds_maps_cr, ('seed/corners', [(seed1, corners1), (seed1, corners1), (seed1, None), (None, corners1)]), title="Maps variating seed and corners")

# wrap vs no-wrap
# ds_maps_wrap = []
# cs_2 = [0.2, 0.5, 0.7, 0.1]
# ds_maps_wrap.append(ds(n=6, roughness=1, seed=123, initial_corners=cs, wrap=True)[0])
# ds_maps_wrap.append(ds(n=6, roughness=1, seed=123, initial_corners=cs, wrap=False)[0])
# ds_maps_wrap.append(ds(n=6, roughness=1, seed=123, initial_corners=cs_2, wrap=True)[0])
# ds_maps_wrap.append(ds(n=6, roughness=1, seed=123, initial_corners=cs_2, wrap=False)[0])
# tp.plot_maps(ds_maps_wrap, ('wrap/corners', [(True, cs), (False, cs), (True, cs_2), (False, cs_2)]), title="Maps with wrap vs. no-wrap")