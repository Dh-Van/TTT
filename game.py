import constants, pygame, gui
from typing import Tuple
import numpy as np

class Game:

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

        self.board = board
        self.gui = gui.Gui(screen = self.screen)

        self.screen.fill(constants.BACKGROUND_COLOR)
        board = self.gui.create_grid(board)

        self.reset = self.gui.create_reset()

    
    def end(self):
        return self.run

    def check_game(self):
        check_list = []

        for i in range(0, 3):
            check_list.append([self.board[0][i], self.board[1][i], self.board[2][i]])

        for i in range(0, 3):
            check_list.append([self.board[i][0], self.board[i][1], self.board[i][2]])
            
        check_list.append([self.board[0][0], self.board[1][1], self.board[2][2]])
        check_list.append([self.board[2][0], self.board[1][1], self.board[0][2]])

        for check in check_list:
            tile1 = check[0]
            tile2 = check[1]
            tile3 = check[2]
        
            result = tile1.get_magic_number() + tile2.get_magic_number() + tile3.get_magic_number()

            if(result == 15):
                self.gui.draw_end("W")
                return False
            if(result == 30):
                self.gui.draw_end("L")
                return False

        counter = 0
        for idx, tile in np.ndenumerate(self.board):
            if(tile.get_shape() != "-"):
                counter += 1
        if(counter == 3**2):
            self.gui.draw_end("T")
            return False

        return True
        
    def get_reset(self):
        return self.reset

    def periodic(self):
        # Loops through every event in the event queue
        for event in pygame.event.get():
            # Check if the event is of type QUIT
            if (event.type == pygame.QUIT):
                # If the event was of type QUIT, ends the main game loop
                self.run = False

            if (event.type == pygame.MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                if(self.reset.collidepoint(pos)):
                    self.reset = True
                if(self.play):
                    for idx, tile in np.ndenumerate(self.board):
                        relative_pos = tile.get_relative_pos()
                        rect = tile.get_rectangle()
                        shape = tile.get_shape()
                        if (rect.collidepoint(pos)):
                            if(self.x_turn and shape == "-"):
                                self.board[relative_pos[0]][relative_pos[1]].set_shape("X")
                                self.gui.draw_x(rect.center)
                            elif(not self.x_turn and shape == "-"):
                                self.board[relative_pos[0]][relative_pos[1]].set_shape("O")
                                self.gui.draw_o(rect.center)
                            if(shape == "-"):
                                self.x_turn = not self.x_turn
                    if(self.check_game() == False):
                        print("test")
                        self.play = False
                    return self.check_game()
                
            pygame.display.flip()
        return True

        