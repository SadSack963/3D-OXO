
from math import ceil
from time import sleep
from turtle import onscreenclick
from draw_screen import screen


class HumanPlayer:
    def __init__(self, value: int):
        self.value = value
        self.row = -1
        self.col = -1

    def get_move(self, board):
        self.row = -1
        self.col = -1
        while self.row == -1 or self.col == -1:
            sleep(0.5)  # TODO: Do I need this?
            onscreenclick(self.get_mouse_click_coord)
            screen.update()

    def get_mouse_click_coord(self, x, y):
        print(x, y)  # mouse coordinates
        if -300 < x < 300 and -300 < y < 300:
            # Convert mouse coordinates to row, col of the grid
            self.row, self.col = (ceil((100 - y) / 200), ceil((100 + x) / 200))
        else:
            print('Outside grid.')
