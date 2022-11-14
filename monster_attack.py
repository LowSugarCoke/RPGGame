
import pygame
import random
from ctypes import sizeof
from pygame.sprite import Sprite



class MonsterAttack(Sprite):
    def __init__(self, game, x1, x2, y1, y2):
        super().__init__()
        self.screen = game.screen
        self.images = []
        self.loadImages()
        self.image = pygame.image.load('./Img/monster_attack/monster_attack-0.png')
        self.rect = self.image.get_rect()
        self.monsterX1 = x1
        self.monsterX2 = x2
        self.monsterY1 = y1
        self.monsterY2 = y2
        self.attackFrame = 0
        self.randomPosition()
        self.damage = 100
        

    def blitme(self):
        self.screen.blit(self.images[self.attackFrame], self.rect)
        self.attackFrame +=1

    def randomPosition(self):
        if self.attackFrame != 12:
            return

        self.attackFrame = 0
        randomX = self.monsterX1+1
        randomY = self.monsterY1+1

        while ( ( randomX > self.monsterX1 and randomX < self.monsterX2 and randomY >self.monsterY1 and randomY < self.monsterY2 ) or randomX > 750 or randomY > 550):
            randomX = random.randint(0, self.screen.get_width())
            randomY = random.randint(0, self.screen.get_height())


        self.rect.x = randomX
        self.rect.y = randomY

    def loadImages(self):
        for i in range(0, 12):
            self.images.append(pygame.image.load(
                './Img/monster_attack/monster_attack-'+str(i)+'.png').convert_alpha())
            self.images[i] = pygame.transform.rotozoom(
                self.images[i], 0, 0.7)

