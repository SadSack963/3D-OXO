import math

import oxo_2d
from turtle import Turtle, Screen, onscreenclick
from time import sleep


def screen_setup():
    screen.setup(700, 700, 400, 300)
    screen.colormode(255)
    screen.bgcolor(60, 60, 60)


def draw_outline():
    screen.tracer(0)
    tim = Turtle()
    tim.hideturtle()
    # Draw the border
    tim.width(4)
    tim.pu()
    tim.goto(-300, 300)
    tim.pd()
    tim.goto(-300, -300)
    tim.goto(300, -300)
    tim.goto(300, 300)
    tim.goto(-300, 300)
    # Draw the lines
    tim.width(2)
    tim.goto(-100, 300)
    tim.goto(-100, -300)
    tim.goto(100, -300)
    tim.goto(100, 300)
    tim.pu()
    tim.goto(-300, 100)
    tim.pd()
    tim.goto(300, 100)
    tim.goto(300, -100)
    tim.goto(-300, -100)
    screen.tracer(1)


def get_move(symbol):
    """
    Accepts a space separated board position input by the player, and returns the integer values

    :param
    :return: (row, column)
    """
    # Get user input
    position = input(f"Player {symbol} position (row col): ").strip().split()
    # Check for two values
    if len(position) != 2:
        return -1, -1
    # Check for numbers only
    try:
        return int(position[0]), int(position[1])
    except ValueError:
        return -1, -1


def draw_x(row, col):
    screen.tracer(0)
    start_x = col * 200 - 270
    start_y = 270 - row * 200
    tim = Turtle()
    tim.hideturtle()
    tim.width(4)
    tim.color('white')
    tim.pu()
    tim.goto(start_x, start_y)
    tim.pd()
    tim.goto(start_x + 140, start_y - 140)
    tim.pu()
    tim.goto(start_x + 140, start_y)
    tim.pd()
    tim.goto(start_x, start_y - 140)
    screen.tracer(1)


def draw_o(row, col):
    screen.tracer(0)
    start_x = col * 200 - 200
    start_y = 130 - row * 200
    tim = Turtle()
    tim.hideturtle()
    tim.width(4)
    tim.color('white')
    tim.pu()
    tim.goto(start_x, start_y)
    tim.pd()
    tim.circle(70)
    screen.tracer(1)


# def define_click_areas():
#     click_areas = [[], [], []]
#     square = []
#     size = 200  # height and width of the clickable area
#     for row in range(3):
#         for col in range(3):
#             centre = (col * size - 200, 200 - row * size)  # centre of the square
#             # Store the coordinates for the square centres
#             click_areas[row].append(centre)
#
#             # # Store the coordinates for the corners of the square in a tuple
#             # square_top_left = centre[0] - 100, centre[1] + 100
#             # square_bottom_left = centre[0] - 100, centre[1] - 100
#             # square_bottom_right = centre[0] + 100, centre[1] - 100
#             # square_top_right = centre[0] + 100, centre[1] + 100
#             # click_areas[row].append(
#             #     (
#             #         square_top_left,
#             #         square_bottom_left,
#             #         square_bottom_right,
#             #         square_top_right
#             #     )
#             # )
#
#     return click_areas


def get_mouse_click_coord(x, y):
    global last_drawn
    print(x, y)  # mouse coordinates
    if -300 < x < 300 and -300 < y < 300:
        # Convert mouse coordinates to row, col of the grid
        row, col = (math.ceil((100 - y) / 200), math.ceil((100 + x) / 200))
        if last_drawn == "X":
            draw_o(row, col)
            last_drawn = "O"
        else:
            draw_x(row, col)
            last_drawn = "X"
    else:
        print('Outside grid.')


def main():
    screen_setup()
    draw_outline()
    # click_areas = define_click_areas()
    # print(click_areas)
    # """
    # Centres of squares
    # [[(-200, 200), (0, 200), (200, 200)],
    #  [(-200, 0), (0, 0), (200, 0)],
    #  [(-200, -200), (0, -200), (200, -200)]]
    # """
    # """
    # Coordinates of squares corners
    # [[((-300, 300), (-300, 100), (-100, 100), (-100, 300)), ((-100, 300), (-100, 100), (100, 100), (100, 300)), ((100, 300), (100, 100), (300, 100), (300, 300))],
    # [((-300, 100), (-300, -100), (-100, -100), (-100, 100)), ((-100, 100), (-100, -100), (100, -100), (100, 100)), ((100, 100), (100, -100), (300, -100), (300, 100))],
    # [((-300, -100), (-300, -300), (-100, -300), (-100, -100)), ((-100, -100), (-100, -300), (100, -300), (100, -100)), ((100, -100), (100, -300), (300, -300), (300, -100))]]
    # """

    while True:
        sleep(0.5)
        onscreenclick(get_mouse_click_coord)
        screen.update()
    # # row, col = get_move('X')
    # draw_x(row, col)
    # # row, col = get_move('O')
    # onscreenclick(get_mouse_click_coord)
    # draw_o(row, col)

    screen.exitonclick()


if __name__ == '__main__':
    screen = Screen()
    last_drawn = "O"
    main()
