"""
This file is used to store global variables which can be imported into whichever file needs them.
"""

from messenger import Messenger
import numpy as np


# Define the matrix representing the game_state
board = np.zeros(shape=(3, 3), dtype=int)

# Define the Turtle used to write messages to the screen
player_msg = Messenger(
    font_size=24,
    font_type="bold italic",
)
