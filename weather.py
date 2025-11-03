import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import defaultdict
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import random
import math

counter = 1

df = pd.DataFrame(columns=['Hours Ago', 'Surface Temperature (°C)'])
for i in range(24):
    df.loc[i] = i, -30 * math.cos(0.261799387799 * (-i - 3)) - 50 + random.random()*5-2.5

fig, ax = plt.subplots()
line, = ax.plot(df['Hours Ago'], df['Surface Temperature (°C)'])
ax.set_xlabel('Hours Ago')
ax.set_ylabel('Surface Temperature (°C)')
ax.set_ylim(-100, 0)
ax.xaxis.set_inverted(True)
ax.set_title('Surface Temperature Over Time')


def update(frame):
    global counter
    current_values = df['Surface Temperature (°C)'].tolist()
    new_value = [-30 * math.cos(0.261799387799 * (counter - 3)) - 50 + random.random()*5-2.5]
    counter += 1
    if counter > 24:
        counter = 0

    updated_values = current_values[:-1]
    new_value.extend(updated_values)
    updated_values = new_value

    df['Surface Temperature (°C)'] = updated_values
    line.set_ydata(df['Surface Temperature (°C)'])
    return line,


ani = animation.FuncAnimation(fig, update, frames=range(200), blit=True, interval=1000)

plt.show()