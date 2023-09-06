'''

Use the create_line() function to draw multiple points that create a bubble letter.  The letter
can be the first letter of your name, or any letter that you think will be challenging.  
Feel free to draw out your letter on paper first if it will help you.  

'''

from tkinter import *

root = Tk()

screen = Canvas(root, width=200, height=200, bg="#FF0000")
screen.pack()


screen.create_line(50, 200, 50, 0, 100, 200, fill="#FFFFFF", width=3.0)  #Sample start
## continue drawing your letter

mainloop()