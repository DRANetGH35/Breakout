import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.width = 300
        self.height = 50
        self.color = (255, 255, 255)
        self.pos = pygame.Vector2((1280/2)-(self.width / 2), 700)
        self.direction = None
    def update(self, screen):
        self.move()
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.width, self.height))
    def move(self):
        if self.direction == "right":
            self.pos = (self.pos[0] + 10, self.pos[1])
        if self.direction == "left":
            self.pos = (self.pos[0] - 10, self.pos[1])
