import random
from model.BolaMais import BolaMais
from model.BolaMateriaNegra import BolaMateriaNegra
from model.BolaMenos import BolaMenos
from model.BolaBranca import BolaBranca
from model.BolaNormal import BolaNormal
import pygame


class GeraBola():

    def __init__(self) -> None:
        self.__max_bola = 5
        self.__min_bola = 1
        self.__lista_bola_especial = [
            BolaMais, BolaMenos, BolaBranca, BolaMateriaNegra
        ]
        self.__elem_dict = {
            1: "H",
            2: "He",
            3: "Li",
            4: "Be",
            5: "B",
            6: "C",
            7: "N",
            8: "O",
            9: "F",
            10: "Ne",
            11: "Na",
            12: "Mg"
        }

    #  Gera bolas de HE no campo
    def geraBola(self, background, coors):
        if random.randint(1, 100) <= 10:
            self.geraBolaEspecial(background, coors)
        else:
            bola_img = pygame.draw.circle(background, "#A89234", coors, 35)
            rand_val = random.randint(self.__min_bola, self.__max_bola)
            bola = BolaNormal(
                rand_val, self.__elem_dict.get(rand_val), bola_img)

            return bola

    def geraBolaEspecial(self, background, coors):

        if random.randint(1, 100) == 1:
            circle_obj = pygame.draw.circle(background, "#888888", coors, 35)
            bola = BolaMateriaNegra(circle_obj, False)
            return bola
        elif random.randint(1, 100) == 1:
            circle_obj = pygame.draw.circle(background, "#888887", coors, 35)
            bola = BolaBranca(circle_obj, False)
            return bola
        elif random.randint(1, 100) <= 30:
            circle_obj = pygame.draw.circle(background, "#888886", coors, 35)
            bola = BolaMenos(circle_obj, False)
            return bola
        else:
            circle_obj = pygame.draw.circle(background, "#888885", coors, 35)
            bola = BolaMais(circle_obj, False)
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
