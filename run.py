import gui, tile
import numpy as np

board = np.array([tile.Tile() for _ in range(3**2)]).reshape(3, 3)
game = gui.GUI(board)

run = True
while run:
    run = game.periodic()