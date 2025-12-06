import pygame
from collision import collision, boundary_collision, pit_collision, paddle_collision
from Ball import Ball
from Wall import Wall
from Boundary import Boundary
from Paddle import Paddle
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ball = Ball(screen)
wall = Wall()
ball.y_speed = -5
ball.x_speed = -5
boundary = Boundary(screen)
paddle = Paddle(screen)

while running:
    if not wall.sprites():
        print("You win")
        running = False
    ball.move()
    #poll for events
    #pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.direction = 'left'
            if event.key == pygame.K_RIGHT:
                paddle.direction = 'right'
        elif event.type == pygame.KEYUP:
            paddle.direction = None
    # wipe anything from last frame
    screen.fill((0, 0, 0))
    #RENDER GAME HERE
    for brick in wall:
        if collision(ball, brick):
            brick.kill()
    boundary_collision(ball, boundary)
    if pit_collision(ball, boundary):
        ball.stop()
        running = False
        print("You lose")
    paddle_collision(ball, paddle, boundary)
    boundary.update(screen)
    wall.update(screen)
    ball.update(screen)
    paddle.update(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()