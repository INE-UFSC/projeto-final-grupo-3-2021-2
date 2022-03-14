from view.leaderboard import LeaderBoard
from view.menuPrincipal import MenuPrincipal
from view.menuModosDeJogo import menu_modos_de_jogo
from controller.controladorClassico import ControladorClassico as cont
import os
import pygame
pygame.init()

state = 'start'
pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load(
    os.path.join('controller', 'sounds', 'musica_menus.mp3'))
pygame.mixer.music.play(-1)
musica = True
som = True
while True:

    if state == 'start':
        Menu_Principal = MenuPrincipal(480, 510)
        state, musica, som = Menu_Principal.desenhar_menu(musica, som)

    elif state == 'rank':
        rank = LeaderBoard(480, 510)
        state, musica, som = rank.desenhar_menu(musica, som)

    elif state == 'mdj':
        mdj = menu_modos_de_jogo(480, 510)
        state, musica, som = mdj.desenhar_menu(musica, som)

    elif state == 'classic':
        pygame.mixer.music.set_volume(0)
        controlador = cont(1000, 600)
        controlador.rodar_jogo()
