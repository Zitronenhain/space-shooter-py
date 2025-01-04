import pygame
from random import randint
from os.path import join

#SETUP:
pygame.init()
pygame.display.set_caption('Space Shoot Py')
WINDOW_WIDTH, WINDOW_HEIGHT = 240, 240
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

#SURFACES:
##PLAYER:
player_surface = pygame.image.load(join('materials','images','player.png')).convert_alpha()
player_rect = player_surface.get_frect( center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
#STARS:
star_surface = pygame.image.load(join('materials','images','star.png')).convert_alpha()
star_height,star_width = star_surface.get_height(),star_surface.get_width()
star_positions = [(randint(0, (WINDOW_WIDTH - star_width)), randint(0, (WINDOW_HEIGHT - star_height))) for i in range(20)]


x = 100
y = 100

while(running):
    #EVENT_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #DRAWING:
    display_surface.fill('gray11')
    for position in star_positions:
        display_surface.blit(star_surface, position)
    player_rect.left+=0.1

    display_surface.blit(player_surface, player_rect)
    pygame.display.update()

pygame.quit()