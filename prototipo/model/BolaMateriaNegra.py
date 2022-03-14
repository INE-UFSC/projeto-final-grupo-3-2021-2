from model.BolaEspecial import BolaEspecial
from model.BolaNormal import BolaNormal
import pygame


class BolaMateriaNegra(BolaEspecial):
    def __init__(self, nome: str, circle_obj, em_campo: bool):
        super().__init__(nome, circle_obj, em_campo)

    def acao(self, index, campo):
        rolou = False
        count = index
        new_value = None
        pontos = 0
        tm_lista = len(campo)
        lista_bolas = []
        lib_index = []
        print('crash1')
        while True:
                count = count + 1
                if count == index:
                    break
                if count == tm_lista:
                    count = 0
                if campo[count].nome != '':
                    lista_bolas.append(campo[count])
                    lib_index.append(count)
        print('crash2')           
        if len(lista_bolas) != 0 :
            rolou = True
            atribuiu = False
            pos_inicial = 0
            for i in range(len(lista_bolas)):
                if not(isinstance(lista_bolas[i], BolaEspecial)):
                    pontos += lista_bolas[i].valor
                    if i == pos_inicial:
                        atribuiu = True
                        valor = lista_bolas[i].valor
                    elif lista_bolas[i].valor > valor:
                        valor = lista_bolas[i].valor
                else:
                    if not(atribuiu):
                        pos_inicial += 1
                    
            new_value = (valor) + len(lista_bolas) - 1
            
           
        print('2')
        campo_lista = []
        for i in lista_bolas:
             boleta = i.nome
             campo_lista.append(boleta)
        print(campo_lista)    
            
        
        return rolou, pontos, new_value, lista_bolas, lib_index
        
