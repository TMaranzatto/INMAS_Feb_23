#import simulation
import matplotlib.animation as anim
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

def visulization(stages):
    color = (colors.ListedColormap(["white", "green"]).with_extremes(over='0.35', under='0.75'))
    bounds = [0,1, 2]
    norm = colors.BoundaryNorm(bounds, color.N)
    images = stages
    M, N = stages[0].shape[0], stages[0].shape[1]
    for i in range(2):
        images.append(images[-1])
    im=[]
    #Create figure and add subplot
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel("Rear",fontsize=10)
    ax.set_title("Entrance",fontsize=10)

    #Add images to the animation:
    for i in range(len(stages)):
        image=ax.imshow(images[i],animated=True,cmap=color,norm=norm)
        ax.set_xticks(np.arange(-0.5,0.5+N,1))
        ax.set_yticks(np.arange(-0.5,0.5+M,1))
        ax.grid(color="k",linestyle="-",linewidth=2.5)  
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
        im.append([image])
    
    mov=anim.ArtistAnimation(fig,im,interval=180)
    plt.show()
