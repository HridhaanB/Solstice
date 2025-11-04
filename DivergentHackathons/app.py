from flask import Flask, render_template, Response
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import random
import io
import math

app = Flask(__name__)

# --- Oxygen Data ---
df_oxygen = pd.DataFrame(columns=['Hours Ago', 'Oxygen Concentration (%)'])
for i in range(49):
    df_oxygen.loc[i] = i, random.randint(18, 24)

# --- Water Data ---
df_water = pd.DataFrame(columns=['Hours Ago', 'Water Used (L)'])
for i in range(49):
    if random.random() < 0.75:
        water = 0
    else:
        water = random.random()*5 + 1.15
    df_water.loc[i] = i, water

# --- Forecast Data ---
df_forecast = pd.DataFrame(columns=['Hours Ago', 'Surface Temperature (°C)'])
for i in range(24):
    df_forecast.loc[i] = i, -30 * math.cos(0.261799387799 * (-i - 3)) - 50 + random.random()*5-2.5
counter_forecast = 0

# --- Oxygen Plot Function ---
def generate_oxygen_plot():
    global df_oxygen
    current_values = df_oxygen['Oxygen Concentration (%)'].tolist()
    value = [random.randint(18, 24)]
    df_oxygen['Oxygen Concentration (%)'] = value + current_values[:-1]

    fig, ax = plt.subplots(figsize=(3, 2))
    fig.patch.set_facecolor('#10131c')
    ax.set_facecolor('#10131c')
    ax.plot(df_oxygen['Hours Ago'], df_oxygen['Oxygen Concentration (%)'], color='#CC4400')
    ax.set_xlabel('Hours Ago')
    ax.set_ylabel('Oxygen Concentration (%)')
    ax.set_ylim(0, 100)
    ax.invert_xaxis()
    ax.spines['bottom'].set_color('#10131c')
    ax.spines['top'].set_color('#10131c')
    ax.spines['right'].set_color('#10131c')
    ax.spines['left'].set_color('#10131c')
    ax.tick_params(axis='x', colors='#CC4400')
    ax.tick_params(axis='y', colors='#CC4400')
    ax.yaxis.label.set_color('#CC4400')
    ax.xaxis.label.set_color('#CC4400')
    ax.set_title('Oxygen Concentration Over Time', color='#CC4400')

    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()

# --- Water Plot Function ---
def generate_water_plot():
    global df_water
    current_values = df_water['Water Used (L)'].tolist()
    if random.random() < 0.7:
        value = [0]
    else:
        value = [abs(current_values[-1] + random.random()*3 - 2.5)]
    df_water['Water Used (L)'] = value + current_values[:-1]

    fig, ax = plt.subplots(figsize=(3, 2))
    fig.patch.set_facecolor('#10131c')
    ax.set_facecolor('#10131c')
    ax.plot(df_water['Hours Ago'], df_water['Water Used (L)'], color='#CC4400')
    ax.set_xlabel('Hours Ago')
    ax.set_ylabel('Water Used (L)')
    ax.set_ylim(0, 20)
    ax.invert_xaxis()
    ax.set_title('Water Usage Over Time', color='#CC4400')
    ax.spines['bottom'].set_color('#10131c')
    ax.spines['top'].set_color('#10131c')
    ax.spines['right'].set_color('#10131c')
    ax.spines['left'].set_color('#10131c')
    ax.tick_params(axis='x', colors='#CC4400')
    ax.tick_params(axis='y', colors='#CC4400')
    ax.yaxis.label.set_color('#CC4400')
    ax.xaxis.label.set_color('#CC4400')

    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()


# --- Forecast Plot ---
def generate_forecast_plot():
    global df_forecast, counter_forecast
    current_values = df_forecast['Surface Temperature (°C)'].tolist()
    new_value = -30 * math.cos(0.261799387799 * (counter_forecast - 3)) - 50 + random.random()*5-2.5
    counter_forecast += 1
    if counter_forecast >= 24:
        counter_forecast = 0
    df_forecast['Surface Temperature (°C)'] = [new_value] + current_values[:-1]

    fig, ax = plt.subplots(figsize=(3, 2))
    fig.patch.set_facecolor('#10131c')
    ax.set_facecolor('#10131c')
    ax.plot(df_forecast['Hours Ago'], df_forecast['Surface Temperature (°C)'], color='#CC4400')
    ax.set_xlabel('Hours Ago')
    ax.set_ylabel('Surface Temperature (°C)')
    ax.set_ylim(-100, 0)
    ax.invert_xaxis()
    ax.set_title('Surface Temperature Over Time', color='#CC4400')
    ax.spines['bottom'].set_color('#10131c')
    ax.spines['top'].set_color('#10131c')
    ax.spines['right'].set_color('#10131c')
    ax.spines['left'].set_color('#10131c')
    ax.tick_params(axis='x', colors='#CC4400')
    ax.tick_params(axis='y', colors='#CC4400')
    ax.yaxis.label.set_color('#CC4400')
    ax.xaxis.label.set_color('#CC4400')

    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()




# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot_oxygen.png')
def plot_oxygen_png():
    return Response(generate_oxygen_plot(), mimetype='image/png')

@app.route('/plot_water.png')
def plot_water_png():
    return Response(generate_water_plot(), mimetype='image/png')

@app.route('/plot_forecast.png')
def plot_forecast_png():
    return Response(generate_forecast_plot(), mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)