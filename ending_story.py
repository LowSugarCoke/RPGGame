import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

class EndingStory():
    def __init__(self, game):
        self.screen = game.screen
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        return

    def drawWinDialog(self):

        self.screen.fill(white)

        content = 'Win'
        text = pygame.font.Font('freesansbold.ttf', 96).render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width()*2 // 4, self.screen.get_height() // 5+30)
        self.screen.blit(text, textRect)

        content = 'The princess went home with the prince,'
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width()*2 // 4, self.screen.get_height()*2 // 5)
        self.screen.blit(text, textRect)

        content = 'and they lived happily ever after'
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width()*2 // 4 , self.screen.get_height() *2// 5 + 30)
        self.screen.blit(text, textRect)

        image = pygame.image.load('img/prince.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*6/12 - rect.width/2 +30
        rect.y = self.screen.get_height()*2/3-rect.height/2 
        self.screen.blit(image, rect)

        image = pygame.image.load('img/princess.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*6/12 - rect.width/2 -30
        rect.y = self.screen.get_height()*2/3-rect.height/2 
        self.screen.blit(image, rect)

        image = pygame.image.load('img/swordsman.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*2/12 - rect.width/2 
        rect.y = self.screen.get_height()-rect.height/2 -100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/orc.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*4/12 - rect.width/2 
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/priest.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*6/12 - rect.width/2 
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/magician.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*8/12 - rect.width/2 
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)

        image = pygame.image.load('img/archer.png')
        rect = image.get_rect()
        rect.x = self.screen.get_width()*10/12 - rect.width/2 
        rect.y = self.screen.get_height()-rect.height/2 - 100
        self.screen.blit(image, rect)

    
    def drawLoseDialog(self):
        
        self.screen.fill(white)
        content = 'Lose'
        text = pygame.font.Font('freesansbold.ttf', 96).render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width()*2 // 4, self.screen.get_height() // 5+30)
        self.screen.blit(text, textRect)

        content = 'The prince goes home in dissapointment.'
        text = self.font.render(content, True, blue, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width()*2 // 4, self.screen.get_height()*2 // 5+30)
        self.screen.blit(text, textRect)



        image = pygame.image.load('img/dog_cry.png')
        image = pygame.transform.rotozoom(image, 0, 0.6)
        rect = image.get_rect()
        rect.x = self.screen.get_width()*6/12 - rect.width/2 
        rect.y = self.screen.get_height()*2/3-rect.height/2 
        self.screen.blit(image, rect)



