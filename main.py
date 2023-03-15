import pygame
import events
from hero import Hero

WIDTH = 1200
HEIGHT = 800

def run():
    pygame.init()
    pygame.display.set_caption("Underwater Adventure")
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.transform.scale(pygame.image.load('Images/bg.jpg'), (WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    hero = Hero(window)


    while True:
        window.blit(background, (0, 0))
        events.event()
        hero.update()
        window.blit(hero.image, hero.rect)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    run()