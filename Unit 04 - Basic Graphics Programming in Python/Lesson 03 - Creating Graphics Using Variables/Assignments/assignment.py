"""
This program will draw a snowman on the screen.
The snowman should have three sections, a bottom snowball with diameter bottom_diameter, 
a middle snowball with diameter middle_diameter, 
and a top snowball with diameter top_diameter.

The circles should all be light gray.

The snowman should be centered horizontally in the world, 
Use canvas_height at 400, canvas_width at 400

bottom_diameter = 150
middle_diameter = 100
top_diameter = 75

Use the variables instead of hardcoded values to create your snowman 
so that the snowman will always be sitting in the same position no matter the size of the canvas!

If you are feeling adventurous, can you give the snowman a hat, buttons, or eyes?

Use the image as a reference.  

"""

from tkinter import *

root = Tk()

canvas_width = 400
canvas_height = 400
bottom_diameter = 150
middle_diameter = 100
top_diameter = 75
color = "grey"
center_x = canvas_width / 2

# Create canvas
screen = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
screen.pack()

# Add shapes here!
bottom_center_y = canvas_height - bottom_diameter / 2
top_left_x = center_x - bottom_diameter / 2
top_left_y = bottom_center_y - bottom_diameter / 2

bot_right_x = center_x + bottom_diameter / 2
bot_right_y = bottom_center_y + bottom_diameter / 2

screen.create_oval(top_left_x, top_left_y, bot_right_x, bot_right_y, fill=color)


middle_center_y = canvas_height - bottom_diameter - middle_diameter / 2
#cpy lines 43-49 and change bottom to middle for the copy of 43-49
# Add shapes to canvas
mainloop()