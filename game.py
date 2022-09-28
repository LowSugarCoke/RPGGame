import pygame
import os
import math
from monster import Monster
from adventurer import Adventurer
from archer import Archer
from attack import Attack
from archer_attack import ArcherAttack
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

        
        self.monster = Monster(self)
        monsterX1, monsterY1 = self.monster.getPosition()
        monsterRect = self.monster.getMonsterRect()
        self.monster_attack = MonsterAttack(self, monsterX1, monsterX1+monsterRect.width, monsterY1, monsterY1+monsterRect.height)

        self.adventurer = Adventurer(self)
        a_x, a_y = self.adventurer.getPosition()
        self.attack = Attack(self, a_x, a_y)

        self.archer = Archer(self)
        archerX, archerY = self.archer.getPosition()
        self.archerAttack = ArcherAttack(self, archerX, archerY)

        i = 0
        adventurerDamage=0
        monsterDamage = 0

        archerDamage = 0

        while not crashed:            
            clock.tick(10)            
            self.screen.fill((0,0,0))

            self.attack.blitme(i)
            self.adventurer.blitme()
            adventurerDamage = self.adventurer.showHarm(adventurerDamage)

            monsterX, monsterY = self.monster.getPosition()
            archerX, archerY = self.archer.getPosition()
            distance = math.sqrt((monsterX - archerX)**2 + (monsterY - archerY) **2 )
            if(distance<=400):
                self.archerAttack.blitme(i)
            self.archer.blitme()
            archerDamage = self.archer.showHarm(archerDamage)
                            
            self.monster.blitme()
            self.monster_attack.blitme(i)           
            monsterDamage = self.monster.showHarm(monsterDamage)

            i = i+1
            if(i == 12):
                self.monster_attack.randomPosition()
                i = 0

                crash_result = pygame.sprite.collide_rect_ratio(0.9)(self.attack, self.monster)
                if crash_result == 1:         
                    damage = self.attack.damage
                    self.monster.life -= damage
                    monsterDamage = damage
                else:
                    self.adventurer.move()
                    px, py = self.adventurer.getPosition()
                    self.attack.move(py)
                    
            

                
                print(distance)
                if(distance>400):
                    self.archer.move()
                    px, py = self.archer.getPosition()
                    self.archerAttack.move(py)
                else:
                    damage = self.archerAttack.damage
                    self.monster.life -= damage
                    monsterDamage = damage

                harmAdventurer = pygame.sprite.collide_rect_ratio(0.5)(self.adventurer, self.monster_attack)
                if harmAdventurer:
                    print("Harm ")
                    damage = self.monster_attack.damage
                    self.adventurer.life -= damage
                    adventurerDamage = damage

                harmArcher = pygame.sprite.collide_rect_ratio(0.5)(self.archer, self.monster_attack)
                if harmArcher:
                    print("Harm ")
                    damage = self.monster_attack.damage
                    self.archer.life -= damage
                    archerDamage = damage

                                        
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
            if self.adventurer.life <= 0:
                print("Lose")
                crashed = True
                pygame.display.update()
                pygame.quit()
                quit()
            
            pygame.display.flip()
