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
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 16
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 17
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 18
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 19
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 20
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 21
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 22
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 23
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 24
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 25
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 26
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 27
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 28
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 29
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 30
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],  # row 31

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

def draw_sprite16x16(sprite):
    x = 0
    y = 0
    size = 20
    for row in sprite:
        for color in row:
            draw_rectangle(x, y, size, size, color)
            x += size
        x = 0
        y += size
        
def draw_sprite16x32(sprite):
    x = 0
    y = 0
    size = 10
    for row in sprite:
        for pixel in range(32):
            if pixel < 8:
                draw_rectangle(x, y, size, size, g)
            elif pixel >= 24:
                draw_rectangle(x, y, size, size, g)
            else:          
                color = row[pixel - 8]            
                draw_rectangle(x, y, size, size, color)
            x += size
        x = 0
        y += size

def draw_sprite(sprite):
    if len(sprite) == 16:
        draw_sprite16x16(sprite)
    elif len(sprite) == 32:
        draw_sprite16x32(sprite)


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


mainloop()
