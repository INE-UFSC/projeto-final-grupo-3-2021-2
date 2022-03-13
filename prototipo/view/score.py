import pygame


class Placar:
    def __init__(self, tela, width, height):
        self.__tela = tela
        self.__width = width
        self.__height = height
        self.__score = 0

    def pontuar(self, pontos):
        self.__score += pontos

    @property
    def score(self):
        return self.__score

    def desenha_placar(self):
        fundo_placar = pygame.draw.rect(
            self.__tela, (255, 255, 255), (20, 20, 250, 40))
        fonte_placar = pygame.font.SysFont('arial', 30, True, True)
        legenda_placar = fonte_placar.render(
            f'PONTOS: {self.__score}', 1, (0, 0, 0))
        self.__tela.blit(legenda_placar, (20, 20))
