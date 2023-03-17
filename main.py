import pygame
import events
from hero import Hero
import background as bg


def run():
    pygame.init()
    pygame.display.set_caption("Underwater Adventure")
    window = pygame.display.set_mode((bg.WIDTH, bg.HEIGHT))
    clock = pygame.time.Clock()
    hero = Hero(window)
    background = bg.Background()


    while True:

        background.update()
        background.render(window)
        events.event()
        hero.update()
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    run()