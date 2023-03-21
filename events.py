import pygame

from enemy import Enemy
from random import randint

def event(enemies):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            for e in enemies:
                if e.rect.collidepoint(x,y):
                    e.kill()

def make_enemies(enemies, window):

    enemies.update()
    enemies.draw(window)
    if len(enemies) < 5:
        enemy = Enemy(randint(4, 6), enemies)
        enemies.add(enemy)
        if enemy.rect.x > 0:
            enemy.kill()

def collide_enemy(hero, enemies):
    if pygame.sprite.spritecollide(hero, enemies, True):
        hero.life -= 1
        print(hero.life)