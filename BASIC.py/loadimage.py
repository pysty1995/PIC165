from Tkinter import Tk, Frame, BOTH, Button,RIGHT,RAISED
from Tkinter import BooleanVar,Checkbutton,Canvas,PhotoImage
from Tkinter import Scale,StringVar,END,Listbox,Label,Menu
from PIL import Image
import ttk
import thread
import pylab
from Tkinter import Image     
root = Tk()      
canvas = Canvas(root, width = 1500, height = 1500)      
canvas.pack()      
img = PhotoImage(file="img.png")      
canvas.create_image(100,0,  image=img)      

root.mainloop()  
