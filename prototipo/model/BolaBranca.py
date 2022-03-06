from model.BolaEspecial import BolaEspecial
from model.BolaNormal import BolaNormal


class BolaBranca(BolaEspecial):
    def __init__(self, circle_obj, em_campo: bool):
        super().__init__(circle_obj, em_campo)

    def acao(self, bola: BolaNormal):
        self.circle_obj = bola.circle_obj
