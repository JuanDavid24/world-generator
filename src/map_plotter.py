import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# generate colormap for terrain
colors = ["darkblue", "blue", "sandybrown", "yellowgreen", "olivedrab", "saddlebrown", "snow"]
positions = [0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0]
terrain_cmap = mcolors.LinearSegmentedColormap.from_list("my_terrain", list(zip(positions, colors)))

def plot_maps(maps, tags, min=0, max=1,title="Maps"): 
    plt.figure(figsize=(10, 10))
    plt.suptitle(title, fontsize=16)
    plt.subplots_adjust(left=0, bottom=0.03, right=0.9, top=0.9, hspace=0.2, wspace=0)
    for i, map in enumerate(maps):
        plt.subplot(2, 2, i + 1)
        plt.title(tags[0] + "=" + str(tags[1][i]))
        plt.imshow(map, cmap=terrain_cmap, vmin=min, vmax=max)
        plt.colorbar()
    plt.show()

def plot_map(map, min=0, max=1,):
    plt.imshow(map, cmap=terrain_cmap, vmin=min, vmax=max)
    plt.colorbar()
    plt.show()