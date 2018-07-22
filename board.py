import pygame
import ground
import rock
import metal
from array import *
import random
from pygame.locals import *


class Board(object):
    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        # Create the surface and pass in a tuple with its length and width
        self.squares = []
        self.breakableWallPosition = [[0 for i in range(11)] for j in range(11)]

    def createBoard(self, window):
        walls = []
        x = y = 0
        for i in range(11):
            for j in range(11):
                ground.Ground(x, y, window)
                x += 40

            y += 40
            x = 0

        x = y = 0
        for i in range(11):
            for j in range(11):
                if i % 2 != 0 and j % 2 != 0:
                    metal.Metal(x, y, window)
                    walls.append(pygame.Rect(x, y, 40, 40))
                x += 40

            y += 40
            x = 0
        x = y = 0
        for i in range(11):
            for j in range(11):
                if (i, j) == (0, 0) or (i, j) == (0, 1) or (i, j) == (1, 0):
                    x += 40
                    continue
                chanceRock = random.randint(1, 2)
                if not (i % 2 != 0 and j % 2 != 0):
                    if chanceRock == 1:
                        walls.append(pygame.Rect(x, y, 40, 40))
                        self.breakableWallPosition[j][i] = 1
                x += 40
            y += 40
            x = 0
        return walls

    def blitBoard(self, window):
        x = y = 0
        for i in range(11):
            for j in range(11):
                ground.Ground(x, y, window)
                x += 40

            y += 40
            x = 0

        x = y = 0
        for i in range(11):
            for j in range(11):
                if i % 2 != 0 and j % 2 != 0:
                    metal.Metal(x, y, window)
                x += 40

            y += 40
            x = 0

    def blitBreakableWalls(self, window):
        x = y = 0
        for i in range(11):
            for j in range(11):
                if self.breakableWallPosition[j][i] == 1:
                    rock.Rock(x, y, window)
                x += 40
            y += 40
            x = 0

    def createSquares(self, window):
        x = 0
        y = 0
        for i in range(0, 10):
            newSquareArray = []
            for j in range(0, 10):
                generatedGround = ground.Ground(x, y, window)
                newSquareArray.append(generatedGround)
                x += 40
            self.squares.append(newSquareArray)
            y += 40
            x = 0

    def createHurdles(self, window):
        for rowGround in self.squares:
            for colGround in rowGround:
                chanceRock = random.randint(1, 4)
                # a ajouter : function qui permet de checker qu'un obsctacle ne soit pas dans un coin
                if (chanceRock == 1):
                    colGround = rock.Rock(colGround.x, colGround.y, window)
