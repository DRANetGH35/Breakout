import pygame

pygame.init()

class Wall(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

