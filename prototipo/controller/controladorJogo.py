from cmath import sqrt
import sys
sys.path.append("/Users/Windows/Documents/GitHub/projeto-final-grupo-3-2021-2")
from prototipo.model.geraBola import GeraBola
import prototipo.model.bola as bola
import prototipo.model.campo as campo
import pygame
from abc import ABC



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

        self.__campo.setar_campo(background, screen)

        screen.blit(background, (0, 0))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    (x, y) = pygame.mouse.get_pos()
                    
                    min_dis = 1000
                    closest_obj = None
                    
                    for bola in self.__campo.campo:
                        if bola.nome == '':
                            circle_pos = bola.circle_obj.center
                            
                            temp = abs(sqrt((x-circle_pos[0])**2 + (y-circle_pos[0])**2))
                            if temp < min_dis:
                                min_dis = temp
                                closest_obj = bola
                    
                    if closest_obj != None:
                        self.__campo.desloca_bola(closest_obj)
                        
                pygame.display.update()
        
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
