import pygame
from collision import collision, boundary_collision
from Ball import Ball
from Brick import Brick
from Wall import Wall
from Boundary import Boundary

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ball = Ball(screen)
wall = Wall()
ball.y_speed = -1
ball.x_speed = -11
boundary = Boundary(screen)

while running:
    ball.move()
    #poll for events
    #pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # wipe anything from last frame
    screen.fill((0, 0, 0))
    #RENDER GAME HERE
    for brick in wall:
        if collision(ball, brick):
            brick.kill()
    boundary_collision(ball, boundary)
    boundary.update(screen)
    wall.update(screen)
    ball.update(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()