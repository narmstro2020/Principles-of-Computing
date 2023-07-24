'''
tkinter
'''

from tkinter import *

root = Tk()

screen = Canvas(root, width=400, height=300, bg="#4d2d44")
screen.pack()

screen.create_line(50, 50, 200, 100, 50, 100, 50, 50)




mainloop()