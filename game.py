import pygame
from monster import Monster
from adventurer import Adventurer
from attack import Attack


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

        print(pygame.display.get_surface().get_size())

        self.monster = Monster(self)
        self.adventorer = Adventurer(self)
        self.attack = Attack(self)
        i = 0
        while not crashed:

            clock.tick(10)
            pygame.display.flip()

            self.monster.blitme()
            self.adventorer.blitme()
            self.attack.blitme(i)
            i = i+1
            if(i == 12):
                i = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    print(event)
                    pygame.display.update()

                    pygame.quit()
                    quit()
