import pygame
import square;
from pygame.locals import *

class Ground (square.Square):
    """
    Represent the ground
    """

    def __init__(self, x, y):
        super(Ground, self).__init__(x,y)
        self.background = pygame.image.load("ground.jpg").convert()