from abc import ABC
from ..model.Bola import Bola
from ..model.campo import Campo


class ControladorJogo:
    def __init__(self, pygame, campo: Campo, placar: Placar) -> None:
        self.__bola_central = {}
        self.__campo = campo
        self.__nome = ''
        self.__placar = placar
        self.__pygame = pygame

    def rodar_jogo(self):
        running = True
        while running:
            for event in self.__pygame.event.get():
                if event.type == self.__pygame.QUIT:
                    running = False

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

    @property
    def pygame(self):
        return self.__pygame

    @bola_central.setter
    def bola_central(self, bola: Bola):
        self.__bola_central = bola

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
