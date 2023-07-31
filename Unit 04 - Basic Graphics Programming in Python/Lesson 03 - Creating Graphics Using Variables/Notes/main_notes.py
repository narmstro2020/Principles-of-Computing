'''
tkinter
'''

from tkinter import *

root = Tk()

canvas_height = 300
canvas_width = 400
circle_radius = 100
background_color = "white"
oval_fill = "red"
oval_outline = ""


screen = Canvas(root, width=canvas_width, height=canvas_height, bg=background_color)
screen.pack()

top_x = canvas_width / 2 - circle_radius
top_y = canvas_height / 2 - circle_radius

bottom_x = canvas_width / 2 + circle_radius
bottom_y = canvas_height / 2 + circle_radius

screen.create_oval(top_x, top_y, bottom_x, bottom_y, fill=oval_fill, outline=oval_outline)



mainloop()