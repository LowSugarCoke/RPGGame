
from ctypes import sizeof
import pygame
from pygame.sprite import Sprite


class Attack(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.images = []
        self.image = None
        self.rect = None
        self.damage = 0
        self.rotation = 0
        self.zoom = 0

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def blitme(self, num):
        self.screen.blit(self.images[num], self.rect)

    def loadImages(self, path):
        for i in range(0, 12):
            self.images.append(pygame.image.load(
                path+str(i)+'.png').convert_alpha())
            self.images[i] = pygame.transform.rotozoom(
                self.images[i], self.rotation,  self.zoom)
        print(len(self.images))

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
