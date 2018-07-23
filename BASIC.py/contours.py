from Tkinter import Tk, Frame, BOTH, Button,RIGHT,RAISED,LEFT,IntVar,BOTTOM
from Tkinter import BooleanVar,Checkbutton,PhotoImage,Canvas,W
from Tkinter import Scale,StringVar,END,Listbox,Label,Menu,Entry
from PIL import Image
import ttk
import thread
import pylab
import threading
import cv2
import numpy as np
import argparse
from threading import Thread
#import Messagebox as mbox
from Tkinter import * 
import tkMessageBox
import  sys

root = Tk()      
canvas = Canvas(root, width = 400, height = 300)      
canvas.pack()      
   



im = cv2.imread('out.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#imgray = im
ret,thresh = cv2.threshold(imgray,0,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#
#cv2.imshow("image",image)
img=cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imwrite("abc.png",img)
#img11=img
img11 = PhotoImage(file="abc.png")      
canvas.create_image(100,0,  image=img11)   

root.mainloop()  
