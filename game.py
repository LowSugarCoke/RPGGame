import pygame


class RPGGame:
    def __init__(self, w=1920, h=1080):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('RPG Game')
