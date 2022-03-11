import random
from model.BolaMais import BolaMais
from model.BolaMateriaNegra import BolaMateriaNegra
from model.BolaMenos import BolaMenos
from model.BolaBranca import BolaBranca
from model.BolaNormal import BolaNormal
import pygame


class GeraBola():

    def __init__(self) -> None:
        self.__max_bola = 4
        self.__min_bola = 1
        self.__lista_bola_especial = [
            BolaMais, BolaMenos, BolaBranca, BolaMateriaNegra
        ]
        

    #  Gera bolas de HE no campo
    def geraBola(self, elementos,background, coors, start: bool):
        # não podemos gerar bolas especiais no início do jogo
        if random.randint(1, 100) <= 40 and not start:
            bola = self.geraBolaEspecial(background, coors)
            return bola
        else:
            bola_img = pygame.draw.circle(background, "#A89234", coors, 35)
            rand_val = random.randint(self.__min_bola, self.__max_bola)
            bola = BolaNormal(
                rand_val, elementos.get(rand_val), bola_img)

            return bola

    def geraBolaEspecial(self, background, coors):

        if random.randint(1, 100) == 1:
            circle_obj = pygame.draw.circle(background, "#000000", coors, 35)
            bola = BolaMateriaNegra("#", circle_obj, False)
            return bola
        elif random.randint(1, 100) == 1:
            circle_obj = pygame.draw.circle(background, "#f2efda", coors, 35)
            bola = BolaBranca("*", circle_obj, False)
            return bola
        elif random.randint(1, 100) <= 30:
            circle_obj = pygame.draw.circle(background, "#277edb", coors, 35)
            bola = BolaMenos("-", circle_obj, False)
            return bola
        else:
            circle_obj = pygame.draw.circle(background, "#d13d32", coors, 35)
            bola = BolaMais("+", circle_obj, False)
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
