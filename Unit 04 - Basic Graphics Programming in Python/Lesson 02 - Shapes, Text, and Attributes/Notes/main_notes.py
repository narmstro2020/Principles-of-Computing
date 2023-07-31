'''
tkinter
'''

from tkinter import *

root = Tk()

screen = Canvas(root, width=400, height=300)
screen.pack()


screen.create_rectangle(10, 20, 110, 100, fill="blue")

screen.create_rectangle(20, 20, 40, 40, fill="green", outline="yellow", dash="2")

screen.create_line(100, 100, 300, 300, dash="20", width="10")

screen.create_arc(20, 20, 40, 40, start="45", extent="90", fill="red")

screen.create_oval(50, 50, 100, 100, fill="purple")

screen.create_polygon(100, 100, 150, 150, 50, 150, 100, 100, fill="#E3A092")

screen.create_text(100, 200, text="Principles of Computing")


mainloop()