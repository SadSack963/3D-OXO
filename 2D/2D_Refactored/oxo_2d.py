# 2-D OXO
# =======

import numpy as np
from human import HumanPlayer
from ai import AIPlayer
from evaluate_board_state import check_for_winner
from draw_screen import DrawScreen
from options import Options


def draw_grid(screen):
    """
    Draw the game_state grid layout.

    :param screen: Tkinter window
    :return: nothing
    """
    screen.screen_setup()
    screen.draw_outline()


def choose_players():
    # TODO: Choose Player Type
    options = Options()
    players = options.player_dict
    print(players)
    if players['player_1'] == 'human':
        if players['player_2'] == 'human':
            return HumanPlayer(1), HumanPlayer(2)
        else:
            return HumanPlayer(1), AIPlayer(2)
    else:
        if players['player_2'] == 'human':
            return AIPlayer(1), HumanPlayer(2)
        else:
            return AIPlayer(1), AIPlayer(2)


def get_move(player, game_state, screen):
    """
    Get the move from the player passing the current game_state state to the player.
    Draw the move on the window.
    Finally check for a winner.

    :param game_state: The current state of the game
    :param screen: Tkinter window
    :param player: Human or AI player
    :return: bool True if the game is ending (either a winner or a tie)
    """
    if player.value == 1:
        player.get_move(screen, game_state)
    else:
        player.get_move(screen, game_state)

    board[player.row][player.col] = player.value
    draw_move(player, screen)
    return check_for_winner(player, board)


def draw_move(player, screen):
    """
    Draw the player's move on the window.

    :param screen: Tkinter window
    :param player: Human or AI player
    :return: nothing
    """
    if player.value == 1:
        screen.draw_x(player.row, player.col)
    else:
        screen.draw_o(player.row, player.col)


def main():
    # Game Loop
    end_game = False
    # This Tkinter window must be before drawing the Turtle screen
    # If the order is swapped, then you cannot choose the players
    # You cannot have two root Tkinter windows open at the same time
    player_1, player_2 = choose_players()
    screen = DrawScreen()
    draw_grid(screen)

    while not end_game:
        end_game = get_move(player_1, board, screen)
        if end_game:
            break
        end_game = get_move(player_2, board, screen)
        if end_game:
            break
    print('Thanks for playing.')
    screen.window.exitonclick()


if __name__ == "__main__":
    # Define the matrix representing the game game_state
    board = np.zeros(shape=(3, 3), dtype=int)
    main()
