#from Tkinter import Tk, Frame, BOTH, Button,RIGHT,RAISED,LEFT,IntVar,BOTTOM
#from Tkinter import BooleanVar,Checkbutton,PhotoImage,Canvas,W
#from Tkinter import Scale,StringVar,END,Listbox,Label,Menu,Entry
#from PIL import Image
#import ttk
#import time
#import thread
#import pylab
#import threading
#import cv2

#import numpy as np
#import argparse
#from threading import Thread
#import Messagebox as mbox
#from Tkinter import * 
#import tkMessageBox
#import  sys
#################
#import signal
#import traceback
#from datetime import datetime
#from multiprocessing import Process

#import picamera
#import picamera.array
#import cmlib
#from cmlib import piLib
from library import *
import os

cmlib.LightOn()
#cmlib.LightOff()
camera=picamera.PiCamera()

camera.resolution=(400,300)
camera.framerate=80
loadprogram=0
now = datetime.now()
######

##################
#import ImageTk

root = Tk()




#############################################    khai bao ban dau
class Example(Frame):
	
#######################################################################

	
 def __init__(self, parent):
  Frame.__init__(self, width=1000,height=1000, background="green")
  self.parent = parent
  self.pack(fill=BOTH,expand=True)
  self.initUI()
  
  

 def initUI(self):
  self.parent.title("Cravis_ver1")
  self.pack(fill=BOTH, expand=1)
  TakePicButton = Button(self,text="TakePic",command=self.Takepic)
  TakePicButton.place(x=150,y=20)


###############################################################################   button  to analyse image
 def Takepic(self):  ## take pic button 
	  src=camera.capture('src.png')
	  analysed=camera.capture('analysed.png')
	  
	  #print analysed[5,5][0].get()
	  
	 
	  img_origin=PhotoImage(file="src.png")
	  img_RGB=cv2.imread("src.png")
	  retval,res = cv2.threshold(src, self.varLow.get(), self.varHigh.get(), cv2.THRESH_BINARY)
	  cv2.imwrite("analysed.png",res)

	  self.OK_NG=1
	  
	  if self.OK_NG==1:
		  print OK
	  else :
		  print NG

###########################################################

############################################################################################   get data 

###################################################################################		 
 
 
############################################################################################  main
	
root.geometry("1600x750+100+100")
app = Example(root)
print loadprogram

root.mainloop()


###################


