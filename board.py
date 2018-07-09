import pygame
import ground;
from pygame.locals import *

class Board (object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.arraySquare = []

    '''
    fonction de test
    '''
    def mapCreation(self):
        x = 0
        y = 0
        i = 0
        while i < self.width:
            self.arraySquare[i] = ground.Ground(x, y)
            x += 40
            i += 40