# 2-D OXO
# =======

from math import inf
import numpy as np
import os


def cls():
    # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def check_win(user_id):
    """
    Check for a winning combination

    :param user_id: player ID
    :return: None if no winner, otherwise user_id
    """



    # Rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == user_id:
            return user_id

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == user_id:
            return user_id

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == user_id:
        return user_id

    if board[0][2] == board[1][1] == board[2][0] == user_id:
        return user_id

    # Check if the board is full
    if np.all(board):
        return 0  # Tie
    else:
        return None  # Free spaces


def get_user_input(user_id):
    """
    Accepts a space separated board position input by the player, and returns the integer values

    :param user_id: player ID
    :return: (row, column)
    """
    # Get user input
    position = input(f"Player {symbols[user_id - 1]} position (row col): ").strip().split()
    # Check for two values
    if len(position) != 2:
        return -1, -1
    # Check for numbers only
    try:
        return int(position[0]), int(position[1])
    except ValueError:
        return -1, -1


def draw_board():
    # TODO: Draw the board (2D)
    print(board)


def ai_best_move():
    # minimax algorithm

    # AI to make it's move
    depth = 0  # number of moves to analyze in the tree (i.e. think depth moves ahead)
    best_score = -inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # check that the spot is free
                board[i][j] = ai  # make a test move
                score = minimax(board, depth, maximizing=False)  # next player is the human (maximizing)
                print(i, j, score)
                board[i][j] = 0  # undo the test move
                if score > best_score:
                    best_score = score
                    best_move = [i, j]

    return best_move[0], best_move[1]
    # board[best_move[0]][best_move[1]] = ai
    # current_player = human


def minimax(board, depth, maximizing):
    # Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm
    # https://www.youtube.com/watch?v=trKjYdBASyQ
    result = check_win(human)
    if result:
        return scores[result]

    if maximizing:  # ai is the maximizing player
        best_score = -inf
        # if depth < 0:
        #     return best_score
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # is the spot free
                    board[i][j] = ai  # make a test move
                    score = minimax(board, depth + 1, maximizing=False)  # next player is the ai (minimizing)
                    board[i][j] = 0  # undo the test move
                    best_score = max(score, best_score)
        return best_score

    else:  # human is the minimizing player
        best_score = inf
        # if depth < 0:
        #     return best_score
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # is the spot free
                    board[i][j] = human  # make a test move
                    score = minimax(board, depth + 1, maximizing=True)  # next player is the human (maximizing)
                    board[i][j] = 0  # undo the test move
                    best_score = min(score, best_score)
        return best_score


# Define the matrix representing the game board
board = np.zeros(shape=(3, 3), dtype=int)

symbols = ["X", "O"]

human = 1  # 'X'
ai = 2  # 'O'
scores = {
    1: 10,
    2: -10,
    0: 0
}


def main():
    # Game Loop
    positions_free = board.size
    game_on = True

    while game_on:
        for user in [human, ai]:
            if user == human:
                while True:
                    row, col = get_user_input(user)
                    if row < 0 or row > 2 or col < 0 or col > 2:
                        print('Invalid value. Try again.')
                    elif board[row][col] != 0:
                        print("That position is already taken.")
                    else:
                        break
            else:
                row, col = ai_best_move()
                print(f'AI move: {row} {col}')
            board[row][col] = user
            positions_free -= 1
            draw_board()
            winner = check_win(user)
            if winner == user:
                print(f"Player {symbols[user - 1]} wins!")
                game_on = False
                break
            if positions_free == 0:
                print("It's a tie!")
                game_on = False
                break


if __name__ == "__main__":
    main()
