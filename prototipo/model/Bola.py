from abc import ABC

class Bola(ABC):

    def __init__(self, raio: float, circle):
        self.__raio = raio
        self.__circle_obj = circle

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, novo_raio: str):
        self.__raio = novo_raio
        
    @property
    def circle_obj(self):
        return self.__circle_obj

    @circle_obj.setter
    def circle_obj(self, novo_circle_obj: str):
        self.__circle_obj = novo_circle_obj