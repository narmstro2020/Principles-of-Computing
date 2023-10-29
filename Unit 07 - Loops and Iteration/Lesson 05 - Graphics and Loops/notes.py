from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 400
num_circles = 15
radius = (canvas_width/num_circles)/2

# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()

# Create circles across canvas
for i in range(num_circles):
    screen.create_oval(i * radius * 2, canvas_height/2 - radius, radius * 2 * (i+1), canvas_height/2 + radius)

# Add shapes to canvas
mainloop()