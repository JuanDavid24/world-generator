import matplotlib.pyplot as plt

def plotMaps(maps, tags): 
    plt.figure(figsize=(10, 10))
    plt.suptitle("Mapas generados con distintos parámetros", fontsize=16)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    for i, map in enumerate(maps):
        plt.subplot(2, 2, i + 1)
        plt.title(tags[0] + "=" + str(tags[1][i]))
        plt.imshow(map, cmap='gray')
        plt.colorbar()
    plt.show()