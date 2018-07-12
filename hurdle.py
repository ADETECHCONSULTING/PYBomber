import square
import pygame

class Hurdle (square.Square):

    def __init__(self, x, y, window):
        super(Hurdle, self).__init__(x, y)
        self.background = pygame.image.load("bomb.png").convert()
        window.blit(self.background, (x, y))