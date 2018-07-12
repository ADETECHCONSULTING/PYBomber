import pygame
import ground
import rock
from array import *
import random
from pygame.locals import *

class Board (object):
    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        # Create the surface and pass in a tuple with its length and width
        self.surface = pygame.image.load("./resources/backgroundarena.png")
        self.rect = self.surface.get_rect()
        window.blit(self.surface, (0, 0))
        self.squares = []


    def createSquares(self, window):
        x = 30
        y = 30
        for i in range(0, 20):
            newSquareArray = []
            for j in range(0, 20):
                generatedGround = ground.Ground(x, y, window)
                newSquareArray.append(generatedGround)
                x += 30
            self.squares.append(newSquareArray)
            y += 30
            x = 30

    def createHurdles(self, window):
        for rowGround in self.squares:
            for colGround in rowGround:
                chanceRock = random.randint(1,20)
                #a ajouter : function qui permet de checker qu'un obsctacle ne soit pas dans un coin
                if(chanceRock == 5):
                    colGround = rock.Rock(colGround.x, colGround.y, window)





