import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import defaultdict
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import random
import math

df = pd.DataFrame(columns=['Hours Ago', 'Water Used (L)'])
for i in range(49):
    if random.random() < 0.75:
        water = 0
    else:
        water = random.random()*5+1.15
    df.loc[i] = i, water

fig, ax = plt.subplots()
line, = ax.plot(df['Hours Ago'], df['Water Used (L)'])
ax.set_xlabel('Hours Ago')
ax.set_ylabel('Water Used (L)')
ax.set_ylim(0, 20)
ax.xaxis.set_inverted(True)
ax.set_title('Water Usage Over Time')

def update(frame):
    current_values = df['Water Used (L)'].tolist()
    if random.random() < 0.7:
        value = [0]
    else:
        value = [abs(current_values[-1] + random.random()*3 - 2.5)]
    updated_values = current_values[:-1]
    value.extend(updated_values)
    updated_values = value
    df['Water Used (L)'] = updated_values
    line.set_ydata(df['Water Used (L)'])
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(200), blit=True, interval=1000)

plt.show()