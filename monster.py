import pygame
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
        self.blood_bar_position = [self.screen.get_width()/4, self.rect.y]
        self.life = self.screen.get_width()/2
        self.damage = 100
        self.damageCount = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 128, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], self.screen.get_width()/2, 8))
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.blood_bar_position[0], self.blood_bar_position[1], self.life, 8))

    def getPosition(self):
        return self.rect.x, self.rect.y

    def getMonsterRect(self):
        return self.rect

    def showHarm(self, harm):
        if harm!=0 :
            textSurface = self.font.render(str(harm), True, (255,0,0), (0, 0, 0))
            self.screen.blit(textSurface,(self.rect.x+200,self.rect.y+30))
            self.damageCount+=1
                            
        if self.damageCount > 6:
            harm = 0
            self.damageCount = 0
            return 0

        return harm
