import pygame


class Ball(pygame.sprite.Sprite):
    x_speed = 0
    y_speed = 0
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
    def update(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, 10, 0)
    def move(self):
        self.pos[0] += self.x_speed
        self.pos[1] += self.y_speed