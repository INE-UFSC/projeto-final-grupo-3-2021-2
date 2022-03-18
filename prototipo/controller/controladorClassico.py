import pygame
from controller.controladorJogo import ControladorJogo as CJ
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


class ControladorClassico(CJ):
    def __init__(self, tela_width: int, tela_height: int) -> None:
        super().__init__(tela_width, tela_height)
        
    def checkModoDeJogo(self):
        return 'classic'
        
    def checar_fim_de_jogo(self):
        fim_de_jogo = False
        if (super().campo.verificaCampo(super().campo.campo) == False):
            fim_de_jogo = True
            
        return fim_de_jogo
