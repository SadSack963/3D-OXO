# 2-D OXO
# =======

from math import inf
import numpy as np
import os


def cls():
    # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_board():
    # TODO: Draw the test_state (2D)
    print(board)


def evaluate_board():
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


def check_for_winner(player):
    winner = evaluate_board()
    if winner:
        print(f"Player {player.symbol} wins!")
        return True
    if winner == 0:
        print("It's a tie!")
        return True


class HumanPlayer:
    def __init__(self, symbol: str, value: int):
        self.symbol = symbol
        self.value = value

    def get_move(self):
        """
        Accepts a space separated board position input by the player, and returns the integer values

        :param
        :return: (row, column)
        """
        # Get user input
        position = input(f"Player {self.symbol} position (row col): ").strip().split()
        # Check for two values
        if len(position) != 2:
            return -1, -1
        # Check for numbers only
        try:
            return int(position[0]), int(position[1])
        except ValueError:
            return -1, -1


class AIPlayer:
    def __init__(self, symbol: str, value: int):
        self.symbol = symbol
        self.value = value
        self.opposition_value = 2 if self.value == 1 else 1
        self.score = 1
        self.opposition_score = -1

    def get_move(self):
        """
        Finds the best possible move for the AI player using the minimax algorithm plus alpha-beta. \n

        https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

        :param
        :return: selected move: (row, column)
        """

        # https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

        # AI tests moves one by one and uses minimax to look ahead and decide upon the best move
        best_move = i, j = 0, 0  # This is only here to define the variables (to remove linter warnings below)
        best_score = -inf  # Maximizing player
        alpha = -inf
        beta = inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # check that the spot is free
                    board[i][j] = self.value  # make a test move
                    score = self.minimax(board, alpha, beta, maximizing=False)  # next player is Minimizing player
                    board[i][j] = 0  # undo the test move
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        print(f'AI move: {i} {j}')
        return best_move

    def minimax(self, test_state: np.ndarray, alpha: float, beta: float, maximizing: bool):
        """
        Test moves at every remaining position on the board to find the best possible move. \n
        Maximizing player (current AI player) looks for the highest score. \n
        Minimizing player (opposition) looks for the lowest score. \n

        https://www.youtube.com/watch?v=fT3YWCKvuQE \n
        https://github.com/kying18/tic-tac-toe

        :param test_state: state of the board during the test move
        :param alpha: best (highest) score so far for maximizing player
        :param beta: best (lowest) score so far for minimizing player
        :param maximizing: this player is maximizing (or minimizing)
        :return: best score for the current test move
        """

        # count the number of zero values in the board
        # add 1 because this is used as a multiplier and should never be zero
        free_spaces = 1 + np.count_nonzero(test_state == 0)

        # if the test board results in a win or draw, then return the score
        result = evaluate_board()  # check_win() returns 0 = Tie, 1 = Player 1 win, 2 = Player 2 win, or None
        if result == self.value:
            return self.score * free_spaces
        elif result == self.opposition_value:
            return self.opposition_score * free_spaces
        elif result == 0:
            return 0

        if maximizing:  # looking for the highest score
            best_score = -inf
            for i in range(3):
                for j in range(3):
                    if test_state[i][j] == 0:  # is the spot free
                        test_state[i][j] = self.value  # make a test move
                        score = self.minimax(test_state, alpha, beta, maximizing=False)  # next player is Minimizing player
                        test_state[i][j] = 0  # undo the test move
                        best_score = max(score, best_score)

                        # Maximizing: check score against beta, update alpha
                        if best_score >= beta:
                            return best_score
                        if best_score > alpha:
                            alpha = best_score

            return best_score

        else:  # looking for the lowest score
            best_score = inf
            for i in range(3):
                for j in range(3):
                    if test_state[i][j] == 0:  # is the spot free
                        test_state[i][j] = self.opposition_value  # make a test move
                        score = self.minimax(test_state, alpha, beta, maximizing=True)  # next player is Maximizing player
                        test_state[i][j] = 0  # undo the test move
                        best_score = min(score, best_score)

                        # Minimizing: check score against alpha, update beta
                        if best_score <= alpha:
                            return best_score
                        if best_score < beta:
                            beta = best_score

            return best_score


def main():
    # Game Loop
    end_game = False
    # player_1 = HumanPlayer('X', 1)
    # player_2 = AIPlayer('O', 2)

    player_2 = HumanPlayer('O', 2)
    player_1 = AIPlayer('X', 1)

    while not end_game:
        row, col = player_1.get_move()
        board[row][col] = player_1.value
        draw_board()
        end_game = check_for_winner(player_1)
        if end_game:
            break

        row, col = player_2.get_move()
        board[row][col] = player_2.value
        draw_board()
        end_game = check_for_winner(player_2)
        if end_game:
            break
    print('Thanks for playing.')


if __name__ == "__main__":
    # Define the matrix representing the game board
    board = np.zeros(shape=(3, 3), dtype=int)
    print(board)

    main()
