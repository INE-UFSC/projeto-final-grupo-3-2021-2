from campo import Campo
from bolaMais import BolaMais
from bolaMateriaNegra import BolaMateriaNegra
from bolaMenos import BolaMenos
from bolaBranca import BolaBranca


class GeraBola():

    def __init__(self, campo: Campo) -> None:
        self.__max_bola = 0
        self.__min_bola = 0
        self.__campo = campo
        self.__lista_bola_especial = [
            BolaMais, BolaMenos, BolaBranca, BolaMateriaNegra
        ]
