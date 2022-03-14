from itertools import count
from random import randint
import pygame
from model.Bola import Bola
from model.BolaNormal import BolaNormal
from model.geraBola import GeraBola
from model.BolaMais import BolaMais
from model.BolaEspecial import BolaEspecial


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
            12: "Mg",
            13: "Al",
            14: "Si",
            15: "P",
            16: "S",
            17: "Cl",
            18: "Ar",
            19: "K",
            20: "Ca",
            21: "Sc",
            22: "Ti",
            23: "V",
            24: "Cr",
            25: "Mn",
            26: "Fe",
            27: "Co",
            28: "Ni",
            29: "Cu",
            30: "Zn",
            31: "Ga",
            32: "Ge",
            33: "As",
            34: "Se",
            35: "Br",
            36: "Kr",
            37: "Rb",
            38: "Sr",
            39: "Y",
            40: "Zr",
            41: "Nb",
            42: "Mo",
            43: "Tc",
            44: "Ru",
            45: "Rh",
            46: "Pd",
            47: "Ag",
            48: "Cd",
            49: "In",
            50: "Sn",
        }
        self.__list_coors = [None] * self.__capacidade

    def add_bola(self, bola: Bola):
        if isinstance(bola, Bola):
            self.__campo.append(bola)

    def setar_campo(self, background, screen):

        self.__campo = [None] * self.__capacidade

        campo_pos = (self.__tela_width / 2, self.__tela_height / 2)
        campo = pygame.draw.circle(background, (0, 0, 0), campo_pos,
                                   self.__raio, 5)

        self.__bola_central = self.__gerador_bola.geraBola(
            self.__elem_dict, background, campo_pos, True)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(self.__elem_dict.get(self.__bola_central.valor), True, (0, 0, 0)),
                        (campo_pos[0] - 15, campo_pos[1] - 20))

        angulo = 0
        for i in range(len(self.__campo)):
            vec = pygame.math.Vector2(0, -self.__raio * 0.8).rotate(angulo)
            pt_x, pt_y = campo_pos[0] + int(vec.x), campo_pos[1] + int(vec.y)

            coors = (pt_x, pt_y)

            fonte = pygame.font.SysFont(None, 50)

            if randint(1, 100) <= 30:
                # Gera bolas inicialmente setadas no campo (menos a bola central)
                self.__campo[i] = self.__gerador_bola.geraBola(
                    self.__elem_dict, background, coors, True)
                background.blit(fonte.render(self.__campo[i].nome, True, (0, 0, 0)), (
                    self.__campo[i].circle_obj.x + 12, self.__campo[i].circle_obj.y + 20))
                self.__list_coors[i] = coors
            else:
                # Gera espaços vazios (bolas cinzas)
                bola_empty = self.desenhaBolaHolder(coors, background)
                self.__list_coors[i] = coors
                self.__campo[i] = bola_empty
            angulo += 360 / self.__capacidade

        screen.blit(background, (0, 0))

    def desloca_bola(self, bola, background):
        obj = self.__bola_central
        x = bola.circle_obj.x - obj.circle_obj.x
        y = bola.circle_obj.y - obj.circle_obj.y

        pygame.Rect.move_ip(obj.circle_obj, x + 25, y + 25)
        if(obj.nome == "+"):
            pygame.draw.circle(background, "#d13d32",
                               (obj.circle_obj.x + 10, obj.circle_obj.y + 10), obj.circle_obj.height / 2)
            obj.em_campo = True
        elif(obj.nome == "-"):
            pygame.draw.circle(background, "#277edb",
                               (obj.circle_obj.x + 10, obj.circle_obj.y + 10), obj.circle_obj.height / 2)
        elif(obj.nome == "="):
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
                        True, (0, 0, 0)), (bola.circle_obj.x + 15, bola.circle_obj.y + 15))

        campo_pos = (self.__tela_width / 2, self.__tela_height / 2)
        self.__bola_central = self.__gerador_bola.geraBola(
            self.__elem_dict, background, campo_pos, False)
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

    def desenhaBolaAoAcaoMenos(self, background, bola, coors_no_campo):
        pygame.draw.circle(
            background, "#A89234", (bola.circle_obj.x + 35, bola.circle_obj.y + 35), bola.circle_obj.height / 2)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(bola.nome,
                                     True, (0, 0, 0)), (bola.circle_obj.x + 20, bola.circle_obj.y + 15))

        corrected_coors = self.corrigirCoors(coors_no_campo)

        bola_empty = self.desenhaBolaHolder(corrected_coors, background)

        self.atualizaSelfCampo(bola_empty, bola)

    def desenhaBolaAoAcaoBranca(self, background, bola):
        pygame.draw.circle(
            background, "#A89234", (bola.circle_obj.x + 35, bola.circle_obj.y + 35), bola.circle_obj.height / 2)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(bola.nome,
                                     True, (0, 0, 0)), (bola.circle_obj.x + 20, bola.circle_obj.y + 15))

    def desenhaBolaAcaoMateriaNega(self, background, bolaNegra):
        print('1')
        campo_lista = []
        for i in self.__campo:
            boleta = i.nome
            campo_lista.append(boleta)
        print(campo_lista)

        index = self.__campo.index(bolaNegra)
        rolou, pontos, new_value, lista_bolas, lib_index = bolaNegra.acao(
            index, self.__campo)
        if rolou:
            circle = pygame.draw.circle(
                background, "#A89234", (bolaNegra.circle_obj.x + 10, bolaNegra.circle_obj.y + 10), bolaNegra.circle_obj.height / 2)
            nova_bola = BolaNormal(
                new_value, self.__elem_dict[new_value], circle)
            fonte = pygame.font.SysFont(None, 50)
            background.blit(fonte.render(nova_bola.nome,
                                         True, (0, 0, 0)), (nova_bola.circle_obj.x + 20, nova_bola.circle_obj.y + 15))

            self.__campo[index] = nova_bola

            for i in range(0, len(lista_bolas)):
                coors = (lista_bolas[i].circle_obj.center[0],
                         lista_bolas[i].circle_obj.center[1])
                corrected_coors = self.corrigirCoors(coors)
                bola_empty1 = self.desenhaBolaHolder(
                    corrected_coors, background)
                self.__campo[lib_index[i]] = bola_empty1

        print('3')
        campo_lista = []
        for i in self.__campo:
            boleta = i.nome
            campo_lista.append(boleta)
        print(campo_lista)
        self.__gerador_bola.atualizaMinMaxBola(self.__campo)

        return pontos

    def desenhaBolaAoAcaoMais(self, background, bolaMais):
        index = self.__campo.index(bolaMais)
        rolou, pontos, new_value, casais, casais_index = bolaMais.acao(
            index, self.__campo)

        if rolou:

            circle = pygame.draw.circle(
                background, "#A89234", (bolaMais.circle_obj.x + 10, bolaMais.circle_obj.y + 10), bolaMais.circle_obj.height / 2)
            nova_bola = BolaNormal(
                new_value, self.__elem_dict[new_value], circle)
            fonte = pygame.font.SysFont(None, 50)
            background.blit(fonte.render(nova_bola.nome,
                                         True, (0, 0, 0)), (nova_bola.circle_obj.x + 20, nova_bola.circle_obj.y + 15))

            self.__campo[index] = nova_bola

            for i in range(0, len(casais), +2):
                coors = (casais[i].circle_obj.center[0],
                         casais[i].circle_obj.center[1])
                corrected_coors = self.corrigirCoors(coors)
                bola_empty1 = self.desenhaBolaHolder(
                    corrected_coors, background)
                self.__campo[casais_index[i]] = bola_empty1

                coors = (casais[i+1].circle_obj.center[0],
                         casais[i+1].circle_obj.center[1])
                corrected_coors = self.corrigirCoors(coors)
                bola_empty2 = self.desenhaBolaHolder(
                    corrected_coors, background)
                self.__campo[casais_index[i+1]] = bola_empty2

        self.__gerador_bola.atualizaMinMaxBola(self.__campo)

        return pontos

    def desenhaBolaHolder(self, coors, background, cor="#808080"):
        holder = pygame.draw.circle(
            background, cor, coors, 35)

        return BolaNormal(0, '', holder)

    def corrigirCoors(self, coors):
        lista = self.__list_coors
        flag = True
        for coor in lista:
            if(int(coor[0]) == coors[0] and int(coor[1]) == coors[1]):
                flag = False

        if flag:
            return (coors[0] - 25, coors[1] - 25)
        else:
            return coors

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
