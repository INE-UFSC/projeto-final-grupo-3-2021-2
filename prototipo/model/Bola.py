from abc import ABC


class Bola(ABC):

    def __init__(self, cor: str, raio: float):
        self.__cor = cor
        self.__raio = raio

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, nova_cor: str):
        self.__cor = nova_cor

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, novo_raio: str):
        self.__raio = novo_raio