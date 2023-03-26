import pygame
from enemy import Enemy
from random import randint
from sound import take_photo, bite_piranha, heal_hero


def event(enemies, score,group_pearls,pearl):

    for event in pygame.event.get():
        if score.game:
            if event.type == pygame.USEREVENT:
                make_pearl(group_pearls,pearl)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                for fish in enemies:
                    if fish.rect.collidepoint(x,y):
                        take_photo()
                        enemies.remove(fish)
                        fish.image = pygame.transform.scale(pygame.image.load('Images/good_fish.png'), (50,50))
                        fish.speed = 4
                        score.amount_photo += 1

        if event.type == pygame.QUIT:
            exit()
def make_fish(enemies, window, friends):
    enemies.draw(window)
    if len(enemies) < 5:
        enemy = Enemy(randint(4, 6))
        enemies.add(enemy)
        friends.add(enemy)

def make_friend(friends, window):
    friends.update()
    friends.draw(window)


def make_pearl(group_pearls,pearl):
    group_pearls.add(pearl)

def move_pearl(window, group_pearls):
    group_pearls.update()
    group_pearls.draw(window)


def collide(hero, enemies, group_pearls):
    if pygame.sprite.spritecollide(hero, enemies, True):
        hero.health -= 1
        bite_piranha()

    if pygame.sprite.spritecollide(hero, group_pearls, True):
        if hero.health < 3:
            hero.health += 1
            heal_hero()
