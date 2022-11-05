import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

class OpeningStory():
    def __init__(self, game):
        self.screen = game.screen
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)

      
        return

    def drawDialog1(self):
        content = 'Once upon a time, there was '
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width() // 3, self.screen.get_height() // 5)
        self.screen.blit(text, textRect)

        content = 'a prince and a princess.'
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width() // 3 - 40, self.screen.get_height() // 5 + 30)
        self.screen.blit(text, textRect)

    def drawDialog2(self):
        content = 'One day, a monster boss '
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width() // 3 -30 , self.screen.get_height()*2 // 5 )
        self.screen.blit(text, textRect)

        content = 'captured the princess.'
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width() // 3-55 , self.screen.get_height()*2 // 5 +30)
        self.screen.blit(text, textRect)

    def drawDialog3(self):
        content = 'The prince decided to gain back'
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width() // 3+25 , self.screen.get_height()*3 // 5)
        self.screen.blit(text, textRect)

        content = 'his princess with the help of his team!!'
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width() // 3+80 , self.screen.get_height()*3 // 5 +30)
        self.screen.blit(text, textRect)

    def drawCharacter1(self):
        image = pygame.image.load('img/prince.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2 -10
        rect.y = self.screen.get_height()/2-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/princess.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2-70
        rect.y = self.screen.get_height()/2-rect.height/2 - 100
        self.screen.blit(image, rect)

    def drawCharacter2(self):
        image = pygame.image.load('img/prince.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2 +80
        rect.y = self.screen.get_height()/2-rect.height/2 -40
        self.screen.blit(image, rect)

        image = pygame.image.load('img/exclamation_point.png')
        image = pygame.transform.rotozoom(image, 0, 0.4)
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2 +80
        rect.y = self.screen.get_height()/2-rect.height/2 - 120
        self.screen.blit(image, rect)

        image = pygame.image.load('img/monster.gif')
        image = pygame.transform.rotozoom(image, 0, 0.4)
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2-70
        rect.y = self.screen.get_height()/2-rect.height/2 - 100
        self.screen.blit(image, rect)

    def drawCharacter3(self):
        image = pygame.image.load('img/prince.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2 +80
        rect.y = self.screen.get_height()/2-rect.height/2 - 40
        self.screen.blit(image, rect)

        image = pygame.image.load('img/prince_sword.png')
        image = pygame.transform.rotozoom(image, 0, 0.06)
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2 +35
        rect.y = self.screen.get_height()/2-rect.height/2 - 60
        self.screen.blit(image, rect)

        image = pygame.image.load('img/monster.gif')
        image = pygame.transform.rotozoom(image, 0, 0.4)
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2-70
        rect.y = self.screen.get_height()/2-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/swordsman.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*1/12 - rect.width/2 +35
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/orc.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*3/12 - rect.width/2 +35
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/priest.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*5/12 - rect.width/2 +35
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/magician.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*7/12 - rect.width/2 +35
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/archer.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*9/12 - rect.width/2 +35
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)