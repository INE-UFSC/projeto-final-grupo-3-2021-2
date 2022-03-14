from ntpath import realpath
import pygame
from os.path import dirname, realpath
import os
import PySimpleGUI as sg
import json


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
            self.__tela, (250, 250, 250), (20, 20, 250, 40))
        fonte_placar = pygame.font.SysFont('arial', 30, True, True)
        legenda_placar = fonte_placar.render(
            f'PONTOS: {self.__score}', 1, (0, 0, 0))
        self.__tela.blit(legenda_placar, (20, 20))
        
class Rank:
    def __init__(self):
        self.__path = f'{dirname(realpath(__file__))}/rank.json'
        if os.path.exists(self.__path):
            with open (self.__path, 'r') as f:
                self.__memoria = json.load(f)
        else:
            self.__memoria = {}
                
    def escrever(self, valor, nome):
        self.__memoria[nome] = int(valor)
        with open(self.__path, 'w') as f:
            json.dump(self.__memoria, f)
    
    def clean(self):
        self.__memoria = {}
        with open(self.__path, 'w') as f:
            json.dump(self.__memoria, f)
            
    def carregar(self):
        with open (self.__path, 'r') as f:
                self.__memoria = json.load(f)
        return self.__memoria

    def desenhar_input(self, pontos):
        layout =[[sg.Text(f'Pontuação alcançada: {pontos}')],[sg.Text('Qual seu nome de campeão?'), sg.InputText()],[sg.Submit('Entrar para história!')]]
        window = sg.Window('GAMEOVER').Layout(layout)
        botao, nome = window.Read()
        return nome[0]