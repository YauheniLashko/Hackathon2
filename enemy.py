import pygame
import background as bg
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Images/piranha.png'), (50,50))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.y = randint(140, 620)
        self.rect.x = bg.WIDTH

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

    def draw(self, window):
        window.blit(self.image, self.rect)


