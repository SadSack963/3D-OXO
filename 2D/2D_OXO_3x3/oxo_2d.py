# 2-D OXO - 3x3 board
# ===================

"""
This program uses a Tkinter window to choose the Players.
Then a Turtle graphics window is used for the game play.
"""

import global_vars
from human import HumanPlayer
from ai import AIPlayer
from evaluate_board_state import check_for_winner
from options import Options
from draw_screen import DrawScreen


def draw_grid(screen):
    """
    Draw the game_state grid layout.

    :param screen: Tkinter window
    :return: nothing
    """
    screen.screen_setup()
    screen.draw_outline()


def choose_players():
    """
    Use a Tkinter window to allow the user to choose the players.

    :return: player_1, player_2: Human or AI
    """
    # Choose Player Type
    options = Options()  # Create a Tkinter window object
    players = options.player_dict  # The dictionary is read when the window is closed
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


def get_move(player, screen):
    """
    Get the move from the player passing the current game_state state to the player.
    Draw the move on the window.
    Finally check for a winner.

    :param screen: Turtle Graphics window
    :param player: Human or AI player
    :return: bool True if the game is ending (either a winner or a tie)
    """
    player.get_move(screen=screen)

    global_vars.board[player.row][player.col] = player.value
    draw_move(player, screen)
    return check_for_winner(player)


def draw_move(player, screen):
    """
    Draw the player's move on the window.

    :param screen: Turtle Graphics window
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

    # The Options Tkinter window must be used before drawing the Turtle screen
    # If the order is swapped, then you cannot choose the players.
    # Having two root Tkinter windows open at the same time causes a conflict of some sort
    # We can't even make it a child, because the Turtle window is not a simple Tkinter window
    player_1, player_2 = choose_players()

    screen = DrawScreen()
    draw_grid(screen)

    # Here we actually create the messenger Turtle.
    # This must be done after the Options screen has closed, otherwise the options do not work.
    global_vars.player_msg.create_messenger()

    while not end_game:
        end_game = get_move(player_1, screen=screen)
        if end_game:
            break
        end_game = get_move(player_2, screen=screen)
        if end_game:
            break
    # print('Thanks for playing.')
    global_vars.player_msg.message_time('Thanks for playing.')
    screen.window.exitonclick()


if __name__ == "__main__":
    main()
