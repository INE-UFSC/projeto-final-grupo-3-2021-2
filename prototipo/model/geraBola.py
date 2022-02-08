from random import randint
from campo import Campo
from bolaMais import BolaMais
from bolaMateriaNegra import BolaMateriaNegra
from bolaMenos import BolaMenos
from bolaBranca import BolaBranca
from bolaNormal import BolaNormal
import pygame


class GeraBola():

    def __init__(self, campo: Campo) -> None:
        self.__max_bola = 5
        self.__min_bola = 1
        self.__campo = campo
        self.__lista_bola_especial = [
            BolaMais, BolaMenos, BolaBranca, BolaMateriaNegra
        ]

    def geraBola(self, background, coors):
        bola_img = pygame.draw.circle(background, "#A89234", coors, 35)
        bola = BolaNormal(35, randint(
            self.__min_bola, self.__max_bola), "He", bola_img)

        return bola
