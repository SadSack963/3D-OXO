# Basic Python Turtle Embedded in Tkinter Program
# -----------------------------------------------

# https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/

import turtle
import tkinter as tk


def do_stuff():
    # Use lift and lower to hide the button behind another widget.
    # This avoids other widgets rearranging themselves
    # button.lift(aboveThis=widget)

    button.pack_forget()
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        my_lovely_turtle.right(120)
    button.pack()

    # button.lower(belowThis=widget)


def press():
    do_stuff()


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=600, height=200)
    canvas.pack(side=tk.LEFT)
    screen = turtle.TurtleScreen(cv=canvas)
    screen.bgcolor("cyan")
    button = tk.Button(master=root, text="Press me", command=press)
    button.pack()
    my_lovely_turtle = turtle.RawTurtle(canvas=screen, shape="turtle")
    root.mainloop()
