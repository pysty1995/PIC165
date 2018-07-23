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
#################









##################
#import ImageTk
onvideo=1
root = Tk()

cwgt=Canvas(root)
cwgt2=Canvas(root)

cwgt.pack(fill=BOTH,expand=False,side=RIGHT,padx=1,pady=1)
cwgt2.pack(fill=BOTH,expand=False,side=RIGHT,padx=1,pady=1)
#
cwgt.img="menu.png"
cap = cv2.VideoCapture(0)
#startIndex = 0
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
##
#tkMessageBox.showinfo(title="dsfs",message="sdgdgd")
############





#############################################    khai bao ban dau
class Example(Frame):
 def __init__(self, parent):
  Frame.__init__(self, width=1000,height=1000, background="black")
  self.parent = parent
  self.initUI()
  
  

 def initUI(self):
  self.parent.title("Cravis_ver1")
  self.pack(fill=BOTH, expand=1)
  frame = Frame(self, width=750,height=200,relief=RAISED, borderwidth=1)
  frame.pack(expand=True)
  #frame.config(bg="blue")
  self.pack(expand=False)
  #####
 

  #####
  
  frame2 = Frame(self, width=750,height=200,relief=RAISED, borderwidth=1)
  frame2.pack(expand=False)
  self.pack(expand=False)
  
  
  self.var1=BooleanVar() 
  self.var2=BooleanVar()
  self.var3=BooleanVar()
  self.var4=BooleanVar() 
  self.var5=BooleanVar()
  self.content=IntVar()
  
  
  
  
  
  closeButton = Button(self, text="Close",background="green",command=self.error)
  closeButton.pack(side=RIGHT, padx=5, pady=5)
  
  okButton = Button(self, text="OK",background="green")
  okButton.pack(side=RIGHT)

  
  quitButton = Button(self,text="Quit",command=self.off_video)
  quitButton.place(x=50,y=20)
  
  startButton = Button(self,text="Start",command=self.on_start)
  startButton.place(x=100,y=20)
  
  TakePicButton = Button(self,text="TakePic",command=self.Takepic)
  TakePicButton.place(x=150,y=20)
  
  ######
  
  cb1 = Checkbutton(self, text="Binary", variable=self.var1 ,command=self.on_Binary)
  cb1.place(x=80, y=60)
 
  cb2 = Checkbutton(self, text="Partical", variable=self.var2 ,command=self.on_Partical)
  cb2.place(x=80, y=80)
  
  cb3 = Checkbutton(self, text="Sobel", variable=self.var3 ,command=self.on_Sobel)
  cb3.place(x=80, y=100)
  
  cb4 = Checkbutton(self, text="Median", variable=self.var4 ,command=self.on_Median)
  cb4.place(x=80, y=120)
  
  cb5 = Checkbutton(self, text="Level_Adjust", variable=self.var5 ,command=self.on_LevelAdjust)
  cb5.place(x=80, y=140)
  #####
  
  ###################################
  
  #infor=Text(self,state="disable",width=50,height=10,wrap='none')
  
  self.infor=Text(self,width=50,height=2)
  self.infor.pack()
  thongtin="CHAO MUNG DEN VOI CHUONG TRINH CRAVIS_V1                 DESIGN BY VISUAL GROUP"
  self.infor.insert(END,thongtin)
  
  ################################
  
  
  

  menuBar = Menu(self.parent)
  self.parent.config(menu=menuBar)
  
  fileMenu1 = Menu(menuBar)
  fileMenu2 = Menu(menuBar)
  fileMenu3 = Menu(menuBar)
  
  fileMenu1.add_command(label="zoom", command=self.zoom)
  fileMenu1.add_command(label="password", command=self.password)
  fileMenu1.add_command(label="2", command=self.onExit)
  fileMenu1.add_command(label="3", command=self.onExit)
  
  fileMenu2.add_command(label="Exit", command=self.onExit)
  fileMenu2.add_command(label="1", command=self.onExit)
  fileMenu2.add_command(label="2", command=self.onExit)
  fileMenu2.add_command(label="3", command=self.onExit)
  
  fileMenu3.add_command(label="help", command=self.file_help)
  fileMenu3.add_command(label="1", command=self.onExit)
  fileMenu3.add_command(label="2", command=self.onExit)
  fileMenu3.add_command(label="3", command=self.onExit)
  
  menuBar.add_cascade(label="File", menu=fileMenu1)
  menuBar.add_cascade(label="Infor", menu=fileMenu2)
  menuBar.add_cascade(label="Help", menu=fileMenu3)
  ######
  
  ####### ################################################               function for menu 

 def onScale_H(self, val):
    v = int(float(val))
    self.varHigh.set(v)
    print (v)
	#self.varHigh.set(v)
	
    
 def onScale_L(self, val):
    v = int(float(val))
    self.varLow.set(v)
    print (v)
  
 ###
 def onScale_R_L(self, val):
    v = int(float(val))
    self.varRed_L.set(v)
    print (v)
 def onScale_R_H(self, val):
    v = int(float(val))
    self.varRed_H.set(v)
    print (v)

 def onScale_G_L(self, val):
    v = int(float(val))
    self.varGreen_L.set(v)
    print (v)
 def onScale_G_H(self, val):
    v = int(float(val))
    self.varGreen_H.set(v)
    print (v)
    
 def onScale_B_L(self, val):
    v = int(float(val))
    self.varBlue_L.set(v)
    print (v)
 def onScale_B_H(self, val):
    v = int(float(val))
    self.varBlue_H.set(v)
    print (v)
  ###
 def on_Select(self, val):
   sender = val.widget
   idx = sender.curselection()
   value = sender.get(idx)
  
   self.varSelect.set(value)

 def onExit(self):
    self.quit()
    
 def file_help(self):
	 f=open('a.txt','r')
	 line=f.readline()
	 for line in f:
		print (line)
 def zoom(self):
	 root.geometry("1500x500")
######################################################   ############       Algorithm
 def on_Binary(self):
	 if self.var1.get() == True:
	  print ("Binary")
	  self.show_Binary() #show window
	 else :
		 print("No_Binary")
		 self.ThBinary.destroy()
 def on_Partical(self):
	 if self.var2.get() == True:
	  print ("Partical")
	  self.show_Extract()
	 else :
		 self.ThExtract.destroy()
		 print("No_Partical")
	 
 def on_Sobel(self):
	 if self.var3.get() == True:
	  print ("Sobel")
	 else :
		 print("No_Sobel")
		 
 def on_Median(self):
	 if self.var4.get() == True:
	  print ("Median")
	 else :
		 print("No_Median")
		 
 def on_LevelAdjust(self):
	 if self.var5.get() == True:
	  print ("LevAd")
	 else :
		 print("No_LevAd")
	 


 def showvideo(self):
  a=0
  while(cap.isOpened()):
      frame = Frame(cwgt, width=300,height=200,relief=RAISED, borderwidth=1)
      cwgt.pack(fill=BOTH, expand=True)
      
      self._camera.start_preview(fullscreen = False, window = (30,30) + self._camera.resolution)
      stream = picamera.array.PiRGBArray(self._camera)
      #ret, frame = cap.read()
	  #self._camera.capture(stream, format='bgr', use_video_port=True)
	  #frame = stream.array
	 
      if ret==True:
        #frame = cv2.flip(frame,0)
        #out.write(frame)
        cv2.imshow('frame',frame)
        cv2.waitKey(200)
        a=a+1
        print(a)
        #if (a==20):
		#	 cap.release()
		#	 cv2.destroyAllWindows()
			 
		

#
###############################################################################   button  to analyse image
 def Takepic(self):  ## take pic button 
	  
	  #ret, frame = cap.read()
	  img = Frame(cwgt, width=300,height=200,relief=RAISED, borderwidth=1)
	  ret, img = cap.read()
	  #img=PhotoImage(file="img.png")
	  cv2.imshow('yhhhhhh',img)
	  
	  #cv2.imshow('ugho',frame)
	  cv2.waitKey(500)
	  #cv2.imshow('img',img)
	  #img_origin=PhotoImage(file="new.png")
	  #cwgt2.img=img_origin
	  #cwgt2.create_image(0, 0,  image=img_origin)
	  #cwgt2.create_image(0, 0,  image=img)
	  #img = cv2.imread('new.png')
	  
	  if self.var1.get() == True:
		#retval, after_Binary = cv2.threshold(img, self.varLow.get(), self.varHigh.get(), cv2.THRESH_BINARY)
		#cv2.imwrite("out.png",after_Binary)
		#after_Binary=PhotoImage(file="out.png")
		#cwgt.img=after_Binary
		#cwgt.create_image(0, 0,  image=after_Binary)
		
		
		
		
		retval, after_Binary = cv2.threshold(img, self.varLow.get(), self.varHigh.get(), cv2.THRESH_BINARY)
		#after_Blurr =cv2.blur(img,(5,5))
		#after_MedianBlur=cv2.medianBlur(after_Blurr,5)
		
		#cv2.imwrite("out.png",res)
		#after_Binary=PhotoImage(file="out.png")
		#cwgt.img=res
		#cv2.imshow("show",res)
		cwgt.create_image(0, 0,  image=after_Binary)
		#cwgt.create_image(0, 0,  image=mask)
		
		#after_Canny=cv2.Canny(after_MedianBlur,100,200)
		
		#findlabel=cv2.findContours(after_Blurr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		#findlabel=cv2.findContours(after_Binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		#im = cv2.imread('new.png')
		#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		#ret,thresh = cv2.threshold(imgray,0,255,0)
		#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
		#img=cv2.drawContours(image,contours,-1,(0,255,0),1)
		#cv2.imwrite("out.png",after_Binary)
		#cv2.imwrite("blur.png",after_Blurr)
		#cv2.imwrite("median blur.png",after_MedianBlur)
		#cv2.imwrite("Canny.png",after_Canny)
		
		#after_Binary=PhotoImage(file="out.png")
		#cwgt.img=after_Binary
		#cwgt.create_image(0, 0,  image=after_Binary)
	    
	    
	   
	  else:
		#cwgt.create_image(0, 0,  image=img_origin)
		print("xsfd")
		#print img_origin[100,100][0]
		#www=img_origin.width()
		#print www
	   
	  
	 
#

 def on_start(self):
	print("xsfd")
	self.showvideo()
	
 def off_video(self):
	 cwgt.frame.destroy()
 
	 
	 
	 ########
 
 
 


 ######################################################################################   show window 
 def show_Binary(self):     ## input Thresh_Binary
	 self.ThBinary=Tk()
	 self.ThBinary.geometry("350x100+350+350")
	 self.ThBinary.title("Binary")
	 self.scale_L = Scale(self.ThBinary, from_=255, to=0, command=self.onScale_L)
	 self.scale_L.pack(side=LEFT, padx=10)
  
	 self.varLow = IntVar()
	 self.label1 = Label(self.ThBinary,text="LOW")
	 self.label1.pack(side=LEFT,padx=0)
  
 
	 self.scale_H = Scale(self.ThBinary, from_=255, to=0, command=self.onScale_H)
	 self.scale_H.pack(side=LEFT, padx=20)
  
  
  
	 self.varHigh = IntVar()
	 self.label2 = Label(self.ThBinary, text="HIGH")
	 self.label2.pack(side=LEFT,padx=1) 
	 
	 binary = Button(self.ThBinary, text="OK", width=5,background="green" ,command=self.getdata_Binary)
	 binary.pack(side=LEFT)
	 #binary = Button(self.ThBinary, text="Get_Binary",background="green",command=self.getdata_Binary)
     #binary.pack()
 
########
 def show_Extract(self):     ## input Thresh_Extract
	 self.ThExtract=Tk()
	 self.ThExtract.geometry("750x100+350+350")
	 self.ThExtract.title("Extract_Color")
	 ###
	 self.scale_R_L = Scale(self.ThExtract, from_=255, to=0, command=self.onScale_R_L)
	 self.scale_R_L.pack(side=LEFT, padx=10)
  
	 self.varRed_L = IntVar()
	 self.label_R_L = Label(self.ThExtract,text="Red_L")
	 self.label_R_L.pack(side=LEFT,padx=0)
	 
	 self.scale_R_H = Scale(self.ThExtract, from_=255, to=0, command=self.onScale_R_H)
	 self.scale_R_H.pack(side=LEFT, padx=10)
  
	 self.varRed_H = IntVar()
	 self.label_R_H = Label(self.ThExtract,text="Red_H")
	 self.label_R_H.pack(side=LEFT,padx=0)
  
	 ###
	 self.scale_G_L = Scale(self.ThExtract, from_=255, to=0, command=self.onScale_G_L)
	 self.scale_G_L.pack(side=LEFT, padx=10)
  
	 self.varGreen_L = IntVar()
	 self.label_G_L = Label(self.ThExtract,text="Green_L")
	 self.label_G_L.pack(side=LEFT,padx=0)
	 
	 self.scale_G_H = Scale(self.ThExtract, from_=255, to=0, command=self.onScale_G_H)
	 self.scale_G_H.pack(side=LEFT, padx=10)
  
	 self.varGreen_H = IntVar()
	 self.label_G_H = Label(self.ThExtract,text="Green_H")
	 self.label_G_H.pack(side=LEFT,padx=0)
	 ###
	 self.scale_B_L = Scale(self.ThExtract, from_=255, to=0, command=self.onScale_B_L)
	 self.scale_B_L.pack(side=LEFT, padx=10)
  
	 self.varBlue_L = IntVar()
	 self.label_B_L = Label(self.ThExtract,text="Blue_L")
	 self.label_B_L.pack(side=LEFT,padx=0)
	 
	 self.scale_B_H = Scale(self.ThExtract, from_=255, to=0, command=self.onScale_B_H)
	 self.scale_B_H.pack(side=LEFT, padx=10)
  
	 self.varBlue_H= IntVar()
	 self.label_G_H = Label(self.ThExtract,text="Blue_H")
	 self.label_G_H.pack(side=LEFT,padx=0)
	 ###
	 
	 Extract = Button(self.ThExtract, text="OK", width=5,background="green" ,command=self.getdata_Extract)
	 Extract.pack(side=LEFT)
	 
##########
 def show_Partical(self):
	 print("")
     #self.ThBinary=Tk()
	 #self.ThBinary.geometry("200x70+350+350")
	 #self.ThBinary.title("Binary")
	 #self.scale_L = Scale(self.ThBinary, from_=0, to=255, command=self.onScale_L)
	 #self.scale_L.pack(side=LEFT, padx=10)
  
	 #self.varLow = IntVar()
	 #self.label1 = Label(self.ThBinary,text="LOW")
	 #self.label1.pack(side=LEFT,padx=0)
  
 
	 #self.scale_H = Scale(self.ThBinary, from_=0, to=255, command=self.onScale_H)
	 #self.scale_H.pack(side=LEFT, padx=20)
  
  
  
	 #self.varHigh = IntVar()
	 #self.label2 = Label(self.ThBinary, text="HIGH")
	 #self.label2.pack(side=LEFT,padx=1) 
	 
	

#########


 def password(self):       ##input password
	
	self.master = Tk()
	self.master.title("pass")
	self.master.geometry("200x70+350+350")
	self.content = StringVar()
	
	self.entry = Entry(self.master, text="000", textvariable=self.content)
	self.entry.pack()
	
	b = Button(self.master, text="get", width=10, command=self.getdata)
	b.pack()
	text123 = self.content.get()
	self.content.set(text123)
	print(self.content.get()) 
############
 def  error(self):
	 mbox.showerror("dh","dsfsdf")
	 mbox.showwarning("fdf","fsdfs")
############################################################################################   get data 
 def getdata(self): ## get password button
	 print(self.entry.get())
	 
	 if self.entry.get()=="1111":
		 self.master.destroy()
		 
	 else:
	   tkMessageBox.showinfo(title="fail",message="again")	
####
 def getdata_Binary(self):
	
	 min_binary=str(self.varLow.get())
	 max_binary=str(self.varHigh.get())
	 text_binary=str("Binary : " + min_binary + "," + max_binary )
	 
	 #print(text_binary)
	 #if (self.infor) in globals():
	#	print "fijdkjkhkkkkkkkkkkkkkkkkkkkkkkkkk"
	 if hasattr(self,'infor'):
		self.infor.destroy()
	 if hasattr(self,'infor_Binary'):
		self.infor_Binary.destroy()
	 #self.infor_Binary.destroy()
	 if self.varHigh.get()>self.varLow.get():
		self.infor_Binary=Text(self,width=50,height=1)
		self.infor_Binary.pack()
		self.infor_Binary.insert(END,text_binary)
		self.ThBinary.destroy()
	 else :
		 tkMessageBox.showinfo(title="fail",message="again")
 	 
####
 def getdata_Extract(self):
	
	 min_R=str(self.varRed_L.get())
	 max_R=str(self.varRed_H.get())
	 
	 min_G=str(self.varGreen_L.get())
	 max_G=str(self.varGreen_H.get())
	 
	 min_B=str(self.varBlue_L.get())
	 max_B=str(self.varBlue_H.get())
	 
	 
	 text_Extract=str("Extract : " + "R(" + min_R + "," + max_R +")"  + "G(" + min_G +"," + max_G +")" + "B(" + min_B +"," + max_B +")" )
	
	 if hasattr(self,'infor'):
		self.infor.destroy()
	 if hasattr(self,'infor_Extract'):
		self.infor_Extract.destroy()
	 #self.infor.destroy()
	 #self.infor_Extract.destroy()
	 self.infor_Extract=Text(self,width=50,height=1)
	 self.infor_Extract.pack()
	 self.infor_Extract.insert(END,text_Extract)
	 
	 self.ThExtract.destroy()
###########
 # def getdata_Partical(self):
	
#	 min_binary=str(self.varLow.get())
#	 max_binary=str(self.varHigh.get())
#	 text_binary=str("Binary : " + min_binary + "," + max_binary )
	 
	 #print(text_binary)
#	 self.infor.destroy()
	 
#	 self.infor=Text(self,width=50,height=1)
#	 self.infor.pack()
#	 thongtin2="hello"
#	 self.infor.insert(END,text_binary)	 

  ######
     
	 
############################################################################################  main
	
root.geometry("1500x520+100+100")
app = Example(root)
root.mainloop()


###################


