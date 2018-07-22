import pygame
import ground
import board
import player
from pygame.locals import *

pygame.init()
maxWidth = 440
maxHeight = 440

window = pygame.display.set_mode((maxWidth, maxHeight))

board = board.Board(maxWidth, maxHeight, window)
walls = board.createBoard(window)
pygame.display.flip()


player = player.Player(walls)


#exit manager
running = True
clock = pygame.time.Clock()

while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False

    board.blitBoard(window)
    board.blitBreakableWalls(window)
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    player.draw(window)
    pygame.display.update()
    clock.tick(40)

