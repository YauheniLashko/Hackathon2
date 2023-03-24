import pygame
from time import sleep


class Scores():
    def __init__(self, window):
        self.image_hp = pygame.transform.scale(pygame.image.load('Images/heart.png'), (50, 50))
        self.image_camera = pygame.transform.scale(pygame.image.load('Images/camera.png'), (50, 50))
        self.window = window
        self.amount_photo = 0
        self.game = True

    def show_health(self, hero):
        x = 10
        for hp in range(hero.health):
            self.window.blit(self.image_hp, (x, 20))
            x += 50

    def draw_photo(self):
        print_score = pygame.font.SysFont('comicsansms', 50).render(str(self.amount_photo), True, (209, 52, 52))
        self.window.blit(self.image_camera, (1050, 20))
        self.window.blit(print_score, (1110, 10))

    def finish(self, hero):
        if hero.health < 1:
            finish_text = pygame.font.SysFont('comicsansms', 50).render\
                ('Ты очень понравился пираньям!', True, (209, 52, 52))
            self.window.blit(finish_text, (200, 400))
            self.game = False
        elif self.amount_photo > 9:
            finish_text = pygame.font.SysFont('comicsansms', 50).render\
                (f'Поздравляю! Ты сделал {self.amount_photo} фото!', True, (209, 52, 52))
            self.window.blit(finish_text, (200, 400))
            self.game = False
