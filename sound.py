import pygame

def take_photo():
    take_photo = pygame.mixer.Sound('Sound/photo_sound.ogg')
    take_photo.play()

def bite_piranha():
    bite = pygame.mixer.Sound('Sound/piranha.ogg')
    bite.play()

def bg_music():
    pygame.mixer.music.load('Sound/deep.mp3')
    pygame.mixer.music.play(-1)

def heal_hero():
    heal = pygame.mixer.Sound('Sound/heal.ogg')
    heal.play()