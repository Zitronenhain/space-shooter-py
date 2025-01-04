import pygame
from random import randint
from os.path import join

#SETUP:
pygame.init()
pygame.display.set_caption('Space Shoot Py')
WINDOW_WIDTH, WINDOW_HEIGHT = 240.0, 240.0
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()


running = True
borders = pygame.FRect(10.0, 10.0,(WINDOW_WIDTH - 20.0), (WINDOW_HEIGHT - 20.0))

#SURFACES:

##STARS:
star_surface = pygame.image.load(join('materials','images','star.png')).convert_alpha()
star_height, star_width = star_surface.get_height(), star_surface.get_width()
star_positions = [(randint(0, (int(WINDOW_WIDTH) - star_width)), randint(0, (int(WINDOW_HEIGHT) - star_height))) for i in range(20)]

##PLAYER:
player_surface = pygame.image.load(join('materials','images','player.png')).convert_alpha()
player_frect = player_surface.get_frect( center = (WINDOW_WIDTH / 2.0, WINDOW_HEIGHT / 2.0))
player_movement = pygame.math.Vector2(0.0, 0.0)
player_speed = 128.0

##ASTEROIDS
asteroid_surface = pygame.image.load(join('materials','images','asteroid.png')).convert_alpha()
asteroid_frect = asteroid_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 8))
asteroid_movement = pygame.math.Vector2(0.8,-0.6)
asteroid_speed = 128.0

laser_surface = pygame.image.load(join('materials','images','laser.png')).convert_alpha()
laser_frect = laser_surface.get_frect(center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 6))

while running:
    #SET_FPS:
    delta_time = clock.tick() / 1000
    #print(clock.get_fps())

    #EVENT_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #MOVEMENT:
    keys = pygame.key.get_pressed()

    player_movement.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_movement.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    # fixing speed boost by going diagonal with vector normalization, but check if it is not zero:
    player_movement = player_movement.normalize() if player_movement else player_movement

    player_frect.center += player_movement * player_speed * delta_time

    #DRAWING:
    display_surface.fill('gray11')
    for star_position in star_positions:
        display_surface.blit(star_surface, star_position)

    #DRAW_ENEMY:
    display_surface.blit(asteroid_surface, asteroid_frect)

    asteroid_frect.center += asteroid_movement * asteroid_speed * delta_time

    if asteroid_frect.right > borders.right or asteroid_frect.left < borders.left:
        asteroid_movement[0] = -asteroid_movement[0]

    if asteroid_frect.bottom > borders.bottom or asteroid_frect.top < borders.top:
        asteroid_movement[1] = -asteroid_movement[1]

    #DRAW_PLAYER:
    display_surface.blit(laser_surface, laser_frect)
    display_surface.blit(player_surface, player_frect)

    pygame.display.update()

pygame.quit()