import pygame


class AdventurerData:
    def __init__(self, screenWidth, screenHeight):
        self.character = ""
        self.width = screenWidth
        self.height = screenHeight
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/swordsman.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 0
        self.attack = None
        self.attackPosition = []
        self.moveSpeed = 0
        self.cdTime = 0

    def createSwordsman(self, swordsManAttack):
        self.character = "Swordsman"
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/swordsman.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.width*3/7 - self.rect.width/2
        self.rect.y = self.height-self.rect.height
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 1000
        self.moveSpeed = 15
        self.attackPosition = [-30, -140]
        self.attack = swordsManAttack
        self.attack.image = pygame.image.load('img/sword_attack/attack-0.png')
        self.attack.rect = self.attack.image.get_rect()
        self.attack.damageCountDistance = [10,50]         
        self.attack.rotation = -90
        self.attack.zoom = 0.4
        self.attack.loadImages('img/sword_attack/attack-')
        self.attack.waitFrame = 12
        self.distanceWithMonster = 250
        self.cdTime = 1
   

    def createArcher(self, archerAttack):
        self.character = "Archer"
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/archer.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.width*1/7 - self.rect.width/2
        self.rect.y = self.height-self.rect.height
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 1000
        self.attackPosition = [-15, -135]
        self.moveSpeed = 20
        self.attack = archerAttack
        self.attack.image = pygame.image.load('img/sword_attack/attack-0.png')
        self.attack.rect = self.attack.image.get_rect()
        self.attack.damageCountDistance = [20,70]         
        self.attack.rotation = -130
        self.attack.zoom = 0.5
        self.attack.loadImages('img/archer_attack/attack-')
        self.attack.waitFrame = 12
        self.distanceWithMonster = 400
 
    def createOrc(self, orcAttack):
        self.character = "Orc"
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/orc.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.width*4/7 - self.rect.width/2
        self.rect.y = self.height-self.rect.height
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 1000
        self.moveSpeed = 10
        self.attackPosition = [-30, -140]
        self.attack = orcAttack
        self.attack.image = pygame.image.load('img/orc_attack/attack-0.png')
        self.attack.rect = self.attack.image.get_rect()
        self.attack.damageCountDistance = [0,100]      
        self.attack.rotation = -90
        self.attack.zoom = 0.4
        self.attack.loadImages('img/orc_attack/attack-')
        self.attack.waitFrame = 12
        self.distanceWithMonster = 300
        self.cdTime = 2
    
    def createMagician(self, magicianAttack):
        self.character = "Magician"
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/magician.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.width*5/7 - self.rect.width/2
        self.rect.y = self.height-self.rect.height
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 1000
        self.moveSpeed = 5
        self.attackPosition = [-220, -400]
        self.attack = magicianAttack
        self.attack.image = pygame.image.load('img/magician_attack/attack-0.png')
        self.attack.rect = self.attack.image.get_rect()
        self.attack.damageCountDistance = [30,150]      
        self.attack.rotation = 0
        self.attack.zoom = 0.5
        self.attack.loadImages('img/magician_attack/attack-')
        self.attack.waitFrame = 12
        self.distanceWithMonster = 500
        self.cdTime = 5

    def createPriest(self, priestAttack):
        self.character ="Priest"
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/priest.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.width*2/7 - self.rect.width/2
        self.rect.y = self.height-self.rect.height
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 1000
        self.moveSpeed = 5
        self.attackPosition = [-220, -400]
        self.attack = priestAttack
        self.attack.image = pygame.image.load('img/priest_attack/attack-0.png')
        self.attack.rect = self.attack.image.get_rect()
        self.attack.damageCountDistance = [30,150]      
        self.attack.healDistance = [10,30]
        self.attack.rotation = 0
        self.attack.zoom = 0.5
        self.attack.loadImages('img/priest_attack/attack-')
        self.attack.waitFrame = 12
        self.distanceWithMonster = 500
        self.cdTime = 0
 