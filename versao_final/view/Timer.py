import pygame
import time
from _thread import *
import math
class Timer:
    def __init__(self, surface, cor_de_fundo):
        self.__cor_fundo = (255, 255, 255)
        self.__size = [0, 0]
        self.__x = 574
        self.__y = 0  
        self.__clock_values = ['00', '00', '10']
        self.__surface = surface
        self.__font = pygame.font.SysFont('Arial', 85)
        self.__change = True
        self.__tempo_somado = 0
        self.__over = False
        self.__cor_fundo = cor_de_fundo
        self.__cor_do_timer = (255, 255, 255)
    
    
    def timerOver(self):
        self.__over = True
        
    def timer(self, start_time, t):

        while int(time.time()-start_time) != t:
            self.__clock_values[0], self.__clock_values[1], self.__clock_values[2] = self.atod(t - int(time.time()-start_time))
        else:
            if self.__tempo_somado == 0:
                self.timerOver()
            else:
                self.atualiza_tempo(self.__tempo_somado) 
                self.__tempo_somado = 0
                self.__change = True
    def text_renderer(self, msg, font, rect):

        text = font.render(msg, True, self.__cor_do_timer)

        self.__surface.blit(text, rect)
        
        
    def dtoa(self, clock_values):
        time_in_sec = int(clock_values[0])*3600 + int(clock_values[1])*60 + int(clock_values[2])

        return time_in_sec


    def atod(self, time_in_sec):
        sec = '0'+str(time_in_sec%60)
        sec = sec[len(sec)-2:]
        minutes = time_in_sec//60
        minute = '0' + str(minutes%60)
        minute = minute[len(minute)-2:]
        hour = '0' + str(minutes//60)
        hour = hour[len(hour)-2:]

        return hour, minute, sec
    
    def desenhar_timer(self):
        if self.__change:
            start_new_thread(self.timer, (time.time(), self.dtoa(self.__clock_values)))
            self.aumentar_tempo(0)
            self.__change = False
        fundo_timer = pygame.draw.rect(
            self.__surface, self.__cor_fundo, (733, 20, 250, 70))    
        for i in range(1,3):
            self.text_renderer(self.__clock_values[i][0], self.__font, pygame.Rect(self.__x+(i*150)+8, self.__y+5, self.__size[0], self.__size[1]))
            self.text_renderer(self.__clock_values[i][1], self.__font, pygame.Rect(self.__x+55+(i*150)+8, self.__y+5, self.__size[0], self.__size[1]))
                    
        for i in range(1,2):
            pygame.draw.rect(self.__surface, self.__cor_do_timer, (self.__x+132+(i*150), self.__y+30, 10, 10))
            pygame.draw.rect(self.__surface, self.__cor_do_timer, (self.__x+132+(i*150), self.__y+60, 10, 10))
            
    def aumentar_tempo(self, tempo):
        self.__tempo_somado += tempo
        self.desenha_tempo_somado(self.__tempo_somado)
        
    def desenha_tempo_somado(self, tempo):
        
        fonte_ts = pygame.font.SysFont('arial', 23, True, True)
        legenda_ts_titulo = fonte_ts.render(
            f'TEMPO ACUMULADO(s)', 1, (255, 255,255))
        
        
        fundo_ts_valor = pygame.draw.rect(
            self.__surface, self.__cor_fundo, (780, 110, 250, 60))
        fonte_ts_valor = pygame.font.SysFont('arial', 50, True, True)
        legenda_ts_valor = fonte_ts_valor.render(
            f'{tempo}', 1, (255, 255,255))
        self.__surface.blit(legenda_ts_titulo, (731, 90))
        self.__surface.blit(legenda_ts_valor, (830, 110))
        
    def atualiza_tempo(self, tempo):
        minutos = int(self.__clock_values[1])
        segundos = int(self.__clock_values[2])
        if segundos + tempo > 60:
            
            if minutos + 1 > 60 :
                minutos = 60
            minutos = math.floor((segundos + tempo)/60)
            segundos = (segundos + tempo) % 60
        else:
            segundos += tempo
        
        if minutos < 10:
            minutos = '0'+str(minutos)
        else:
            minutos = str(minutos)
            
        if segundos < 10:
            segundos = '0'+str(segundos)
        else:
            segundos = str(segundos)

        self.__clock_values = ['00', minutos, segundos]
        

    @property
    def over(self):
        return self.__over
    
    @over.setter
    def over(self, over):
        self.__over = over