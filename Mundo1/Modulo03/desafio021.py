#Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3
import pygame

pygame.mixer.init()
pygame.mixer.music.load('testemp3')
pygame.mixer.music.play()

