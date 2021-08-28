from math import ceil
from turtle import onscreenclick
import numpy as np
from time import sleep


class HumanPlayer:
    def __init__(self, value: int):
        self.value = value
        self.row = -1
        self.col = -1

    def get_move(self, screen):
        """
        Get a valid grid selection.\n
        The selected move is stored in self.row, self,col

        :param screen - update the window while looking for mouse clicks
        :return: nothing
        """
        # game_state is not used by the human player, but it is used by the AI player
        self.row = -1
        self.col = -1
        onscreenclick(self.get_mouse_click_coord)
        while self.row == -1 or self.col == -1:
            screen.window.update()

    def get_mouse_click_coord(self, x, y):
        """
        Derive the selected grid position from the mouse click coordinates.\n
        The selected move is stored in self.row, self,col

        :param x: mouse click x coordinate from turtle.onscreenclick()
        :param y: mouse click y coordinate from turtle.onscreenclick()
        :return: nothing
        """
        if -300 < x < 300 and -300 < y < 300:
            # Convert mouse coordinates to row, col of the grid
            self.row, self.col = (ceil((100 - y) / 200), ceil((100 + x) / 200))
