
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

