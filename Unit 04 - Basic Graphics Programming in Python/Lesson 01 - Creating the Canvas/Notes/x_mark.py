from tkinter import *

root = Tk()

screen = Canvas(root, width=300, height=200, bg="#4d2d44")
screen.pack()

screen.create_line(0, 0, 300, 200)
screen.create_line(0, 200, 300, 0)





mainloop()