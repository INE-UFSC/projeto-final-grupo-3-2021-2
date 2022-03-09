from model.BolaEspecial import BolaEspecial
from model.BolaNormal import BolaNormal


class BolaMenos(BolaEspecial):
    def __init__(self, nome: str, circle_obj, em_campo: bool):
        super().__init__(nome, circle_obj, em_campo)
        self.__click = 0

    def acao(self, bola: BolaNormal):
        if self.__click == 0:
            self.circle_obj = bola.circle_obj
            del bola
