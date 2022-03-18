import pygame
import PySimpleGUI as sg

from view.LeaderboardDAO import LeaderboardDAO


class Placar:
    def __init__(self, tela, width, height, cor_de_fundo):
        self.__tela = tela
        self.__width = width
        self.__height = height
        self.__cor_de_fundo = cor_de_fundo
        self.__score = 0
        self.__leaderboardDAO = LeaderboardDAO()

    def pontuar(self, pontos):
        self.__score += pontos

    @property
    def score(self):
        return self.__score

    def desenha_placar(self):
        fundo_placar = pygame.draw.rect(
            self.__tela, self.__cor_de_fundo, (20, 20, 250, 40))
        fonte_placar = pygame.font.SysFont('arial', 30, True, True)
        legenda_placar = fonte_placar.render(
            f'PONTOS: {self.__score}', 1, (255, 255,255))
        self.__tela.blit(legenda_placar, (20, 20))

    def desenhar_input(self, pontos):
        sg.theme('DarkPurple1')
        layout = [[sg.Text(f'Pontuação alcançada: {pontos}')], [sg.Text(
            'Qual seu nome de campeão?'), sg.InputText()], [sg.Submit('Entrar para história!')]]
        window = sg.Window('GAMEOVER').Layout(layout)
        botao, nome = window.Read()
        window.close()
        return nome[0]

    @property
    def leaderboardDAO(self):
        return self.__leaderboardDAO
