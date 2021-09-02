import global_vars
import numpy as np


def evaluate_board(game_state: np.ndarray):
    """
    Check for a winning combination

    :param game_state: current state of the game
    :return: 0 = Tie,
             1 = Player 1 win,
             2 = Player 2 win,
             or None if the game_state is not full and there is no winner yet
    """
    # Rows
    for row in range(3):
        if game_state[row][0] != 0 \
                and game_state[row][0] == game_state[row][1] \
                and game_state[row][0] == game_state[row][2]:
            return game_state[row][0]

    # Columns
    for col in range(3):
        if game_state[0][col] != 0 \
                and game_state[0][col] == game_state[1][col] \
                and game_state[0][col] == game_state[2][col]:
            return game_state[0][col]

    # Diagonals
    if game_state[0][0] != 0 \
            and game_state[0][0] == game_state[1][1] \
            and game_state[0][0] == game_state[2][2]:
        return game_state[0][0]

    if game_state[0][2] != 0 \
            and game_state[0][2] == game_state[1][1] \
            and game_state[0][2] == game_state[2][0]:
        return game_state[0][2]

    # Check if the game_state is full
    if np.all(game_state):
        return 0  # Tie
    else:
        return None  # Free spaces remaining


def check_for_winner(player):
    """
    Check if there is a winner.

    :param player: Human or AI player
    :return: bool - True if there is a winner or a tie
    """

    winner = evaluate_board(global_vars.board)
    if winner:
        # print(f"Player {player.value} wins!")
        global_vars.player_msg.message_time(f"Player {player.value} wins!", time=2)
        return True
    if winner == 0:
        # print("It's a tie!")
        global_vars.player_msg.message_time("It's a tie!", time=2)
        return True
    return False
