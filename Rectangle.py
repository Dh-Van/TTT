from typing import Tuple

from pygame import Rect

class centeredRect:

    position = [0, 0]
    size = [0, 0]
    shape = ""
        
    def __init__(self, position : Tuple[int, int], size : Tuple[int, int], shape : str):
        self.position = position
        self.size = size
        self.shape = shape

    def getRect(self):
        rect = Rect(0, 0, 0, 0)
        rect.size = self.size
        rect.center = self.position
        return rect

    def setShape(self, shape):
        self.shape = shape

    def getShape(self):
        return self.shape
