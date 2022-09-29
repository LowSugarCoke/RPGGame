import pygame


class AdventurerData:
    def __init__(self, screenWidth, screenHeight):
        self.width = screenWidth
        self.height = screenHeight
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/swordsman.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 0
        self.damageCountDistance = [0,100]        
        self.attack = None
        self.attackPosition = []
        self.moveDistance = 0

    def createSwordsman(self, swordsManAttack):
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/swordsman.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.width*3/7 - self.rect.width/2
        self.rect.y = self.height-self.rect.height
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 1000
        self.moveDistance = 15
        self.attackPosition = [-30, -140]
        self.attack = swordsManAttack
        self.attack.image = pygame.image.load('img/sword_attack/attack-0.png')
        self.attack.rect = self.attack.image.get_rect()
        self.attack.damage = 100
        self.attack.rotation = -90
        self.attack.zoom = 0.4
        self.attack.loadImages('img/sword_attack/attack-')
        self.distanceWithMonster = 250
   

    def createArcher(self, archerAttack):
        self.font = pygame.font.SysFont("arial", 36)
        self.image = pygame.image.load('img/archer.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.width*2/7 - self.rect.width/2
        self.rect.y = self.height-self.rect.height
        self.blood_bar_position = [self.rect.x, self.rect.y]
        self.life = 1000
        self.attackPosition = [-15, -135]
        self.moveDistance = 20
        self.attack = archerAttack
        self.attack.image = pygame.image.load('img/sword_attack/attack-0.png')
        self.attack.rect = self.attack.image.get_rect()
        self.attack.damage = 100
        self.attack.rotation = -130
        self.attack.zoom = 0.5
        self.attack.loadImages('img/archer_attack/attack-')
        self.distanceWithMonster = 400
 