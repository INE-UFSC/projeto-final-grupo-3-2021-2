import sys
sys.path.append("/home/jose/Documents/POO2/projeto-final-grupo-3-2021-2")
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
class Textos():
    def __init__(self, val):
        self.__val = val

    def printMyText():
        print("My Text")
def main():
    
    pygame.init()
    c = cont(width, height, whatever)
    c.rodar_jogo()


# main()
