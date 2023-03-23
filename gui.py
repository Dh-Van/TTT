import pygame
import utils
from pygame.locals import *

# Initializes pygame
pygame.init()
# Sets the screen size to 600x600
screen = pygame.display.set_mode((1000, 1000))
# Sets the window title to TTT-AI
pygame.display.set_caption("TTT-AI")

pygame.draw.rect(screen, "red", rect = utils.get_centered_rect((500, 500), (500, 500)))
# pygame.draw.rect(screen, "black", rect = utils.get_centered_rect((300, 300), (199, 199)))

 
collisionList = []
rectList = []

for x in range(300, 700, 200):
    for y in range(300, 700, 200):
        pygame.draw.rect(screen, "black", rect = utils.get_centered_rect((x, y), (200, 200)))

run = True

# Main game loop
while run:
    # Loops through every event in the event queue
    for event in pygame.event.get():
        # Check if the event is of type QUIT
        if(event.type == pygame.QUIT):
            # If the event was of type QUIT, ends the main game loop
            run = False

        if(event.type == pygame.MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            print(pos)

        pygame.display.flip()
# Deactivates pygame
pygame.quit()

