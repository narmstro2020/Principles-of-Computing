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
top_dimater = 75

Use the variables instead of hardcoded values to create your snowman 
so that the snowman will always be sitting in the same position no matter the size of the canvas!

If you are feeling adventurous, can you give the snowman a hat, buttons, or eyes?

Use the image as a reference.  

"""

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 400
bottom_diameter = canvas_height/2
middle_diameter = bottom_diameter/2
top_diameter = middle_diameter/2

# Create canvas
screen = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
screen.pack()

# Add shapes here!



# Add shapes to canvas
mainloop()