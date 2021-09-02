import math
from turtle import Turtle, Screen, onscreenclick
from time import sleep

DARK = (60, 60, 60)

# TODO: Replace hard-coded dimensions with values derived from the window size


class DrawScreen:
    # Since turtle.Screen() returns a singular object, we cannot inherit from Screen
    def __init__(self):
        self.window = Screen()

    def screen_setup(self):
        """
        Basic window setup

        :return: nothing
        """
        self.window.setup(700, 700, 400, 300)
        self.window.colormode(255)
        self.window.bgcolor(DARK)

    def draw_outline(self):
        """
        Draw the game_state grid layout

        :return: nothing
        """
        self.window.tracer(0)
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
        self.window.tracer(1)

    def draw_x(self, row: int, col: int):
        """
        Draw an X on the window

        :param row: x coordinate of the array
        :param col: y coordinate of the array
        :return: nothing
        """
        self.window.tracer(0)
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
        self.window.tracer(1)

    def draw_o(self, row, col):
        """
        Draw an O on the window

        :param row: x coordinate of the array
        :param col: y coordinate of the array
        :return: nothing
        """
        self.window.tracer(0)
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
        self.window.tracer(1)


# --------------------------------- TEST CODE ---------------------------------
def test_get_mouse_click(x, y):
    global last_drawn
    print(x, y)  # mouse coordinates
    if -300 < x < 300 and -300 < y < 300:
        # Convert mouse coordinates to row, col of the grid
        row, col = (math.ceil((100 - y) / 200), math.ceil((100 + x) / 200))
        if last_drawn == "X":
            screen.draw_o(row, col)
            last_drawn = "O"
        else:
            screen.draw_x(row, col)
            last_drawn = "X"
    else:
        print('Outside grid.')


def test():
    # Test drawing the window and using mouse clicks

    screen.screen_setup()
    screen.draw_outline()
    while True:
        sleep(0.5)
        screen.window.update()


if __name__ == '__main__':
    last_drawn = "O"
    screen = DrawScreen()
    onscreenclick(test_get_mouse_click)
    test()
    screen.window.exitonclick()
