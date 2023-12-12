from tkinter import *

root = Tk()

k = "#000000"  # black
r = "#d62b18"  # mario's red
b = "#876f16"  # mario's brown, goomba brown
s = "#fa9644"  # mario's skin tone, goomba lite tan
g = "#6185f8"  # background
clear_color = "#4d2d44"  # purpley color

# finish this mario sprite
small_mario = [
    [g, g, g, r, r, r, r, r, r, g, g, g, g, g, g, g],  # row 0
    [g, g, r, r, r, r, r, r, r, r, r, r, g, g, g, g],  # row 1
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

# finish this goomba sprite
goomba = [
    [g, g],  # row 0
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

# YOUDO:  Work on big mario
big_mario = [
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 0
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 1
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 2
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 3
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 4
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 5
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 6
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 7
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 8
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 9
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 10
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 11
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 12
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 13
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 14
    [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],  # row 15
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 16
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 17
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 18
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 19
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 20
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 21
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 22
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 23
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 24
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 25
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 26
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 27
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 28
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 29
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 30
    [k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k],  # row 31

]

screen = Canvas(root, width=320, height=320, bg=clear_color)
screen.pack()

options = [
    "Small Mario",
    "Goomba", 
    "Big Mario"
]

clicked = StringVar()
clicked.set("Small Mario")

drop_down = OptionMenu(root, clicked, *options)
drop_down.pack()


def draw_rectangle(x, y, width, height, color):
    ending_x = x + width
    ending_y = y + height
    screen.create_rectangle(x, y, ending_x, ending_y, fill=color)

def draw_sprite16(sprite):
    x = 0
    y = 0
    size = 20
    for row in sprite:
        for color in row:
            draw_rectangle(x, y, size, size, color)
            x += size
        x = 0
        y += size
        
def draw_sprite32(sprite):
    x = 0
    y = 0
    size = 10
    for row in sprite:
        for i in range(32):
            if i < 8:
                draw_rectangle(x, y, size, size, g)
            elif i >= 24:
                draw_rectangle(x, y, size, size, g)
            else:
                color = row[i - 8]
                draw_rectangle(x, y, size, size, color)
            x += size
        x = 0
        y += size      


def draw_sprite(sprite):
    if len(sprite) == 16:
        draw_sprite16(sprite)
    elif len(sprite) == 32:
        draw_sprite32(sprite)



def clear():
    screen.delete("all")


def draw():
    clear()
    current_selection = clicked.get()
    if current_selection == "Small Mario":
        draw_sprite(small_mario)
    elif current_selection == "Goomba":
        draw_sprite(goomba)
    elif current_selection == "Big Mario":
        draw_sprite(big_mario)



draw_button = Button(root, text="Draw Sprite", command=draw)
draw_button.pack()

clear_button = Button(root, text="Clear", command=clear)
clear_button.pack()

# Note if testing big mario.  You will only get the top half
# call:  draw_sprite(big_mario) to test.

mainloop()
