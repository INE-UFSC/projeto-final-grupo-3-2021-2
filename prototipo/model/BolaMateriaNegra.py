from BolaEspecial import BolaEspecial
from BolaNormal import BolaNormal


class BolaMateriaNegra(BolaEspecial):
    def __init__(self, cor: str, raio: float, chance: float, em_campo: bool):
        super().__init__(cor, raio, chance, em_campo)

    def juntar_bolas(bola: BolaNormal):
        pass
