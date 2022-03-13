import pygame
from model.BolaEspecial import BolaEspecial
from model.BolaNormal import BolaNormal


class BolaBranca(BolaEspecial):
    def __init__(self, nome: str, circle_obj, em_campo: bool):
        super().__init__(nome, circle_obj, em_campo)
        self.__click = 0

    def acao(self, bola: BolaNormal):
        if self.__click == 0:
            x = bola.circle_obj.x
            y = bola.circle_obj.y
            pygame.Rect.move_ip(bola.circle_obj,
                                self.circle_obj.x - x, self.circle_obj.y - y)

            return bola