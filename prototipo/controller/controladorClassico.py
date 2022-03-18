import pygame
from .controladorJogo import ControladorJogo
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


class ControladorClassico(ControladorJogo):
    def __init__(self, tela_width: int, tela_height: int) -> None:
        super().__init__(tela_width, tela_height)
        
        
    def checar_fim_de_jogo(self):
        fim_de_jogo = False
        if super().campo.capacidade == len(super().campo.campo):
            fim_de_jogo = True
            
        return fim_de_jogo
