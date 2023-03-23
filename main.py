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
    enemies = pygame.sprite.Group()
    friends = pygame.sprite.Group()
    background = bg.Background()


    while True:

        background.update()
        background.render(window)
        events.event(enemies)
        hero.update()
        events.make_friend(friends, window)
        events.make_fish(enemies, window, friends)
        events.collide_enemy(hero, enemies)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    run()