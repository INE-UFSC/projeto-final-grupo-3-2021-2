import time
import model.campo as campo
import model.Bola as bola
from model.geraBola import GeraBola
from abc import ABC
import pygame
from cmath import sqrt
import sys
import os
from model.BolaBranca import BolaBranca

from model.BolaEspecial import BolaEspecial
from model.BolaMais import BolaMais
from model.BolaMenos import BolaMenos
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

                    closest_obj = None
                    count = 0

                    for bola in self.__campo.campo:
                        count += 1

                        if bola.nome == '':

                            if x <= bola.circle_obj.x + 10 + 30 and x >= bola.circle_obj.x + 10 - 30:
                                if y <= bola.circle_obj.y + 10 + 30 and y >= bola.circle_obj.y + 10 - 30:
                                    closest_obj = bola
                        elif not isinstance(bola, BolaEspecial) and (isinstance(self.__campo.bola_central, BolaMenos) or isinstance(self.__campo.bola_central, BolaBranca)):
                            if x <= bola.circle_obj.x + 10 + 30 and x >= bola.circle_obj.x + 10 - 30:
                                if y <= bola.circle_obj.y + 10 + 30 and y >= bola.circle_obj.y + 10 - 30:
                                    closest_obj = bola

                    if closest_obj != None:
                        if closest_obj.nome == "" and not (isinstance(self.__campo.bola_central, BolaMenos) or isinstance(self.__campo.bola_central, BolaBranca)):
                            obj = self.__campo.desloca_bola(
                                closest_obj, background)

                            if isinstance(obj, BolaMais):
                                index = self.__campo.campo.index(obj)

                                if index == 0:
                                    bola1 = self.__campo.campo[len(
                                        self.__campo.campo) - 1]
                                    bola2 = self.__campo.campo[index + 1]
                                elif index == len(self.__campo.campo) - 1:
                                    bola1 = self.__campo.campo[index - 1]
                                    bola2 = self.__campo.campo[0]
                                else:
                                    bola1 = self.__campo.campo[index - 1]
                                    bola2 = self.__campo.campo[index + 1]

                                lista_com_valor_e_coors = obj.acao(
                                    bola1, bola2)

                            # Essa função compara e atualiza as bolas na lista
                            self.__campo.atualizaSelfCampo(obj, closest_obj)
                        elif closest_obj.nome != "":
                            if isinstance(self.__campo.bola_central, BolaMenos):
                                obj = self.__campo.bola_central.acao(
                                    closest_obj)
                                self.__campo.bola_central = obj

                                self.__campo.desenhaBola(background, obj)

            screen.blit(background, (0, 0))
            pygame.display.update()
            clock.tick(40)

            if(self.__campo.verificaCampo(self.__campo.campo) == False):
                time.sleep(2)
                running = False
                pygame.quit()
                exit()

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
