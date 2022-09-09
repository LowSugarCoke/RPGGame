import pygame


class RPGGame:
    def __init__(self, w=800, h=600):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('RPG Game')
        clock = pygame.time.Clock()
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    print(event)
                    pygame.display.update()
                    clock.tick(60)
                    pygame.quit()
                    quit()
