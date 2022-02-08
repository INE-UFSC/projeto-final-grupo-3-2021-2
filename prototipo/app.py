import sys
sys.path.append("/Users/Windows/Documents/GitHub/projeto-final-grupo-3-2021-2")
import prototipo.controller.controladorClassico as cont
import pygame

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

def main():
    
    pygame.init()
    c = cont.ControladorClassico(width, height, whatever)
    c.rodar_jogo()
    pygame.display.update()
    
    while c.checar_fim_de_jogo() == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


main()
