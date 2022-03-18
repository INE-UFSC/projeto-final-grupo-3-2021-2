import sys
import os
from controller.controladorJogo import ControladorJogo as CJ
sys.path.append(
    os.path.dirname(os.path.realpath(__file__)))


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
