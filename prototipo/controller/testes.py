from controladorClassico import ControladorClassico
import pygame

width = 1000
height = 600
whatever = {}

def main():
    
    pygame.init()
    c = ControladorClassico(width, height, whatever)
    c.rodar_jogo()
    pygame.display.update()
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


main()
