
from ctypes import sizeof
import pygame
from pygame.sprite import Sprite


class Attack(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.images = []
        self.loadImages()
        self.image = pygame.image.load('img/monster.gif')
        self.rect = self.image.get_rect()
        self.rect.x = self.screen.get_width()/2 - self.rect.width/2
        self.rect.y = self.screen.get_height()/2

    def blitme(self, num):
        self.screen.blit(self.images[num], self.rect)

    def loadImages(self):
        for i in range(0, 12):
            self.images.append(pygame.image.load(
                'img/sword/attack-'+str(i)+'.jpg').convert_alpha())
            self.images[i] = pygame.transform.rotozoom(self.images[i], 0, 0.5)
        print(len(self.images))
