import pygame
import events

from scores import Scores
from hero import Hero
from sound import bg_music
from pearl import Pearl

import background as bg


def run():
    pygame.init()
    pygame.display.set_caption("Underwater Adventure")
    window = pygame.display.set_mode((bg.WIDTH, bg.HEIGHT))
    clock = pygame.time.Clock()
    hero = Hero(window)

    enemies = pygame.sprite.Group()
    friends = pygame.sprite.Group()
    group_pearls = pygame.sprite.Group()

    background = bg.Background()
    score = Scores(window)
    pygame.time.set_timer(pygame.USEREVENT, 10000)

    bg_music()
    while True:
        pearl = Pearl() #создаем в цикле новый объект perl для разных картинок
        events.event(enemies, score,group_pearls,pearl)
        if score.game:

            background.update()
            background.render(window)
            hero.update()
            score.show_health(hero)
            score.draw_photo()
            score.finish(hero)
            events.make_friend(friends, window)
            events.make_fish(enemies, window, friends)
            events.move_pearl(window,group_pearls)
            events.collide(hero, enemies,group_pearls)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    run()
