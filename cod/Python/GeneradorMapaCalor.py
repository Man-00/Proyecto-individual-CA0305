"""
Created on Sat Jun  8 09:53:15 2024

@author: Manfred Porras
"""

from mplsoccer.pitch import Pitch
from mplsoccer import arrowhead_marker
import numpy as np
import ScraperFC as sfc
import pandas as pd
import matplotlib.pyplot as plt


class GeneradorMapaCalor:
    def __init__(self):
        """
        Constructor de la clase GeneradorMapaCalor.
        Inicializa el scraper de Sofascore.
        """
        self._scraper = sfc.Sofascore()

    @property
    def scraper(self):
        """
        Propiedad de solo lectura que devuelve el objeto scraper de Sofascore.

        Returns:
            object: El objeto scraper de Sofascore.
        """
        return self._scraper

    @scraper.setter
    def scraper(self, nuevo_scraper):
        """
        Setter para actualizar el objeto scraper de Sofascore.

        Parameters:
            nuevo_scraper (object): El nuevo objeto scraper de Sofascore.
        """
        self._scraper = nuevo_scraper

    def obtener_datos_mapa_calor(self, url_partido, nombre_jugador):
        """
        Obtiene los datos del mapa de calor de un jugador en un partido.

        Parameters:
            url_partido (str): La URL del partido en Sofascore.
            nombre_jugador (str): El nombre del jugador.

        Returns:
            DataFrame: Los datos del mapa de calor del jugador en el partido.
        """
        return self.scraper.get_player_heatmap(url_partido, player=nombre_jugador)
    
    def dibujar_mapa_calor(self, datos_mapa_calor, nombre_jugador, titulo_partido):
        """
        Dibuja el mapa de calor de un jugador en un partido.

        Parameters:
            datos_mapa_calor (DataFrame): Los datos del mapa de calor del jugador.
            nombre_jugador (str): El nombre del jugador.
            titulo_partido (str): El título del partido.
        """
        fig, ax = plt.subplots(figsize=(16, 9))
        
        pitch = Pitch(pitch_type='opta')
        pitch.draw(ax=ax)
        pitch.kdeplot(datos_mapa_calor.x, datos_mapa_calor.y, ax=ax,
                      levels=100, fill=True, zorder=-1, 
                      shade_lowest=True, cmap='inferno')
        
        # Agregar flecha hacia la derecha
        propiedades_flecha = dict(facecolor='black', arrowstyle='<-')
        ax.annotate('', xy=(0.5, 1), xytext=(0.6, 1),
                    arrowprops=propiedades_flecha, fontsize=12, 
                    ha='center', va='center', xycoords='axes fraction')
        
        # Agregar título en la parte superior izquierda
        ax.text(0.04, 1, f"{nombre_jugador} - {titulo_partido}", fontsize=14,
                ha='left', va='center', transform=ax.transAxes)
        
        plt.show()

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto.

        Returns:
            str: Una cadena que representa el objeto.
        """
        return "GeneradorMapaCalor()"

