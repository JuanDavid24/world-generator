import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Map_plotter:
    def __init__(self, 
                 colors = ["darkblue", "blue", "sandybrown", "yellowgreen", "olivedrab", "saddlebrown", "snow"],
                 positions = [0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0]):

        self.colors = colors
        self.positions = positions
        self.generate_colormap()

    def generate_colormap(self):
        self.color_map = mcolors.LinearSegmentedColormap.from_list("my_terrain", list(zip(self.positions, self.colors)))
        
    def plot_maps(self, maps, tags, min=-1, max=1, title="Maps"): 
        plt.figure(figsize=(10, 10))
        plt.suptitle(title, fontsize=16)
        plt.subplots_adjust(left=0, bottom=0.03, right=0.9, top=0.9, hspace=0.2, wspace=0)
        for i, map in enumerate(maps):
            plt.subplot(2, 2, i + 1)
            plt.title(tags[0] + "=" + str(tags[1][i]))
            plt.imshow(map, cmap=self.color_map, vmin=min, vmax=max)
            plt.colorbar()
        plt.show()

    def plot_map(self, map, min=-1, max=1, title="Maps"):
        plt.title(title)
        plt.imshow(map, cmap=self.color_map, vmin=min, vmax=max)
        plt.colorbar()
        plt.show()
        
    
    