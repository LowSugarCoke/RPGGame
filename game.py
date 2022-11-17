
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
from ending_story import EndingStory
from press_space import PressSpace
from ghost import Ghost
from ghost_attack import GhostAttack
from level1_opening import Level1Opening
from level2_opening import Level2Opening


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
        pygame.mixer.init()  # add this line
        pygame.mixer.music.load(os.path.join("Sound", 'Feel-Good.ogg'))
        pygame.mixer.music.play() # -1 means repeatly

      # init press space sign
        self.pressSpace = PressSpace(self)

        # Testing Ending story
        # self.tendingStory = EndingStory(self)
        # tdialogOn = True
        # self.istWin = False
        # while tdialogOn:
        #     if(self.istWin == True):
        #         self.tendingStory.drawWinDialog()
        #     else:
        #         self.tendingStory.drawLoseDialog()

        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_SPACE:
        #                 tdialogOn = False
        #         if event.type == pygame.QUIT:
        #             pygame.display.update()
        #             pygame.quit()
        #             quit()

        #         pygame.display.flip()

        # Opening
        self.opening = Opening(self)
        dialogOn = True
        a = 0
        while dialogOn:
            clock.tick(12)
            self.screen.fill((255, 255, 255))
            self.opening.drawDialog()
            self.pressSpace.showPressSpace()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.screen.fill((0, 0, 0))
                        dialogOn = False
                        self.pressSpace.pressSpace()
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()

            pygame.display.flip()

        pygame.mixer.music.load(os.path.join("Sound", 'Rise.ogg'))
        pygame.mixer.music.play(-1) # -1 means repeatly
        # Opening Story
        self.openingStory = OpeningStory(self)
        dialogOn = True
        while dialogOn:
            clock.tick(12)
            self.screen.fill((255, 255, 255))
            self.openingStory.drawDialog1()
            self.openingStory.drawCharacter1()
            self.pressSpace.showPressSpace()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogOn = False
                        self.pressSpace.pressSpace()
                       
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()
            pygame.display.flip()

        dialogOn = True
        while dialogOn:
            clock.tick(12)
            self.screen.fill((255, 255, 255))
            self.openingStory.drawCharacter2()
            self.openingStory.drawDialog1()
            self.openingStory.drawDialog2()
            self.pressSpace.showPressSpace()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogOn = False
                        self.pressSpace.pressSpace()
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()
            pygame.display.flip()

        dialogOn = True
        while dialogOn:
            clock.tick(12)
            self.screen.fill((255, 255, 255))
            self.openingStory.drawCharacter3()
            self.openingStory.drawDialog1()
            self.openingStory.drawDialog2()
            self.openingStory.drawDialog3()
            self.pressSpace.showPressSpace()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogOn = False
                        self.pressSpace.pressSpace()
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()
            pygame.display.flip()

        # init adventurer data
        self.swordsmanData = AdventurerData(
            self.screen.get_width(), self.screen.get_height())
        self.archerData = AdventurerData(
            self.screen.get_width(), self.screen.get_height())
        self.orcData = AdventurerData(
            self.screen.get_width(), self.screen.get_height())
        self.magicianData = AdventurerData(
            self.screen.get_width(), self.screen.get_height())
        self.priestData = AdventurerData(
            self.screen.get_width(), self.screen.get_height())

        # initial attack
        self.initialAttack()

        # initial ghost
        self.ghosts = pygame.sprite.Group()
        self.ghosts_attack = pygame.sprite.Group()
        for i in range(0, 5):
            ghost = Ghost(self)
            ghost.rect.x = self.screen.get_width() * (1+i) / 7
            ghost.rect.y = 10
            self.ghosts.add(ghost)

            ghostX1, ghostY1 = ghost.getPosition()
            ghostRect = ghost.getMonsterRect()
            ghost_attack = GhostAttack(
                self, ghostX1+ghostRect.width/2,  ghostY1+ghostRect.height/2)
            self.ghosts_attack.add(ghost_attack)


        # initial monster
        self.monster = Monster(self)
        monsterX1, monsterY1 = self.monster.getPosition()
        monsterRect = self.monster.getMonsterRect()
        self.monster_attack = MonsterAttack(
            self, monsterX1, monsterX1+monsterRect.width, monsterY1, monsterY1+monsterRect.height)

        self.adventurer = [Adventurer(self, self.swordsmanData), Adventurer(self, self.archerData),  Adventurer(self, self.orcData), Adventurer(self, self.magicianData),
                           Adventurer(self, self.priestData)]

        # adventurer dialog
        self.adventurerAttribute = AdventurerAttribute(self, self.adventurer)

        adventurerDialogOn = True
        while adventurerDialogOn:
            clock.tick(12)
            self.adventurerAttribute.drawDialog()
            self.pressSpace.showPressSpace()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        adventurerDialogOn = False
                        self.pressSpace.pressSpace()
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()

            pygame.display.flip()


        # Level 1 opening
        pygame.mixer.music.load(os.path.join("Sound", 'level_opening.ogg'))
        pygame.mixer.music.play(-1) # -1 means repeatly
        self.level1_opening = Level1Opening(self)
        dialogOn = True
        while dialogOn:
            clock.tick(12)
            self.screen.fill((255, 255, 255))
            self.level1_opening.drawDialog()
            self.pressSpace.showPressSpace()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogOn = False
                        self.pressSpace.pressSpace()
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()
            pygame.display.flip()



        self.deadNum = 0
        healIndex = 0
        self.isWin = False

        pygame.mixer.music.load(os.path.join("Sound", 'battle_1.ogg'))
        pygame.mixer.music.play(-1) # -1 means repeatly
        # Ghost
        while not crashed:
            clock.tick(12)
            self.screen.fill((0, 0, 0))
            self.deadNum = 0

            for ghost in self.ghosts:
                if ghost.isAlive():
                    ghost.blitme()
                    ghost.showHarm()
                else:
                    self.deadNum==1
            
            if self.deadNum==len(self.ghosts):
                crashed=True
                break
           
            for adventurer in self.adventurer:
                if adventurer.life <= 0:
                    self.deadNum += 1
                    continue
                
                self.deadNum=0
                for ghost in self.ghosts:
                    if not ghost.isAlive():
                        self.deadNum+=1

                if self.deadNum==len(self.ghosts):
                    crashed=True
                    break


                ghost =  adventurer.findCloseMonster(self.ghosts)
                adventurer.countFrame()
                if adventurer.isFrameContinue() == False:
                    for ghost_attack in self.ghosts_attack:
                        if pygame.sprite.collide_circle_ratio(0.9)(adventurer, ghost_attack):
                            ghost_attack.attackAdventurer(adventurer)
                            ghost_attack.clearAttack()
                    
                
                    if adventurer.isInAttackRange(ghost) and adventurer.character != "Priest":
                        adventurer.attackMonster(ghost)
                    elif adventurer.character == "Priest":
                        healIndex = random.randint(0, 4)
                        while self.adventurer[healIndex].life < 0:
                            healIndex = random.randint(0, 4)
                        adventurer.heal(self.adventurer[healIndex])
                    else:
                        adventurer.moveToGhost(ghost)
                else:
                    if adventurer.character != "Priest":
                        adventurer.showAttack(ghost)
                    else:
                        adventurer.showHeal(self.adventurer[healIndex])

                adventurer.blitme()
                adventurer.showHarm()
                self.adventurer[healIndex].showHealBlood()


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(event)
                    pygame.display.update()
                    pygame.quit()
                    quit()

        crashed = False

        # Level 2 opening
        pygame.mixer.music.load(os.path.join("Sound", 'level_opening.ogg'))
        pygame.mixer.music.play(-1) # -1 means repeatly
        self.level2_opening = Level2Opening(self)
        dialogOn = True
        while dialogOn:
            clock.tick(12)
            self.screen.fill((255, 255, 255))
            self.level2_opening.drawDialog()
            self.pressSpace.showPressSpace()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogOn = False
                        self.pressSpace.pressSpace()
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()
            pygame.display.flip()



        # initial
        for adventurer in self.adventurer:
            adventurer.initial()


        pygame.mixer.music.load(os.path.join("Sound", 'battle_2.ogg'))
        pygame.mixer.music.play(-1) # -1 means repeatly
        # Monster
        while not crashed:
            clock.tick(12)
            self.screen.fill((0, 0, 0))

            self.monster.blitme()
            self.monster.showHarm()
            self.deadNum = 0

            for adventurer in self.adventurer:

                if adventurer.life <= 0:
                    self.deadNum += 1
                    continue

                adventurer.countFrame()
                if adventurer.isFrameContinue() == False:
                    if pygame.sprite.collide_rect_ratio(0.9)(adventurer, self.monster_attack):
                        self.monster.attackAdventurer(adventurer)
                    if adventurer.isInAttackRange(self.monster) and adventurer.character != "Priest":
                        adventurer.attackMonster(self.monster)
                    elif adventurer.character == "Priest":
                        healIndex = random.randint(0, 4)
                        while self.adventurer[healIndex].life < 0:
                            healIndex = random.randint(0, 4)
                        adventurer.heal(self.adventurer[healIndex])
                    else:
                        adventurer.move()
                else:
                    if adventurer.character != "Priest":
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

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(event)
                    pygame.display.update()
                    pygame.quit()
                    quit()

        # Ending story
        self.endingStory = EndingStory(self)
        dialogOn = True
        if self.isWin == True:
            pygame.mixer.music.load(os.path.join("Sound", 'Pathway-Home.ogg'))
            pygame.mixer.music.play(-1) # -1 means repeatly
        else:
            pygame.mixer.music.load(os.path.join("Sound", 'Sovereign.ogg'))
            pygame.mixer.music.play(-1) # -1 means repeatly

        while dialogOn:
            if(self.isWin == True):
                self.endingStory.drawWinDialog()
            else:
                self.endingStory.drawLoseDialog()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogOn = False
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    pygame.quit()
                    quit()

            pygame.display.flip()

        pygame.display.update()
        pygame.quit()
        quit()

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
        if self.deadNum == len(self.adventurer):
            print("Lose")
            self.isWin = False
            return True
        if self.monster.life < 0:
            print("Win")
            self.isWin = True
            return True
