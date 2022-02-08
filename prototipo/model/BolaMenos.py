from prototipo.model.bolaEspecial import BolaEspecial
from .bolaNormal import BolaNormal


class BolaMenos(BolaEspecial):
    def __init__(self, cor: str, raio: float, chance: float, em_campo: bool):
        super().__init__(cor, raio, chance, em_campo)

    def pegar_bola(bola: BolaNormal):
        pass

    def transformar_em_mais():
        pass
