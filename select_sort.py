import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib
import random
count = 0

cmap = None

def new_cmap():
    global cmap
    norm = matplotlib.colors.Normalize(0,1)
    color1 = "#{:0>2x}".format(np.random.randint(0, 256)) + "{:0>2x}".format(np.random.randint(0, 256)) + "{:0>2x}".format(np.random.randint(0, 256))
    color2 = "#{:0>2x}".format(np.random.randint(0, 256)) + "{:0>2x}".format(np.random.randint(0, 256)) + "{:0>2x}".format(np.random.randint(0, 256))
    colors = [[norm(0), color1],
              [norm( 1.0), color2]]
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)


def animate2(i):
    global array
    global count
    global cmap
    ax.clear()
    ax.set_title("Select sort")
    ax.set_xticks([i for i in range(s)])
    #ax.set_xticklabels(["elem "+str(i) for i in range(s)], rotation = 90)
    ax.set_yticks([])
    for i,e in enumerate(array[0]):
        color = "#000000" if e > 127 else "#ffffff"
        ax.text(i, 0, e, color = color, weight = 1000, ha = 'center', va = 'center')
    ax.imshow(array, cmap = cmap, interpolation="bicubic")

    axg.clear()
    axg.set_title("Select sort (gray)")
    axg.set_xticks([i for i in range(s)])
    axg.set_yticks([])
    for i,e in enumerate(array[0]):
        color = "#000000" if e > 127 else "#ffffff"
        axg.text(i, 0, e, color = color, weight = 1000, ha = 'center', va = 'center')
    axg.imshow(array, cmap = 'gray')

    i = count
    if i < len(array[0]) - 1:
        min = array[0][i]
        mini = i
        for t in range(i, len(array[0])):
            if array[0][t] < min:
                min = array[0][t]
                mini = t
        array[0][i], array[0][mini] = array[0][mini], array[0][i]
        count += 1
    else:
        array = np.random.randint(0,256,(1,s))
        count = 0
        new_cmap()



new_cmap()
s = 30
array = np.random.randint(0,256,(1,s))
fig = plt.figure(figsize = (1080 / 80, 500 / 80))
ax = fig.add_subplot(2,1,1)
axg = fig.add_subplot(2,1,2)
ani = animation.FuncAnimation(fig, animate2, interval = 250, cache_frame_data=False)
plt.show()
