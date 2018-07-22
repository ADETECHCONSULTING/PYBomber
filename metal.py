import square
import pygame


class Metal(pygame.sprite.Sprite):

    def __init__(self, x, y, window):
        super(Metal, self).__init__()
        self.x = x
        self.y = y
        self.background = pygame.image.load("./resources/metal.jpg").convert()
        self.rect = pygame.Rect(x, y, 40, 40)
        window.blit(self.background, (x, y))
