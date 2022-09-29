import pygame
import random
import math
from pygame.sprite import Sprite
from monster import Monster


class Adventurer(Sprite):
    def __init__(self, game, adventurerData):
        super().__init__()
        self.screen = game.screen
        self.adventurerData = adventurerData
        self.font =  self.adventurerData.font
        self.image =  self.adventurerData.image
        self.rect = self.image.get_rect()
        self.rect.x =  self.adventurerData.rect.x
        self.rect.y =self.adventurerData.rect.y
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.maxLife = self.adventurerData.life
        self.life =  self.adventurerData.life
        self.damageCountDistance =  self.adventurerData.damageCountDistance
        self.attack = self.adventurerData.attack
        self.attack.setPosition(self.rect.x+self.adventurerData.attackPosition[0], self.rect.y+self.adventurerData.attackPosition[1])

        self.harmTimer = 0
        self.lastHarm = 0
        self.distanceWithMonster = self.adventurerData.distanceWithMonster
        

    def blitme(self):        
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 128, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], self.rect.width, 8))
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], (self.life * self.rect.width/self.maxLife), 8))

    def getPosition(self):
        return self.rect.x, self.rect.y

    def move(self):
        self.rect.y -= self.adventurerData.moveDistance
        self.blood_bar_position = [self.rect.x, self.rect.y]

    def attackMonster(self, monster):
        damage = random.randint(self.damageCountDistance[0], self.damageCountDistance[1])
        monster.getHarm(damage)

    def getHarm(self, harm):
        self.lastHarm = harm
        self.life -= harm
        self.harmTimer = 6

    # def blitAttack(self):


    def showHarm(self):
        if self.harmTimer>0 :
            textSurface = self.font.render(str(self.lastHarm), True, (255,0,0), (0, 0, 0))
            self.screen.blit(textSurface,(self.rect.x+50,self.rect.y-50))
            self.harmTimer-=1
    
    def showAttack(self, monster, num):
        if self.isInAttackRange(monster):
            self.attack.blitme(num)
            self.attack.move(self.rect.x+self.adventurerData.attackPosition[0], self.rect.y+self.adventurerData.attackPosition[1])

    def isInAttackRange(self, monster):
        monsterX, monsterY = monster.getPosition()        
        distance = math.sqrt((monsterX - self.rect.x)**2 + (monsterY - self.rect.y) **2 )
        if(distance <= self.distanceWithMonster):
            return True
        else:
            return False