import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


content = 'CYCU x BME x RPG'


class Opening():
    def __init__(self, game):
        self.screen = game.screen
        font = pygame.font.Font('freesansbold.ttf', 32)

        self.text = font.render(content, True, blue, white)
        self.textRect = self.text.get_rect()
        self.textRect.center = (160, 80)
        self.drawDialog()
        return

    def drawDialog(self):
        # self.screen.fill(white)
        image = pygame.image.load('img/cover.jpg')
        image = pygame.transform.rotozoom(image, 0, 1)
        rect = image.get_rect()
        rect.x = 0
        rect.y = 100
        self.screen.blit(image, rect)

        self.screen.blit(self.text, self.textRect)
