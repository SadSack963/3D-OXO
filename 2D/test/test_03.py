# Object Oriented Programming Version of Embedded Turtle Graphics Tkinter Program
# -------------------------------------------------------------------------------

# https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/

import turtle
import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Raw Turtle")
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=600, height=200)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("cyan")
        self.button = tk.Button(self.master, text="Press me", command=self.press)
        self.button.pack()
        self.my_lovely_turtle = turtle.RawTurtle(self.screen, shape="turtle")
        self.my_lovely_turtle.color("green")

    def do_stuff(self):
        # Use lift and lower to hide the button behind another widget.
        # This avoids other widgets rearranging themselves
        # self.button.lift(aboveThis=widget)

        self.button.pack_forget()
        for color in ["red", "yellow", "green"]:
            self.my_lovely_turtle.color(color)
            self.my_lovely_turtle.right(120)
        self.button.pack()

        # self.button.lower(belowThis=widget)

    def press(self):
        self.do_stuff()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
