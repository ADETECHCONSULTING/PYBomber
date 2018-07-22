import pygame
import square;
from pygame.locals import *


class Ground(pygame.sprite.Sprite):
    """
    Represent the ground
    """

    def __init__(self, x, y, window):
        super(Ground, self).__init__()
        self.x = x
        self.y = y
        self.background = pygame.image.load("./resources/ground.jpg").convert()
        window.blit(self.background, (x, y))
