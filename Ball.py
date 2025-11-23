import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
    def update(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, 50, 0)