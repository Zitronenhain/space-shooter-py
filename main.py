import pygame
from random import randint
from os.path import join

#SETUP:
pygame.init()
pygame.display.set_caption('Space Shoot Py')
WINDOW_WIDTH, WINDOW_HEIGHT = 240.0, 240.0
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True
#Rect FRect(left, top, width, height)
borders = pygame.FRect(10.0, 10.0,(WINDOW_WIDTH - 20.0), (WINDOW_HEIGHT - 20.0))
speed = (0.2, 0.2)

#SURFACES:

##STARS:
star_surface = pygame.image.load(join('materials','images','star.png')).convert_alpha()
star_height, star_width = star_surface.get_height(), star_surface.get_width()
star_positions = [(randint(0, (int(WINDOW_WIDTH) - star_width)), randint(0, (int(WINDOW_HEIGHT) - star_height))) for i in range(20)]

##PLAYER:
player_surface = pygame.image.load(join('materials','images','player.png')).convert_alpha()
player_frect = player_surface.get_frect( center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

##ASTEROIDS
asteroid_surface = pygame.image.load(join('materials','images','asteroid.png')).convert_alpha()
asteroid_frect = asteroid_surface.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 8))

laser_surface = pygame.image.load(join('materials','images','laser.png')).convert_alpha()

while running:
    #EVENT_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #DRAWING:
    display_surface.fill('gray11')
    for star_position in star_positions:
        display_surface.blit(star_surface, star_position)

        display_surface.blit(asteroid_surface, asteroid_frect)

        player_frect.move(0.2,0.2)

        #if  player_frect.left <= borders.left or player_frect.right > borders.right:
        #    speed[0] = -speed[0]
        #if player_frect.top <= borders.top or player_frect.bottom > borders.bottom:
        #    speed[1] = -speed[1]

        display_surface.blit(player_surface, player_frect)

    #pygame.draw.rect(display_surface, (255,0,0), borders)

    pygame.display.update()

pygame.quit()