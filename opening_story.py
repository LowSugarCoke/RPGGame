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

        self.drawDialog()
        return

    def drawDialog(self):

        self.screen.fill(white)

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