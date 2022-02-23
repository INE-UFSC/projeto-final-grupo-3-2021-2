from random import randint
import pygame
from model.Bola import Bola
from model.BolaNormal import BolaNormal
from model.geraBola import GeraBola


class Campo():

    def __init__(self, tela_width: int, tela_height: int, geraBola: GeraBola) -> None:
        self.__capacidade = 20
        self.__campo = []
        self.__bola_central = {}
        self.__raio = 300
        self.__tela_width = tela_width
        self.__tela_height = tela_height
        self.__gerador_bola = geraBola

    def add_bola(self, bola: Bola):
        if isinstance(bola, Bola):
            self.__campo.append(bola)

    def setar_campo(self, background, screen):

        self.__campo = [None] * self.__capacidade

        campo_pos = (self.__tela_width / 2, self.__tela_height / 2)
        campo = pygame.draw.circle(background, (0, 0, 0), campo_pos,
                                   self.__raio, 5)

        self.__bola_central = self.__gerador_bola.geraBola(
            background, campo_pos)

        angulo = 0
        for i in range(len(self.__campo)):
            vec = pygame.math.Vector2(0, -self.__raio * 0.8).rotate(angulo)
            pt_x, pt_y = campo_pos[0] + vec.x, campo_pos[1] + vec.y

            coors = (pt_x, pt_y)

            fonte = pygame.font.SysFont(None, 50)

            if i % 3 == 0:
                self.__campo[i] = self.__gerador_bola.geraBola(
                    background, coors)

                """ bola_txt = fonte.render(bola.valor, True, (0, 0, 0)) """
            else:
                holder = pygame.draw.circle(background, (255, 0, 0), coors, 10)
                bola_empty = BolaNormal(0, '', holder, 10)
                self.__campo[i] = bola_empty

            angulo += 360 / self.__capacidade

        screen.blit(background, (0, 0))

    def desloca_bola(self, bola):
        x = bola.circle_obj.x
        y = bola.circle_obj.y

        obj = self.__bola_central.circle_obj

        pygame.Rect.move_ip(obj, x-obj.x, y-obj.y)
        pygame.display.update(obj)
        print(obj)

    @property
    def campo(self):
        return self.__campo

    @property
    def bola_central(self):
        return self.__bola_central

    @property
    def raio(self):
        return self.__raio

    @property
    def capacidade(self):
        return self.__capacidade

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
