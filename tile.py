from pygame.locals import Rect

class Tile:
    world_pos = (0, 0)
    relative_pos = (0, 0)
    shape = "-"
    rectangle = Rect(0, 0, 0, 0)
    
    magic_number = 0
    scalar = 0

    def __init__(self, world_pos = (0, 0), relative_pos = (-1,-1) , shape = "-", rectangle = Rect(0, 0, 0, 0)):
        self.world_pos = world_pos
        self.relative_pos = relative_pos
        self.shape = shape
        self.rectangle = rectangle
        
        if (self.relative_pos == (0, 0)):
            self.magicNumber = 8
        elif (self.relative_pos == (1, 0)):
            self.magicNumber = 1
        elif (self.relative_pos == (2, 0)):
            self.magicNumber = 6
        elif (self.relative_pos == (0, 1)):
            self.magicNumber = 3
        elif (self.relative_pos == (1, 1)):
            self.magicNumber = 5
        elif (self.relative_pos == (2, 1)):
            self.magicNumber = 7
        elif (self.relative_pos == (0, 2)):
            self.magicNumber = 4
        elif (self.relative_pos == (1, 2)):
            self.magicNumber = 9
        elif (self.relative_pos == (2, 2)):
            self.magicNumber = 2

    def set_shape(self, shape):
        self.shape = shape
        if(self.shape == "X"):
            self.scalar = 1
        elif(self.shape == "O"):
            self.scalar = 2
        else:
            self.scalar = 0

    def get_world_pos(self):
        return self.world_pos

    def get_relative_pos(self):
        return self.relative_pos

    def get_rectangle(self):
        return self.rectangle

    def get_shape(self):
        return self.shape

    def get_magic_number(self):
        return self.magicNumber * self.scalar
