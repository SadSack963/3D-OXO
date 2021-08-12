# 3-D OXO
# =======

import numpy as np

# Define the matrix representing the game boundaries
cube = np.zeros(shape=(4, 4, 4), dtype=int)

# Change the value of a single position in the cube
x = 3  # 4th position right
y = 2  # 3rd board down
z = 1  # 2nd row back

cube[y][z][x] = 2
print(f'{cube = }')
"""
cube = array([
   [[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]],

   [[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]],

   [[0, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 0, 0],
    [0, 0, 0, 0]],

   [[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]
])
"""

# TODO: Define the winning combinations


# TODO: Draw the board (2D)

# TODO: Get user1 input

# TODO: Draw the user1 choice on the board

# TODO: Detect a win

# TODO: Get user2 input

# TODO: Draw the user2 choice on the board

# TODO: Detect a win
