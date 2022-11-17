import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)


class Level2Opening():
    def __init__(self, game):
        self.screen = game.screen
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        return

    def drawDialog(self):
        self.screen.fill(white)
        distance = 100
        # content
        font = pygame.font.Font('freesansbold.ttf',30)
        content = 'Level 2'
        text = font.render(content, True, black, white)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_width()/2 , self.screen.get_height()*1/2-150)
        self.screen.blit(text, textRect)

        # Swords man
        image = pygame.image.load('./Img/monster.gif')
        # image = pygame.transform.rotozoom(image, 0,3)
        self.swordsmanPosition = image.get_rect()
        self.swordsmanPosition.x =  self.screen.get_width()/2 -130
        self.swordsmanPosition.y =  self.screen.get_height()/2-130
        self.screen.blit(image, self.swordsmanPosition)




       

     