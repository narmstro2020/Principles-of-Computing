from tkinter import *

root = Tk()

r = "#d62b18"
b = "#876f16"
s = "#fa9644"
g = "#6185f8"

start_x = 0
start_y = 0
size = 20

screen = Canvas(root, width=320, height=320, bg="#4d2d44")
screen.pack()

sprite = [
    [g, g, g, g, r, r, r, r, r, r, g, g, g, g, g, g],
    [g, g, g, r, r, r, r, r, r, r, r, r, r, g, g, g],
    [g, g, g, b, b, b, b, s, s, b, s, g, g, g, g, g],
    [g, g, b, b, s, b, s, s, s, b, s, s, s, g, g, g],
    [g, g, b, b, s, b, b, s, s, s, b, s, s, s, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
]

for row in range(len(sprite)):
    for col in range(len(sprite[row])):
        screen.create_rectangle(start_x + col * size, start_y + row * size,
                                start_x + (col + 1) * size, start_y + size + row * size, fill=sprite[row][col])

mainloop()