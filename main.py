import pygame
from random import randint
from os.path import join

#SETUP:
pygame.init()
pygame.display.set_caption('Space Shoot Py')
WINDOW_WIDTH, WINDOW_HEIGHT = 240.0, 240.0
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True
speed = 0.1
borders = pygame.FRect(10.0, 10.0,(WINDOW_WIDTH - 20.0), (WINDOW_HEIGHT - 20.0))

#SURFACES:

##STARS:
star_surface = pygame.image.load(join('materials','images','star.png')).convert_alpha()
star_height, star_width = star_surface.get_height(), star_surface.get_width()
star_positions = [(randint(0, (int(WINDOW_WIDTH) - star_width)), randint(0, (int(WINDOW_HEIGHT) - star_height))) for i in range(20)]

##PLAYER:
player_surface = pygame.image.load(join('materials','images','player.png')).convert_alpha()
player_frect = player_surface.get_frect( center = (WINDOW_WIDTH / 2.0, WINDOW_HEIGHT / 2.0))
player_movement = 1.0

##ASTEROIDS
asteroid_surface = pygame.image.load(join('materials','images','asteroid.png')).convert_alpha()
asteroid_frect = asteroid_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 8))

laser_surface = pygame.image.load(join('materials','images','laser.png')).convert_alpha()
laser_frect = laser_surface.get_frect(center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 6))

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

    display_surface.blit(laser_surface, laser_frect)

    #DRAW_PLAYER:
    player_frect.x += player_movement * speed
    player_frect.y += -player_movement * speed

    if player_frect.right > borders.right or player_frect.left < borders.left:
        player_movement *= -1
    if player_frect.bottom > borders.bottom or player_frect.top < borders.top:
        player_movement *= -1
    display_surface.blit(player_surface, player_frect)

    pygame.display.update()

pygame.quit()