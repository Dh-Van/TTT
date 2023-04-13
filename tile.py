from pygame.locals import Rect

class Tile:
    # Initializes member variable to default values
    world_pos = (0, 0)
    relative_pos = (0, 0)
    shape = "-"
    rectangle = Rect(0, 0, 0, 0)
    
    magic_number = 0
    scalar = 0

    def __init__(self, world_pos = (0, 0), relative_pos = (-1,-1) , shape = "-", rectangle = Rect(0, 0, 0, 0)):
        # Sets the member variables to the passed in variables
        self.world_pos = world_pos
        self.relative_pos = relative_pos
        self.shape = shape
        self.rectangle = rectangle
        
        # Sets the magic number based on the relative pos
        # A magic square is a sqaure where every number 3 in a row will add up to x, x = 15
        if (self.relative_pos == (0, 0)):
            self.magic_number = 8
        elif (self.relative_pos == (1, 0)):
            self.magic_number = 1
        elif (self.relative_pos == (2, 0)):
            self.magic_number = 6
        elif (self.relative_pos == (0, 1)):
            self.magic_number = 3
        elif (self.relative_pos == (1, 1)):
            self.magic_number = 5
        elif (self.relative_pos == (2, 1)):
            self.magic_number = 7
        elif (self.relative_pos == (0, 2)):
            self.magic_number = 4
        elif (self.relative_pos == (1, 2)):
            self.magic_number = 9
        elif (self.relative_pos == (2, 2)):
            self.magic_number = 2

    # Sets the shape and scalar of the tile
    def set_shape(self, shape):
        self.shape = shape
        # If the shape is X, sets the scalar to 1
        if(self.shape == "X"):
            self.scalar = 1
        # If the shape is O, sets the scalar to 2
        elif(self.shape == "O"):
            self.scalar = 2
        else:
            self.scalar = 0

    # Returns the x, y coordinate of the tile
    def get_world_pos(self):
        return self.world_pos

    # Returns the relative position of the tile
    def get_relative_pos(self):
        return self.relative_pos

    # Returns the rectangle that represents the tile
    def get_rectangle(self):
        return self.rectangle

    # Returns the shape that the tile has right now (X, O)
    def get_shape(self):
        return self.shape

    # Returns the magic number of the tile multipled by the scalar
    def get_magic_number(self):
        return self.magic_number * self.scalar