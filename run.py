import gui, tile
import numpy as np

board = np.array([tile.Tile() for _ in range(3**2)]).reshape(3, 3)
game = gui.GUI(board)

run = True
game_instance = True
while run:
    run = game.end()
    game_instance = game.periodic()