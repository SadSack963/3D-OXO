# 2-D OXO
# =======

import numpy as np
import os
from human import HumanPlayer
from ai import AIPlayer
from evaluate_board_state import check_for_winner
from draw_screen import screen_setup, draw_outline, draw_x, draw_o, screen


def cls():
    # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_board():
    screen_setup()
    draw_outline()


def get_move(player):
    player.get_move(board)
    board[player.row][player.col] = player.value
    draw_move(player)
    return check_for_winner(player, board)


def draw_move(player):
    if player.value == 1:
        draw_x(player.row, player.col)
    else:
        draw_o(player.row, player.col)


def main():
    # Game Loop
    end_game = False

    player_1 = HumanPlayer(1)
    player_2 = HumanPlayer(2)

    # player_1 = HumanPlayer(1)
    # player_2 = AIPlayer(2)

    # player_1 = AIPlayer(1)
    # player_2 = HumanPlayer(2)

    # player_1 = AIPlayer(1)
    # player_2 = AIPlayer(2)

    draw_board()

    while not end_game:
        end_game = get_move(player_1)
        if end_game:
            break
        end_game = get_move(player_2)
        if end_game:
            break
    print('Thanks for playing.')


if __name__ == "__main__":
    # Define the matrix representing the game board
    board = np.zeros(shape=(3, 3), dtype=int)
    print(board)

    main()
    screen.exitonclick()
