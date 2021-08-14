# 2-D OXO
# =======

from math import inf
import numpy as np
import os


def cls():
    # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_input(player):
    """
    Accepts a space separated board position input by the player, and returns the integer values

    :param player: player ID
    :return: (row, column)
    """
    # Get user input
    position = input(f"Player {symbols[player]} position (row col): ").strip().split()
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


def check_win():
    """
    Check for a winning combination

    :return: Value of the winning pieces, zero if a tie, None if board is not full and no winner
    """

    # Rows
    for row in range(3):
        if board[row][0] != 0 and board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            return board[row][0]

    # Columns
    for col in range(3):
        if board[0][col] != 0 and board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            return board[0][col]

    # Diagonals
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]

    if board[0][2] != 0 and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]

    # Check if the board is full
    if np.all(board):
        return 0  # Tie
    else:
        return None  # Free spaces remaining


def ai_best_move():
    # minimax algorithm

    # AI tests moves and uses minimax to decide upon the best move
    depth = 3  # number of moves to analyze in the tree (i.e. think depth moves ahead)
    best_score = -inf
    best_move = [0, 0]
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # check that the spot is free
                board[i][j] = players['ai']  # make a test move
                # AI is the Maximizing player
                # Human is the Minimizing player
                score = minimax(board, depth, maximizing=False)  # Human is the next player
                board[i][j] = 0  # undo the test move
                if score > best_score:
                    best_score = score
                    best_move = [i, j]

    return best_move[0], best_move[1]


def minimax(board, depth, maximizing):
    # Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm
    # https://www.youtube.com/watch?v=trKjYdBASyQ
    result = check_win()
    if result:
        return scores[result]
    # if depth == 0:
    #     return 0  # Tie

    if maximizing:  # ai is the maximizing player (looking for the highest score)
        best_score = -inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # is the spot free
                    board[i][j] = players['ai']  # make a test move
                    score = minimax(board, depth - 1, maximizing=False)  # Human is the next player
                    board[i][j] = 0  # undo the test move
                    best_score = max(score, best_score)
        return best_score

    else:  # human is the minimizing player (looking for the lowest score)
        best_score = inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # is the spot free
                    board[i][j] = players['human']  # make a test move
                    score = minimax(board, depth - 1, maximizing=True)  # AI is the next player
                    board[i][j] = 0  # undo the test move
                    best_score = min(score, best_score)
        return best_score


def main():
    # Game Loop
    game_on = True

    while game_on:
        for player in players:
            current_player = players[player]
            if current_player == players['human']:
                while True:
                    row, col = get_user_input(current_player)
                    if row < 0 or row > 2 or col < 0 or col > 2:
                        print('Invalid value. Try again.')
                    elif board[row][col] != 0:
                        print("That position is already taken.")
                    else:
                        break
            else:
                row, col = ai_best_move()
                print(f'AI move: {row} {col}')
            board[row][col] = current_player
            draw_board()
            winner = check_win()
            print(f'{winner = }')
            if winner == current_player:
                print(f"Player {symbols[current_player]} wins!")
                game_on = False
                break
            if winner == 0:
                print("It's a tie!")
                game_on = False
                break
    print('Thanks for playing.')


# Define the matrix representing the game board
board = np.zeros(shape=(3, 3), dtype=int)
# board = np.array([
#             [1, 0, 0],
#             [0, 0, 1],
#             [2, 2, 0]
#         ])
print(board)

# human = 1  # 'X'
# ai = 2  # 'O'
players = {"human": 1, "ai": 2}
symbols = {players['human']: "X", players['ai']: "O"}
scores = {
    players['human']: - 10,
    players['ai']: 10,
    0: 0  # Tie
}


if __name__ == "__main__":
    main()
