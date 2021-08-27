import math
from turtle import Turtle, Screen, onscreenclick
from time import sleep


screen = Screen()


def screen_setup():
    """
    Basic screen setup

    :return: nothing
    """
    screen.setup(700, 700, 400, 300)
    screen.colormode(255)
    screen.bgcolor(60, 60, 60)


def draw_outline():
    """
    Draw the game_state grid layout

    :return: nothing
    """
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
    # Draw the grid lines
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


def draw_x(row: int, col: int):
    """
    Draw an X on the screen

    :param row: x coordinate of the array
    :param col: y coordinate of the array
    :return: nothing
    """
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
    """
    Draw an O on the screen

    :param row: x coordinate of the array
    :param col: y coordinate of the array
    :return: nothing
    """
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


# --------------------------------- TEST CODE ---------------------------------
def test_get_mouse_click(x, y):
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


def test():
    # Test drawing the screen and using mouse clicks
    screen_setup()
    draw_outline()
    while True:
        sleep(0.5)
        screen.update()


if __name__ == '__main__':
    last_drawn = "O"
    onscreenclick(test_get_mouse_click)
    test()
    screen.exitonclick()
