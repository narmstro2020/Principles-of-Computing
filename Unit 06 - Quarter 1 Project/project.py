from tkinter import *

root = Tk()

red = "#d62b18"
brown = "#876f16"
skin = "#fa9644"
background = "#6185f8"

start_x = 0
start_y = 0
size = 20

screen = Canvas(root, width=320, height=320, bg="#4d2d44")
screen.pack()

row = 0
screen.create_rectangle(start_x + 0 * size, start_y + row * size, start_x + 1 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 1 * size, start_y + row * size, start_x + 2 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 2 * size, start_y + row * size, start_x + 3 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 3 * size, start_y + row * size, start_x + 4 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 4 * size, start_y + row * size, start_x + 5 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 5 * size, start_y + row * size, start_x + 6 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 6 * size, start_y + row * size, start_x + 7 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 7 * size, start_y + row * size, start_x + 8 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 8 * size, start_y + row * size, start_x + 9 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 9 * size, start_y + row * size, start_x + 10 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 10 * size, start_y + row * size, start_x + 11 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 11 * size, start_y + row * size, start_x + 12 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 12 * size, start_y + row * size, start_x + 13 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 13 * size, start_y + row * size, start_x + 14 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 14 * size, start_y + row * size, start_x + 15 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 15 * size, start_y + row * size, start_x + 16 * size, start_y + size + row * size, fill=background)

row = 1
screen.create_rectangle(start_x + 0 * size, start_y + row * size, start_x + 1 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 1 * size, start_y + row * size, start_x + 2 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 2 * size, start_y + row * size, start_x + 3 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 3 * size, start_y + row * size, start_x + 4 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 4 * size, start_y + row * size, start_x + 5 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 5 * size, start_y + row * size, start_x + 6 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 6 * size, start_y + row * size, start_x + 7 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 7 * size, start_y + row * size, start_x + 8 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 8 * size, start_y + row * size, start_x + 9 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 9 * size, start_y + row * size, start_x + 10 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 10 * size, start_y + row * size, start_x + 11 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 11 * size, start_y + row * size, start_x + 12 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 12 * size, start_y + row * size, start_x + 13 * size, start_y + size + row * size, fill=red)
screen.create_rectangle(start_x + 13 * size, start_y + row * size, start_x + 14 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 14 * size, start_y + row * size, start_x + 15 * size, start_y + size + row * size, fill=background)
screen.create_rectangle(start_x + 15 * size, start_y + row * size, start_x + 16 * size, start_y + size + row * size, fill=background)






mainloop()