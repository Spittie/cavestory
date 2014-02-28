import pygame
from graphics import Graphics
from sprite import Sprite


class Game(object):
    def __init__(self, height=640, width=480, fps=60):
        self.height = height
        self.width = width
        self.fps = fps

        pygame.init()
        self.graphics = Graphics(self.height, self.width)
        self.clock = pygame.time.Clock()

        self.quote = Sprite("../con/MyChar.bmp", 0, 0, 32, 32)

    def __del__(self):
        pygame.quit()

    def eventloop(self):
        running = True



        while running:
            # Handle input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Handle everything else
            self.update()
            self.draw()

            # 60fps
            print (self.clock.get_fps())
            self.clock.tick(self.fps)

    def update(self):
        pass

    def draw(self):
        self.quote.draw(self.graphics, 55, 55)
        pygame.display.flip()