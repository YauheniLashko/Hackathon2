import pygame

from enemy import Enemy
from random import randint
from scores import Scores

def event(enemies, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            for fish in enemies:
                if fish.rect.collidepoint(x,y):
                    enemies.remove(fish)
                    fish.image = pygame.transform.scale(pygame.image.load('Images/good_fish.png'), (50,50))
                    fish.speed = 4
                    score.amount_photo += 1

def make_fish(enemies, window, friends):
    enemies.draw(window)
    if len(enemies) < 5:
        enemy = Enemy(randint(4, 6))
        enemies.add(enemy)
        friends.add(enemy)

def make_friend(friends, window):
    friends.update()
    friends.draw(window)


def collide_enemy(hero, enemies):
    if pygame.sprite.spritecollide(hero, enemies, True):
        hero.health -= 1


