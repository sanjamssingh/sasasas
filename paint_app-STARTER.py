'''
Paint App Project
Author: Sanjam Singh
Date: August 6, 2024
 
'''

from tkinter import *

root = Tk()
root.title('Paint')

f= Frame(root)
f.pack()
c= Canvas(root, bg= "white", height= 1000, width=1000)
c.pack()

COLOUR = 'black'
SIZE = 10

class ColourButton():
     
    
     def __init__(self, colour):
          self.colour = colour
          self.Button = Button(f, bg= colour, command= self.update)

     def update(self):
          global COLOUR
          COLOUR= self.colour
     
def draw_circle(event):
     c.create_oval(event.x, event.y, event.x + SIZE.get(), event.y + SIZE.get(), fill= COLOUR, outline= COLOUR, tags= [COLOUR])
    
def clear_canvas():
     c.delete('all')


colours = ['red', 'blue', 'orange', 'purple', 'violet', 'pink','black','yellow','white']
for i in range(len(colours)):
    x = ColourButton(colours[i])
    x.Button.grid(row=0, column=i)

clearbutton= Button(f, text= "CLEAR", command= clear_canvas)
clearbutton.grid(row=0, column= i + 1)



SIZE = IntVar() 
scalebar = Scale(f, variable= SIZE, bg= "grey", tickinterval= 1,resolution= 1, orient= HORIZONTAL, from_= 1, to= 10 )
scalebar.grid(row = 0, column = i + 2)



c.bind("<B1-Motion>", draw_circle)
root.bind("<q>", quit)
root.mainloop()