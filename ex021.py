"""
Exercício Python 21:
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

"""

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
pygame.quit()
