from random import randint
from .bolaMais import BolaMais
from .bolaMateriaNegra import BolaMateriaNegra
from .bolaMenos import BolaMenos
from .bolaBranca import BolaBranca
from .bolaNormal import BolaNormal
import pygame


class GeraBola():

    def __init__(self) -> None:
        self.__max_bola = 5
        self.__min_bola = 1
        self.__lista_bola_especial = [
            BolaMais, BolaMenos, BolaBranca, BolaMateriaNegra
        ]

    def geraBola(self, background, coors):
        bola_img = pygame.draw.circle(background, "#A89234", coors, 35)
        bola = BolaNormal(randint(
            self.__min_bola, self.__max_bola), "He", bola_img)

        return bola

    @property
    def max_bola(self):
        return self.__max_bola

    @max_bola.setter
    def max_bola(self, valor):
        self.__max_bola = valor

    @property
    def min_bola(self):
        return self.__min_bola

    @min_bola.setter
    def min_bola(self, valor):
        self.__min_bola = valor

    @property
    def lista_bola_especial(self):
        return self.__lista_bola_especial
