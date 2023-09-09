
import pygame
from sys import exit
# if you want to change the icon
# pygame.display.set_icon()
pygame.display.set_caption('Untitled rougelike V 0.1')
pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
background_surf = pygame.image.load('background.png').convert()
Ground_surf = pygame.image.load('ground.png').convert()
player = pygame.image.load('player-1.png.png').convert_alpha()
player_surf = pygame.transform.scale(player,(75,100.5))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background_surf,(0,0))
    screen.blit(Ground_surf,(0,300))
    screen.blit(player_surf, (0,200))
    clock.tick(60)
    pygame.display.update()
