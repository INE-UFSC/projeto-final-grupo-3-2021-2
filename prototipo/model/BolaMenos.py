from model.BolaEspecial import BolaEspecial
from model.BolaNormal import BolaNormal


class BolaMenos(BolaEspecial):
    def __init__(self, circle_obj, raio: float, em_campo: bool):
        super().__init__(circle_obj, raio, em_campo)
        self.__click = 0

    def acao(self, bola: BolaNormal):
        if self.__click == 0:
            pass

    def transformar_em_mais():
        pass
