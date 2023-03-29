from typing import Tuple

from pygame import Rect

class centeredRect:

    position = [0, 0]
    size = [0, 0]
    relPos = [0, 0]
        
    def __init__(self, position : Tuple[int, int], size : Tuple[int, int], relPos : Tuple[int, int]):
        self.position = position
        self.size = size
        self.relPos = relPos

    def getRect(self):
        rect = Rect(0, 0, 0, 0)
        rect.size = self.size
        rect.center = self.position
        return rect

    def getRelPos(self):
        return self.relPos
