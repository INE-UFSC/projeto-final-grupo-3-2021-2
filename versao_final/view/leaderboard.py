import pygame
from view.menu import Menu
from view.LeaderboardDAO import LeaderboardDAO
import os


class LeaderBoard(Menu):
    def __init__(self, tela_width, tela_height):
        super().__init__(tela_width, tela_height)
        self.__tela = pygame.display.set_mode((tela_width, tela_height))
        self.__background = pygame.Surface(self.__tela.get_size())
        self.__dimensoes = [tela_width, tela_height]
        self.__leaderboardDAO = LeaderboardDAO()
        self.__rank = []

        dados = self.__leaderboardDAO.get_all()
        for i in sorted(dados, key=dados.get, reverse=True):
            self.__rank.append((i, dados[i]))

    def desenhar_menu(self, musica, som):
        pygame.init()
        barulho_opc = pygame.mixer.Sound(os.path.join(
            'controller', 'sounds', 'sound_option.wav'))
        click = False
        if musica:
            cor_musica = (0, 255, 0)
            pygame.mixer.music.set_volume(0.5)
        else:
            cor_musica = (255, 0, 0)
            pygame.mixer.music.set_volume(0)

        if som:
            cor_som = (0, 255, 0)
            barulho_opc.set_volume(4)
        else:
            cor_som = (255, 0, 0)
            barulho_opc.set_volume(0)

        borda_volta = 3
        while True:

            width = self.__dimensoes[0]
            height = self.__dimensoes[1]

            mx, my = pygame.mouse.get_pos()
            display = pygame.display
            display.set_caption('ATOMIKO')

            self.__background = self.__background.convert()
            self.__background.fill((250, 250, 250))

            # CHECAGEM DE EVENTO
            for event in pygame.event.get():
                if event.type == 256:
                    pygame.quit()
                    exit()
                if event.type == 1025:
                    click = True
                if event.type == 1026:
                    click = False

            fonte_titulo = pygame.font.SysFont('arial', 55, True, True)
            titulo = fonte_titulo.render("ATOMIKO", 1, (10, 10, 10))
            titulo_pos = titulo.get_rect()
            titulo_pos.centerx = self.__background.get_rect().centerx

            self.__background.blit(titulo, titulo_pos)

            vertice1 = (width/6 - 20, height/8 + 10)
            vertice2 = (width/6 - 20, height/8 + 47)
            vertice3 = (width/6 - 55, height/8 + 29)

            fonte_leader = pygame.font.SysFont('arial', 25, True, True)
            opc_volta = pygame.draw.polygon(
                self.__background, (0, 0, 0), (vertice1, vertice2, vertice3), borda_volta)
            legenda_rank_titulo = fonte_leader.render(
                'LEADERBOARD', 1, (0, 0, 0))
            self.__background.blit(legenda_rank_titulo,
                                   (width / 4 + 19, height / 8 + 15))

            fonte_musica = pygame.font.SysFont('arial', 20, True, True)
            legenda_musica = fonte_musica.render('MUSIC', 1, cor_musica)

            opc_musica = pygame.draw.rect(
                self.__background, (255, 255, 255), (10, height - 26, 65, 15))
            self.__background.blit(legenda_musica, (10, height - 30))

            fonte_som = pygame.font.SysFont('arial', 20, True, True)
            legenda_som = fonte_som.render('SOUND', 1, cor_som)

            opc_som = pygame.draw.rect(
                self.__background, (255, 255, 255), (92, height - 26, 70, 15))
            self.__background.blit(legenda_som, (90, height - 30))

            self.__tela.blit(self.__background, (0, 0))
            if opc_som.collidepoint((mx, my)):
                if click:
                    click = False
                    if som:
                        cor_som = (255, 0, 0)
                        barulho_opc.set_volume(0)
                        som = False
                    else:
                        cor_som = (0, 255, 0)
                        barulho_opc.set_volume(4)
                        som = True
            if opc_musica.collidepoint((mx, my)):
                if click:
                    click = False
                    if musica:
                        cor_musica = (255, 0, 0)
                        pygame.mixer.music.set_volume(0)
                        musica = False
                    else:
                        pygame.mixer.music.set_volume(0.5)
                        cor_musica = (0, 255, 0)
                        musica = True
            # Desenhando rank
            tamanho = len(self.__rank)
            if tamanho > 10:
                tamanho = 10
            for i in range(1, tamanho + 1):
                if i == 1:
                    cor_rank = (255, 215, 0)
                    fonte_size = 26
                    fonte_rank = pygame.font.SysFont(
                        'arial', fonte_size, True, True)
                    lista_rank = fonte_rank.render(
                        f'{i} - {self.__rank[i-1][0]}.....{self.__rank[i-1][1]}', 1, cor_rank)
                    pos_x = (width / 4) + 20
                    pos_y = (height / 6) + 50

                else:
                    pos_y = pos_y + 35
                    cor_rank = (0, 0, 0)
                    fonte_size = 20
                    if i == 2:
                        fonte_size = 24
                        cor_rank = (192, 192, 192)
                    elif i == 3:
                        fonte_size = 22
                        cor_rank = (205, 127, 50)
                    fonte_rank = pygame.font.SysFont(
                        'arial', fonte_size, True, True)
                    lista_rank = fonte_rank.render(
                        f'{i} - {self.__rank[i-1][0]}.....{self.__rank[i-1][1]}', 1, cor_rank)

                self.__background.blit(lista_rank, (pos_x, pos_y))

            if opc_volta.collidepoint((mx, my)):
                borda_volta = 0
                if click:
                    barulho_opc.play()
                    return self.voltar(musica, som)
            else:
                borda_volta = 3
            self.__tela.blit(self.__background, (0, 0))
            pygame.display.update()

    def voltar(self, musica, som):

        return 'start', musica, som

    @property
    def tela(self):
        return self.__tela

    @property
    def background(self):
        return self.__background
