from menu import Menu
import pygame


class MenuPrincipal(Menu):
    def __init__(self, tela_width, tela_height):
        super().__init__(tela_width, tela_height)
        self.__tela = pygame.display.set_mode((tela_width, tela_height))
        self.__background = pygame.Surface(self.__tela.get_size())

    def desenhar_menu(self):
        display = pygame.display
        display.set_caption('ATOMIKO')

        self.__background = self.__background.convert()
        self.__background.fill((250, 250, 250))

        fonte = pygame.font.Font(None, 36)
        titulo = fonte.render("ATOMIKO", 1, (10, 10, 10))
        titulo_pos = titulo.get_rect()
        titulo_pos.centerx = self.__background.get_rect().centerx
        self.__background.blit(titulo, titulo_pos)

        self.__tela.blit(self.__background, (0, 0))

    def voltar(self):
        pass

    @property
    def tela(self):
        return self.__tela

    @property
    def background(self):
        return self.__background
