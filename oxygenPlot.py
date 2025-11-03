import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import defaultdict
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import random

df = pd.DataFrame(columns=['Hours Ago', 'Oxygen Concentration (%)'])
for i in range(49):
    df.loc[i] = i, random.randint(18,24)

fig, ax = plt.subplots()
line, = ax.plot(df['Hours Ago'], df['Oxygen Concentration (%)'])
ax.set_xlabel('Hours Ago')
ax.set_ylabel('Oxygen Concentration (%)')
ax.set_ylim(0, 100)
ax.xaxis.set_inverted(True)
ax.set_title('Oxygen Concentration Over Time')

def update(frame):
    current_values = df['Oxygen Concentration (%)'].tolist()
    value = [random.randint(18,24)]
    updated_values = current_values[:-1]
    value.extend(updated_values)
    updated_values = value
    df['Oxygen Concentration (%)'] = updated_values
    line.set_ydata(df['Oxygen Concentration (%)'])
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(200), blit=True, interval=1000)

plt.show()