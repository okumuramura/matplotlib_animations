import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

norm = mpl.colors.Normalize(0,1)
color1 = "#d63e2a"
color2 = "#ff820d"
colors = [[norm(0), color1],
          [norm(1), color2]]
lava = mpl.colors.LinearSegmentedColormap.from_list("", colors)

def animate(i):
    global img
    global ax
    global lava
    ax.clear()
    line = np.random.randint(0,256, 10) * np.random.choice([0,1], 10, True, [0.4, 0.6])
    img = np.append(img[1:], line.reshape(1,10), 0)
    ax.imshow(img, cmap = lava, interpolation="bicubic")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
noise = np.random.randint(0,256,(10,10))
mask = np.random.choice([0,1], (10,10), True, [0.4, 0.6])
img = noise * mask

#plt.imshow(img, cmap = lava, interpolation="bicubic")

ani = animation.FuncAnimation(fig, animate, interval=20, cache_frame_data = False)
plt.show()