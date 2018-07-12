import pygame

from pygame.locals import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./resources/player_1.png")
        self.player1W = self.surf.get_width()
        self.player1H = self.surf.get_height()
        self.rect = self.surf.get_rect()
        self.x = 0
        self.y = 0

    def update(self, pressed_keys):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.y -= 5
        if pressed_keys[K_DOWN]:
            self.y += 5
        if pressed_keys[K_LEFT]:
            self.x -= 5
        if pressed_keys[K_RIGHT]:
            self.x += 5

    def _set_x(self, x):
        if x < 0:
            x = 0
        if x > 480 - self.player1W:
            x = 480 - self.player1W
        self._x = x

    def _get_x(self):
        return self._x

    def _set_y(self, y):
        if y < 0:
            y = 0
        if y > 427 - self.player1H:
            y = 427 - self.player1H
        self._y = y

    def _get_y(self):
        return self._y

    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.surf, (self.x, self.y))
