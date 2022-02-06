import pygame
from Bola import Bola


class Campo():
    def __init__(self, tela_width: int, tela_height: int) -> None:
        self.__capacidade = 20
        self.__campo = []
        self.__positions = []
        self.__raio = 300
        self.__tela_width = tela_width
        self.__tela_height = tela_height

    def add_bola(self, bola: Bola):
        if isinstance(bola, Bola):
            self.__campo.append(bola)

    def setar_campo(self, background, screen):

        self.__positions = [None] * self.__capacidade

        campo_pos = (self.__tela_width/2, self.__tela_height/2)
        campo = pygame.draw.circle(
            background, (0, 0, 0), campo_pos, self.__raio, 5)

        centro_campo = pygame.draw.circle(background, (0, 0, 0), campo_pos, 5)

        angulo = 0
        for i in range(len(self.__positions)):
            vec = pygame.math.Vector2(0, -self.__raio * 0.8).rotate(angulo)
            pt_x, pt_y = campo_pos[0] + vec.x, campo_pos[1] + vec.y

            coors = (pt_x, pt_y)

            pygame.draw.circle(background, (255, 0, 0), coors, 10)

            self.__positions[i] = coors

            angulo += 360 / self.__capacidade

        screen.blit(background, (0, 0))

    @property
    def campo(self):
        return self.__campo

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
