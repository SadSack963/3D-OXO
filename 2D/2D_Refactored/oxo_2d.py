# 2-D OXO
# =======

import numpy as np
from human import HumanPlayer
from ai import AIPlayer
from evaluate_board_state import check_for_winner
from draw_screen import screen_setup, draw_outline, draw_x, draw_o, screen
from options import Options


def draw_grid():
    """
    Draw the game_state grid layout.

    :return: nothing
    """
    screen_setup()
    draw_outline()


def choose_players():
    # TODO: Choose Player Type
    options = Options()
    print(options)

    exit()
    return HumanPlayer(1), HumanPlayer(2)

    # return HumanPlayer(1), AIPlayer(2)
    #
    # return AIPlayer(1), HumanPlayer(2)
    #
    # return AIPlayer(1), AIPlayer(2)


def get_move(player):
    """
    Get the move from the player passing the current game_state state to the player.
    Draw the move on the screen.
    Finally check for a winner.

    :param player: Human or AI player
    :return: bool True if the game is ending (either a winner or a tie)
    """
    player.get_move(board)
    board[player.row][player.col] = player.value
    draw_move(player)
    return check_for_winner(player, board)


def draw_move(player):
    """
    Draw the player's move on the screen.

    :param player: Human or AI player
    :return: nothing
    """
    if player.value == 1:
        draw_x(player.row, player.col)
    else:
        draw_o(player.row, player.col)


def main():
    # Game Loop
    end_game = False
    player_1, player_2 = choose_players()
    draw_grid()

    while not end_game:
        end_game = get_move(player_1)
        if end_game:
            break
        end_game = get_move(player_2)
        if end_game:
            break
    print('Thanks for playing.')


if __name__ == "__main__":
    # Define the matrix representing the game game_state
    board = np.zeros(shape=(3, 3), dtype=int)
    main()
    screen.exitonclick()
