import pygame


class Graphics(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((self.height, self.width))
        pass

    def __del__(self):
        pass

    def blit(self, source, dest, area=None, special_flags=0):
        self.screen.blit(source, dest, area, special_flags)