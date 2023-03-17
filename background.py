import pygame

WIDTH = 1200
HEIGHT = 800

class Background():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('Images/bg.jpg').convert(), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rect.width

        self.moving_speed = 2

    def update(self):
        print(self.bgX1, self.rect.width)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.bgX1 -= self.moving_speed
            self.bgX2 -= self.moving_speed
        if keys[pygame.K_LEFT]:
            self.bgX1 += self.moving_speed
            self.bgX2 += self.moving_speed
        if self.bgX1 <= -self.rect.width:
            self.bgX1 = self.rect.width
        if self.bgX2 <= -self.rect.width:
            self.bgX2 = self.rect.width

    def render(self, window):

        window.blit(self.image, (self.bgX1, self.bgY1))
        window.blit(self.image, (self.bgX2, self.bgY2))



