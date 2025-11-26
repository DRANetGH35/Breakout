import pygame
from Brick import Brick

pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Wall(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        for x in range(10):
            for y in range(3):
                new_brick = Brick(screen, (x * 105 + 100, y * 55 + 10))
                self.add(new_brick)
