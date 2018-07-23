import Tkinter
import Image
from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style
import cv2
import os
import time
import itertools
from Tkinter import Tk, Frame, BOTH, Button,RIGHT,RAISED
from Tkinter import BooleanVar,Checkbutton,PhotoImage,Canvas
from Tkinter import Scale,StringVar,END,Listbox,Label,Menu
from PIL import Image
import ttk
import thread
import pylab

root = Tk()
cwgt=Canvas(root)
cwgt.pack(expand=True, fill=BOTH)
image1=PhotoImage(file="1.png")
# keep a link to the image to stop the image being garbage collected
cwgt.img=image1
cwgt.create_image(0, 0,  image=image1)
b1=Button(cwgt, text="Hello", bd=0)
cwgt.create_window(20,20, window=b1)
root.mainloop()
