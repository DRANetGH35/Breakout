import pygame


class Ball(pygame.sprite.Sprite):
    x_speed = 0
    y_speed = 0
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
        self.radius = 10
        self.color = (255, 255, 255)
    def update(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius, 0)
    def move(self):
        self.pos[0] += self.x_speed
        self.pos[1] += self.y_speed
    def stop(self):
        self.x_speed = 0
        self.y_speed = 0
        self.color = (255, 0, 0)