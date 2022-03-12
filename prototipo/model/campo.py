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
        dic_elementos = {}
        for i in range(1, 100):
            dic_elementos[i] = f'{i}'
        self.__elem_dict = dic_elementos
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

            if i % 3 == 0:
                # Gera bolas inicialmente setadas no campo (menos a bola central)
                self.__campo[i] = self.__gerador_bola.geraBola(
                    self.__elem_dict, background, coors, True)
                background.blit(fonte.render(self.__campo[i].nome, True, (0, 0, 0)), (
                    self.__campo[i].circle_obj.x + 12, self.__campo[i].circle_obj.y + 20))
                background.blit(fonte.render('%d x %d' %
                                (coors), True, (0, 0, 0)), (coors))
                self.__list_coors[i] = coors
            else:
                # Gera espaços vazios (bolas cinzas)
                bola_empty = self.desenhaBolaHolder(coors, background)
                background.blit(fonte.render('%d x %d' %
                                (coors), True, (0, 0, 0)), (coors))
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
                        True, (0, 0, 0)), (bola.circle_obj.x + 15, bola.circle_obj.y + 15))

        campo_pos = (self.__tela_width / 2, self.__tela_height / 2)
        self.__bola_central = self.__gerador_bola.geraBola(
            self.__elem_dict,background, campo_pos, False)
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

        bola_empty = self.desenhaBolaHolder(coors_no_campo, background)

        self.atualizaSelfCampo(bola_empty, bola)

    # criação a partir da junção de bolas (por causa da BolaMais)

    def desenhaBolaAoAcaoMais(self, background, bolaMais):

        index = self.__campo.index(bolaMais)
        casais = list()
        casais_index = list()
        procurar = True
        pontos = 0
        tm_lista = len(self.__campo)
        while procurar:
            campo_lista = []
            for i in self.__campo:
                boleta = i.nome
                campo_lista.append(boleta)
            # print(campo_lista)
            # print('index : ', index)
            bola_d = None
            bola_e = None
            count = index
            while True:
                count =  count + 1
                if count == index:
                    break
                if count == tm_lista:
                    count = 0  
                if self.__campo[count].nome != '':
                    bola_d = self.__campo[count]
                    index_d = count
                    break
    
            count = index   
            while True:
                count =  count - 1
                if count == index:
                    break
                if count == -1:
                    count = tm_lista -1 
                if self.__campo[count].nome != '':
                    bola_e = self.__campo[count]
                    index_e = count
                    break
            # print('2')
            campo_lista = []
            for i in self.__campo:
                boleta = i.nome
                campo_lista.append(boleta)
            # print(campo_lista)
            # print('index : ', index)
            if bola_e == None or bola_d == None:
                procurar = False
            elif bola_e.nome != bola_d.nome:
                procurar = False
            else:
                casais_index.append(index_d)
                casais_index.append(index_e)
                casais.append(bola_d)
                casais.append(bola_e)
                bola_d.nome = ''
                bola_e.nome = ''
        # print('3')
        campo_lista = []
        for i in self.__campo:
            boleta = i.nome
            campo_lista.append(boleta)
        # print(campo_lista)
        # print('index : ', index)
        if len(casais) != 0:
        
            #novo valor da bola
            for i in range(0,len(casais),+2):
                if i == 0:
                    valor = casais[i].valor
                    
                elif casais[i].valor > valor:
                    valor = casais[i].valor
                    
            new_value = (valor+1) + (len(casais)/2 - 1)
            
            #pontuação para o placar
            pontos = 0
            for i in casais:
                pontos += i.valor
            
            circle = pygame.draw.circle(
                    background, "#A89234", (bolaMais.circle_obj.x + 10, bolaMais.circle_obj.y + 10), bolaMais.circle_obj.height / 2)
            nova_bola = BolaNormal(
                new_value, self.__elem_dict[new_value], circle)
            fonte = pygame.font.SysFont(None, 50)
            background.blit(fonte.render(nova_bola.nome,
                                            True, (0, 0, 0)), (nova_bola.circle_obj.x + 20, nova_bola.circle_obj.y + 15))

            self.__campo[index] = nova_bola        
            
            for i in range(0,len(casais),+2):
                casais_index[i],casais_index[i+1]
                casais[i], casais[i+1]
                
                coors = (casais[i].circle_obj.center[0], casais[i].circle_obj.center[1])
                print("coors1",coors)
                bola_empty1 = self.desenhaBolaHolder(coors, background, "#03fc13")
                self.__campo[casais_index[i]] = bola_empty1

                coors = (casais[i+1].circle_obj.center[0], casais[i+1].circle_obj.center[1])
                print("coors2",coors)
                bola_empty2 = self.desenhaBolaHolder(coors, background, "#1c03fc")
                self.__campo[casais_index[i+1]] = bola_empty2
            # print('4')
            campo_lista = []
            for i in self.__campo:
                boleta = i.nome
                campo_lista.append(boleta)
                # print(campo_lista)
                # print('index : ', index)    
        return pontos
   
        
            
        
        
           
    def desenhaBolaHolder(self, coors, background, cor="#808080"):
        lista = self.__list_coors
        flag = False
        for coor in lista:
            if(int(coor[0] != coors[0]) and int(coor[1] != coors[1])):
                flag = True
        if(flag):
            newCoors = (coors[0] - 25, coors[1] - 25)
            holder = pygame.draw.circle(
             background, cor, newCoors, 35)
        else:
            holder = pygame.draw.circle(
             background, cor, coors, 35)

        return BolaNormal(0, '', holder)

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
