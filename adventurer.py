import pygame
from pygame.sprite import Sprite


class Adventurer(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('img/swordsman.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.screen.get_width()/2 - self.rect.width/2
        self.rect.y = 550
        self.blood_bar_position = [self.rect.x, self.rect.y]

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 128, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], self.rect.width, 8))
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], self.rect.width, 8))

    def getPosition(self):
        return self.rect.x, self.rect.y
