import game, tile
import numpy as np

board = np.array([tile.Tile() for _ in range(3**2)]).reshape(3, 3)
instance = game.Game(board)

run = True
game_instance = True
reset = False
while run:
    run = instance.end()
    game_instance = instance.periodic()
    reset = instance.get_reset()

    if(reset == True):
        board = np.array([tile.Tile() for _ in range(3**2)]).reshape(3, 3)
        instance = game.Game(board)