"""
This program will draw the Polish flag.
Use the image assignment1.jpg as a reference to create this flag
"""

from tkinter import *

root = Tk()

# Create canvas
screen = Canvas(root, width = 400, height = 300, bg = "white")
screen.pack()

# Draw red rectangle
screen.create_rectangle(0, 150, 400, 300, fill="red", outline="")

# Add shapes to canvas
mainloop()