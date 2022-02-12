
import app as App
from view.leaderboard import LeaderBoard
from view.menuPrincipal import MenuPrincipal
from view.menuModosDeJogo import menu_modos_de_jogo

import pygame
pygame.init()
MenuPrincipal =  MenuPrincipal(1000, 600)
rank = LeaderBoard(1000, 600, ['Jônata','Mateus','Thiago','José', 'Kalleo','Bernardo','','','',''])
mdj = menu_modos_de_jogo(1000, 600)
state = 'start'
pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('/home/jose/Documents/POO2/projeto-final-grupo-3-2021-2/prototipo/controller/sounds/musica_menus.mp3')
pygame.mixer.music.play(-1)
musica = True
som = True
while True:

    if state == 'start':
        state, musica, som = MenuPrincipal.desenhar_menu(musica, som)

    elif state == 'rank':
        state, musica, som = rank.desenhar_menu(musica, som)

    elif state == 'mdj':
        state, musica, som = mdj.desenhar_menu(musica, som)

    elif state == 'classic':
        '''Só falta fazer o vínculo com o jogo por aqui'''
        App.main()
        '''state, musica, som = main()'''