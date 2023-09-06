'''
Starting with a 200x200 red canvas, use the create_line() function to draw two horizontal and two vertical lines
on the canvas to create a Tic Tac Toe board.  Try your best to center your board and leave space around the outside like so
'''

from tkinter import *

root = Tk()

screen = Canvas(root, width=200, height=200, bg="#FF0000")
screen.pack()

screen.create_line(0, 67, 200, 67)   #horizontal line
# add another horizontal line

screen.create_line(67, 0, 67, 200)   #vertical line
# add another vertical line


mainloop()
