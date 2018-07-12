import pygame
import ground
import board
import player
from pygame.locals import *

pygame.init()
maxWidth = 480
maxHeight = 427

window = pygame.display.set_mode((maxWidth, maxHeight))

board = board.Board(maxWidth, maxHeight, window)
board.createSquares(window)
board.createHurdles(window)
pygame.display.flip()


player = player.Player()


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

    pressed_keys = pygame.key.get_pressed()
    window.blit(board.surface, (0, 0))
    player.update(pressed_keys)
    player.draw(window)
    # window.draw(player.surf, (400, 300))
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(40)

