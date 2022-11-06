import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)  # background
green = (0, 255, 0)  # font
blue = (0, 0, 128)  # font background

GoodContent = 'Ending'
BadContent = 'You lose'


class Ending():
    def __init__(self, game):
        self.screen = game.screen

        font = pygame.font.Font('freesansbold.ttf', 50)
        self.goodText = font.render(GoodContent, True, green, blue)
        self.goodTextRect = self.goodText.get_rect()  # x, y position
        self.goodTextRect.center = (self.screen.get_width() /
                                    2, self.screen.get_height() / 2)

        self.badText = font.render(BadContent, True, green, blue)
        self.badTextRect = self.badText.get_rect()  # x, y position
        self.badTextRect.center = (self.screen.get_width() /
                                   2, self.screen.get_height() / 2)

        return

    def drawDialog(self, isGoodEnding):
        self.screen.fill(white)
        if isGoodEnding:
            self.screen.blit(self.goodText, self.goodTextRect)
        else:
            self.screen.blit(self.badText, self.badTextRect)
