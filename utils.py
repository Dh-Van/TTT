import pygame
from pygame.locals import *
from typing import Tuple

def get_centered_rect(position : Tuple[int, int], size : Tuple[int, int]):
    rect = Rect(0, 0, 0, 0)
    rect.size = size
    rect.center = position
    return rect