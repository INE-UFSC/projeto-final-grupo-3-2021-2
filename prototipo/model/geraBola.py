import random
from model.BolaMais import BolaMais
from model.BolaMateriaNegra import BolaMateriaNegra
from model.BolaMenos import BolaMenos
from model.BolaBranca import BolaBranca
from model.BolaNormal import BolaNormal
from model.BolaEspecial import BolaEspecial
import pygame


class GeraBola():

    def __init__(self) -> None:
        self.__max_bola = 3
        self.__min_bola = 1
        self.__ultima_especial = False

    #  Gera bolas de HE no campo

    def geraBola(self, elementos, background, coors, start: bool, cores):
        # não podemos gerar bolas especiais no início do jogo
        if random.randint(1, 100) <= 40 and not start and not(self.__ultima_especial):
            
            bola = self.geraBolaEspecial(background, coors)
            self.__ultima_especial = True
            return bola
        else:
            print(self.__max_bola)
            print(self.__min_bola)
            self.__ultima_especial = False
            # gap = 5
            # if self.__min_bola + gap < self.__max_bola:
            #     rand_val = random.randint(self.__max_bola - gap, self.__max_bola)
            # else:
            rand_val = random.randint(self.__min_bola, self.__max_bola)
            bola_img = pygame.draw.circle(
                background, cores.get(rand_val), coors, 35)
            bola = BolaNormal(
                rand_val, elementos.get(rand_val), bola_img)

            return bola

    def geraBolaEspecial(self, background, coors):

        if random.randint(1, 100) == 1:
            circle_obj = pygame.draw.circle(background, "#080808", coors, 35)
            bola = BolaMateriaNegra("#", circle_obj, False)
            return bola
        elif random.randint(1, 100) <= 5:
            circle_obj = pygame.draw.circle(background, "#f75f11", coors, 35)
            bola = BolaBranca("=", circle_obj, False)
            return bola
        elif random.randint(1, 100) <= 20:
            circle_obj = pygame.draw.circle(background, "#277edb", coors, 35)
            bola = BolaMenos("-", circle_obj, False)
            return bola
        else:
            circle_obj = pygame.draw.circle(background, "#d13d32", coors, 35)
            bola = BolaMais("+", circle_obj, False)
            return bola

    def atualizaMinMaxBola(self, campo):
        count = 0
        for bola in campo:
            if not isinstance(bola, BolaEspecial):
                if count == 0 and bola.valor != 0:
                    maior = bola.valor
                    menor = bola.valor
                    print('Entrou')
                    count = 1
                elif count == 1 and bola.valor != 0:
                    if bola.valor > maior:
                        maior = bola.valor
                    
                    elif bola.valor < menor:
                        menor = bola.valor
                        
        self.__max_bola = maior
        self.__min_bola = menor
                

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
