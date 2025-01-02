import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

def plot_data():
    data = pd.read_csv("bungee_drops.csv")

    x = data['drop_height']
    y = data['drop_mass']
    z = data['optimal_drop_length']

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=z, cmap='viridis')
    ax.set_xlabel('drop height')
    ax.set_ylabel('drop mass')
    ax.set_zlabel('stretch length')
    ax.set_title('bungee drops data')
    plt.show()


def plot_predictions():
    data = pd.read_csv("bungee_predictions.csv", header=None)

    x = data.iloc[0, 1:].apply(lambda val: float(''.join(filter(str.isdigit, str(val)))))
    y = data.iloc[1:, 0].apply(lambda val: float(''.join(filter(str.isdigit, str(val)))))
    z = data.iloc[1:, 1:].map(lambda val: float(''.join(filter(str.isdigit, str(val)))))

    X, Y = np.meshgrid(x, y)
    Z = z.to_numpy()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
    fig.colorbar(surf)
    ax.set_xlabel('drop height')
    ax.set_ylabel('drop mass')
    ax.set_zlabel('stretch length')
    ax.set_title('bungee predictions data')
    plt.show()


plot_data()
plot_predictions()
time.sleep(100000000)
