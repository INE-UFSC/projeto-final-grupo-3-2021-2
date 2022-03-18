from abc import ABC, abstractclassmethod


class Menu(ABC):
    def __init__(self, tela_width: int, tela_height: int) -> None:
        self.__tela_width = tela_width
        self.__tela_height = tela_height

    @abstractclassmethod
    def voltar():
        pass

    @abstractclassmethod
    def desenhar_menu():
        pass

    @property
    def tela_width(self):
        return self.__tela_width

    @property
    def tela_height(self):
        return self.__tela_height

    @tela_width.setter
    def tela_width(self, width):
        self.__tela_width = width

    @tela_height.setter
    def tela_height(self, height):
        self.__tela_height = height
