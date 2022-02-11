from menu import Menu
import pygame


class MenuPrincipal(Menu):
    def __init__(self, tela_width, tela_height):
        super().__init__(tela_width, tela_height)
        self.__tela = pygame.display.set_mode((tela_width, tela_height))
        self.__background = pygame.Surface(self.__tela.get_size())
        self.__dimensoes = [tela_width, tela_height]

    def desenhar_menu(self, musica, som):
        pygame.init()
        barulho_opc = pygame.mixer.Sound('sounds\sound_option.wav')
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

        cor_fundo_rank = (148, 0, 211)
        cor_fundo_mdj = (148, 0, 211)
        while True:

            width = self.__dimensoes[0]
            height =  self.__dimensoes[1]

            mx, my  = pygame.mouse.get_pos()
            display = pygame.display
            display.set_caption('ATOMIKO')

            self.__background = self.__background.convert()
            self.__background.fill((250, 250, 250))


            #CHECAGEM DE EVENTO
            for event in pygame.event.get():
                if event.type == 256:
                    pygame.quit()
                    exit()
                if event.type == 1025:
                    click = True
                if event.type == 1026:
                    click = False

            fonte_titulo = pygame.font.SysFont('arial', 55, True,True)
            titulo = fonte_titulo.render("ATOMIKO", 1, (10, 10, 10))
            titulo_pos = titulo.get_rect()
            titulo_pos.centerx = self.__background.get_rect().centerx

            self.__background.blit(titulo, titulo_pos)
            fonte_opcoes = pygame.font.SysFont('arial',25,True,True)


            opc_mdj = pygame.draw.rect(self.__background, cor_fundo_mdj, (width/4, height/3, width/2, height/(15/2)))
            legenda_mdj = fonte_opcoes.render('MODOS DE JOGO',1,(255, 255, 255))
            self.__background.blit(legenda_mdj,(width/4 + 12 , height/3 + 18))

            opc_rank = pygame.draw.rect(self.__background, cor_fundo_rank, (width/4, 2*(height/3), width/2, height/(15/2)))
            legenda_rank = fonte_opcoes.render('RANKING',1,(255, 255, 255))

            self.__background.blit(legenda_rank, (width/4 + 60, 2*(height/3)+ 18))

            fonte_musica = pygame.font.SysFont('arial', 20, True, True)
            legenda_musica = fonte_musica.render('MUSIC', 1, cor_musica)

            opc_musica = pygame.draw.rect(self.__background,(255,255,255),(10, height - 26, 65, 15))
            self.__background.blit(legenda_musica, (10, height - 30))

            fonte_som = pygame.font.SysFont('arial', 20, True, True)
            legenda_som = fonte_som.render('SOUND', 1, cor_som)

            opc_som = pygame.draw.rect(self.__background, (255, 255, 255), (92, height - 26, 70, 15))
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
                        musica =  False
                    else:
                        pygame.mixer.music.set_volume(0.5)
                        cor_musica = (0, 255, 0)
                        musica = True

            if opc_mdj.collidepoint((mx, my)):
                cor_fundo_mdj = (153, 102, 204)

                if click:
                    barulho_opc.play()
                    return 'mdj', musica, som
            else:
                cor_fundo_mdj = (148, 0, 211)

            if opc_rank.collidepoint((mx, my)):
                cor_fundo_rank = (153, 102, 204)

                if click:
                    barulho_opc.play()
                    return 'rank', musica, som
            else:
                cor_fundo_rank = (148, 0, 211)


            pygame.display.update()
    def voltar(self):
        pass

    @property
    def tela(self):
        return self.__tela

    @property
    def background(self):
        return self.__background
