from menuPrincipal import MenuPrincipal


class ControladorMenu():
    def __init__(self, pygame, tela_width, tela_height) -> None:
        self.__pygame = pygame
        self.__menus = {}
        self.__tela_width = tela_width
        self.__tela_height = tela_height

    def inicializar_menus(self):
        self.__menus["MenuPrincipal"] = MenuPrincipal(
            self.__pygame, self.__tela_width, self.__tela_height)

    @property
    def pygame(self):
        return self.__pygame

    @property
    def tela_width(self):
        return self.__tela_width

    @property
    def tela_height(self):
        return self.__tela_height
