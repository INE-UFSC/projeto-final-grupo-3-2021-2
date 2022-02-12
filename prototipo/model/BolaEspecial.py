
from Bola import Bola

class BolaEspecial(Bola):
    def __init__(self, cor: str, raio: float, chance: float, em_campo: bool):
        super().__init__(cor, raio)
        self.__chance = chance
        self.__em_campo = em_campo

    @property
    def chance(self):
        return self.__chance

    @chance.setter
    def chance(self, nova_chance: float):
        self.__chance = nova_chance

    @property
    def em_campo(self):
        return self.__em_campo

    @em_campo.setter
    def em_campo(self, novo_em_campo: bool):
        self.__em_campo = novo_em_campo
