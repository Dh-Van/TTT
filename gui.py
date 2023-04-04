import constants, pygame, utils, tile
from typing import Tuple
import numpy as np

class GUI:

    board = None
    screen = None
    run = True
    is_turn = True
    play = True

    def __init__(self, board):
        # Initializes pygame
        pygame.init()
        # Sets the screen size to 1000x1000
        self.screen = pygame.display.set_mode((1000, 1000))
        # Sets the window title to TTT-AI
        pygame.display.set_caption("TTT-AI")

        self.board = board

        self.screen.fill(constants.BACKGROUND_COLOR)
        self.createGrid()

    def createGrid(self):
        base = utils.get_centered_rect((500, 500), (500, 500))
        pygame.draw.rect(self.screen, constants.GRID_COLOR, rect=base)

        for x in range(330, 671, 170):
            for y in range(330, 671, 170):
                rect = utils.get_centered_rect((x, y), (160, 160))
                pygame.draw.rect(self.screen, constants.BACKGROUND_COLOR, rect = rect)
                t = tile.Tile((x , y), ((x//170) - 1, (y//170) - 1), "-", rect)
                self.board[(x//170) - 1][(y//170) - 1] = t

        # print(self.board)
    
    def drawX(self, center : Tuple[int, int]):
        pygame.draw.line(self.screen, constants.GRID_COLOR, (center[0] - 60, center[1] - 60), (center[0] + 60, center[1] + 60), width= constants.PIECE_THICKNESS)
        pygame.draw.line(self.screen, constants.GRID_COLOR, (center[0] + 60, center[1] - 60), (center[0] - 60, center[1] + 60), width= constants.PIECE_THICKNESS)

    def drawO(self, center : Tuple[int, int]):
        pygame.draw.circle(self.screen, constants.GRID_COLOR, center, 60, width= constants.PIECE_THICKNESS)

    def drawEnd(self, score):
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
        self.screen.blit(end, (250, 250))
        self.screen.blit(text, text_rect)



    def checkGame(self):
        checkList = []

        print(self.board[0][0].get_magic_number())

        for i in range(0, 3):
            checkList.append([self.board[0][i], self.board[1][i], self.board[2][i]])

        for i in range(0, 3):
            checkList.append([self.board[i][0], self.board[i][1], self.board[i][2]])
            
        checkList.append([self.board[0][0], self.board[1][1], self.board[2][2]])
        checkList.append([self.board[2][0], self.board[1][1], self.board[0][2]])

        for check in checkList:
            tile1 = check[0]
            tile2 = check[1]
            tile3 = check[2]
        
            result = tile1.get_magic_number() + tile2.get_magic_number() + tile3.get_magic_number()
            # print(result)

            if(result == 15):
                self.drawEnd("W")
                return False
            if(result == 30):
                self.drawEnd("L")
                return False

        counter = 0
        for idx, tile in np.ndenumerate(self.board):
            if(tile.get_shape() != "-"):
                counter += 1
        if(counter == 3**2):
            self.drawEnd("T")
            return False

        return True
        


    def periodic(self):
        # Loops through every event in the event queue
        for event in pygame.event.get():
            # Check if the event is of type QUIT
            if (event.type == pygame.QUIT):
                # If the event was of type QUIT, ends the main game loop
                return False

            if (event.type == pygame.MOUSEBUTTONUP):
                if(self.play):
                    pos = pygame.mouse.get_pos()
                    for idx, tile in np.ndenumerate(self.board):
                        relative_pos = tile.get_relative_pos()
                        rect = tile.get_rectangle()
                        shape = tile.get_shape()
                        if (rect.collidepoint(pos)):
                            if(self.is_turn and shape == "-"):
                                self.board[relative_pos[0]][relative_pos[1]].set_shape("X")
                                print(self.board[relative_pos[0]][relative_pos[1]].get_shape())
                                self.drawX(rect.center)
                            elif(not self.is_turn and shape == "-"):
                                self.board[relative_pos[0]][relative_pos[1]].set_shape("O")
                                self.drawO(rect.center)
                            if(shape == "-"):
                                self.is_turn = not self.is_turn
                    print(self.checkGame())
                
            pygame.display.flip()
        return True

        