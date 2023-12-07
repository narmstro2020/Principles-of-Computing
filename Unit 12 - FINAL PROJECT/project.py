from tkinter import *

root = Tk()

r = "#d62b18"
b = "#876f16"
s = "#fa9644"
g = "#6185f8"
clear_color = "#4d2d44"

start_x = 0
start_y = 0
size = 20

small_mario = [
    [g, g, g, r, r, r, r, r, r, g, g, g, g, g, g, g], #row 0
    [g, g, r, r, r, r, r, r, r, r, r, r, g, g, g, g], #row 1
    [], #row 2
    [], #row 3
    [], #row 4
    [], #row 5
    [], #row 6
    [], #row 7
    [], #row 8
    [], #row 9
    [], #row 10
    [], #row 11
    [], #row 12
    [], #row 13
    [], #row 14
    [], #row 15
]

screen = Canvas(root, width=320, height=320, bg=clear_color)
screen.pack()

def draw_rectangle(x, y, width, height, color):
    ending_x = x + width
    ending_y = y + height
    screen.create_rectangle(x, y, ending_x, ending_y, fill=color)

def draw_sprite(sprite):
    x = start_x
    y = start_y
    for row in sprite:
        for color in row:
            draw_rectangle(x, y, size, size, color)
            x += size
        x = start_x
        y += size
        

draw_sprite(small_mario)

mainloop()
