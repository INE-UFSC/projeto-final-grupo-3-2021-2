from itertools import count
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
        self.__elem_dict = {
            1: "H",
            2: "He",
            3: "Li",
            4: "Be",
            5: "B",
            6: "C",
            7: "N",
            8: "O",
            9: "F",
            10: "Ne",
            11: "Na",
            12: "Mg"
        }

    def add_bola(self, bola: Bola):
        if isinstance(bola, Bola):
            self.__campo.append(bola)

    def setar_campo(self, background, screen):

        self.__campo = [None] * self.__capacidade

        campo_pos = (self.__tela_width / 2, self.__tela_height / 2)
        campo = pygame.draw.circle(background, (0, 0, 0), campo_pos,
                                   self.__raio, 5)

        self.__bola_central = self.__gerador_bola.geraBola(
            background, campo_pos, True)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(self.__elem_dict.get(self.__bola_central.valor), True, (0, 0, 0)),
                        (campo_pos[0] - 15, campo_pos[1] - 20))

        angulo = 0
        for i in range(len(self.__campo)):
            vec = pygame.math.Vector2(0, -self.__raio * 0.8).rotate(angulo)
            pt_x, pt_y = campo_pos[0] + vec.x, campo_pos[1] + vec.y

            coors = (pt_x, pt_y)

            fonte = pygame.font.SysFont(None, 50)

            if i % 3 == 0:
                # Gera bolas inicialmente setadas no campo (menos a bola central)
                self.__campo[i] = self.__gerador_bola.geraBola(
                    background, coors, True)
                background.blit(fonte.render(self.__campo[i].nome, True, (0, 0, 0)), (
                    self.__campo[i].circle_obj.x + 12, self.__campo[i].circle_obj.y + 20))
            else:
                # Gera espaços vazios (bolas vermelhas)
                holder = pygame.draw.circle(background, (255, 0, 0), coors, 10)
                fonte = pygame.font.SysFont('Arial', 25)
                bola_empty = BolaNormal(0, '', holder, 10)

                self.__campo[i] = bola_empty
            angulo += 360 / self.__capacidade

        screen.blit(background, (0, 0))

    def desloca_bola(self, bola, background):
        x = bola.circle_obj.x
        y = bola.circle_obj.y
        obj = self.__bola_central
        pygame.Rect.move_ip(obj.circle_obj, x -
                            obj.circle_obj.x, y-obj.circle_obj.y)
        if(obj.nome == "+"):
            pygame.draw.circle(background, "#d13d32",
                               (obj.circle_obj.x + 10, obj.circle_obj.y + 10), obj.circle_obj.height / 2)
            obj.em_campo = True
        elif(obj.nome == "-"):
            pygame.draw.circle(background, "#277edb",
                               (obj.circle_obj.x + 10, obj.circle_obj.y + 10), obj.circle_obj.height / 2)
        elif(obj.nome == "*"):
            pygame.draw.circle(background, "#f2efda",
                               (obj.circle_obj.x + 10, obj.circle_obj.y + 10), obj.circle_obj.height / 2)
        elif(obj.nome == "#"):
            pygame.draw.circle(background, "#888888",
                               (obj.circle_obj.x + 10, obj.circle_obj.y + 10), obj.circle_obj.height / 2)
            obj.em_campo = True
        else:
            pygame.draw.circle(background, "#A89234",
                               (obj.circle_obj.x + 10, obj.circle_obj.y + 10), obj.circle_obj.height / 2)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(self.__bola_central.nome,
                        True, (0, 0, 0)), (x - 10, y - 10))

        campo_pos = (self.__tela_width / 2, self.__tela_height / 2)
        self.__bola_central = self.__gerador_bola.geraBola(
            background, campo_pos, False)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(self.__bola_central.nome,
                        True, (0, 0, 0)), (campo_pos[0] - 15, campo_pos[1] - 20))

        return obj

    # Funcao que verifica como esta campo para
    # encerrar o jogo caso esteja cheio
    def verificaCampo(self, objList):
        countBola = 0
        for bola in objList:
            if(bola.nome == ""):
                countBola += 1
        if(countBola > 0):
            return True
        else:
            return False

    def atualizaSelfCampo(self, obj_add, obj_remove):
        index = self.__campo.index(obj_remove)
        self.__campo[index] = obj_add

    def desenhaBola(self, background, bola):
        pygame.draw.circle(
            background, "#A89234", (bola.circle_obj.x + 35, bola.circle_obj.y + 35), bola.circle_obj.height / 2)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(bola.nome,
                                     True, (0, 0, 0)), (bola.circle_obj.x + 20, bola.circle_obj.y + 15))

    # criação a partir da junção de bolas (por causa da BolaMais)
    def criaEDesenhaBola(self, background, valor: int, coors: tuple):
        pass

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

    @bola_central.setter
    def bola_central(self, bola):
        self.__bola_central = bola
