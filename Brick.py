import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, screen, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.pos = pygame.Vector2(pos)
        self.width = 100
        self.height = 50
        self.color = color
    def update(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.width, self.height))