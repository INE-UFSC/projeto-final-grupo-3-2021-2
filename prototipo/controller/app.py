import pygame
from controller.controladorClassico import ControladorClassico as cont

width = 1000
height = 600
whatever = {}

elem_dict = {
    1: "H",
    2: "He",
    3: "Li",
    4: "Be",
    5: "B",
    6: "C",
    7: "N",
    8: "O",
    9: "F",
    10: "Ne",
    11: "Na",
    12: "Mg"
}

class App:

    def main():

        pygame.init()
        c = cont(width, height, whatever)
        c.rodar_jogo()


