
import numpy as np


def evaluate_board(board):
    """
    Check for a winning combination

    :return: Value of the winning pieces, zero if a tie, None if test_state is not full and no winner
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


def check_for_winner(player, board):
    winner = evaluate_board(board)
    if winner:
        print(f"Player {player.value} wins!")
        return True
    if winner == 0:
        print("It's a tie!")
        return True
