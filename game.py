import pygame
import os
import math
from adventurer_data import AdventurerData
from monster import Monster
from adventurer import Adventurer
from attack import Attack
from monster_attack import MonsterAttack


class RPGGame:
    def __init__(self, w=800, h=600):
        pygame.init()
        self.w = w
        self.h = h
        self.win = False

        # init display
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption('RPG Game')
        clock = pygame.time.Clock()
        crashed = False      

        #init music
        pygame.mixer.init() # add this line
        pygame.mixer.music.load(os.path.join("Sound", 'battle.ogg'))
        # pygame.mixer.music.play(-1)
        
        #init adventurer data
        self.swordsmanData = AdventurerData(self.screen.get_width(), self.screen.get_height())
        self.archerData = AdventurerData(self.screen.get_width(), self.screen.get_height())
  
        #initial attack
        self.initialAttack()

        self.monster = Monster(self)
        monsterX1, monsterY1 = self.monster.getPosition()
        monsterRect = self.monster.getMonsterRect()
        self.monster_attack = MonsterAttack(self, monsterX1, monsterX1+monsterRect.width, monsterY1, monsterY1+monsterRect.height)

        self.swordsman = Adventurer(self, self.swordsmanData)
        self.archer = Adventurer(self, self.archerData)
        
        i = 0

        while not crashed:            
            clock.tick(20)            
            self.screen.fill((0,0,0))
    
            self.monster.blitme()      
            self.monster.showHarm()

            if self.swordsman.life > 0:
                self.swordsman.showAttack(self.monster, i)
                self.swordsman.blitme()
                self.swordsman.showHarm()

            if self.archer.life>0:
                self.archer.showAttack(self.monster, i)
                self.archer.blitme()
                self.archer.showHarm()

            self.monster_attack.blitme(i)     

            i = i+1
            if(i == 11):
                self.monster_attack.randomPosition()
                i = 0

                if self.swordsman.isInAttackRange(self.monster):               
                    self.swordsman.attackMonster(self.monster)         
                else:
                    self.swordsman.move()

                if(self.archer.isInAttackRange(self.monster)):
                    self.archer.attackMonster(self.monster)
                else: 
                    self.archer.move()

                harmAdventurer = pygame.sprite.collide_rect_ratio(0.5)(self.swordsman, self.monster_attack)
                if harmAdventurer:
                    self.monster.attackAdventurer(self.swordsman)


                harmArcher = pygame.sprite.collide_rect_ratio(0.5)(self.archer, self.monster_attack)
                if harmArcher:
                    self.monster.attackAdventurer(self.archer)

                                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    print(event)
                    pygame.display.update()

                    pygame.quit()
                    quit()

            if self.monster.life <= 0:
                print("win")
                crashed = True
                pygame.display.update()
                pygame.quit()
                quit()
            if self.swordsman.life <= 0:
                print("Lose")
                crashed = True
                pygame.display.update()
                pygame.quit()
                quit()
            
            pygame.display.flip()
        
    def initialAttack(self):
        self.swordsmanAttack = Attack(self)
        self.swordsmanData.createSwordsman(self.swordsmanAttack)

        self.archerAttack = Attack(self)
        self.archerData.createArcher(self.archerAttack)
            
