import pygame, tile, constants
from typing import Tuple
import numpy as np
from pygame.locals import *

class Gui:
    # Initializes member variable to default values
    screen = None

    def __init__(self, screen):
        # Sets the member screen variable to the passed in screen variable
        self.screen = screen

    # Returns a rectangle at the position and size passed in
    def get_centered_rect(self, position : Tuple[int, int], size : Tuple[int, int]):
        # Creates an invisible rectangle at (0,0)
        rect = Rect(0, 0, 0, 0)
        # Sets the size of the rectangle to the size passed in
        rect.size = size
        # Sets the center of the rectangle to the position passed in
        rect.center = position
        # Returns the centered rectangle
        return rect

    # Creates a 3x3 grid
    def create_grid(self, board):
        # Creates a rectangle at the middle of the screen that is 500x500
        base = self.get_centered_rect((500, 500), (500, 500))
        # Draws the rectangle
        pygame.draw.rect(self.screen, constants.GRID_COLOR, rect=base)

        # Loops the centers of where every tile should be
        for x in range(330, 671, 170):
            for y in range(330, 671, 170):
                # Draws a rectangle at the center position that is 160x160
                rect = self.get_centered_rect((x, y), (160, 160))
                pygame.draw.rect(self.screen, constants.BACKGROUND_COLOR, rect = rect)
                # Creates a tile object with the (x, y) position, relative position to the grid, and an empty symbol
                t = tile.Tile((x , y), ((x//170) - 1, (y//170) - 1), "-", rect)
                # Sets the board at [x][y] to the tile created above
                board[(x//170) - 1][(y//170) - 1] = t
        # Returns the modified board
        return board
    
    # Draws 2 intersecting lines, with the center point being the passed in tuple, 120x120
    def draw_x(self, center : Tuple[int, int]):
        pygame.draw.line(self.screen, constants.GRID_COLOR, (center[0] - 60, center[1] - 60), (center[0] + 60, center[1] + 60), width= constants.PIECE_THICKNESS)
        pygame.draw.line(self.screen, constants.GRID_COLOR, (center[0] + 60, center[1] - 60), (center[0] - 60, center[1] + 60), width= constants.PIECE_THICKNESS)

    # Draws a circle with the center point being the passed in tuple, radius: 60
    def draw_o(self, center : Tuple[int, int]):
        pygame.draw.circle(self.screen, constants.GRID_COLOR, center, 60, width= constants.PIECE_THICKNESS)

    # Function to draw the end screen
    def draw_end(self, score):
        # Creates a surface that is compatible with rgba values
        end = pygame.Surface((500, 500), pygame.SRCALPHA)
        # Credit for font: https://www.dafont.com/mtheme.php?id=5
        # Creates a font using the LM.otf font
        font = pygame.font.Font("resources/LM.otf", 32)
        words = ""

        # If the player has won
        if(score == "W"):
            # Sets the color to the constant win color
            color = constants.WIN_COLOR
            # Sets the message to You Win
            words = "YOU WIN!"
        # If the player has lost
        elif(score == "L"):
            # Sets the color to the constant loose color
            color = constants.LOSE_COLOR
            # Sets the message to you lose
            words = "YOU LOSE."
        # If the player tied
        else:
            # Sets the color to the constant tie color
            color = constants.TIE_COLOR
            # Sets the message to tie
            words = "TIE"

        # Sets the text object to the words and constant grid color
        text = font.render(words, True, constants.GRID_COLOR)
        text_rect = text.get_rect()
        # Puts the text horizontally in the middle of the screen, and 1/4 of the way up
        text_rect.center = (1000 // 2, 250 // 2)

        # Fills the end surface with the win, loose, or tie color
        end.fill(color)
        # Adds the surface to the main screen
        self.screen.blit(end, (250, 250))
        # Adds the text to the main screen
        self.screen.blit(text, text_rect)
        # Updates the display
        pygame.display.flip()

    # Creates the reset button
    def create_reset(self):
        # Credit for image: https://icons8.com/icons/set/reset
        # Loads the reset.png
        i_reset = pygame.image.load('resources/reset.png')
        # Converts the image to rgba values that pygame can read
        i_reset.convert()
        # Puts the reset image at (500, 900)
        reset = i_reset.get_rect()
        reset.center = (500, 900)
        # Adds the reset image and reset button to the main screen
        self.screen.blit(i_reset, reset)
        # Retusn the reset button
        return reset