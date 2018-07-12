import pygame
import square;
from pygame.locals import *

class Ground (square.Square):
    """
    Represent the ground
    """

    def __init__(self, x, y, window):
        super(Ground, self).__init__(x,y)
        self.x = x
        self.y = y
        self.background = pygame.image.load("ground.jpg").convert()
        window.blit(self.background, (x, y))
