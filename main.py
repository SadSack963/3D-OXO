# Define the matrix representing the game boundaries
# A position is defined by three coordinates:
#     [board, row, column] = [up->down, front->back, left->right] from a front view
# A row is 4 locations, forming a 4 x 1 array
# A board ia 4 rows, forming a 4 x 4 grid
# A cube is 4 boards stacked one on top of another, forming a 4 x 4 x 4 cube
# row = [
#     0,
#     0,
#     0,
#     0
# ]
# board = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]
cube = [
    #   row 0         row 1         row 2         row 3
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # board 0
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # board 1
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # board 2
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]   # board 3
]

# Change the value of a single position in the cube
x = 3  # 4th position right
y = 2  # 3rd board down
z = 1  # 2nd row back

cube[y][z][x] = 2
print(f'{cube = }')

"""
cube = [
    #   row 0         row 1         row 2         row 3
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # board 0
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # board 1
    [[0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0]],  # board 2
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]   # board 3
]
"""

# TODO: Define the winning combinations


# TODO: Draw the board (2D)

# TODO: Get user1 input

# TODO: Draw the user1 choice on the board

# TODO: Detect a win

# TODO: Get user2 input

# TODO: Draw the user2 choice on the board

# TODO: Detect a win
