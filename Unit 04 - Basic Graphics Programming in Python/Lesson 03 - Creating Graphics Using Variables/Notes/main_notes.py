'''
tkinter
'''

from tkinter import *

root = Tk()

canvas_height = 300
canvas_width = 400
circle_radius = 50
background_color = "white"
oval_fill = "red"
oval_outline = ""
center_x = canvas_width / 2
center_y = canvas_height / 2

screen = Canvas(root, width=canvas_width, height=canvas_height, bg=background_color)
screen.pack()

top_left_x = center_x - circle_radius
top_left_y = center_y - circle_radius

bot_right_x = center_x + circle_radius
bot_right_y = center_y + circle_radius

screen.create_oval(top_left_x, top_left_y, bot_right_x, bot_right_y, fill=oval_fill, outline=oval_outline)



mainloop()