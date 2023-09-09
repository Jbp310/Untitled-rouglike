# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
from sys import exit
#if you want to change the icon
#pygame.display.set_icon()
pygame.display.set_caption('Untitled rougelike V 0.1')
pygame.init()
screen = pygame.display.set_mode((800,400))
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

