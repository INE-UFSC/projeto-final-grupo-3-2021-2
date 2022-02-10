from Bola import Bola


class BolaNormal(Bola):
    def __init__(self, valor: int, nome: str, circle_obj, raio = 35):
        super().__init__(raio, circle_obj)
        self.__valor = valor
        self.__nome = nome

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor: str):
        self.__valor = novo_valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome
