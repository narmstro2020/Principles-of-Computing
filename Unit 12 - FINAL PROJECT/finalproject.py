from tkinter import *

root = Tk()

k = "#000000"  # black
r = "#d62b18"  # mario's red
b = "#876f16"  # mario's brown, goomba brown
s = "#fa9644"  # mario's skin tone, goomba lite tan
g = "#6185f8"  # background
gb = "#c84c0c" #goomba brown
ge = "#fcbcb0" #goomba eye
pr = "#c41d0d"  # peach red
pw = "#fffeff"  # peach white
pc = "#f29900"  # peach crown and skin
pp = "#dc4278"  #lost levels peach pink
bg = "#17b217"  #bowser green
bs = "#ffaa60" # bowser skin
bw = "#ffffff" # bowser white and luigi white
lg = "#0c9300" #luigi green
ls = "#ea9e22" #luigi skin
lw = bw
fr = "#f73804" #fire red
fw = "#ffe1ab" #fire white
fs = "#ffa441" #fire skin

clear_color = "#4d2d44"  # purpley color
pixel_size = 20


# YOUDO:  finish this mario sprite
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

# YOUDO:  finish this goomba sprite
goomba = [
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],  # row 0
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

# YOUDO:  Finish big mario
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

#YOUDO:  Finish Peach
peach = [
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

#YOUDO:  Code princess peach from lost levels the one on the right with the pink dress.  
peach_ll_sprite = [
    
]

#YOUDO:  Code the bowser sprite
bowser = [
    
]

screen = Canvas(root, width=320, height=320, bg=clear_color)
screen.pack()

#YOUDO:  Add options for all sprites
options = [
    "Small Mario",
    "Goomba",
    "Big Mario"
]

clicked = StringVar()
clicked.set("Small Mario")

drop_down = OptionMenu(root, clicked, *options)
drop_down.pack()

current_sprite = small_mario
current_sprite_name = "Small Mario"

    


def draw_rectangle(x, y, width, height, color):
    ending_x = x + width
    ending_y = y + height
    screen.create_rectangle(x, y, ending_x, ending_y, fill=color)


def draw_sprite(sprite):
    clear()
    x = 0
    y = 0
    height_in_pixels = len(sprite)
    width_in_pixels = len(sprite[0])
    canvas_height = height_in_pixels * pixel_size
    canvas_width = width_in_pixels * pixel_size
    screen.config(width=canvas_width, height=canvas_height)

    for row in sprite:
        for color in row:
            draw_rectangle(x, y, pixel_size, pixel_size, color)
            x += pixel_size
        x = 0
        y += pixel_size


def clear():
    screen.delete("all")

#YOUDO:  add elifs for remaining sprites
def draw():
    global current_sprite
    global current_sprite_name
    current_selection = clicked.get()
    current_sprite_name = current_selection
    if current_selection == "Small Mario":
        current_sprite = small_mario
        draw_sprite(small_mario)
    elif current_selection == "Goomba":
        current_sprite = goomba
        draw_sprite(goomba)
    elif current_selection == "Big Mario":
        current_sprite = big_mario
        draw_sprite(big_mario)

        
def luigi():
    if(current_sprite_name == "Small Mario" or current_sprite_name == "Big Mario"):       
        luigi_sprite = []
        for row in current_sprite:
            new_row = []
            for color in row:
                if color == r:
                    new_row.append(lw)
                elif color == s:
                    new_row.append(ls)
                elif color == b:
                    new_row.append(lg)
                else:
                    new_row.append(color)
            luigi_sprite.append(new_row)
        draw_sprite(luigi_sprite)

#YOUDO:  create the fire function
def fire():
    # check if the current_sprite_name is either Big Mario
    # if it is.  Then
    fire_sprite = []
    # use whatever sprite is in current_sprite along with a double for loop
    for row in current_sprite:
        for color in row:
            # build the fire_sprite from current_sprite but with different colors:
            pass  # remove when done.
    # Then call the draw_sprite function with fire_sprite
    pass  # Don't forget to remove the pass when done.

draw_button = Button(root, text="Draw Sprite", command=draw)
draw_button.pack()

clear_button = Button(root, text="Clear", command=clear)
clear_button.pack()

draw_luigi = Button(root, text="Draw Luigi", command=luigi)
draw_luigi.pack()

#YOUDO:  Make a button called FIRE that makes big mario fire.  NEED A FUNCTION CALLED fire
#YOUDO:  Don't forget to pack.  




mainloop()
