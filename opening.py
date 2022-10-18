import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

content = 'Good game'

class Opening():
    def __init__(self, game):
        self.screen = game.screen
        font = pygame.font.Font('freesansbold.ttf', 32)

        self.text = font.render(content, True, green, blue)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
        self.drawDialog()
        return

    def drawDialog(self):
        self.screen.fill(white)
        self.screen.blit(self.text, self.textRect)