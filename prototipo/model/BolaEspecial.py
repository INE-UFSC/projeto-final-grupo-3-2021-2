
from model.Bola import Bola
from abc import ABC, abstractmethod


class BolaEspecial(Bola, ABC):
    def __init__(self, circle_obj, raio: float, em_campo: bool):
        super().__init__(raio, circle_obj)
        self.__em_campo = em_campo

    @property
    def em_campo(self):
        return self.__em_campo

    @em_campo.setter
    def em_campo(self, novo_em_campo: bool):
        self.__em_campo = novo_em_campo

    " Cada bola especial implementa a sua ação com esse método, para haver polimorfismo "
    @abstractmethod
    def acao(self):
        pass
