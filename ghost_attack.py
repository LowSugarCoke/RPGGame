
import pygame
import random
from ctypes import sizeof
from pygame.sprite import Sprite


class GhostAttack(Sprite):
    def __init__(self, game, ghost_x,ghost_y):
        super().__init__()
        self.screen = game.screen
        self.images = []
        self.loadImages()
        self.image = pygame.image.load(
            './Img/ghost_attack/ghost_attack-0.png')
        self.rect = self.image.get_rect()
        self.ghostX = ghost_x
        self.ghostY = ghost_y
        self.attackFrame = 0
        self.rect.x = self.ghostX
        self.rect.y = self.ghostY
        self.dirX = 0
        self.dirY = 0
        self.randomDirection()
        self.damageCountDistance = [70, 150]

    def blitme(self):
        self.screen.blit(self.images[self.attackFrame], self.rect)
        self.attackFrame += 1

    def move(self):
        if self.attackFrame != 8:
            return

        self.attackFrame = 0

        if(self.rect.x <0 or self.rect.y <0 or self.rect.x> self.screen.get_width() or self.rect.y > self.screen.get_height()):
            self.randomDirection()
            self.rect.x = self.ghostX
            self.rect.y = self.ghostY


        self.rect.x = self.rect.x + self.dirX
        self.rect.y = self.rect.y + self.dirY

    def randomDirection(self):
        randomX = random.randint(-30, 30)
        randomY = random.randint(10, 30)

        self.dirX = randomX
        self.dirY = randomY


    def loadImages(self):
        for i in range(0, 8):
            self.images.append(pygame.image.load(
                './Img/ghost_attack/ghost_attack-'+str(i)+'.png').convert_alpha())
            self.images[i] = pygame.transform.rotozoom(
                self.images[i], 0, 1)

    def clearAttack(self):
        self.randomDirection()
        self.rect.x = self.ghostX
        self.rect.y = self.ghostY

    def attackAdventurer(self, adventurer):
        damage = random.randint(
            self.damageCountDistance[0], self.damageCountDistance[1])
        adventurer.getHarm(damage)
