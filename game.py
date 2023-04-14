import constants, pygame, gui
from typing import Tuple
import numpy as np

class Game:

    # Initializes member variable to default values
    board = None
    reset = None
    screen = None
    run = True
    x_turn = True
    gui = None
    play = True

    def __init__(self, board):
        # Initializes pygame
        pygame.init()
        # Sets the screen size to 1000x1000
        self.screen = pygame.display.set_mode((1000, 1000))
        # Sets the window title to TTT-AI
        pygame.display.set_caption("TTT-AI")

        # Sets the member board variable to the passed in board variable
        self.board = board
        # Creates a gui object from the GUI class
        self.gui = gui.Gui(screen = self.screen)

        # Sets the background of the screen as the background color from constants
        self.screen.fill(constants.BACKGROUND_COLOR)
        # Calls the create grid function that returns an empty 3x3 array of tiles
        board = self.gui.create_grid(board)

        # Creates the reset button by calling the create reset function from the GUI class
        self.reset = self.gui.create_reset()

    # Retuns if the current instance of the game is running    
    def end(self):
        return self.run
    
    # Returns if the game should be running or not
    def check_game(self, board):
        # Array that contains all combinations of 3 in a row in a 3x3 array
        check_list = []

        # Adds vertical links to the check list
        for i in range(0, 3):   
            check_list.append([board[0][i], board[1][i], board[2][i]])

        # Adds horizontal links to the check list
        for i in range(0, 3):
            check_list.append([board[i][0], board[i][1], board[i][2]])
            
        # Adds diagonal links to the check list
        check_list.append([board[0][0], board[1][1], board[2][2]])
        check_list.append([board[2][0], board[1][1], board[0][2]])

        # Loops through every link in the check list
        for check in check_list:
            # 3 tiles in the combination
            tile1 = check[0]
            tile2 = check[1]
            tile3 = check[2]
        
            # A magic square is a sqaure where every number 3 in a row will add up to x
            # Adds up the magic numbers of the 3 tiles
            result = tile1.get_magic_number() + tile2.get_magic_number() + tile3.get_magic_number()

            # If the tiles have a X, and X has won, then the magic numbers will add up to 15
            if(result == 15):
                # Calls the end screen from gui, with win passed in
                self.gui.draw_end("W")
                # Returns false because the game should not be running
                return False
            # If the tiles have a O, and O has won, then the magic numbers will add up to 30
            if(result == 30):
                # Calls the end screen from gui, with loose passed in
                self.gui.draw_end("L")
                # Returns false because the game should not be running
                return False

        # If the code gets to this point, then either the game has not finished yet or it has resulted in a tie
        # Counter that keeps track of any filled sqaures in the grid
        counter = 0
        for idx, tile in np.ndenumerate(board):
            # If the tile either a X or O
            if(tile.get_shape() != "-"):
                # Increments the counter
                counter += 1
        # If the counter equals the number of squares in the grid, then the game has resulted in a tie
        if(counter == 3**2):
            # Calls the end screen from gui, with tie passed in
            self.gui.draw_end("T")
            # Returns false because the game should not be running
            return False

        # If there is not a win, loose, or tie, then the game should be running so returns True
        return True
        
    # Returns the state of the reset button
    def get_reset(self):
        return self.reset

    # Function that should be called periodically
    # Handles all of the looping funcionality
    def periodic(self):
        # Loops through every event in the event queue
        for event in pygame.event.get():
            # Check if the event is of type QUIT
            if (event.type == pygame.QUIT):
                # If the event was of type QUIT, ends the main game loop
                self.run = False

            # If there was a mouse click
            if (event.type == pygame.MOUSEBUTTONUP):
                # Gets the position of the mouse
                pos = pygame.mouse.get_pos()
                # If the mouse has clicked the reset button
                if(self.reset.collidepoint(pos)):
                    # Sets the state of the reset button to true
                    self.reset = True
                # If the game should be running
                if(self.play):
                    # Loops through every tile in the board
                    for idx, tile in np.ndenumerate(self.board):
                        # Returns the position of the tile, relative to the positon
                        # [0][0] would be the top left, [2][2] would be the bottom right
                        relative_pos = tile.get_relative_pos()
                        # Gets the rectangle that represents the tile
                        rect = tile.get_rectangle()
                        # Gets the symbol (X or O) currently in the tile
                        shape = tile.get_shape()
                        # If the mouse clicked this specific tile
                        if (rect.collidepoint(pos)):
                            # If X is playing and the tile was empty
                            if(self.x_turn and shape == "-"):
                                # Sets the tile in the board to X
                                self.board[relative_pos[0]][relative_pos[1]].set_shape("X")
                                # Draws an X at the position of the rectangle
                                self.gui.draw_x(rect.center)
                            # If O is playing and the tile was empty
                            elif(not self.x_turn and shape == "-"):
                                # Sets the tile in the board to X
                                self.board[relative_pos[0]][relative_pos[1]].set_shape("O")
                                # Draws an X at the position of the rectangle
                                self.gui.draw_o(rect.center)
                            # If the shape was empty, then it switches the player playing
                            if(shape == "-"):
                                self.x_turn = not self.x_turn
                    # If the game should not be running
                    if(self.check_game(self.board) == False):
                        # Sets the play state of the game to False
                        self.play = False
                    # Returns if the game should be running or not
                    return self.check_game(self.board)
            # Updates the pygame display
            pygame.display.flip()
        # Returns a defualt value of True
        return True

        