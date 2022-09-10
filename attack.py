
from ctypes import sizeof
import pygame
from pygame.sprite import Sprite


class Attack(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.images = []
        self.loadImages()
        self.image = pygame.image.load('img/monster.gif')
        self.rect = self.image.get_rect()
        self.rect.x = x-30
        self.rect.y = y-170
        self.damage = 100

    def blitme(self, num):
        self.screen.blit(self.images[num], self.rect)

    def loadImages(self):
        for i in range(0, 12):
            self.images.append(pygame.image.load(
                'img/sword/attack-'+str(i)+'.jpg').convert_alpha())
            self.images[i] = pygame.transform.rotozoom(
                self.images[i], -90, 0.5)
        print(len(self.images))

    def move(self, y):
        self.rect.y = y-170
