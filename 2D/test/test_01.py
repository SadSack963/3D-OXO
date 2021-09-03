# Using a Tkinter Button inside a Python Turtle Program
# -----------------------------------------------------

# https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/

import turtle
import tkinter as tk


def do_stuff():
    canvas.itemconfig(window_id, state='hidden')
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        my_lovely_turtle.right(120)
    canvas.itemconfig(window_id, state='normal')


def press():
    do_stuff()


if __name__ == "__main__":
    screen = turtle.Screen()  # screen.master is _Root
    screen.bgcolor("cyan")

    # Return the Canvas of this TurtleScreen, type ScrolledCanvas
    canvas = screen.getcanvas()  # canvas.master is _Root

    # The master of an object is implicit in the new name given to it at creation time.
    # In Tkinter, masters are specified explicitly.
    button = tk.Button(master=canvas.master, text="Press me", command=press)

    # You can place any Tkinter widget onto a canvas by using a canvas window object.
    # A window is a rectangular area that can hold one Tkinter widget.
    # The widget must be the child of the same top-level window as the canvas,
    # or the child of some widget located in the same top-level window.
    # id = Canvas.create_window(x, y, option, ...)
    window_id = canvas.create_window(-200, -200, window=button)

    my_lovely_turtle = turtle.Turtle(shape="turtle")
    turtle.done()
