import pygame
from Ball import Ball
from Brick import Brick
from Wall import Wall

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ball = Ball(screen)
brick = Brick(screen, (100, 100))
wall = Wall(brick)


while running:
    #poll for events
    #pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # wipe anything from last frame
    screen.fill((0, 0, 0))
    #RENDER GAME HERE
    ball.update(screen)
    brick.update(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()