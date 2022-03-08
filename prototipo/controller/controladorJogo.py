from itertools import count
import model.campo as campo
import model.Bola as bola
from model.geraBola import GeraBola
from abc import ABC
import pygame
from cmath import sqrt
import sys
import os
sys.path.append(
    os.path.dirname(os.path.realpath(__file__)))

clock = pygame.time.Clock()


class ControladorJogo(ABC):
    def __init__(self, tela_width: int, tela_height: int, placar) -> None:
        self.__bola_central = {}
        self.__campo = campo.Campo(
            tela_width, tela_height, GeraBola())
        self.__nome = ''
        self.__placar = placar
        self.__tela_width = tela_width
        self.__tela_height = tela_height

    def rodar_jogo(self):

        screen = pygame.display.set_mode(
            (self.__tela_width, self.__tela_height))

        pygame.display.set_caption('ATOMIKO')

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        running = True
        self.__campo.setar_campo(background, screen)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    min_dis = 10000
                    closest_obj = None
                    count = 0
                    for bola in self.__campo.campo:
                        count+=1
                        if bola.nome == '':
                            circle_pos = bola.circle_obj.center

                            temp = abs(
                                sqrt((x-circle_pos[0])**2 + (y-circle_pos[0])**2))

                            if x <= bola.circle_obj.x + 10 + 30 and x >= bola.circle_obj.x + 10 - 30:
                                if y <= bola.circle_obj.y + 10 + 30 and y >= bola.circle_obj.y + 10 - 30:
                                    closest_obj = bola

                    if closest_obj != None:
                        print(len(self.campo.campo))
                        self.__campo.verificaCampo(self.__campo.campo)
                        obj = self.__campo.desloca_bola(closest_obj, background)
                        for bola in self.__campo.campo:
                            print(bola.__dict__)
                        self.__campo.campo.append(obj)
                        if(closest_obj.circle_obj.x == obj.circle_obj.x and closest_obj.circle_obj.y == obj.circle_obj.y):
                            self.__campo.campo.remove(closest_obj)

            screen.blit(background, (0, 0))
            pygame.display.update()
            clock.tick(40)

        pygame.quit()

    @property
    def bola_central(self):
        return self.__bola_central

    @property
    def campo(self):
        return self.__campo

    @property
    def nome(self):
        return self.__nome

    @property
    def placar(self):
        return self.__placar

    @bola_central.setter
    def bola_central(self, bola: bola.Bola):
        self.__bola_central = bola

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def positions(self):
        return self.__positions

    @property
    def tela_width(self):
        return self.__tela_width

    @property
    def tela_height(self):
        return self.__tela_height

    @tela_width.setter
    def tela_width(self, width):
        self.__tela_width = width

    @tela_height.setter
    def tela_height(self, height):
        self.__tela_height = height
