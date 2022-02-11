from leaderboard import LeaderBoard
from MenuPrincipal import MenuPrincipal
from menuModosDeJogo import menu_modos_de_jogo
import pygame
pygame.init()
MenuPrincipal =  MenuPrincipal(480, 510)
rank = LeaderBoard(480, 510, ['Jônata','Mateus','Thiago','José', 'Kalleo','Bernardo','','','',''])
mdj = menu_modos_de_jogo(480, 510)
state = 'start'
pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('sounds\musica_menus.mp3')
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
        state, musica, som
