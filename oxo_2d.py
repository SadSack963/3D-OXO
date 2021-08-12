# Define the matrix representing the game boundaries
# A position is defined by two coordinates:
#     [row, column] = [front->back, left->right] from a top-down view
# A row is 4 locations, forming a 3 x 1 array
# A board ia 4 rows, forming a 3 x 3 grid
# row = [
#     0,
#     0,
#     0
# ]
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# # Change the value of a single position in the board
# col = 2  # 3rd position right
# row = 1  # 2nd row back
#
# board[row][col] = 2
# print(board)
# """
# [[0, 0, 0], [0, 0, 2], [0, 0, 0]]
# """


# TODO: Define the winning combinations
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


# TODO: Draw the board (2D)


# TODO: Get user input
def get_user_input(user):
    position = input(f"Player {symbols[user - 1]} position (row col): ").split(" ")
    row = int(position[0])
    col = int(position[1])
    return row, col


# TODO: Draw the user1 choice on the board


# TODO: Detect a win


# TODO: Get user2 input


# TODO: Draw the user2 choice on the board


# TODO: Detect a win
symbols = ["X", "O"]
game_on = True
while game_on:
    for user in [1, 2]:
        row, col = get_user_input(user)
        while board[row][col] != 0:
            print("That position is already taken.")
            row, col = get_user_input(user)
        board[row][col] = user
        print(board)
        winner = check_win(user)
        if winner == user:
            print(f"{symbols[user - 1]} win")
            game_on = False
            break
