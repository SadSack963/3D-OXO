# Define the matrix representing the game boundaries
# A position is defined by two coordinates:
#     [row, column] = [front->back, left->right] from a top-down view
# A row is 4 locations, forming a 3 x 1 array
# A board ia 4 rows, forming a 3 x 3 grid
# row = [
#     0,
#     0,
#     0
# ]
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Change the value of a single position in the board
x = 2  # 3rd position right
z = 1  # 2nd row back

board[z][x] = 2
print(board)
"""
[[0, 0, 0], [0, 0, 2], [0, 0, 0]]
"""

# TODO: Define the winning combinations
# Rows
for row in range(3):
    if board[row][0] == board[row][1] == board[row][2] == 1:
        print("X win")
    elif board[row][0] == board[row][1] == board[row][2] == 2:
        print("O win")

# Columns
for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] == 1:
        print("X win")
    elif board[0][col] == board[1][col] == board[2][col] == 2:
        print("O win")

# Diagonals
if board[0][0] == board[1][1] == board[2][2] == 1:
    print("X win")
elif board[0][0] == board[1][1] == board[2][2] == 2:
    print("O win")

if board[0][2] == board[1][1] == board[2][0] == 1:
    print("X win")
elif board[0][2] == board[1][1] == board[2][0] == 2:
    print("O win")


# TODO: Draw the board (2D)

# TODO: Get user1 input

# TODO: Draw the user1 choice on the board

# TODO: Detect a win

# TODO: Get user2 input

# TODO: Draw the user2 choice on the board

# TODO: Detect a win
