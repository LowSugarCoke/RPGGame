import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


class PressSpace():
    def __init__(self, game):
        self.screen = game.screen
        self.frame = 0

    def showPressSpace(self):
        if(self.frame > 12 and self.frame < 24):
            font = pygame.font.Font('freesansbold.ttf', 25)
            content = 'Press Space'
            text = font.render(content, True, blue, green)
            textRect = text.get_rect()
            textRect.center = (self.screen.get_width() // 2,
                               self.screen.get_height()-30)
            self.screen.blit(text, textRect)
            self.frame += 1
        elif(self.frame == 24):
            self.frame = 0
        else:
            self.frame += 1
