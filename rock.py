import square
import pygame

class Rock (square.Square):

    def __init__(self, x, y, window):
        super(Rock, self).__init__(x, y)
        self.background = pygame.image.load("./resources/rock.png").convert()
        window.blit(self.background, (x, y))