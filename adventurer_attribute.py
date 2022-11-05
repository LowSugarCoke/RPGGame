import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)


class AdventurerAttribute():
    def __init__(self, game, adventurer):
        self.screen = game.screen
        self.adventurer = adventurer
        self.font = pygame.font.Font('freesansbold.ttf', 16)

        

        self.drawDialog()
        return

    def drawDialog(self):
        self.screen.fill(white)
        distance = 100
        # content
        font = pygame.font.Font('freesansbold.ttf', 25)
        content = 'Adventurers'
        text = font.render(content, True, black, white)
        textRect = text.get_rect()
        textRect.center = (150 , self.screen.get_height()*1/2)
        self.screen.blit(text, textRect)

        
        # Swords man
        self.swordsmanPosition = self.adventurer[0].image.get_rect()
        self.swordsmanPosition.x =  self.screen.get_width()*5//20+distance
        self.swordsmanPosition.y =  self.screen.get_height()//16
        self.screen.blit(self.adventurer[0].image, self.swordsmanPosition)

        swordsManContent = 'Swordsman'
        swordsManText = self.font.render(swordsManContent, True, black, white)
        swordsManTextRect = swordsManText.get_rect()
        swordsManTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *3 // 32)
        self.screen.blit(swordsManText, swordsManTextRect)

        swordsManContent = "HP:"+str(self.adventurer[0].life)+"/CD:"+str(self.adventurer[0].adventurerData.cdTime)
        swordsManText = self.font.render(swordsManContent, True, black, white)
        swordsManTextRect = swordsManText.get_rect()
        swordsManTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *4 // 32)
        self.screen.blit(swordsManText, swordsManTextRect)

        swordsManContent = "Damage range:"+str(self.adventurer[0].damageCountDistance[0])+"~"+str(self.adventurer[0].damageCountDistance[1])
        swordsManText = self.font.render(swordsManContent, True, black, white)
        swordsManTextRect = swordsManText.get_rect()
        swordsManTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *5 // 32)
        self.screen.blit(swordsManText, swordsManTextRect)
  
        # Archer
        self.archerPosition = self.adventurer[1].image.get_rect()
        self.archerPosition.x =  self.screen.get_width()*5//20+distance
        self.archerPosition.y =  self.screen.get_height()*4//16
        self.screen.blit(self.adventurer[1].image, self.archerPosition)

        archerContentContent = 'Archer'
        archerText = self.font.render(archerContentContent, True, black, white)
        archerTextRect = archerText.get_rect()
        archerTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *9 // 32)
        self.screen.blit(archerText, archerTextRect)

        archerContentContent = "HP:"+str(self.adventurer[1].life)+"/CD:"+str(self.adventurer[1].adventurerData.cdTime)
        archerText = self.font.render(archerContentContent, True, black, white)
        archerTextRect = archerText.get_rect()
        archerTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *10 // 32)
        self.screen.blit(archerText, archerTextRect)
        
        archerContent = "Damage range:"+str(self.adventurer[1].damageCountDistance[0])+"~"+str(self.adventurer[1].damageCountDistance[1])
        archerText = self.font.render(archerContent, True, black, white)
        archerTextRect = archerText.get_rect()
        archerTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *11 // 32)
        self.screen.blit(archerText, archerTextRect)

        # Orc
        self.orcPosition = self.adventurer[2].image.get_rect()
        self.orcPosition.x =  self.screen.get_width()*5//20+distance
        self.orcPosition.y =  self.screen.get_height()*7//16
        self.screen.blit(self.adventurer[2].image, self.orcPosition)

        orcContentContent = 'Orc'
        orcText = self.font.render(orcContentContent, True, black, white)
        orcTextRect = orcText.get_rect()
        orcTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *15 // 32)
        self.screen.blit(orcText, orcTextRect)

        orcContentContent = "HP:"+str(self.adventurer[2].life)+"/CD:"+str(self.adventurer[2].adventurerData.cdTime)
        orcText = self.font.render(orcContentContent, True, black, white)
        orcTextRect = orcText.get_rect()
        orcTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *16 // 32)
        self.screen.blit(orcText, orcTextRect)
        
        orcContent = "Damage range:"+str(self.adventurer[2].damageCountDistance[0])+"~"+str(self.adventurer[2].damageCountDistance[1])
        orcText = self.font.render(orcContent, True, black, white)
        orcTextRect = orcText.get_rect()
        orcTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *17 // 32)
        self.screen.blit(orcText, orcTextRect)

        # Magician
        self.magicianPosition = self.adventurer[3].image.get_rect()
        self.magicianPosition.x =  self.screen.get_width()*5//20+distance
        self.magicianPosition.y =  self.screen.get_height()*10//16
        self.screen.blit(self.adventurer[3].image, self.magicianPosition)

        magicianContentContent = 'Magician'
        magicianText = self.font.render(magicianContentContent, True, black, white)
        magicianTextRect = magicianText.get_rect()
        magicianTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *21 // 32)
        self.screen.blit(magicianText, magicianTextRect)
        
        magicianContentContent = "HP:"+str(self.adventurer[3].life)+"/CD:"+str(self.adventurer[3].adventurerData.cdTime)
        magicianText = self.font.render(magicianContentContent, True, black, white)
        magicianTextRect = magicianText.get_rect()
        magicianTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *22 // 32)
        self.screen.blit(magicianText, magicianTextRect)

        magicianContent = "Damage range:"+str(self.adventurer[3].damageCountDistance[0])+"~"+str(self.adventurer[3].damageCountDistance[1])
        magicianText = self.font.render(magicianContent, True, black, white)
        magicianTextRect = magicianText.get_rect()
        magicianTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *23 // 32)
        self.screen.blit(magicianText, magicianTextRect)
        
        # Priest
        self.priestPosition = self.adventurer[4].image.get_rect()
        self.priestPosition.x =  self.screen.get_width()*5//20+distance
        self.priestPosition.y =  self.screen.get_height()*13//16
        self.screen.blit(self.adventurer[4].image, self.priestPosition)

        priestContentContent = 'Priest'
        priestText = self.font.render(priestContentContent, True, black, white)
        priestTextRect = priestText.get_rect()
        priestTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *27 // 32)
        self.screen.blit(priestText, priestTextRect)

        priestContentContent = "HP:"+str(self.adventurer[4].life)+"/CD:"+str(self.adventurer[4].adventurerData.cdTime)
        priestText = self.font.render(priestContentContent, True, black, white)
        priestTextRect = priestText.get_rect()
        priestTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *28 // 32)
        self.screen.blit(priestText, priestTextRect)
        
        priestContent = "Heal range:"+str(self.adventurer[4].adventurerData.attack.healDistance[0])+"~"+str(self.adventurer[4].adventurerData.attack.healDistance[1])
        priestText = self.font.render(priestContent, True, black, white)
        priestTextRect = priestText.get_rect()
        priestTextRect.center = (self.screen.get_width()*6 // 10+distance, self.screen.get_height() *29 // 32)
        self.screen.blit(priestText, priestTextRect)
            

     