import oxo_2d
from turtle import Turtle, Screen


def screen_setup(screen):
    screen.setup(700, 700, 400, 300)
    screen.colormode(255)
    screen.bgcolor(60, 60, 60)


def draw_outline():
    tim = Turtle()
    tim.hideturtle()
    tim.width(4)
    tim.pu()
    tim.goto(-300, 300)
    tim.pd()
    tim.goto(-300, -300)
    tim.goto(300, -300)
    tim.goto(300, 300)
    tim.goto(-300, 300)
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


def draw_o(row, col):
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


def main():
    screen = Screen()
    screen_setup(screen)
    draw_outline()
    row, col = get_move('X')
    draw_x(row, col)
    row, col = get_move('O')
    draw_o(row, col)

    screen.exitonclick()


if __name__ == '__main__':
    main()
