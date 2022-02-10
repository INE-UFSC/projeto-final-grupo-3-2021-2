import sys
sys.path.append("C:/Users/kalle/Documents/projeto_final_gp3/prototipo/projeto-final-grupo-3-2021-2-main")
from controller.controladorClassico import ControladorClassico as cont
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
    c = cont(width, height, whatever)
    c.rodar_jogo()


main()
