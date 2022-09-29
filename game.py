import pygame
import os
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
        self.orcData = AdventurerData(self.screen.get_width(), self.screen.get_height())
        self.magicianData = AdventurerData(self.screen.get_width(), self.screen.get_height())

        #initial attack
        self.initialAttack()

        self.monster = Monster(self)
        monsterX1, monsterY1 = self.monster.getPosition()
        monsterRect = self.monster.getMonsterRect()
        self.monster_attack = MonsterAttack(self, monsterX1, monsterX1+monsterRect.width, monsterY1, monsterY1+monsterRect.height)

        self.adventurer = [Adventurer(self, self.swordsmanData),Adventurer(self, self.archerData),  Adventurer(self, self.orcData), Adventurer(self, self.magicianData)]

        i = 0

        deadNum = 0
        while not crashed:            
            clock.tick(24)            
            self.screen.fill((0,0,0))
    
            self.monster.blitme()      
            self.monster.showHarm()

            for adventurer in self.adventurer:
                deadNum = 0
                if adventurer.life >0:
                    adventurer.showAttack(self.monster, i)
                    adventurer.blitme()
                    adventurer.showHarm()
                else:
                    deadNum+=1
            
            self.monster_attack.blitme(i)     

            i = i+1
            if(i == 11):
                self.monster_attack.randomPosition()
                i = 0

                for adventurer in self.adventurer:
                    if pygame.sprite.collide_rect_ratio(0.9)(adventurer, self.monster_attack):
                        self.monster.attackAdventurer(adventurer)
                    if adventurer.isInAttackRange(self.monster):
                        adventurer.attackMonster(self.monster)
                    else:
                        adventurer.move()
                                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    print(event)
                    pygame.display.update()

                    pygame.quit()
                    quit()


            if deadNum == len(self.adventurer ):
                print("Lose")
                crashed = True
                pygame.display.update()
                pygame.quit()
                quit()
            if self.monster.life <0:
                print("Win")
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
            
        self.orcAttack = Attack(self)
        self.orcData.createOrc(self.orcAttack)

        self.magicianAttack = Attack(self)
        self.magicianData.createMagician(self.magicianAttack)
