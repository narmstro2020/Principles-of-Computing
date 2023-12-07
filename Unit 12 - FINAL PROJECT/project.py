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
    [],  #row0
    [],  #row1
    [],  #row2
    [],  #row3
    [],  #row4
    [],  #row5
    [],  #row6
    [],  #row7
    [],  #row8
    [],  #row9
    [],  #row10
    [],  #row11
    [],  #row12
    [],  #row13
    [],  #row14
    [],  # row15
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
