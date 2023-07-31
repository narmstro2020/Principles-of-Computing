'''
Write a program to draw a ghost on the screen. 
You must do this by using the constant values given (this will allow us to easily alter the size or color of the ghost.)


'''


from tkinter import *

root = Tk()

# Constant values
canvas_width = 400
canvas_height = 300

head_radius = canvas_width/4
body_width = head_radius * 2
body_height = canvas_height/3
num_feet = 3
foot_radius = body_width / (num_feet * 2)
body_color = "red"

eye_radius = head_radius/4
eye_offset = eye_radius * 1.5
eye_color = "white"
pupil_radius = eye_radius/2.5
pupil_left_offset = eye_radius
pupil_right_offset = pupil_radius * 5
pupil_color = "blue"

# Create canvas
screen = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
screen.pack()

# Write program here








# Add shapes to canvas
mainloop()