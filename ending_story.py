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


