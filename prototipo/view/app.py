from view.leaderboard import LeaderBoard
from view.menuPrincipal import MenuPrincipal
from view.menuModosDeJogo import menu_modos_de_jogo
from controller.controladorClassico import ControladorClassico as cont
import os
import pygame


class Singleton(object):
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance


class App(Singleton):
    def __init__(self) -> None:
        pygame.init()

        self.__state = 'start'
        self.__musica_de_fundo = pygame.mixer.music.load(
            os.path.join('controller', 'sounds', 'musica_menus.mp3'))
        self.__musica = True
        self.__som = True

        pygame.mixer.music.play(-1)

    def iniciar(self):
        while True:

            if self.__state == 'start':
                Menu_Principal = MenuPrincipal(480, 510)
                self.__state, self.__musica, self.__som = Menu_Principal.desenhar_menu(
                    self.__musica, self.__som)

            elif self.__state == 'rank':
                rank = LeaderBoard(480, 510)
                self.__state, self.__musica, self.__som = rank.desenhar_menu(
                    self.__musica, self.__som)

            elif self.__state == 'mdj':
                mdj = menu_modos_de_jogo(480, 510)
                self.__state, self.__musica, self.__som = mdj.desenhar_menu(
                    self.__musica, self.__som)

            elif self.__state == 'classic':
                pygame.mixer.music.set_volume(0)
                controlador = cont(1000, 600)
                self.__state = controlador.rodar_jogo()
                pygame.mixer.init()
                pygame.mixer.music.set_volume(0)
                self.__musica_de_fundo = pygame.mixer.music.load(
                    os.path.join('controller', 'sounds', 'musica_menus.mp3'))
                pygame.mixer.music.play(-1)
