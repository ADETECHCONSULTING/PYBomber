import pygame


class Bomb(pygame.sprite.Sprite):

    def __init__(self, x, y, window):
        super(Bomb, self).__init__()
        self.x = x
        self.y = y
        self.background = pygame.image.load("./resources/bomb.png").convert()
        self.rect = pygame.Rect(x, y, 40, 40)
        window.blit(self.background, (x, y))

    def draw(self, window):
        window.blit(self.background, (self.x, self.y))