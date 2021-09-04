import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data.csv')
BBox = (df.longitude.min(),   df.longitude.max(),
        df.latitude.min(), df.latitude.max())

map_craft = plt.imread('./map.png')

fig, ax = plt.subplots(figsize=(8, 7))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha=0.2, c='b', s=10)
ax.set_title('Our walk with Chungy')
ax.set_xlim(BBox[0], BBox[1])
ax.set_ylim(BBox[2], BBox[3])
ax.imshow(map_craft, zorder=0, extent=BBox, aspect='equal')

plt.show()
