import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.pos = pygame.Vector2(pos)

    def update(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.pos[0], self.pos[1], 100, 50))