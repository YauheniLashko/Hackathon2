import pygame


def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
