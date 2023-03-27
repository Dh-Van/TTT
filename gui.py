from typing import Tuple
import pygame
import utils
from pygame.locals import *
import Rectangle

# Initializes pygame
pygame.init()
# Sets the screen size to 600x600
screen = pygame.display.set_mode((1000, 1000))
# Sets the window title to TTT-AI
pygame.display.set_caption("TTT-AI")

screen.fill("black")

board = [[0]*100]*100
rectList = []

base = Rectangle.centeredRect((500, 500), (500, 500), "X").getRect()

pygame.draw.rect(screen, "red", rect = base)

for x in range(330, 671, 170):
    for y in range(330, 671, 170):
        rect = Rectangle.centeredRect((x, y), (160, 160), "")
        rectList.append(rect)
        pygame.draw.rect(screen, "black", rect = rect.getRect())
        board[x//170][y//170] = rect

def drawX(center : Tuple[int, int]):
    pygame.draw.line(screen, "red", (center[0] - 60, center[1] - 60), (center[0] + 60, center[1] + 60), width=5)
    pygame.draw.line(screen, "red", (center[0] + 60, center[1] - 60), (center[0] - 60, center[1] + 60), width=5)

def drawO(center : Tuple[int, int]):
    pygame.draw.circle(screen, "red", center, 60, width=5)

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
            for r in rectList:
                if r.getRect().collidepoint(pos):
                    if(event.button == 1 and r.getShape() == ""):
                        r.setShape("X")
                    elif(event.button == 3 and r.getShape() == ""):
                        r.setShape("O")

            for r in rectList:
                if(r.getShape() == "X"):
                    drawX(r.getRect().center)
                elif(r.getShape() == "O"):
                    drawO(r.getRect().center)

        pygame.display.flip()
# Deactivates pygame
pygame.quit()

