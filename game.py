
import pygame
import os
import random
from adventurer_data import AdventurerData
from monster import Monster
from adventurer import Adventurer
from attack import Attack
from monster_attack import MonsterAttack
from opening import Opening
from opening_story import OpeningStory
from adventurer_attribute import AdventurerAttribute

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

        # init music
        pygame.mixer.init() # add this line
        pygame.mixer.music.load(os.path.join("Sound", 'battle.ogg'))
        # pygame.mixer.music.play(-1)
        
        # Opening
        self.opening = Opening(self)
        dialogOn = True
        while dialogOn:
            self.opening.drawDialog()

            for event in pygame.event.get():     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogOn = False
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()

                pygame.display.flip()


        # Opening Story
        self.openingStory = OpeningStory(self)
        dialogOn = True
        while dialogOn:
            self.openingStory.drawDialog()

            for event in pygame.event.get():     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogOn = False
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()

                pygame.display.flip()


        # init adventurer data
        self.swordsmanData = AdventurerData(self.screen.get_width(), self.screen.get_height())
        self.archerData = AdventurerData(self.screen.get_width(), self.screen.get_height())
        self.orcData = AdventurerData(self.screen.get_width(), self.screen.get_height())
        self.magicianData = AdventurerData(self.screen.get_width(), self.screen.get_height())
        self.priestData = AdventurerData(self.screen.get_width(), self.screen.get_height())

        # initial attack
        self.initialAttack()

        self.monster = Monster(self)
        monsterX1, monsterY1 = self.monster.getPosition()
        monsterRect = self.monster.getMonsterRect()
        self.monster_attack = MonsterAttack(self, monsterX1, monsterX1+monsterRect.width, monsterY1, monsterY1+monsterRect.height)

        self.adventurer = [Adventurer(self, self.swordsmanData),Adventurer(self, self.archerData),  Adventurer(self, self.orcData), Adventurer(self, self.magicianData),
        Adventurer(self, self.priestData)]


        # adventurer dialog
        self.adventurerAttribute = AdventurerAttribute(self, self.adventurer)

        adventurerDialogOn = True
        while adventurerDialogOn:
            self.adventurerAttribute.drawDialog()

            for event in pygame.event.get():     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        adventurerDialogOn = False
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()

                pygame.display.flip()


        self.deadNum = 0
        healIndex = 0
        while not crashed:            
            clock.tick(12)
            self.screen.fill((0,0,0))
    
            self.monster.blitme()      
            self.monster.showHarm()

            for adventurer in self.adventurer:
                self.deadNum = 0
                if adventurer.life <=0 :
                    self.deadNum+=1
                    continue

                adventurer.countFrame()
                if adventurer.isFrameContinue() == False:      
                    if pygame.sprite.collide_rect_ratio(0.9)(adventurer, self.monster_attack):
                        self.monster.attackAdventurer(adventurer)
                    if adventurer.isInAttackRange(self.monster) and adventurer.character != "Priest":
                        adventurer.attackMonster(self.monster)
                    elif adventurer.character == "Priest":
                        healIndex = random.randint(0, 4)
                        while self.adventurer[healIndex].life <0:
                            healIndex = random.randint(0, 4)
                        adventurer.heal(self.adventurer[healIndex])
                    else:
                        adventurer.move()
                else:
                    if adventurer.character !="Priest":
                        adventurer.showAttack(self.monster)
                    else:
                        adventurer.showHeal(self.adventurer[healIndex])           

                adventurer.blitme()
                adventurer.showHarm()
                self.adventurer[healIndex].showHealBlood()
      
            self.monster_attack.blitme()     
            self.monster_attack.randomPosition()
        
    
            if self.isFinish():
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

        self.priestAttack = Attack(self)
        self.priestData.createPriest(self.priestAttack)

    def isFinish(self):
        if self.deadNum == len(self.adventurer)-1:
            print("Lose")
            return True
        if self.monster.life <0:
            print("Win")
            return True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                return True
