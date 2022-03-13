from copy import copy
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
from view.score import Placar
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
        # Inicializando placar
        self.__placar = Placar(
            background, self.__tela_width, self.__tela_height)

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
                            if bola.circle_obj.x + 35 - 30 <= x <= bola.circle_obj.x + 35 + 30 and bola.circle_obj.y + 35 - 30 <= y <= bola.circle_obj.y + 35 + 30:
                                closest_obj = bola
                        elif not isinstance(bola, BolaEspecial) and (isinstance(self.__campo.bola_central, BolaMenos) or isinstance(self.__campo.bola_central, BolaBranca)):
                            if bola.circle_obj.x + 35 - 30 <= x <= bola.circle_obj.x + 35 + 30 and bola.circle_obj.y + 35 - 30 <= y <= bola.circle_obj.y + 35 + 30:
                                closest_obj = bola

                    # Se tiver alguma bola vermelha no campo ele ativa
                    count = 0
                    while True:
                        if count == len(self.__campo.campo):
                            break
                        elif self.__campo.campo[count].nome == '+':
                            self.__campo.desenhaBolaAoAcaoMais(
                                background, self.__campo.campo[count])

                        count += 1

                    if closest_obj != None:
                        if closest_obj.nome == "" and not (isinstance(self.__campo.bola_central, BolaMenos) or isinstance(self.__campo.bola_central, BolaBranca)):
                            obj = self.__campo.desloca_bola(
                                closest_obj, background)

                            # Essa função compara e atualiza as bolas na lista
                            self.__campo.atualizaSelfCampo(obj, closest_obj)

                            if isinstance(obj, BolaMais):

                                new_value = self.__campo.desenhaBolaAoAcaoMais(
                                    background, obj)
                                self.__placar.pontuar(int(new_value))

                        elif closest_obj.nome != "":
                            if isinstance(self.__campo.bola_central, BolaMenos):

                                coors_no_campo = closest_obj.circle_obj.center

                                obj = self.__campo.bola_central.acao(
                                    closest_obj)
                                self.__campo.bola_central = obj

                                self.__campo.desenhaBolaAoAcaoMenos(
                                    background, obj, coors_no_campo)

                            elif isinstance(self.__campo.bola_central, BolaBranca):
                                coors_no_campo = closest_obj.circle_obj.center

                                obj = self.__campo.bola_central.acao(
                                    closest_obj)
                                self.__campo.bola_central = copy(obj)

                                self.__campo.desenhaBolaAoAcaoBranca(
                                    background, obj, coors_no_campo)

            self.__placar.desenha_placar()
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
