import pygame
from monster import Monster


class RPGGame:
    def __init__(self, w=800, h=600):
        pygame.init()
        self.w = w
        self.h = h

        # init display
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('RPG Game')
        clock = pygame.time.Clock()
        crashed = False

        self.monster = Monster(self)
        while not crashed:
            pygame.display.flip()
            self.monster.blitme()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    print(event)
                    pygame.display.update()
                    clock.tick(60)
                    pygame.quit()
                    quit()
