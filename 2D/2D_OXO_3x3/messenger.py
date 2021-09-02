from turtle import Turtle
from time import sleep


class Messenger(Turtle):
    def __init__(self, font_name='Comic Sans', font_color='red', font_size=16, font_type='normal'):
        """
        Turtle Class to enable writing messages to the screen

        :param font_name: string font name
        :param font_color: string colour
        :param font_size: integer points
        :param font_type: string space separated (e.g. bold italic)
        """
        self.font_name = font_name
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.font = (self.font_name, self.font_size, self.font_type)

    def create_messenger(self):
        """
        This function should be run after the Option tkinter window has closed.
        We have to initialize the turtle here because otherwise it creates a tkinter turtle Screen() object
        which interferes with the initial Options tkinter window and prevents it working.

        :return: nothing
        """
        super(Messenger, self).__init__()
        self.pu()
        self.hideturtle()
        self.setposition(0, 0)
        self.pencolor(self.font_color)

    def message_time(self, message, time=0, align='center', position=(0, 0)):
        """
        Displays message at the given position for the given time.
        Previous message are cleared, which allows messages to be written to the same location on screen.
        If time <= 0 then the message is not cleared until the next message is written.

        :param message: string
        :param time: float (seconds)
        :param align: string space separated (e.g. center, bottom left, top right, etc.)
        :param position: tuple cartesian coordinate - (0, 0) is the center of the screen.
        :return: nothing
        """
        self.clear()  # Clear any previous message
        self.setposition(position)
        self.write(arg=message, move=False, align=align, font=self.font)
        if time > 0:
            sleep(time)
            self.clear()
