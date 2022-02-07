import pygame
from abc import ABC
import os
import sys
sys.path.append("/Users/Windows/Documents/GitHub/projeto-final-grupo-3-2021-2")
import prototipo.model.campo
import prototipo.model.bola

class ControladorJogo:
    def __init__(self, tela_width: int, tela_height: int, placar) -> None:
        self.__bola_central = {}
        self.__campo = prototipo.model.campo.Campo(tela_width, tela_height)
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
        
        self.__campo.setar_campo(background, screen)
        
        screen.blit(background, (0, 0))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

    @bola_central.setter
    def bola_central(self, bola: prototipo.model.bola.Bola):
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