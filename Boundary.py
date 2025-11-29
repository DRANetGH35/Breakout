import pygame
from Brick import Brick

pygame.init()

class Boundary(pygame.sprite.Group):
    def __init__(self, screen):
        self.LEFT_SIDE = 0
        self.TOP_SIDE = 0
        self.HEIGHT = 720
        self.WIDTH = 1280
        self.RIGHT_SIDE = self.WIDTH
        self.BOTTOM_SIDE = self.HEIGHT
        self.color = (255, 0, 0)
        pygame.sprite.Group.__init__(self)
    def update(self, screen):
        pygame.draw.rect(screen, self.color, (self.LEFT_SIDE, self.TOP_SIDE, self.WIDTH, 1))
        pygame.draw.rect(screen, self.color, (self.LEFT_SIDE, self.TOP_SIDE, 1, self.HEIGHT))
        pygame.draw.rect(screen, self.color, (self.RIGHT_SIDE, self.TOP_SIDE, 1, self.HEIGHT))