import model.campo as campo
import model.Bola as bola
from model.geraBola import GeraBola
from abc import ABC
import pygame
import sys
import os
from model.BolaBranca import BolaBranca
from view.Placar import Placar
from model.BolaEspecial import BolaEspecial
from model.BolaMais import BolaMais
from model.BolaMenos import BolaMenos
from model.BolaMateriaNegra import BolaMateriaNegra
from controller.controladorJogo import ControladorJogo as CJ
from view.Timer import Timer
sys.path.append(
    os.path.dirname(os.path.realpath(__file__)))

clock = pygame.time.Clock()


class ControladorTimeAttack(CJ):
    def __init__(self, tela_width: int, tela_height: int) -> None:
        super().__init__(tela_width, tela_height)

    def checkModoDeJogo(self):
        return 'timeattack'

    def checar_fim_de_jogo(self):
        fim_de_jogo = False
        if (super().campo.verificaCampo(super().campo.campo) == False) or super().timer.over:
            fim_de_jogo = True

        return fim_de_jogo
