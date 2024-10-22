import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge
from matplotlib.animation import FuncAnimation
from config import ruleta

def mostrar_ruleta_animada(resultado):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')

    circle = plt.Circle((0, 0), 1, color='gray', ec='black', lw=2)
    ax.add_artist(circle)

    wedges = []
    for i in range(37):
        theta = np.deg2rad(360 / 37 * i)
        color = ruleta[i]
        wedge = Wedge((0, 0), 1, np.rad2deg(theta), np.rad2deg(theta + np.deg2rad(360 / 37)), color=color, edgecolor='black')
        ax.add_artist(wedge)
        wedges.append(wedge)

    def update(frame):
        # Aquí puedes agregar lógica para rotar la ruleta
        for wedge in wedges:
            wedge.set_visible(False)  # Esconde todos los wedges
        current_theta = (frame * 10) % 360  # Cambia la velocidad de rotación
        wedge = wedges[int(current_theta / (360 / 37))]  # Determina el wedge visible
        wedge.set_visible(True)

    ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)
    
    plt.title('Ruleta', fontsize=16)
    plt.axis('off')
    plt.show()

# Usa esta función en tu juego
# mostrar_ruleta_animada(resultado)
