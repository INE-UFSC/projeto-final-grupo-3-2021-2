from turtle import circle
from model.BolaEspecial import BolaEspecial
from model.BolaNormal import BolaNormal
import pygame


class BolaMais(BolaEspecial):
    def __init__(self, nome: str, circle_obj, em_campo: bool):
        super().__init__(nome, circle_obj, em_campo)

    def acao(self, index, campo):
        pontos = 0 
        rolou = False
        new_value = None
        casais = list()
        casais_index = list()
        procurar = True
        tm_lista = len(campo)
        while procurar:
            # campo_lista = []
            # for i in campo:
            #     boleta = i.nome
            #     campo_lista.append(boleta)
            # print(campo_lista)
            # print('index : ', index)
            bola_d = None
            bola_e = None
            count = index
            while True:
                count = count + 1
                if count == index:
                    break
                if count == tm_lista:
                    count = 0
                if campo[count].nome != '':
                    bola_d = campo[count]
                    index_d = count
                    break

            count = index
            while True:
                count = count - 1
                if count == index:
                    break
                if count == -1:
                    count = tm_lista - 1
                if campo[count].nome != '':
                    bola_e = campo[count]
                    index_e = count
                    break
            # print('2')
            # campo_lista = []
            # for i in self.__campo:
            #     boleta = i.nome
            #     campo_lista.append(boleta)
            # print(campo_lista)
            # print('index : ', index)
            if bola_e == None or bola_d == None:
                procurar = False
            elif bola_e == bola_d:
                procurar = False
            elif isinstance(bola_d, BolaEspecial) or isinstance(bola_d, BolaEspecial):
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
                
        if len(casais) != 0:
            rolou = True
            # novo valor da bola
            for i in range(0, len(casais), +2):
                if i == 0 :
                    valor = casais[i].valor

                elif casais[i].valor > valor:
                    valor = casais[i].valor

            new_value = (valor+1) + (len(casais)/2 - 1)

            # pontuação para o placar
            for i in casais:
                pontos += i.valor
            
        return rolou, pontos, new_value, casais,casais_index
        # print('3')
        # campo_lista = []
        # for i in self.__campo:
        #     boleta = i.nome
        #     campo_lista.append(boleta)
        # print(campo_lista)
        # print('index : ', index)