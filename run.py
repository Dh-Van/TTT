import game, tile
import numpy as np

# Creates a 3x3 array with empty tiles
board = np.array([tile.Tile() for _ in range(3**2)]).reshape(3, 3)
# Creates the initial game instance
instance = game.Game(board)

run = True
game_instance = True
reset = False
# While the players have not clicked the X button
while run:
    # Checks if the player has clicked the X button
    run = instance.end()
    # Updates the current game instance
    game_instance = instance.periodic()
    # Updates the reset state of the game
    reset = instance.get_reset()

    # If the game has been reset
    if(reset == True):
        # Remakes the 3x3 array
        board = np.array([tile.Tile() for _ in range(3**2)]).reshape(3, 3)
        # Creates a new game instance
        instance = game.Game(board)