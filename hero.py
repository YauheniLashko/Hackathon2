import pygame
import events

class Hero(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.pick_ind = 0
        self.window = window
        self.speed = 3
        self.move_right = [pygame.transform.scale(pygame.image.load('Images/right1.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right2.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right3.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right4.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right5.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right6.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right7.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right8.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right9.png').convert_alpha(), (250, 120)),
                           pygame.transform.scale(pygame.image.load('Images/right10.png').convert_alpha(), (250, 120))]
        self.move_left = [pygame.transform.scale(pygame.image.load('Images/left1.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left2.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left3.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left4.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left5.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left6.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left7.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left8.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left9.png').convert_alpha(), (250, 120)),
                          pygame.transform.scale(pygame.image.load('Images/left10.png').convert_alpha(), (250, 120))]
        self.image = self.move_right[self.pick_ind]
        self.rect = self.image.get_rect(bottom=450)



    def update(self):
        self.image = self.move_right[self.pick_ind // 6]
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.image = self.move_right[self.pick_ind // 6]
            self.rect.x += self.speed
            print(self.rect.x)
        if keys[pygame.K_LEFT]:
            self.image = self.move_left[self.pick_ind // 6]
            self.rect.x -= self.speed
            print(self.rect.x)
        if keys[pygame.K_UP] and self.rect.y > 140:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed

        if self.pick_ind < 54:
            self.pick_ind += 1
        else:
            self.pick_ind = 0

        self.window.blit(self.image, (self.rect))