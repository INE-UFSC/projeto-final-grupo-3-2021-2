from turtle import width
from controladorJogo import ControladorJogo
import pygame

width = 1000
height = 600
whatever = {}

pygame.init()
c = ControladorJogo(width, height, whatever)
c.rodar_jogo()


def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()


main()
