from tkinter import *

root = Tk()

k = "#000000"  #black
r = "#d62b18"  #mario's red
b = "#876f16"  #mario's brown
s = "#fa9644"  #mario's skin tone
g = "#6185f8"  #background
clear_color = "#4d2d44"  #purpley color

start_x = 0
start_y = 0
size = 20

#finish this mario sprite
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

# finish this goomba sprite
goomba = [
    [],  # row 0
    [],  # row 1
    [],  # row 2
    [],  # row 3
    [],  # row 4
    [],  # row 5
    [],  # row 6
    [],  # row 7
    [],  # row 8
    [],  # row 9
    [],  # row 10
    [],  # row 11
    [],  # row 12
    [],  # row 13
    [],  # row 14
    [],  # row 15
]

screen = Canvas(root, width=320, height=320, bg=clear_color)
screen.pack()

options = [
    "Small Mario",
    "Goomba"
]

clicked = StringVar()
clicked.set("Small Mario")

drop_down = OptionMenu(root, clicked, *options)
drop_down.pack()


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
        

draw_sprite(goomba)

mainloop()
