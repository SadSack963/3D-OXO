# 3-D OXO
# =======

import numpy as np


# Check for a winning combination
def check_win(user_id):
    # check each plane
    for pln in range(4):
        # Rows
        for row in range(4):
            if cube[pln][row][0] == cube[pln][row][1] == cube[pln][row][2] == cube[pln][row][3] == user_id:
                return user_id

        # Columns
        for col in range(4):
            if cube[pln][0][col] == cube[pln][1][col] == cube[pln][2][col] == cube[pln][3][col] == user_id:
                return user_id

        # Diagonals
        if cube[pln][0][0] == cube[pln][1][1] == cube[pln][2][2] == cube[pln][3][3] == user_id:
            return user_id

        if cube[pln][0][3] == cube[pln][1][2] == cube[pln][2][1] == cube[pln][3][0] == user_id:
            return user_id
    # TODO: check for vertical wins


# Get user input
def get_user_input(user_id):
    position = input(f"Player {symbols[user_id - 1]} position (plane row column): ").split(" ")
    pln = int(position[0])
    row = int(position[1])
    col = int(position[2])
    return pln, row, col


# TODO: Draw the board (3D)
def draw_board():
    print(cube)


# Define the matrix representing the game boundaries
cube = np.zeros(shape=(4, 4, 4), dtype=int)

symbols = ["X", "O"]
positions_free = cube.size

# Game Loop
game_on = True
while game_on:
    for user in [1, 2]:
        pln, row, col = get_user_input(user)
        while cube[pln][row][col] != 0:
            print("That position is already taken.")
            pln, row, col = get_user_input(user)
        cube[pln][row][col] = user
        positions_free -= 1
        draw_board()
        winner = check_win(user)
        if winner == user:
            print(f"Player {symbols[user - 1]} wins!")
            game_on = False
            break
        if positions_free == 0:
            print("It's a draw!")
            game_on = False
            break
