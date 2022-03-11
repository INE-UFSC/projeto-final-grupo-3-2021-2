from model.Bola import Bola


class BolaNormal(Bola):
    def __init__(self, valor: int, nome: str, circle_obj, raio=35):
        super().__init__(nome, raio, circle_obj)
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor: str):
        self.__valor = novo_valor
