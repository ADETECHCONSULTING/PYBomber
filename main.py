import pygame
import ground
import player
from pygame.locals import *

pygame.init()
maxWidth = 600
maxHeight = 600

window = pygame.display.set_mode((maxWidth,maxHeight))

# Create the surface and pass in a tuple with its length and width
board = pygame.Surface((maxWidth, maxHeight))
board.fill((122, 205, 185))
rect = board.get_rect()
window.blit(board, (0, 0))
pygame.display.flip()


player = player.Player()


#exit manager
running = True

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

    player.update(pressed_keys)

    window.blit(player.surf, (400, 300))
    pygame.display.flip()

