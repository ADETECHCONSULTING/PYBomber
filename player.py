import pygame

from pygame.locals import *


class Player(pygame.sprite.Sprite):

    def __init__(self, walls):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./resources/player_1.png")
        self.player1W = self.surf.get_width()
        self.player1H = self.surf.get_height()
        self.rect = self.surf.get_rect()
        self.walls = walls

    def update(self, pressed_keys):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.move(0, -5)
        if pressed_keys[K_DOWN]:
            self.move(0, 5)
        if pressed_keys[K_LEFT]:
            self.move(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.move(5, 0)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        if self.rect.x + dx < 0 or self.rect.x + dx > 440 or self.rect.y + dy < 0 or self.rect.y + dy > 440:
            return

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in self.walls:
            if self.rect.colliderect(wall):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.bottom

    def _set_x(self, x):
        if x < 0:
            self.rect.x = 0
        if x > 440 - self.player1W:
            self.rect.x = 440 - self.player1W
        self.rect.x = x

    def _get_x(self):
        return self._x

    def _set_y(self, y):
        if y < 0:
            self.rect.y = 0
        if y > 440 - self.player1H:
            self.rect.y = 440 - self.player1H
        self.rect.y = y

    def _get_y(self):
        return self._y

    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.surf, (self.rect.left, self.rect.top))
