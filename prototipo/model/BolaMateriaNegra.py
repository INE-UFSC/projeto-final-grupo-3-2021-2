from model.BolaEspecial import BolaEspecial
from model.BolaNormal import BolaNormal
import pygame


class BolaMateriaNegra(BolaEspecial):
    def __init__(self, circle_obj, em_campo: bool):
        super().__init__(circle_obj, em_campo)

    def acao(bola1: BolaNormal, bola2: BolaNormal):
        new_value = (bola1.valor + bola2.valor) // 2 + 1

        bola_obj = BolaNormal(new_value, "holder",
                              pygame.bola1.circle_obj.copy())

        " O circle_obj da bola retornada pode ser que precise ser atualizado (usando draw.circle) "
        return bola_obj
