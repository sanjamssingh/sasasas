'''
To-Do List App - STARTER
Author: Sanjam Singh
Date: July 30, 2024

[Project Description]

'''

'''
TODO:
1. Draw out your app on paper! Choose a colourscheme and your widget arrangement.
2. Set up your window and create your frames. (under class definitions)
3. Fill out the Classes, following the commented instructions

    Classes and other outlines are just suggestions! If you find it more complicated
    to follow this structure than make your own - go ahead and make your own or change
    the classes here!

4. Configure rows and columns (under frame and label creation)
5. Modify layout to make it look nice!
6. Test it out!
    - Ensure that progress bar resizes with window
    - Ensure that progress bar is accurate (should be 2/3 full if there are 3 items, 2 checked off)
7. Clean up your code! Check to make sure all your instance variables are actually necessary, etc.

'''

'''
EXTRAS THAT WILL BE HELPFUL:

root.winfo_width() <- returns current width of the window
[Canvas].winfo_width() <- returns current width of chosen Canvas
winfo_height() will do the same for current height
'''

from tkinter import *
root = Tk()
# Configure root here, give it a title, start size, resizability, etc.
mf= Frame(root, padx= 10, pady= 10)
mf.grid(row= 0, column= 0, sticky= "news" )
l1= Label(mf, text= "TO DO: ", bg= "light blue", fg= "black")
l1.grid(row= 0, column= 0, sticky= "ew")

lf= Frame(mf, bg= "light blue", padx= 5, pady= 5)
lf.grid(row= 1, column= 0, columnspan= 2, sticky= "news")

NUM_ITEMS = 0
NUM_DONE = 0

trashpic= PhotoImage(file= "C:\\Users\\ucbra\\OneDrive\\Ultimate Coders\\Sanjam Singh\\trashcan.png")

class ProgressBar():
    def __init__(self, bg, fg):

        self.c= Canvas(mf, bg= bg, width= 160, height= 15)
        self.bar= self.c.create_rectangle(0,0,0,0, outline= "black", fill= fg)
        self.c.grid(row= 4, column= 0, columnspan= 2, sticky= "ew")

    def resize(self, event):
        unit_size= self.c.winfo_width() // NUM_ITEMS
        new_width= unit_size*NUM_DONE
        self.c.coords(self.bar, 0, 0, new_width, self.c.winfo_height())

pb=ProgressBar("light grey", "black")
root.bind("<Configure>", pb.resize)

class ListItem():
    def __init__(self, row):
        # Set up any instance attributes here
        self.row = row
        self.cb_var = StringVar()
        self.cb_state_var = IntVar()
       
        self.ent_var= StringVar(value= "Enter list item here: ")
      
        self.cb= Checkbutton(lf, textvariable= self.cb_var, bg= "light blue", command= self.update, onvalue= 1, offvalue= 0, variable= self.cb_state_var)

        
        self.cb.grid(row= row, column=0, sticky= "W")
        self.ent= Entry(lf, textvariable=self.ent_var, bg= "light blue")
        self.ent.grid(row=row, column=0, sticky= "W")

        
        self.ent.bind("<ButtonPress>", self.clear_entry)
        self.ent.bind("<Return>", self.destroy_entry)

        lf.rowconfigure(row, weight=1)

    def clear_entry(self, event):
        self.ent_var.set(' ')

    def destroy_entry(self, event):
        global NUM_ITEMS
        NUM_ITEMS += 1
        self.ent.destroy()
        self.cb_var.set(self.ent_var.get().strip())

        self.trash= Button(lf, image= trashpic, relief= "raised", bg= "light blue", justify= "right", command= self.delete)
        self.trash.grid(row=self.row, column= 1, sticky= "E")

        ListItem(self.row + 1)

    def update(self):
        global NUM_DONE
        if self.cb_state_var.get():
            NUM_DONE += 1
            pb.resize(None)
        else:
            NUM_DONE -= 1
            pb.resize(None)

    def delete(self):
        global NUM_DONE
        global NUM_ITEMS
        if self.cb_state_var.get():
            NUM_DONE -=1
        self.cb.destroy()
        self.trash.destroy()
        NUM_ITEMS -= 1

ListItem(0)

pblabel= Label(mf, text= 'PROGRESS: ', bg= 'lightgrey', relief= 'flat')
pblabel.grid(row= 3, column= 0, columnspan= 2, sticky= "ew")

root.rowconfigure(0, weight= 1)
root.columnconfigure(0, weight= 1)

for i in range(4):
    mf.rowconfigure(i, weight= 1, minsize= 30)

mf.rowconfigure(1, weight=2)
mf.columnconfigure(0, weight= 1)

lf.rowconfigure(0, weight= 1)
lf.columnconfigure(0, weight= 2)
lf.columnconfigure(1, weight= 0)

root.mainloop()