import pygame
import os

class Sprite(object):
    def __init__(self, file_path, source_x, source_y, width, height):
        self.image = pygame.image.load(file_path).convert()
        self.source_rect = pygame.Rect(source_x, source_y, width, height)

    def __del__(self):
        pass

    def draw(self, graphics, x, y):
        graphics.blit(self.image, (x,y), area=self.source_rect)