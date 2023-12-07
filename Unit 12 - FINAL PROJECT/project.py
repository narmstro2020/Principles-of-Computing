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

screen = Canvas(root, width=320, height=320, bg=clear_color)
screen.pack()

#YOUDO.  Code Mario
small_mario = [
    [g, g, g, r, r, r, r, r, r, g, g, g, g, g, g, g],
    [g, g, r, r, r, r, r, r, r, r, r, r, g, g, g, g],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

def draw_rectangle(x, y, width, height, color="#000000"):
    ending_x = x + width
    ending_y = y + height
    screen.create_rectangle(x, y, ending_x, ending_y, fill=color)
    
def draw_sprite(sprite_data):
    x = start_x
    y = start_y
    for row in sprite_data:
        for color in row:
           draw_rectangle(x, y, size, size, color)
           x += size
        x = start_x
        y = y + size
        
def clear():
    x = start_x
    y = start_y
    for row in range(16):
        for color in range(16):
           draw_rectangle(x, y, size, size, clear_color)
           x += size
        x = start_x
        y = y + size
    
    
draw_sprite(small_mario)




mainloop()