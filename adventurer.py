import pygame
from pygame.sprite import Sprite


class Adventurer(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('img/swordsman.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.screen.get_width()/2 - self.rect.width/2
        self.rect.y = self.screen.get_height() - self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
