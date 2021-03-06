
from model.Bola import Bola
from abc import ABC, abstractmethod


class BolaEspecial(Bola, ABC):
    # Interface agora pede apenas em_campo e o circle_obj, tamanho (raio) fixo para todas as bolas especiais
    def __init__(self, nome: str, circle_obj, em_campo: bool, raio=35):
        super().__init__(nome, raio, circle_obj)
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
