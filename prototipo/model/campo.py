import pygame
from Bola import Bola


class Campo():
    def __init__(self) -> None:
        self.__capacidade = 20
        self.__campo = []
        self.__positions = []
        self.__raio = 300

    def add_bola(self, bola: Bola):
        if isinstance(bola, Bola):
            self.__campo.append(bola)

    def setar_campo(self):

        self.__positions = [None] * self.__capacidade

        width = 1080
        height = 600
        red = ()

        screen = pygame.display.set_mode((width, height))

        display = pygame.display
        display.set_caption('ATOMIKO')

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        campo_pos = (width/2, height/2)
        campo = pygame.draw.circle(
            background, (0, 0, 0), campo_pos, self.__raio, 5)

        centro_campo = pygame.draw.circle(background, (0, 0, 0), campo_pos, 5)

        angulo = 0
        for i in range(len(self.__positions)):
            vec = pygame.math.Vector2(0, -self.__raio * 0.8).rotate(angulo)
            pt_x, pt_y = campo_pos[0] + vec.x, campo_pos[1] + vec.y

            pygame.draw.circle(background, (255, 0, 0), (pt_x, pt_y), 5)

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
