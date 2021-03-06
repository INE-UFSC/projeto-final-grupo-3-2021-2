from itertools import count
from random import randint
import pygame
import math
from model.Bola import Bola
from model.BolaNormal import BolaNormal
from model.geraBola import GeraBola
from model.BolaMais import BolaMais
from model.BolaEspecial import BolaEspecial


class Campo():

    def __init__(self, tela_width: int, tela_height: int, geraBola: GeraBola, cor_bola_holder ) -> None:
        self.__capacidade = 20
        self.__campo = []
        self.__bola_central = {}
        self.__cor_bola_holder = cor_bola_holder
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
        self.__elem_cor = {1: (235, 110, 238),2: (135, 206, 187),3: (96, 134, 170),4: (138, 109, 222),
                           5: (163, 207, 150),6: (238, 103, 173),7: (141, 155, 105),8: (211, 185, 154),
                           9: (164, 200, 103),10: (134, 234, 183),11: (186, 87, 238),12: (173, 218, 114),
                           13: (119, 163, 69),14: (82, 186, 148),15: (79, 82, 147),16: (112, 141, 146),
                           17: (144, 232, 238),18: (93, 222, 227),19: (126, 217, 128),20: (239, 167, 205),
                           21: (111, 128, 186),22: (154, 131, 179),23: (161, 78, 144),24: (143, 234, 170),
                           25: (79, 203, 128),26: (74, 205, 217),27: (204, 235, 118),28: (229, 168, 137),
                           29: (169, 232, 161),30: (174, 217, 200),31: (104, 236, 192),32: (68, 137, 160),
                           33: (197, 187, 103),34: (150, 176, 124),35: (96, 133, 141),36: (103, 79, 119),
                           37: (77, 136, 182),38: (222, 72, 131),39: (71, 176, 111),40: (208, 199, 147),
                           41: (143, 155, 216),42: (233, 133, 87),43: (149, 212, 183),44: (180, 132, 103),
                           45: (116, 172, 175),46: (132, 164, 195),47: (181, 208, 171),48: (146, 123, 153),
                           49: (183, 177, 200),50: (114, 157, 67)}
        self.__list_coors = [None] * self.__capacidade

    def add_bola(self, bola: Bola):
        if isinstance(bola, Bola):
            self.__campo.append(bola)

    def setar_campo(self, background, screen):

        self.__campo = [None] * self.__capacidade

        campo_pos = (self.__tela_width / 2, self.__tela_height / 2)
        campo = pygame.draw.circle(background, (255, 255, 255), campo_pos,
                                   self.__raio, 5)

        self.__bola_central = self.__gerador_bola.geraBola(
            self.__elem_dict, background, campo_pos, True, self.__elem_cor)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(self.__elem_dict.get(self.__bola_central.valor), True, (255, 255, 255)),
                        (campo_pos[0] - 15, campo_pos[1] - 20))

        angulo = 0
        for i in range(len(self.__campo)):
            vec = pygame.math.Vector2(0, -self.__raio * 0.8).rotate(angulo)
            pt_x, pt_y = campo_pos[0] + int(vec.x), campo_pos[1] + int(vec.y)

            coors = (pt_x, pt_y)

            fonte = pygame.font.SysFont(None, 50)

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

            for i in range(1, len(self.__elem_dict.values())+1):
                if self.__elem_dict[i] == self.__bola_central.nome:
                    cor = self.__elem_cor[i]

            pygame.draw.circle(background, cor,
                               (obj.circle_obj.x + 10, obj.circle_obj.y + 10), obj.circle_obj.height / 2)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(self.__bola_central.nome,
                        True, (255, 255, 255)), (bola.circle_obj.x + 15, bola.circle_obj.y + 15))

        campo_pos = (self.__tela_width / 2, self.__tela_height / 2)
        self.__bola_central = self.__gerador_bola.geraBola(
            self.__elem_dict, background, campo_pos, False, self.__elem_cor)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(self.__bola_central.nome,
                        True, (255, 255, 255)), (campo_pos[0] - 15, campo_pos[1] - 20))

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
        for i in range(1, len(self.__elem_dict.values())+1):
            if self.__elem_dict[i] == bola.nome:
                cor = self.__elem_cor[i]
        pygame.draw.circle(
            background, cor, (bola.circle_obj.x + 35, bola.circle_obj.y + 35), bola.circle_obj.height / 2)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(bola.nome,
                                     True, (255, 255, 255)), (bola.circle_obj.x + 20, bola.circle_obj.y + 15))

        corrected_coors = self.corrigirCoors(coors_no_campo)

        bola_empty = self.desenhaBolaHolder(corrected_coors, background)

        self.atualizaSelfCampo(bola_empty, bola)

    def desenhaBolaAoAcaoBranca(self, background, bola):
        for i in range(1, len(self.__elem_dict.values())+1):
            if self.__elem_dict[i] == bola.nome:
                cor = self.__elem_cor[i]

        pygame.draw.circle(
            background, cor, (bola.circle_obj.x + 35, bola.circle_obj.y + 35), bola.circle_obj.height / 2)
        fonte = pygame.font.SysFont(None, 50)
        background.blit(fonte.render(bola.nome,
                                     True, (255, 255, 255)), (bola.circle_obj.x + 20, bola.circle_obj.y + 15))

    def desenhaBolaAcaoMateriaNegra(self, background, bolaNegra):

        index = self.__campo.index(bolaNegra)
        rolou, pontos, new_value, lista_bolas, lib_index = bolaNegra.acao(
            index, self.__campo)
        if rolou:
            circle = pygame.draw.circle(
                background, self.__elem_cor[new_value], (bolaNegra.circle_obj.x + 10, bolaNegra.circle_obj.y + 10), bolaNegra.circle_obj.height / 2)
            nova_bola = BolaNormal(
                new_value, self.__elem_dict[new_value], circle)
            fonte = pygame.font.SysFont(None, 50)
            background.blit(fonte.render(nova_bola.nome,
                                         True, (255, 255, 255)), (nova_bola.circle_obj.x + 20, nova_bola.circle_obj.y + 15))

            self.__campo[index] = nova_bola

            for i in range(0, len(lista_bolas)):
                coors = (lista_bolas[i].circle_obj.center[0],
                         lista_bolas[i].circle_obj.center[1])
                corrected_coors = self.corrigirCoors(coors)
                bola_empty1 = self.desenhaBolaHolder(
                    corrected_coors, background)
                self.__campo[lib_index[i]] = bola_empty1

        self.__gerador_bola.atualizaMinMaxBola(self.__campo)
        tempo_timer = (math.ceil(len(lista_bolas)/2))*5

        return pontos, tempo_timer

    def desenhaBolaAoAcaoMais(self, background, bolaMais):
        index = self.__campo.index(bolaMais)
        rolou, pontos, new_value, casais, casais_index = bolaMais.acao(
            index, self.__campo)

        if rolou:

            circle = pygame.draw.circle(
                background, self.__elem_cor[new_value], (bolaMais.circle_obj.x + 10, bolaMais.circle_obj.y + 10), bolaMais.circle_obj.height / 2)
            nova_bola = BolaNormal(
                new_value, self.__elem_dict[new_value], circle)
            fonte = pygame.font.SysFont(None, 50)
            background.blit(fonte.render(nova_bola.nome,
                                         True, (255, 255, 255)), (nova_bola.circle_obj.x + 20, nova_bola.circle_obj.y + 15))

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
        tempo_timer = ((len(casais)/2)*5)
        return pontos, tempo_timer

    def desenhaBolaHolder(self, coors, background):
        holder = pygame.draw.circle(
            background, self.__cor_bola_holder, coors, 35)

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
