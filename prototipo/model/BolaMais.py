from turtle import circle
from model.BolaEspecial import BolaEspecial
from model.BolaNormal import BolaNormal
import pygame


class BolaMais(BolaEspecial):
    def __init__(self, nome: str, circle_obj, em_campo: bool):
        super().__init__(nome, circle_obj, em_campo)

    def acao(self, bola1: BolaNormal, bola2: BolaNormal):
        if bola1.valor == bola2.valor:
            new_value = (bola1.valor + bola2.valor) // 2 + 1

            lista = [new_value, (self.circle_obj.x, self.circle_obj.y)]
        else:
            lista = None

        " Retorna lista com valor e posiçao da bola a ser criada "
        return lista
