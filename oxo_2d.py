# 2-D OXO
# =======


# Check for a winning combination
def check_win(user):
    # Rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == user:
            return user

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == user:
            return user

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == user:
        return user

    if board[0][2] == board[1][1] == board[2][0] == user:
        return user


# Get user input
def get_user_input(user):
    position = input(f"Player {symbols[user - 1]} position (row col): ").split(" ")
    row = int(position[0])
    col = int(position[1])
    return row, col


# TODO: Draw the board (2D)
def draw_board():
    print(f'{board[0]}\n{board[1]}\n{board[2]}')


# Define the matrix representing the game board
row0 = [0, 0, 0]
row1 = [0, 0, 0]
row2 = [0, 0, 0]

board = [row0, row1, row2]

symbols = ["X", "O"]
positions_free = len(row0) * len(board)

# Game Loop

game_on = True
while game_on:
    for user in [1, 2]:
        row, col = get_user_input(user)
        while board[row][col] != 0:
            print("That position is already taken.")
            row, col = get_user_input(user)
        board[row][col] = user
        positions_free -= 1
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
