"""
Created on Sat Jun  8 10:39:21 2024

@author: Manfred Porras
"""

from mplsoccer import Radar, FontManager, grid
from mplsoccer.pitch import Pitch
from mplsoccer import arrowhead_marker
import numpy as np
import ScraperFC as sfc
import pandas as pd
import matplotlib.pyplot as plt

class GeneradorRadarComparativo:
    def __init__(self, data):
        """
        Constructor de la clase GeneradorRadarComparativo.
        
        Parameters:
            data (dict): Un diccionario de datos que contiene los parámetros y valores de los jugadores.
        """
        self._data = data

    @property
    def data(self):
        """
        Propiedad de solo lectura que devuelve el diccionario de datos.

        Returns:
            dict: El diccionario de datos.
        """
        return self._data

    @data.setter
    def data(self, new_data):
        """
        Setter para actualizar el diccionario de datos.

        Parameters:
            new_data (dict): El nuevo diccionario de datos.
        """
        self._data = new_data

    def generar_radar(self, player1_name, player1_team, player1_color, player2_name, player2_team, player2_color):
        """
        Genera un radar comparativo entre dos jugadores.

        Parameters:
            player1_name (str): El nombre del primer jugador.
            player1_team (str): El equipo del primer jugador.
            player1_color (str): El color del primer jugador.
            player2_name (str): El nombre del segundo jugador.
            player2_team (str): El equipo del segundo jugador.
            player2_color (str): El color del segundo jugador.
        """
        params = self.data["Parameter"]
        low = self.data["Low"]
        high = self.data["High"]
        player1_values = self.data[player1_name]
        player2_values = self.data[player2_name]

        radar = Radar(params, low, high,
                      round_int=[True]*len(params),
                      num_rings=4,
                      ring_width=1, center_circle_radius=1)

        fig, axs = grid(figheight=8, grid_height=0.915, title_height=0.06, endnote_height=0.025,
                        title_space=0, endnote_space=0, grid_key='radar', axis=False)

        radar.setup_axis(ax=axs['radar'])
        rings_inner = radar.draw_circles(ax=axs['radar'], facecolor='#E0E0E0', edgecolor='#BDBDBD')
        radar_output = radar.draw_radar_compare(player1_values, player2_values, ax=axs['radar'],
                                                kwargs_radar={'facecolor': player1_color, 'alpha': 0.6},
                                                kwargs_compare={'facecolor': player2_color, 'alpha': 0.6})
        radar_poly, radar_poly2, vertices1, vertices2 = radar_output
        range_labels = radar.draw_range_labels(ax=axs['radar'], fontsize=16,
                                               fontproperties=robotto_thin.prop)
        param_labels = radar.draw_param_labels(ax=axs['radar'], fontsize=22,
                                               fontproperties=robotto_thin.prop)
        axs['radar'].scatter(vertices1[:, 0], vertices1[:, 1],
                             c=player1_color, edgecolors=player1_color, marker='o', s=100, zorder=2)
        axs['radar'].scatter(vertices2[:, 0], vertices2[:, 1],
                             c=player2_color, edgecolors=player2_color, marker='o', s=100, zorder=2)

        ring_values = np.linspace(np.min(low), np.max(high), radar.num_rings + 1)
        exclude_values = set(ring_values) | {1, 2}

        for i, (x, y) in enumerate(vertices1):
            if player1_values[i] not in exclude_values:
                axs['radar'].text(x - 0.3, y - 0.4, str(player1_values[i]), fontsize=12, color=player1_color, ha='center', va='bottom')
        for i, (x, y) in enumerate(vertices2):
            if player2_values[i] not in exclude_values:
                axs['radar'].text(x -0.2, y + 0.2, str(player2_values[i]), fontsize=12, color=player2_color, ha='center', va='bottom')

        title1_text = axs['title'].text(0.01, 0.65, player1_name, fontsize=25, color=player1_color,
                                        fontproperties=robotto_bold.prop, ha='left', va='center')
        title2_text = axs['title'].text(0.01, -0.01, player1_team, fontsize=20,
                                        fontproperties=robotto_thin.prop,
                                        ha='left', va='center', color=player1_color)
        title3_text = axs['title'].text(0.99, 0.65, player2_name, fontsize=25,
                                        fontproperties=robotto_bold.prop,
                                        ha='right', va='center', color=player2_color)
        title4_text = axs['title'].text(0.99, -0.1, player2_team, fontsize=20,
                                        fontproperties=robotto_thin.prop,
                                        ha='right', va='center', color=player2_color)

        plt.show()

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto.

        Returns:
            str: Una cadena que representa el objeto.
        """
        return f"GeneradorRadarComparativo(data={self.data})"

URL4 = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf'
robotto_thin = FontManager(URL4)
URL5 = ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
        'RobotoSlab%5Bwght%5D.ttf')
robotto_bold = FontManager(URL5)

