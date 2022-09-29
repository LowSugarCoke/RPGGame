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
        self.damageCountDistance =  self.adventurerData.attack.damageCountDistance
        self.attack = self.adventurerData.attack
        self.attack.setPosition(self.rect.x+self.adventurerData.attackPosition[0], self.rect.y+self.adventurerData.attackPosition[1])
        self.cd = 0
        self.harmTimer = 0
        self.lastHarm = 0
        self.distanceWithMonster = self.adventurerData.distanceWithMonster
        self.character = self.adventurerData.character
        self.lastHeal = 0
        self.healTimer = 0
        

    def blitme(self):        
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 128, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], 80, 8))
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], (self.life * 80/self.maxLife), 8))

    def getPosition(self):
        return self.rect.x, self.rect.y

    def move(self):
        self.rect.y -= self.adventurerData.moveSpeed
        self.blood_bar_position = [self.rect.x, self.rect.y]

    def attackMonster(self, monster):
        if self.cd <= 0:
            damage = random.randint(self.damageCountDistance[0], self.damageCountDistance[1])
            monster.getHarm(damage)
            self.cd = self.adventurerData.cdTime
        else:
            self.cd -=1
            
    def getHarm(self, harm):
        self.lastHarm = harm
        self.life -= harm
        self.harmTimer = 6

    def showHarm(self):
        if self.harmTimer>0 :
            textSurface = self.font.render(str(self.lastHarm), True, (255,0,0), (0, 0, 0))
            self.screen.blit(textSurface,(self.rect.x+50,self.rect.y-50))
            self.harmTimer-=1
    
    def showAttack(self, monster, num):
        if self.isInAttackRange(monster) and self.cd <= 0:
            self.attack.blitme(num)
            self.attack.move(self.rect.x+self.adventurerData.attackPosition[0], self.rect.y+self.adventurerData.attackPosition[1])

    def isInAttackRange(self, monster):
        monsterX, monsterY = monster.getPosition()        
        distance = math.sqrt((monsterX - self.rect.x)**2 + (monsterY - self.rect.y) **2 )
        if(distance <= self.distanceWithMonster):
            return True
        else:
            return False

    def heal(self, adventurer):
        if self.cd <= 0:
            adventurer.lastHeal  = random.randint(self.adventurerData.attack.healDistance[0], self.adventurerData.attack.healDistance[1])       
            adventurer.life += adventurer.lastHeal        
            if adventurer.life > adventurer.maxLife:
                adventurer.life = adventurer.maxLife
            self.cd = self.adventurerData.cdTime
        else:
            self.cd -=1 
    
    def showHeal(self, adventurer , num):
        if self.cd <=0:
            self.attack.blitme(num)
            position = adventurer.getPosition()
            self.attack.move(position[0]-25, position[1]-20)
            adventurer.healTimer = 6

    def showHealBlood(self):
        if self.healTimer >0 and self.lastHeal >0:
            textSurface = self.font.render(str(self.lastHeal), True, (0,255,0), (0, 0, 0))
            self.screen.blit(textSurface,(self.rect.x+50,self.rect.y-50))
            self.healTimer-=1
