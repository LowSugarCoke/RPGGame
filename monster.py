import pygame
import random
from pygame.sprite import Sprite



class Monster(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/monster.gif')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect()
        self.rect.x = self.screen.get_width()/2 - self.rect.width/2
        self.rect.y = 10
        self.blood_bar_position = [0, self.rect.y]
        self.life = 10000
        self.maxLife = 10000
        self.damage = 100
        self.damageCountDistance = [0,100]
        self.harmTimer = 0
        self.lastHarm = 0

    def getHarm(self, harm):
        self.lastHarm = harm
        self.life -= harm
        self.harmTimer = 6
    

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 128, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], self.screen.get_width(), 8))
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], (self.life * self.screen.get_width()/ self.maxLife) , 8))

    def getPosition(self):
        return self.rect.x, self.rect.y

    def getMonsterRect(self):
        return self.rect

    def showHarm(self):
        if self.harmTimer > 0 :
            textSurface = self.font.render(str(self.lastHarm), True, (255,0,0), (0, 0, 0))
            textSurface.set_alpha(127)
            self.screen.blit(textSurface,(self.rect.x+200,self.rect.y+30))
            self.harmTimer-=1


    def attackAdventurer(self, adventurer):
        damage = random.randint(self.damageCountDistance[0], self.damageCountDistance[1])
        adventurer.getHarm(damage)
