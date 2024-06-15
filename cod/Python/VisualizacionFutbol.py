"""
Created on Thu May 30 15:03:08 2024

@author: Manfred Porras
"""

#Instalar paquetes
#pip install mplsoccer
#pip install ScraperFC

#Importar librerias 
from mplsoccer.pitch import Pitch
from mplsoccer import arrowhead_marker
import numpy as np
import ScraperFC as sfc
import pandas as pd
import matplotlib.pyplot as plt



class VisualizacionFutbol:
    def __init__(self, color_campo='grass', color_lineas='white', rayas=True):
        """
        Constructor de la clase VisualizacionFutbol.

        Parameters:
            color_campo (str): Color del campo de fútbol.
            color_lineas (str): Color de las líneas del campo.
            rayas (bool): Indicador de si el campo tiene rayas.
        """
        self._color_campo = color_campo
        self._color_lineas = color_lineas
        self._rayas = rayas
        self._pitch = Pitch(pitch_color=color_campo, line_color=color_lineas, stripe=rayas)
        self._fig, self._ax = self._pitch.draw()

    @property
    def color_campo(self):
        """
        Propiedad de solo lectura que devuelve el color del campo.

        Returns:
            str: El color del campo de fútbol.
        """
        return self._color_campo

    @color_campo.setter
    def color_campo(self, nuevo_color):
        """
        Setter para actualizar el color del campo.

        Parameters:
            nuevo_color (str): El nuevo color del campo.
        """
        self._color_campo = nuevo_color
        self._pitch = Pitch(pitch_color=nuevo_color, line_color=self._color_lineas, stripe=self._rayas)
        self._fig, self._ax = self._pitch.draw()

    def dibujar_campo(self):
        """
        Dibuja el campo de fútbol.
        """
        self._pitch = Pitch()
        self._fig, self._ax = self._pitch.draw()
    
    def dibujar_direccion_pase(self, x_inicio, y_inicio, x_fin, y_fin):
        """
        Dibuja la dirección de un pase en el campo de fútbol.

        Parameters:
            x_inicio (float): Coordenada x de inicio del pase.
            y_inicio (float): Coordenada y de inicio del pase.
            x_fin (float): Coordenada x de fin del pase.
            y_fin (float): Coordenada y de fin del pase.
        """
        self.dibujar_campo()
        self._pitch.arrows(x_inicio, y_inicio, x_fin, y_fin, ax=self._ax)
        plt.show()
    
    def dibujar_direccion_tiro(self, x_inicio, y_inicio, x_fin, y_fin):
        """
        Dibuja la dirección de un tiro en el campo de fútbol.

        Parameters:
            x_inicio (float): Coordenada x de inicio del tiro.
            y_inicio (float): Coordenada y de inicio del tiro.
            x_fin (float): Coordenada x de fin del tiro.
            y_fin (float): Coordenada y de fin del tiro.
        """
        self.dibujar_campo()
        self._pitch.lines(x_inicio, y_inicio, x_fin, y_fin, comet=True, transparent=True, ax=self._ax)
        plt.show()
    
    def dibujar_posicion_jugador(self, x, y):
        """
        Dibuja la posición de un jugador en el campo de fútbol.

        Parameters:
            x (float): Coordenada x de la posición del jugador.
            y (float): Coordenada y de la posición del jugador.
        """
        self.dibujar_campo()
        self._pitch.scatter(x, y, ax=self._ax)
        plt.show()
    
    def dibujar_posicion_jugador_con_flecha(self, x, y, grados_rotacion):
        """
        Dibuja la posición de un jugador con una flecha indicando la dirección.

        Parameters:
            x (float): Coordenada x de la posición del jugador.
            y (float): Coordenada y de la posición del jugador.
            grados_rotacion (float): Grados de rotación de la flecha.
        """
        self.dibujar_campo()
        marcador_flecha = '>'
        self._pitch.scatter(x, y, rotation_degrees=grados_rotacion, marker=marcador_flecha, ax=self._ax)
        plt.show()
    
    def dibujar_posicion_balon(self, x, y):
        """
        Dibuja la posición del balón en el campo de fútbol.

        Parameters:
            x (float): Coordenada x de la posición del balón.
            y (float): Coordenada y de la posición del balón.
        """
        self.dibujar_campo()
        self._pitch.scatter(x, y, marker='football', ax=self._ax)
        plt.show()
    
    def dibujar_angulo_tiro(self, x, y, alpha=0.5, color='red'):
        """
        Dibuja el ángulo de tiro desde una posición en el campo de fútbol.

        Parameters:
            x (float): Coordenada x de la posición del tiro.
            y (float): Coordenada y de la posición del tiro.
            alpha (float): Transparencia del ángulo dibujado.
            color (str): Color del ángulo dibujado.
        """
        self.dibujar_campo()
        self._pitch.goal_angle(x, y, alpha=alpha, color=color, ax=self._ax)
        plt.show()
    
    def dibujar_zonas(self, formas, colores, alphas):
        """
        Dibuja zonas en el campo de fútbol.

        Parameters:
            formas (list): Lista de formas a dibujar.
            colores (list): Lista de colores para las formas.
            alphas (list): Lista de niveles de transparencia para las formas.
        """
        self.dibujar_campo()
        for forma, color, alpha in zip(formas, colores, alphas):
            self._pitch.polygon(verts=[forma], color=color, alpha=alpha, ax=self._ax)
        plt.show()

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto.

        Returns:
            str: Una cadena que representa el objeto.
        """
        return f"VisualizacionFutbol(campo_color='{self._color_campo}', lineas_color='{self._color_lineas}', rayas={self._rayas})"


