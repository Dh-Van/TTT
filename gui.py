import pygame, tile, constants
from typing import Tuple
import numpy as np
from pygame.locals import *


class Gui:

    screen = None

    def __init__(self, screen):
        self.screen = screen

    def get_centered_rect(self, position : Tuple[int, int], size : Tuple[int, int]):
        rect = Rect(0, 0, 0, 0)
        rect.size = size
        rect.center = position
        return rect

    def create_grid(self, board):
        base = self.get_centered_rect((500, 500), (500, 500))
        pygame.draw.rect(self.screen, constants.GRID_COLOR, rect=base)

        for x in range(330, 671, 170):
            for y in range(330, 671, 170):
                rect = self.get_centered_rect((x, y), (160, 160))
                pygame.draw.rect(self.screen, constants.BACKGROUND_COLOR, rect = rect)
                t = tile.Tile((x , y), ((x//170) - 1, (y//170) - 1), "-", rect)
                board[(x//170) - 1][(y//170) - 1] = t

        return board
    
    def draw_x(self, center : Tuple[int, int]):
        pygame.draw.line(self.screen, constants.GRID_COLOR, (center[0] - 60, center[1] - 60), (center[0] + 60, center[1] + 60), width= constants.PIECE_THICKNESS)
        pygame.draw.line(self.screen, constants.GRID_COLOR, (center[0] + 60, center[1] - 60), (center[0] - 60, center[1] + 60), width= constants.PIECE_THICKNESS)

    def draw_o(self, center : Tuple[int, int]):
        pygame.draw.circle(self.screen, constants.GRID_COLOR, center, 60, width= constants.PIECE_THICKNESS)

    def draw_end(self, score):
        end = pygame.Surface((500, 500), pygame.SRCALPHA)
        font = pygame.font.Font("resources/LM.otf", 32)
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
        self.screen.blit(end, (250, 250))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def create_reset(self):
        i_reset = pygame.image.load('resources/reset.png')
        i_reset.convert()
        reset = i_reset.get_rect()
        reset.center = (500, 900)
        self.screen.blit(i_reset, reset)
        return reset