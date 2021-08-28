# 3-D OXO
# =======

import numpy as np
import os


def cls():
    # Cross-platform clear window
    os.system('cls' if os.name == 'nt' else 'clear')


def check_win(user_id):
    # Check for a winning combination

    # check each x-y plane
    for x in range(4):
        # Rows
        for y in range(4):
            if cube[x][y][0] == cube[x][y][1] == cube[x][y][2] == cube[x][y][3] == user_id:
                return user_id

        # Columns
        for z in range(4):
            if cube[x][0][z] == cube[x][1][z] == cube[x][2][z] == cube[x][3][z] == user_id:
                return user_id

        # Diagonals
        if cube[x][0][0] == cube[x][1][1] == cube[x][2][2] == cube[x][3][3] == user_id:
            return user_id

        if cube[x][0][3] == cube[x][1][2] == cube[x][2][1] == cube[x][3][0] == user_id:
            return user_id

    # check each x-z plane
    for x in range(4):
        # Rows
        for y in range(4):
            if cube[y][0][x] == cube[y][1][x] == cube[y][2][x] == cube[y][3][x] == user_id:
                return user_id

        # Columns
        for z in range(4):
            if cube[0][z][x] == cube[1][z][x] == cube[2][z][x] == cube[3][z][x] == user_id:
                return user_id

        # Diagonals
        if cube[0][0][x] == cube[1][1][x] == cube[2][2][x] == cube[3][3][x] == user_id:
            return user_id

        if cube[0][3][x] == cube[1][2][x] == cube[2][1][x] == cube[3][0][x] == user_id:
            return user_id

    # check each y-z plane
    for x in range(4):
        # Rows
        for y in range(4):
            if cube[0][x][y] == cube[1][x][y] == cube[2][x][y] == cube[3][x][y] == user_id:
                return user_id

        # Columns
        for z in range(4):
            if cube[z][x][0] == cube[z][x][1] == cube[z][x][2] == cube[z][x][3] == user_id:
                return user_id

        # Diagonals
        if cube[0][x][0] == cube[1][x][1] == cube[2][x][2] == cube[3][x][3] == user_id:
            return user_id

        if cube[3][x][0] == cube[2][x][1] == cube[1][x][2] == cube[0][x][3] == user_id:
            return user_id

    # Check cube diagonals
    if cube[0][0][0] == cube[1][1][1] == cube[2][2][2] == cube[3][3][3] == user_id:
        return user_id

    if cube[0][0][3] == cube[1][1][2] == cube[2][2][1] == cube[3][3][0] == user_id:
        return user_id

    if cube[0][3][0] == cube[1][2][1] == cube[2][1][2] == cube[3][0][3] == user_id:
        return user_id

    if cube[0][3][3] == cube[1][2][2] == cube[2][1][1] == cube[3][0][0] == user_id:
        return user_id


def get_user_input(user_id):
    # Get user input
    position = input(f"Player {symbols[user_id - 1]} position (plane row column): ").split(" ")
    pln = int(position[0])
    row = int(position[1])
    col = int(position[2])
    return pln, row, col


def draw_board():
    # TODO: Draw the test_state (3D)
    print(cube)


# Define the matrix representing the game boundaries
cube = np.zeros(shape=(4, 4, 4), dtype=int)

symbols = ["X", "O"]


def main():
    positions_free = cube.size

    # Game Loop
    game_on = True
    while game_on:
        for user in [1]:
            pln, row, col = get_user_input(user)
            while cube[pln][row][col] != 0:
                print("That position is already taken.")
                pln, row, col = get_user_input(user)
            cube[pln][row][col] = user
            positions_free -= 1
            cls()
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


if __name__ == "__main__":
    main()
