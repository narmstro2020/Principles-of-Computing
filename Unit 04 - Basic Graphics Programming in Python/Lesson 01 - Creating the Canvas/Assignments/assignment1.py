'''
Starting with a 300x300 red canvas, use the create_line() function to draw two horizontal and two vertical lines
on the canvas to create a Tic Tac Toe board.  Try your best to center your board and leave space around the outside like so
'''

from tkinter import *

root = Tk()

screen = Canvas(root, width=300, height=300, bg="#FF0000")
screen.pack()

screen.create_line(0, 100, 300, 100)   #horizontal line
# add another horizontal line

screen.create_line(100, 0, 100, 300)
# add another vertical line


mainloop()
