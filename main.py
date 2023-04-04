import pygame
import utils
import numpy as np
import tile
from typing import Tuple
import constants

# Initializes pygame
pygame.init()
# Sets the screen size to 1000x1000
screen = pygame.display.set_mode((1000, 1000))
# Sets the window title to TTT-AI
pygame.display.set_caption("TTT-AI")

screen.fill(constants.BACKGROUND_COLOR)

base = utils.get_centered_rect((500, 500), (500, 500))
pygame.draw.rect(screen, constants.GRID_COLOR, rect=base)

# reset = utils.get_centered_rect((500, 900), (100, 100))
i_reset = pygame.image.load('reset.png')
i_reset.convert()
reset = i_reset.get_rect()
reset.center = (500, 900)
screen.blit(i_reset, reset)

board = np.array([tile.Tile() for _ in range(3**2)]).reshape(3, 3)

for x in range(330, 671, 170):
    for y in range(330, 671, 170):
        rect = utils.get_centered_rect((x, y), (160, 160))
        pygame.draw.rect(screen, constants.BACKGROUND_COLOR, rect = rect)
        t = tile.Tile((x , y), ((x//170) - 1, (y//170) - 1), "-", rect)
        board[(x//170) - 1][(y//170) - 1] = t

def drawX(center : Tuple[int, int]):
    pygame.draw.line(screen, constants.GRID_COLOR, (center[0] - 60, center[1] - 60), (center[0] + 60, center[1] + 60), width= constants.PIECE_THICKNESS)
    pygame.draw.line(screen, constants.GRID_COLOR, (center[0] + 60, center[1] - 60), (center[0] - 60, center[1] + 60), width= constants.PIECE_THICKNESS)

def drawO(center : Tuple[int, int]):
    pygame.draw.circle(screen, constants.GRID_COLOR, center, 60, width= constants.PIECE_THICKNESS)

def drawEnd(score):
    end = pygame.Surface((500, 500), pygame.SRCALPHA)
    font = pygame.font.Font("LM.otf", 32)
    words = ""

    if(score == "W"):
        color = constants.WIN_COLOR
        words = "YOU WIN!"
    elif(score == "L"):
        color = constants.LOSE_COLOR
        words = "YOU LOSE."
    else:
        color = constants.TIE_COLOR
        words = "TIE"

    text = font.render(words, True, constants.GRID_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000 // 2, 250 // 2)

    end.fill(color)
    screen.blit(end, (250, 250))
    screen.blit(text, text_rect)



def checkGame():
    checkList = []
    for i in range(0, 3):
        checkList.append([board[0][i], board[1][i], board[2][i]])

    for i in range(0, 3):
        checkList.append([board[i][0], board[i][1], board[i][2]])
        
    checkList.append([board[0][0], board[1][1], board[2][2]])
    checkList.append([board[2][0], board[1][1], board[0][2]])

    for check in checkList:
        tile1 = check[0]
        tile2 = check[1]
        tile3 = check[2]
    
        result = tile1.get_magic_number() + tile2.get_magic_number() + tile3.get_magic_number()
    
        if(result == 15):
            drawEnd("W")
            return False
        if(result == 30):
            drawEnd("L")
            return False

    counter = 0
    for idx, tile in np.ndenumerate(board):
        if(tile.get_shape() != "-"):
            counter += 1
    if(counter == 3**2):
        drawEnd("T")
        return False

    return True
    

run = True
is_turn = True
play = True

# Main game loop
while run:
    # Loops through every event in the event queue
    for event in pygame.event.get():
        # Check if the event is of type QUIT
        if (event.type == pygame.QUIT):
            # If the event was of type QUIT, ends the main game loop
            run = False

        if (event.type == pygame.MOUSEBUTTONUP):
            if(play):
                pos = pygame.mouse.get_pos()
                for idx, tile in np.ndenumerate(board):
                    relative_pos = tile.get_relative_pos()
                    rect = tile.get_rectangle()
                    shape = tile.get_shape()
                    if (rect.collidepoint(pos)):
                        if(is_turn and shape == "-"):
                            board[relative_pos[0]][relative_pos[1]].set_shape("X")
                            drawX(rect.center)
                        elif(not is_turn and shape == "-"):
                            board[relative_pos[0]][relative_pos[1]].set_shape("O")
                            drawO(rect.center)
                        if(shape == "-"):
                            is_turn = not is_turn
                play = checkGame()
            
        pygame.display.flip()
# Deactivates pygame
pygame.quit()
