from abc import ABC, abstractclassmethod


class Menu(ABC):
    def __init__(self, pygame, tela_width: int, tela_height: int) -> None:
        self.__pygame = pygame
        self.__tela_width = tela_width
        self.__tela_height = tela_height

    @abstractclassmethod
    def voltar():
        pass

    @abstractclassmethod
    def desenhar_menu():
        pass

    @property
    def pygame(self):
        return self.__pygame

    @property
    def tela_width(self):
        return self.__tela_width

    @property
    def tela_height(self):
        return self.__tela_height
