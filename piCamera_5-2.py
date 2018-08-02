#from Tkinter import Tk, Frame, BOTH, Button,RIGHT,RAISED,LEFT,IntVar,BOTTOM
#from Tkinter import BooleanVar,Checkbutton,PhotoImage,Canvas,W
#from Tkinter import Scale,StringVar,END,Listbox,Label,Menu,Entry
#from PIL import Image
#import ttk
import time
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
import threading
import tkFileDialog
import cv2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

##############################
Led_OK=16
Led_NG=18
Led_stt=13

####

in1=10
in2=11
in3=12
in4=15

GPIO.setwarnings(False)#trung 1604

#GPIO.setup(in1,GPIO.IN)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#PIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(in3,GPIO.IN)
#GPIO.setup(in4,GPIO.IN)


#####



GPIO.setup(Led_OK,GPIO.OUT)
GPIO.setup(Led_NG,GPIO.OUT)
GPIO.setup(Led_stt,GPIO.OUT)

GPIO.output(Led_OK,GPIO.LOW)
GPIO.output(Led_NG,GPIO.LOW)


##############################
from library import *
import os

#cmlib.Init()
#cmlib.OutClear()
#cmlib.ErrorClear()


#cmlib.LightOff()
camera=picamera.PiCamera()

camera.resolution=(400,300)
camera.framerate=90 #80 trung 
loadprogram=0
now = datetime.now()
######

##################
#import ImageTk
onvideo=1
root = Tk()

cwgt=Canvas(root,width=400)
cwgt2=Canvas(root,width=400)

cwgt.pack(fill=BOTH,expand=False,side=RIGHT,padx=1,pady=1)
cwgt2.pack(fill=BOTH,expand=False,side=RIGHT,padx=1,pady=1)
cwgt.camera=camera
#
cwgt.img="menu.png"
#cap = cv2.VideoCapture(0)
#startIndex = 0
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
##
#tkMessageBox.showinfo(title="dsfs",message="sdgdgd")

def average(src,i,j,n):
	t1=int(src[i-2,j-2][n])+int(src[i-1,j-2][n])+int(src[i,j-2][n])+int(src[i+1][j-2][n])+int(src[i+2,j-2][n])
	t2=int(src[i-2,j-1][n])+int(src[i-1,j-1][n])+int(src[i,j-1][n])+int(src[i+1][j-1][n])+int(src[i+2,j-1][n])
	t3=int(src[i-2,j][n])+int(src[i-1,j][n])+int(src[i,j][n])+int(src[i+1][j][n])+int(src[i+2,j][n])
	t4=int(src[i-2,j+1][n])+int(src[i-1,j+1][n])+int(src[i,j+1][n])+int(src[i+1][j+1][n])+int(src[i+2,j+1][n])
	t5=int(src[i-2,j+2][n])+int(src[i-1,j+2][n])+int(src[i,j+2][n])+int(src[i+1][j+2][n])+int(src[i+2,j+2][n])
	return int (t1+t2+t3+t4+t5)/25
	
def averageV(src,i,j,n):
	t=int(src[i-3,j][n])+int(src[i-2,j][n])+int(src[i-1,j][n])+int(src[i,j][n])+int(src[i+1][j][n])+int(src[i+2,j][n])+int(src[i+3,j][n])
	return int(t/5)


def inttotext1(x0):
	text=str(x0)
	if x0>99:
		text_x0=str(x0)
	else :
		if x0>9:
			text_x0=str("0"+ text)
		else :
			text_x0=str("00"+text)
	return text_x0

	 
#############################################    khai bao ban dau
class Example(Frame):
	
#######################################################################



 def __init__(self, parent):
  Frame.__init__(self, width=1000,height=1000, background="green")
  self.parent = parent
  self.pack(fill=BOTH,expand=True)
  self.initUI()
  cmlib.Init()
  cmlib.LightOn()
  GPIO.output(Led_stt,GPIO.HIGH)
 def initUI(self):
  self.parent.title("Cravis_ver1")
  self.pack(fill=BOTH, expand=1)
  frame = Frame(self, width=1500,height=200,relief=RAISED, borderwidth=1)
  frame.pack(expand=False)
  ####frame.config(bg="blue")
  self.pack(expand=False)
  ####################
  
  ##########################
  
  frame2 = Frame(self, width=1500,height=300,relief=RAISED, borderwidth=1)
  frame2.pack(expand=False)
  self.pack(expand=False)

  #self.var0=BooleanVar()
  self.var1=BooleanVar() 
  self.var2=BooleanVar()
  self.var3=BooleanVar()
  self.var4=BooleanVar() 
  self.var5=BooleanVar()
  self.var6=BooleanVar() 
  self.var7=BooleanVar()
  
  self.varDeBug=BooleanVar()
  self.varJudgement=BooleanVar()
  self.varSaveOK=BooleanVar()
  self.varSaveNG=BooleanVar()
  
  self.varPLC=BooleanVar()
  
  self.varArea1=BooleanVar()
  self.varArea2=BooleanVar()
  self.varArea3=BooleanVar()
  self.varArea4=BooleanVar()
  
  ###
  
  self.varJudgement.set(1)
  ###
  self.content=IntVar()

  
  reset_Area_Button = Button(self, width=10,text="reset_Area",command=self.reset_Area)
  reset_Area_Button.place(x=610,y=400)
  
  set_Area_Button = Button(self, width=10,text="set_Area",command=self.set_Area)
  set_Area_Button.place(x=610,y=430)
  
  show_Area_Button = Button(self, width=10,text="show_Area",command=self.show_Area)
  show_Area_Button.place(x=610,y=460)
  
  
  

  
  quitButton = Button(self,text="Quit",command=self.off_video)
  quitButton.place(x=50,y=20)
  
  startButton = Button(self,text="Video",command=self.showvideo)
  startButton.place(x=100,y=20)
  
  TakePicButton = Button(self,text="TakePic",command=self.Takepic)
  TakePicButton.place(x=150,y=20)
  
  AnalysedButton = Button(self,text="Analyze",bg="green",command=self.Analyse)
  AnalysedButton.place(x=650,y=120)
  
#  LoadDataButton = Button(self,text="Load_Data",bg="green",command=self.confirm_LoadData)
#  LoadDataButton.place(x=550,y=90)
  
  SaveDataButton = Button(self,text="Save_Data",bg="green",command=self.confirm_SaveData)
  SaveDataButton.place(x=550,y=120)
  ######
  cb2 = Checkbutton(self, text="Extract", variable=self.var1 ,command=self.on_Extract)
  cb2.place(x=80, y=50)
  
  cb1 = Checkbutton(self, text="Balance", variable=self.var2 )
  cb1.place(x=80, y=80)
  
  cb3 = Checkbutton(self, text="Partical", variable=self.var3 ,command=self.on_Partical)
  cb3.place(x=80, y=110)
  
  cb4 = Checkbutton(self, text="Binary", variable=self.var4 ,command=self.on_Binary)
  cb4.place(x=80, y=140)
  
  cb5 = Checkbutton(self, text="Sobel", variable=self.var5 ,command=self.on_Sobel)
  cb5.place(x=80, y=170)
  cbNG = Checkbutton(self, text="SaveNG", variable=self.varSaveNG )
  cbNG.place(x=620, y=20)
  cbOK = Checkbutton(self, text="SaveOK", variable=self.varSaveOK )
  cbOK.place(x=550, y=20)
  
  cbDeBug = Checkbutton(self, text="DeBug", variable=self.varDeBug )
  cbDeBug.place(x=550, y=40)
  
  cbPLC = Checkbutton(self, text="PLC", variable=self.varPLC )
  cbPLC.place(x=550, y=60)
  
  cb7 = Checkbutton(self, text="Lamp", variable=self.var7,command=self.on_Lamp )
  cb7.place(x=10, y=470)
######

  self.txt_thresh_Area1=Text(self,width=10,height=1)
  self.txt_thresh_Area1.place(x=450,y=300)
  self.txt_thresh_Area1.insert(END,"0")
  
  self.txt_thresh_Area2=Text(self,width=10,height=1)
  self.txt_thresh_Area2.place(x=530,y=300)
  self.txt_thresh_Area2.insert(END,"0")
  
  self.txt_thresh_Area3=Text(self,width=10,height=1)
  self.txt_thresh_Area3.place(x=610,y=300)
  self.txt_thresh_Area3.insert(END,"0")
  
  self.txt_thresh_Area4=Text(self,width=10,height=1)
  self.txt_thresh_Area4.place(x=690,y=300)
  self.txt_thresh_Area4.insert(END,"0")
  
  self.SaveThreshold()
  #####
  cbJudgement = Checkbutton(self, text="Judgement", variable=self.varJudgement)
  cbJudgement.place(x=550, y=210)
  
  cbArea1 = Checkbutton(self, text="Area1", variable=self.varArea1,command=self.enable_Area1)
  cbArea1.place(x=450, y=330)
  
  cbArea1 = Checkbutton(self, text="Area2", variable=self.varArea2,command=self.enable_Area2)
  cbArea1.place(x=530, y=330)
  
  cbArea1 = Checkbutton(self, text="Area3", variable=self.varArea3,command=self.enable_Area3)
  cbArea1.place(x=610, y=330)
  
  cbArea1 = Checkbutton(self, text="Area4", variable=self.varArea4,command=self.enable_Area4)
  cbArea1.place(x=690, y=330)
  #######
  SaveThreshold = Button(self,text="SaveThreshold",command=self.SaveThreshold)
  SaveThreshold.place(x=550,y=360)
 ###############################
 

  ###################################
 
  AdjustExtractButton = Button(self,text="Adjust_Extract",command=self.AdjustExtract)
  AdjustExtractButton.place(x=340,y=50)
  
  
  AdjustBinaryButton = Button(self,text="Adjust_Partical",command=self.AdjustPartical)
  AdjustBinaryButton.place(x=340,y=110)
  
  AdjustExtractButton = Button(self,text="Adjust_Binary",command=self.AdjustBinary)
  AdjustExtractButton.place(x=340,y=140)
  
  AdjustExtractButton = Button(self,text="Adjust_Sobel",command=self.AdjustSobel)
  AdjustExtractButton.place(x=340,y=170)
  
  
  

  ########
  self.infor_Alg1=Text(self,width=40,height=1)
  self.infor_Alg1.place(x=130,y=250)
  self.label_Alg1 = Label(self,text="Extract: ")
  self.label_Alg1.place(x=50,y=250)
  ##
  #self.infor_Alg2=Text(self,width=40,height=1)
  #self.infor_Alg2.place(x=130,y=270)
  #self.label_Alg2 = Label(self,text="Balance: ")
  #self.label_Alg2.place(x=50,y=270)
  
  ##
  self.infor_Alg3=Text(self,width=40,height=1)
  self.infor_Alg3.place(x=130,y=270)
  self.label_Alg3 = Label(self,text="Partical: ")
  self.label_Alg3.place(x=50,y=270)
  ##
  self.infor_Alg4=Text(self,width=40,height=1)
  self.infor_Alg4.place(x=130,y=290)
  self.label_Alg4 = Label(self,text="Binary: ")
  self.label_Alg4.place(x=50,y=290)
  ##
  self.infor_Alg5=Text(self,width=40,height=1)
  self.infor_Alg5.place(x=130,y=310)
  self.label_Alg5 = Label(self,text="Sobel: ")
  self.label_Alg5.place(x=50,y=310)
  ##
  
  
  self.infor_Area1=Text(self,width=20,height=1)
  self.infor_Area1.place(x=100,y=400)
  self.label_Area1 = Label(self,text="Area1: ")
  self.label_Area1.place(x=50,y=400)
  
  ##
  self.infor_Area2=Text(self,width=20,height=1)
  self.infor_Area2.place(x=350,y=400)
  self.label_Area2 = Label(self,text="Area2: ")
  self.label_Area2.place(x=300,y=400)
  ##
  self.infor_Area3=Text(self,width=20,height=1)
  self.infor_Area3.place(x=100,y=450)
  self.label_Area3 = Label(self,text="Area3: ")
  self.label_Area3.place(x=50,y=450)
  ##
  self.infor_Area4=Text(self,width=20,height=1)
  self.infor_Area4.place(x=350,y=450)
  self.label_Area4 = Label(self,text="Area4: ")
  self.label_Area4.place(x=300,y=450)
  #####
  
  
  ################################
  self.infor=Text(self,width=50,height=2)
  self.infor.pack()
  thongtin="Welcome to CRAVIS Program  \n  VISUAL GROUP (version 01)"
  self.infor.insert(END,thongtin)
  
  #####
  
  self.infor_OK_NG=Text(self,width=25,height=1)
  self.infor_OK_NG.place(x=600,y=510)
  thongtin_OK_NG="Total_OK_NG"
  self.infor_OK_NG.insert(END,thongtin_OK_NG)
  
  #####
  
  self.infor_program=Text(self,width=25,height=1)
  self.infor_program.place(x=600,y=530)
  thongtin_program="Please load program"
  self.infor_program.insert(END,thongtin_program)
  
  ###################################

  menuBar = Menu(self.parent)
  self.parent.config(menu=menuBar)
  
  fileMenu1 = Menu(menuBar)
  fileMenu2 = Menu(menuBar)
  fileMenu3 = Menu(menuBar)
  
  fileMenu1.add_command(label="zoom", command=self.zoom)
  fileMenu1.add_command(label="password", command=self.zoom)
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
  self.var_Program = StringVar()
  self.var_Program.set("13042018newlightv1.txt")#2018_0304newpv2.txt
  self.label_Program = Label(self, text=1, bg="yellow",textvariable=self.var_Program)
  self.label_Program.pack()
  path="/home/pi/Desktop/Program"
  menu_program=os.listdir(os.path.expanduser(path))
  self.lb_Program = Listbox(self)
  for i in menu_program:
	  self.lb_Program.insert(END, i)
  self.lb_Program.bind("<<ListboxSelect>>", self.Select_Program)
  self.lb_Program.pack()
  self.loadButton = Button(self,text="Load_Program",command=self.on_Load)
  self.loadButton.pack()
  ####
  self.set_Area()
  self.reset_Area()
  self.number_OK=0
  self.number_NG=0
  
  self.var7.set(1)
  self.varSaveNG.set(1)
  self.varSaveOK.set(1)
  self.varPLC.set(1)
  
  self.valueAnalyse=0
  self.LoadData()
  #GPIO.add_event_detect(11,GPIO.RISING,callback=self.Start,bouncetime=50)# input from PLC
  GPIO.add_event_detect(11,GPIO.RISING,callback=self.Start,bouncetime=200)# input from PLC
  #GPIO.add_event_detect(15,GPIO.RISING,callback=self.Start,bouncetime=200)# input from PLC
 #def Start(self,channel):
	 #if  self.varPLC.get()==1:
		 #self.varPLC.set =0				# trung 0404 NG takepic 2 times
		# self.Takepic()
		 #GPIO.remove_envent_detect(11)
  
 def Printt(self,channel):
	 print "aa"
 	 
 def Select_Program(self, val):
    sender = val.widget
    idx = sender.curselection()
    value = sender.get(idx)
    self.var_Program.set(value)
    print self.var_Program.get()
 def on_Load(self):
	   self.confirm_LoadData()
########
 def onScale_H(self, val):# Binary High Threshold
    v = int(float(val))
    self.varHigh.set(v)
    print (v)
    
 def onScale_L(self, val):# Binary Low Threshold
    v = int(float(val))
    self.varLow.set(v)
    print (v)
  ###########

 ##
 def onScale_partical_area1(self,val):
	v = int(float(val))
	self.varPartical1.set(v)
	print (v)
 def onScale_partical_area2(self,val):
	v = int(float(val))
	self.varPartical2.set(v)
	print (v)
 def onScale_partical_area3(self,val):
	v = int(float(val))
	self.varPartical3.set(v)
	print (v)
 def onScale_partical_area4(self,val):
	v = int(float(val))
	self.varPartical4.set(v)
	print (v)
 ############################
 def onScale_sobel_H(self, val):
    v = int(float(val))
    self.varHigh_Sobel.set(v)
    print (v)
    
 def onScale_sobel_L(self, val):
    v = int(float(val))
    self.varLow_Sobel.set(v)
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
	 f=open('a.txt','w+')
	 #line=f.readline()
	 infor="1111111111111\n 2222222222222222222\n333333333333333"
	 f.write(infor)
	 line=f.readline()
	 for line in f:
		print (line)
 def zoom(self):
	 root.geometry("1500x500")
######################################################   ############       Algorithm

 def on_Lamp(self):
	 if self.var7.get()==True:
		 cmlib.LightOn()
	 else :
		 cmlib.LightOff()
###
 def on_Extract(self):
	 if self.var1.get() == True:
	  self.show_Extract()
	 else :
		 if hasattr(self,'ThExtract'):
			 self.ThExtract.withdraw()
###	
 def on_Partical(self):
	 if self.var3.get() == True:
	  self.show_Partical()
	 else :
		 if hasattr(self,'ThPartical'):
			 self.ThPartical.withdraw()	 
 def on_Binary(self):
	 if self.var4.get() == True:
	  self.show_Binary() #show window
	 else :
		 if hasattr(self,'ThBinary'):
			 self.ThBinary.withdraw()
###	 
 def on_Sobel(self):
	 if self.var5.get() == True:
	  self.show_Sobel()
	 else :
		 if hasattr(self,'ThSobel'):
			 self.ThSobel.withdraw()
			 
 #####
 def enable_Area1(self):
	 if self.varArea1.get()==True:
		 self.spec1=1
	 else :
		 self.spec1=0
 def enable_Area2(self):
	 if self.varArea2.get()==True:
		 self.spec2=1
	 else :
		 self.spec2=0
 def enable_Area3(self):
	 if self.varArea3.get()==True:
		 self.spec3=1
	 else :
		 self.spec3=0
 def enable_Area4(self):
	 if self.varArea4.get()==True:
		 self.spec4=1
	 else :
		 self.spec4=0	 
###########################		 

 def showvideo(self): 
	 
     if camera.resolution==(400,300):
		print  ("ok")
		cwgt.camera.start_preview()
 def off_video(self):
	 camera.stop_preview()
###############################################################################   button  to analyse image
 def Analyse(self):
	 self.valueAnalyse=1
	 self.in_path=tkFileDialog.askopenfilename()
	 print self.in_path
	 self.Takepic()
############################################# 
 
 #GPIO.add_event_detect(11,GPIO.RISING,callback=self.Start,bouncetime=500)# input from PLC

############################################################
 def Start(self,channel):
	 
	 if  self.varPLC.get()==1:
		 self.varPLC.set =0				# trung 0404 NG takepic 2 times 
		 self.Takepic()
		 #GPIO.remove_envent_detect(11)
		 
 def Takepic(self):  ## take pic button
	  number_White1=0
	  number_White2=0
	  number_White3=0
	  number_White4=0
	  
	  number_Black1=0
	  number_Black2=0
	  number_Black3=0
	  number_Black4=0
	  
	  number_keep1=0
	  number_keep2=0
	  number_keep3=0
	  number_keep4=0
	 # src = Frame(cwgt, width=400,height=300,relief=RAISED, borderwidth=1)
	  
	  
	  if self.valueAnalyse==1:
		img_analyse=cv2.imread( self.in_path)
		cv2.imwrite("src.png",img_analyse)  
		cv2.imwrite("analysed.png",img_analyse) 
		self.valueAnalyse=0
	  else :
		#analysed=camera.capture('analysed.png')
		src=camera.capture('src.png')
		#cv2.imwrite("analysed.png",src)
		#self.varPLC.set =0				# trung 0404 NG takepic 2 times
		analysed=camera.capture('analysed.png')
		#src= analysed
		#cv2.imwrite("src.png",analysed)
		#GPIO.remove_envent_detect(11)
	  #if self.varSaveNG.get()==1:
		#camera.capture("/home/pi/Desktop/New/Image/{0:%Y%m%d-%H%M%S}.png" .format(datetime.now()))
		#img_RGB=cv2.imread("src.png")
	
	  ####
	  if self.var1.get() == True:
		min_R=self.varRed_L.get()
		max_R=self.varRed_H.get()
	  
		min_G=self.varGreen_L.get()
		max_G=self.varGreen_H.get()
	  
		min_B=self.varBlue_L.get()
		max_B=self.varBlue_H.get()  
		
		pro_2 = cv2.imread('analysed.png')
		lower= np.array([min_B,min_G,min_R],np.uint8)
		upper = np.array([max_B,max_G,max_R],np.uint8)
		mask = cv2.inRange(pro_2, lower, upper)
		analysed = cv2.bitwise_and(pro_2,pro_2, mask= mask)
		cv2.imwrite("analysed.png",analysed)
	  #img_show=PhotoImage(file="analysed.png")
	  #cwgt.img=img_show
	  #cwgt.create_image(200, 200,  image=img_show)  
	  
	  if self.var2.get() == True:
		img=cv2.imread("analysed.png")
		equ=cv2.equalizeHist(img[:,:,0])
		cv2.imwrite("analysed.png",equ)
	  ####
	  
	  ####
	  
	  if self.var3.get() == True:
		  src=cv2.imread("analysed.png")
		  src_result=cv2.imread("analysed.png")
		  
		  for j in range(self.x0_1,self.x1_1):
			  for i in range(self.y0_1,self.y1_1):
				  #if src[i,j][0]< int(averageV(src,i,j,0)-self.varPartical1.get()):
					  #src_result[i,j]=[0,0,0]
					  #number_Black1=number_Black1+1
				  if (src[i,j][0]> int(averageV(src,i,j,0)+self.varPartical1.get()) and src[i,j][0]>src[i-1,j][0] and src[i,j][0] > 100) or src[i,j][0]> int(averageV(src,i,j,0)+50) :
					  src_result[i,j]=[255,255,255]
					  number_White1=number_White1+1	 
				  #else :
					#  number_keep1=number_keep1+1
		  for j in range(self.x0_2,self.x1_2):
			  for i in range(self.y0_2,self.y1_2):
				  #if src[i,j][0]< int(averageV(src,i,j,0)-self.varPartical2.get()):
					  #src_result[i,j]=[0,0,0]
					  #number_Black2=number_Black2+1
				  if src[i,j][0]> int(averageV(src,i,j,0)+self.varPartical2.get())and src[i,j][0]>140:
					  src_result[i,j]=[255,255,255]
					  number_White2=number_White2+1	 
				  #else :
					  #number_keep2=number_keep2+1
		  for j in range(self.x0_3,self.x1_3):
			  for i in range(self.y0_3,self.y1_3):
				  #if src[i,j][0]< int(averageV(src,i,j,0)-self.varPartical3.get()):
					 # src_result[i,j]=[0,0,0]
					 # number_Black3=number_Black3+1
				  if src[i,j][0]> int(averageV(src,i,j,0)+self.varPartical3.get())and src[i,j][0]>140:
					  src_result[i,j]=[255,255,255]
					  number_White3=number_White3+1	
				  #else :
					  #number_keep3=number_keep3+1
		  for j in range(self.x0_4,self.x1_4):
			  for i in range(self.y0_4,self.y1_4):
				  #if src[i,j][0]< int(averageV(src,i,j,0)-self.varPartical4.get()):
					  #src_result[i,j]=[0,0,0]
					 # number_Black4=number_Black4+1
				  if src[i,j][0]> int(averageV(src,i,j,0)+self.varPartical4.get())and src[i,j][0]>140:
					  src_result[i,j]=[255,255,255]
					  number_White4=number_White4+1
				  #else :
					  #number_keep4=number_keep4+1 
		  cv2.imwrite("analysed.png",src_result)
	  ####	
	  if self.var4.get()==True:
		  src=cv2.imread("analysed.png")
		  retval,res = cv2.threshold(src, self.varLow.get(), self.varHigh.get(), cv2.THRESH_BINARY)
		  cv2.imwrite("analysed.png",res) 
	  ####		  
	  if self.var5.get() == True:
		  src=cv2.imread("analysed.png")
		  analysed=cv2.Canny(src,self.varLow_Sobel.get(),self.varHigh_Sobel.get())
		  cv2.imwrite("analysed.png",analysed)
		 
	  img_show=PhotoImage(file="analysed.png")
	  cwgt.img=img_show
	  cwgt.create_image(200, 200,  image=img_show)
	  #####
	  thongtinArea=str(str(number_White1)+","+str(number_White2)+","+str(number_White3)+","+str(number_White4))
	  cwgt.inforArea.delete('1.0',END)
	  cwgt.inforArea.insert(END,thongtinArea) 
	  ###
	  thongtinArea_keep=str(str(number_keep1)+","+str(number_keep2)+","+str(number_keep3)+","+str(number_keep4))
	  cwgt.inforArea_Black.delete('1.0',END)
	  cwgt.inforArea_Black.insert(END,thongtinArea_keep) 
	  ###
	  #thongtinArea_Black=str(str(number_Black1)+","+str(number_Black2)+","+str(number_Black3)+","+str(number_Black4))
	  #cwgt.inforArea_Black.delete('1.0',END)
	  #cwgt.inforArea_Black.insert(END,thongtinArea_Black) 
	  #####
	  if self.varDeBug.get()==1:
		  src=cv2.imread("analysed.png")
		  cv2.imwrite("src.png",src)
		  
		  img_origin=PhotoImage(file="analysed.png")
		  cwgt2.img=img_origin
		  cwgt2.create_image(200, 200,  image=img_origin)
	  else :
	      img_origin=PhotoImage(file="src.png")
	      cwgt2.img=img_origin
	      cwgt2.create_image(200, 200,  image=img_origin)
	  #####
	  if self.varJudgement.get() == True : #and self.var3.get() == True:
		  Area1=1
		  Area2=1
		  Area3=1
		  Area4=1
		  if self.varArea1.get()==True and number_White1<self.specArea1:
			  Area1=0
		  if self.varArea2.get()==True and number_White2>self.specArea2:
			  Area2=0
		  if self.varArea3.get()==True and number_White3>self.specArea3:
			  Area3=0
		  if self.varArea4.get()==True and number_White4>self.specArea4:
			  Area4=0
		  
		  #####
		  img_OKNG=cv2.imread("src.png")
		  font = cv2.FONT_HERSHEY_SIMPLEX
		  #trung comment 0404 revise
		  #img_OKNG=cv2.imread("src.png")
		  #font = cv2.FONT_HERSHEY_SIMPLEX
		  #if (number_White2 > 150) or (number_White2 > 100 and number_White2 < 150 and number_White1<20):
		  #if number_White2< 50 :
		  
		  if (Area1==0 or Area4==0) : 
			  
			  if self.varPLC.get()==1:
					GPIO.output(Led_OK,GPIO.LOW)
					GPIO.output(Led_NG,GPIO.HIGH)
			  else:
					GPIO.output(Led_NG,GPIO.LOW)
					GPIO.output(Led_OK,GPIO.LOW)
			  
			  NG=PhotoImage(file="/home/pi/Desktop/Data/ImageOKNG/NG.png")
			  cwgt2.img2=NG
			  cwgt2.create_image(200, 500,  image=NG)
			  
			  self.number_NG=self.number_NG+1
			  Data_result=str("{0:%Y%m%d-%H%M%S : }".format(datetime.now())+" NG ---------- "+thongtinArea +":" + "\n")
			  
			  if self.varSaveNG.get()==1:
				  cv2.putText(img_OKNG,'NG',(50,50), font, 1, (0,0,255), 1, cv2.LINE_AA)
				  cv2.imwrite("/home/pi/Desktop/Data/Image/NG/{0:%Y%m%d-%H%M%S}.png" .format(datetime.now()),img_OKNG)
				  
			
				  
		  else :
			  self.number_OK=self.number_OK+1
			  OK=PhotoImage(file="/home/pi/Desktop/Data/ImageOKNG/OK.png")
			  cwgt2.img2=OK
			  cwgt2.create_image(200, 500,  image=OK)
			  Data_result=str("{0:%Y%m%d-%H%M%S : }".format(datetime.now())+" OK - "+thongtinArea +":" +"\n")
			  ####
			  if self.varSaveOK.get()==1:
				  cv2.putText(img_OKNG,'OK',(50,50), font, 1, (0,255,0), 1, cv2.LINE_AA)
				  cv2.imwrite("/home/pi/Desktop/Data/Image/OK/{0:%Y%m%d-%H%M%S}.png" .format(datetime.now()),img_OKNG)
				  
			  ####
			  if self.varPLC.get()==1:
				  GPIO.output(Led_NG,GPIO.LOW)
				  GPIO.output(Led_OK,GPIO.HIGH)
			  else :
				  GPIO.output(Led_NG,GPIO.LOW)
				  GPIO.output(Led_OK,GPIO.LOW)
		  f=open("/home/pi/Desktop/Data/DataResult/{0:%Y%m%d}".format(datetime.now())+'.txt','a+')
		  f.write(Data_result)
	  		  
	  thongtin_OK_NG=str( "Total:" +str(self.number_OK+self.number_NG) +"  OK:" + str(self.number_OK) + "  " + "NG:" + str(self.number_NG) )
	  self.infor_OK_NG.delete('1.0',END)
	  self.infor_OK_NG.insert(END,thongtin_OK_NG)
	  
	  
	  
	      
	  
	  
	  
	  
	  
	  #########
	  
	  
	  
	 
 
##################

 ######################################################################################   show window 
 def show_Binary(self):     ## input Thresh_Binary
	 
	 if (hasattr(self,'ThBinary')):
		 self.ThBinary.deiconify()
	 else :
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

##################################################
 def show_Extract(self):     ## input Thresh_Extract
	 
	 if hasattr(self,'ThExtract'):
		 self.ThExtract.deiconify()
	 else :
		 
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
###########################################################
 def show_Sobel(self):     ## Sobel
	 
	 if (hasattr(self,'ThSobel')):
		 self.ThSobel.deiconify()
	 else :
		 self.ThSobel=Tk()
		 self.ThSobel.geometry("350x100+350+350")
		 self.ThSobel.title("Sobel")
		 self.scale_sobel_L = Scale(self.ThSobel, from_=255, to=0, command=self.onScale_sobel_L)
		 self.scale_sobel_L.pack(side=LEFT, padx=10)
	  
		 self.varLow_Sobel = IntVar()
		 self.label1 = Label(self.ThSobel,text="LOW")
		 self.label1.pack(side=LEFT,padx=0)
	  
	 
		 self.scale_sobel_H = Scale(self.ThSobel, from_=255, to=0, command=self.onScale_sobel_H)
		 self.scale_sobel_H.pack(side=LEFT, padx=20)
	  
	  
	  
		 self.varHigh_Sobel = IntVar()
		 self.label2 = Label(self.ThSobel, text="HIGH")
		 self.label2.pack(side=LEFT,padx=1) 
		 
		 Sobel = Button(self.ThSobel, text="OK", width=5,background="green" ,command=self.getdata_Sobel)
		 Sobel.pack(side=LEFT)
##########
 def show_Partical(self):
	 if (hasattr(self,'ThPartical')):
		 self.ThPartical.deiconify()
	 else :
		 self.ThPartical=Tk()
		 self.ThPartical.geometry("500x100+350+350")
		 self.ThPartical.title("Partical")
		 
		 self.scale_partical_area1 = Scale(self.ThPartical, from_=200, to=0, command=self.onScale_partical_area1)
		 self.scale_partical_area1.pack(side=LEFT, padx=10)
		 
		 self.varPartical1 = IntVar()
		 self.label1 = Label(self.ThPartical,text="Area1")
		 self.label1.pack(side=LEFT,padx=0)
		 
		 ####
		 
		 self.scale_partical_area2 = Scale(self.ThPartical, from_=200, to=0, command=self.onScale_partical_area2)
		 self.scale_partical_area2.pack(side=LEFT, padx=10)
		 
		 self.varPartical2 = IntVar()
		 self.label2 = Label(self.ThPartical,text="Area2")
		 self.label2.pack(side=LEFT,padx=0)
		 
		 ####
		 
		 self.scale_partical_area3 = Scale(self.ThPartical, from_=200, to=0, command=self.onScale_partical_area3)
		 self.scale_partical_area3.pack(side=LEFT, padx=10)
		 
		 self.varPartical3 = IntVar()
		 self.label3 = Label(self.ThPartical,text="Area3")
		 self.label3.pack(side=LEFT,padx=0)
		 
		 ####
		 
		 self.scale_partical_area4 = Scale(self.ThPartical, from_=200, to=0, command=self.onScale_partical_area4)
		 self.scale_partical_area4.pack(side=LEFT, padx=10)
		 
		 self.varPartical4 = IntVar()
		 self.label4 = Label(self.ThPartical,text="Area4")
		 self.label4.pack(side=LEFT,padx=0)
	  
	 
		 
		 
		 Partical = Button(self.ThPartical, text="OK", width=5,background="green" ,command=self.getdata_Partical)
		 Partical.pack(side=LEFT)
	 
	

#########


 def  reset_Area(self):
	 self.text_empty="000,000,000,000"
	 self.infor_Area1.delete('1.0',END)
	 self.infor_Area2.delete('1.0',END)
	 self.infor_Area3.delete('1.0',END)
	 self.infor_Area4.delete('1.0',END)
	 self.infor_Area1.insert(END,self.text_empty)
	 self.infor_Area2.insert(END,self.text_empty)
	 self.infor_Area3.insert(END,self.text_empty)
	 self.infor_Area4.insert(END,self.text_empty)
	 cwgt.setArea1=0
	 cwgt.setArea2=0
	 cwgt.setArea3=0
	 cwgt.setArea4=0
	 self.set_Area()
	 
 def  set_Area(self):
	 
	 if cwgt.setArea1==0:
		 cwgt.area_x0_1=0
		 cwgt.area_y0_1=0
		 cwgt.area_x1_1=0
		 cwgt.area_y1_1=0
	 if cwgt.setArea2==0:
		 cwgt.area_x0_2=0
		 cwgt.area_y0_2=0
		 cwgt.area_x1_2=0
		 cwgt.area_y1_2=0
	 if cwgt.setArea3==0:
		 cwgt.area_x0_3=0
		 cwgt.area_y0_3=0
		 cwgt.area_x1_3=0
		 cwgt.area_y1_3=0
	 if cwgt.setArea4==0:
		 cwgt.area_x0_4=0
		 cwgt.area_y0_4=0
		 cwgt.area_x1_4=0
		 cwgt.area_y1_4=0
	 ####	 
	 self.x0_1=cwgt.area_x0_1
	 self.y0_1=cwgt.area_y0_1
	 self.x1_1=cwgt.area_x1_1
	 self.y1_1=cwgt.area_y1_1
	 self.textArea1=str(inttotext1(cwgt.area_x0_1)+","+inttotext1(cwgt.area_y0_1)+","+inttotext1(cwgt.area_x1_1)+","+inttotext1(cwgt.area_y1_1))
	 self.infor_Area1.delete('1.0',END)
	 self.infor_Area1.insert(END,self.textArea1)
	 ####
	 self.x0_2=cwgt.area_x0_2
	 self.y0_2=cwgt.area_y0_2
	 self.x1_2=cwgt.area_x1_2
	 self.y1_2=cwgt.area_y1_2
	 self.textArea2=str(inttotext1(cwgt.area_x0_2)+","+inttotext1(cwgt.area_y0_2)+","+inttotext1(cwgt.area_x1_2)+","+inttotext1(cwgt.area_y1_2))
	 self.infor_Area2.delete('1.0',END)
	 self.infor_Area2.insert(END,self.textArea2)
	 ####
	 self.x0_3=cwgt.area_x0_3
	 self.y0_3=cwgt.area_y0_3
	 self.x1_3=cwgt.area_x1_3
	 self.y1_3=cwgt.area_y1_3
	 self.textArea3=str(inttotext1(cwgt.area_x0_3)+","+inttotext1(cwgt.area_y0_3)+","+inttotext1(cwgt.area_x1_3)+","+inttotext1(cwgt.area_y1_3))
	 self.infor_Area3.delete('1.0',END)
	 self.infor_Area3.insert(END,self.textArea3)
	 ####
	 self.x0_4=cwgt.area_x0_4
	 self.y0_4=cwgt.area_y0_4
	 self.x1_4=cwgt.area_x1_4
	 self.y1_4=cwgt.area_y1_4
	 self.textArea4=str(inttotext1(cwgt.area_x0_4)+","+inttotext1(cwgt.area_y0_4)+","+inttotext1(cwgt.area_x1_4)+","+inttotext1(cwgt.area_y1_4))
	 self.infor_Area4.delete('1.0',END)
	 self.infor_Area4.insert(END,self.textArea4)
	 
 def show_Area(self):
	 font = cv2.FONT_HERSHEY_SIMPLEX
	 img = cv2.imread("src.png",cv2.IMREAD_COLOR)
	 cv2.rectangle(img,(self.x0_1,self.y0_1),(self.x1_1,self.y1_1),(255,0,0),2)
	 cv2.rectangle(img,(self.x0_2,self.y0_2),(self.x1_2,self.y1_2),(200,0,0),2)
	 cv2.rectangle(img,(self.x0_3,self.y0_3),(self.x1_3,self.y1_3),(150,0,0),2)
	 cv2.rectangle(img,(self.x0_4,self.y0_4),(self.x1_4,self.y1_4),(100,0,0),2)
	 if cwgt.setArea1==1:
		 cv2.putText(img,'1',(self.x0_1,self.y0_1), font, 1, (0,0,255), 1, cv2.LINE_AA)
	 if cwgt.setArea2==1:
		 cv2.putText(img,'2',(self.x0_2,self.y0_2), font, 1, (0,0,255), 1, cv2.LINE_AA)
	 if cwgt.setArea3==1:
		 cv2.putText(img,'3',(self.x0_3,self.y0_3), font, 1, (0,0,255), 1, cv2.LINE_AA)
	 if cwgt.setArea4==1:
		 cv2.putText(img,'4',(self.x0_4,self.y0_4), font, 1, (0,0,255), 1, cv2.LINE_AA)
	 img_show_Area=img
	 cv2.imwrite("show_Area.png",img_show_Area)
	 img_show=PhotoImage(file="show_Area.png")
	 cwgt2.img=img_show
	 cwgt2.create_image(200, 200,  image=img_show)
	 
	 

 def AdjustExtract(self):
	 if self.var1.get()==True:
		self.ThExtract.withdraw()
		self.ThExtract.deiconify()
	 thread.start_new_thread(printa())
 def AdjustPartical(self):
	 if self.var3.get()==True:
		self.ThPartical.withdraw()
		self.ThPartical.deiconify()
		
 def AdjustBinary(self):
	 if self.var4.get()==True:
		self.ThBinary.withdraw()
		self.ThBinary.deiconify()
 
 def AdjustSobel(self):
	 if self.var5.get()==True:
		self.ThSobel.withdraw()
		self.ThSobel.deiconify()
############################################################################################   get data 

 def confirm_SaveData(self):       ##input password
	
	self.master = Tk()
	self.master.title("pass")
	self.master.geometry("200x70+350+350")
	self.content = StringVar()
	
	self.entry = Entry(self.master, text="000", textvariable=self.content)
	self.entry.pack()
	
	b = Button(self.master, text="get", width=10, command=self.getdata_Save)
	b.pack()
############
 def getdata_Save(self):
	 self.set_Area()
	 
	 if  self.infor_Alg1.get('1.0',END)=="\n":
		 self.text_Extract="R(000,000)G(000,000)B(000,000)"
	 if  self.infor_Alg3.get('1.0',END)=="\n":
		 self.text_Partical="000"
	 if  self.infor_Alg4.get('1.0',END)=="\n":
		 self.text_binary="000,000"
	 if  self.infor_Alg5.get('1.0',END)=="\n":
		 self.text_Sobel="000,000"
	 if self.entry.get()=="1111":
		 self.master.destroy()
		 self.Save_to_()
	 else:
	   tkMessageBox.showinfo(title="fail",message="again")
 def Save_to_(self):
	self.Save = Tk()
	self.Save.title("Save_to")
	self.Save.geometry("200x70+350+350")
	self.content_save = StringVar()
	self.entry2 = Entry(self.Save, text="aaa", textvariable=self.content_save)
	self.entry2.pack()
	
	b = Button(self.Save, text="Save", width=10, command=self.SaveData)
	b.pack()
	print(self.content_save.get())
########
 def SaveData(self): ## get password button
		 
		 self.inforData_Extract="Extract : " + self.text_Extract
		 self.inforData_Partical="Partical : (" + self.text_Partical + ")"
		 self.inforData_binary="Binary : (" + self.text_binary + ")"
		 self.inforData_Sobel="Sobel : (" + self.text_Sobel + ")"
		 
		 self.inforData_Area1="Area1 : " + self.textArea1
		 self.inforData_Area2="Area2 : " + self.textArea2
		 self.inforData_Area3="Area3 : " + self.textArea3
		 self.inforData_Area4="Area4 : " + self.textArea4

			 
		 self.SumSpec=str(str(self.spec1)+str(self.spec2)+str(self.spec3)+str(self.spec4))
		 self.Threshold="Spec : "+str(self.SumSpec) +": "+ str(inttotext1(self.thresh_area1)+","+inttotext1(self.thresh_area2)+","+inttotext1(self.thresh_area3)+","+inttotext1(self.thresh_area4))
		 #print self.Threshold
		 
		 
		 #################
		 if self.var1.get()==1 :
			 data1="1"
		 else :
			data1="0"
		##
		 if self.var2.get()==1 :
			 data2="1"
		 else :
			data2="0"
		 ##
		 if self.var3.get()==1 :
			 data3="1"
		 else :
			data3="0"
		##
		 if self.var4.get()==1 :
			 data4="1"
		 else :
			data4="0"
		##
		 if self.var5.get()==1 :
			 data5="1"
		 else :
			data5="0"
		##
		 self.SumData=(data1+data2+data3+data4+data5)
		 self.inforData=str(self.SumData   + "\n" + self.inforData_Extract + "\n"+ self.inforData_Partical+"\n" + self.inforData_binary+ "\n"+self.inforData_Sobel+ "\n"+ self.inforData_Area1+"\n" + self.inforData_Area2+"\n" + self.inforData_Area3+"\n" + self.inforData_Area4+"\n" + self.Threshold)
		 #self.inforData=str(self.SumData )
		 print self.inforData 
		
		 f=open("/home/pi/Desktop/Program/"+str(self.entry2.get())+'.txt','w+')
		 f.write(self.inforData)
	 	 self.Save.destroy()
		 tkMessageBox.showinfo(title="Save",message="SaveData success !!")
############################################################################################
 def confirm_LoadData(self):
	if self.var_Program.get()=="":
		 tkMessageBox.showinfo(title="No program",message="Please choose Program !!")
	else :
		self.master = Tk()
		self.master.title("pass")
		self.master.geometry("200x70+350+350")
		self.content = StringVar()
		
		self.entry = Entry(self.master, text="000", textvariable=self.content)
		self.entry.pack()
		
		b = Button(self.master, text="get", width=10, command=self.getdata_Load)
		b.pack()
		text123 = self.content.get()
		self.content.set(text123)
		
	
 def getdata_Load(self): 
	 
	 if self.entry.get()=="1111":
		 self.master.destroy()
		 self.LoadData()
		 self.infor_program.delete('1.0',END)
		 thongtin_program=str("Program No : " + self.var_Program.get() )
		 self.infor_program.insert(END,thongtin_program)
		 self.lb_Program.destroy()
		 self.loadButton.destroy()
	 else:
	   tkMessageBox.showinfo(title="fail",message="again")	
##################################
 def LoadData(self):
	 print "Load"
	 #f=open('a.txt','r')
	 f=open("/home/pi/Desktop/Program/"+str(self.var_Program.get()),'r')
	 
	 self.SumData=f.readline()
	 
	 load_extract=f.readline()
	 load_partical=f.readline()
	 load_binary=f.readline()
	 load_sobel=f.readline()
	 
	 load_area1=f.readline()
	 load_area2=f.readline()
	 load_area3=f.readline()
	 load_area4=f.readline()
	 
	 load_threshold=f.readline()
	 
	 text_extract=(load_extract[10]+load_extract[11]+load_extract[12]+load_extract[13]+load_extract[14]+load_extract[15]+load_extract[16]+load_extract[17]+load_extract[18]+load_extract[19]+load_extract[20]+load_extract[21]+load_extract[22]+load_extract[23]+load_extract[24]+load_extract[25]+load_extract[26]+load_extract[27]+load_extract[28]+load_extract[29]+load_extract[30]+load_extract[31]+load_extract[32]+load_extract[33]+load_extract[34]+load_extract[35]+load_extract[36]+load_extract[37]+load_extract[38]+load_extract[39])
	 text_partical=(load_partical[12]+load_partical[13]+load_partical[14]+load_partical[15]+load_partical[16]+load_partical[17]+load_partical[18]+load_partical[19]+load_partical[20]+load_partical[21]+load_partical[22]+load_partical[23]+load_partical[24]+load_partical[25]+load_partical[26])
	 text_binary=(load_binary[10]+load_binary[11]+load_binary[12]+load_binary[13]+load_binary[14]+load_binary[15]+load_binary[16])
	 text_sobel=(load_sobel[9]+load_sobel[10]+load_sobel[11]+load_sobel[12]+load_sobel[13]+load_sobel[14]+load_sobel[15])
	 
	 text_area1=(load_area1[8]+load_area1[9]+load_area1[10]+load_area1[11]+load_area1[12]+load_area1[13]+load_area1[14]+load_area1[15]+load_area1[16]+load_area1[17]+load_area1[18]+load_area1[19]+load_area1[20]+load_area1[21]+load_area1[22])
	 text_area2=(load_area2[8]+load_area2[9]+load_area2[10]+load_area2[11]+load_area2[12]+load_area2[13]+load_area2[14]+load_area2[15]+load_area2[16]+load_area2[17]+load_area2[18]+load_area2[19]+load_area2[20]+load_area2[21]+load_area2[22])
	 text_area3=(load_area3[8]+load_area3[9]+load_area3[10]+load_area3[11]+load_area3[12]+load_area3[13]+load_area3[14]+load_area3[15]+load_area3[16]+load_area3[17]+load_area3[18]+load_area3[19]+load_area3[20]+load_area3[21]+load_area3[22])
	 text_area4=(load_area4[8]+load_area4[9]+load_area4[10]+load_area4[11]+load_area4[12]+load_area4[13]+load_area4[14]+load_area4[15]+load_area4[16]+load_area4[17]+load_area4[18]+load_area4[19]+load_area4[20]+load_area4[21]+load_area4[22])
	 
	 ###################
	 cwgt.area_x0_1=int(load_area1[8]+load_area1[9]+load_area1[10])
	 cwgt.area_y0_1=int(load_area1[12]+load_area1[13]+load_area1[14])
	 cwgt.area_x1_1=int(load_area1[16]+load_area1[17]+load_area1[18])
	 cwgt.area_y1_1=int(load_area1[20]+load_area1[21]+load_area1[22])
	 ##
	 cwgt.area_x0_2=int(load_area2[8]+load_area2[9]+load_area2[10])
	 cwgt.area_y0_2=int(load_area2[12]+load_area2[13]+load_area2[14])
	 cwgt.area_x1_2=int(load_area2[16]+load_area2[17]+load_area2[18])
	 cwgt.area_y1_2=int(load_area2[20]+load_area2[21]+load_area2[22])
	 ##
	 cwgt.area_x0_3=int(load_area3[8]+load_area3[9]+load_area3[10])
	 cwgt.area_y0_3=int(load_area3[12]+load_area3[13]+load_area3[14])
	 cwgt.area_x1_3=int(load_area3[16]+load_area3[17]+load_area3[18])
	 cwgt.area_y1_3=int(load_area3[20]+load_area3[21]+load_area3[22])
	 ##
	 cwgt.area_x0_4=int(load_area4[8]+load_area4[9]+load_area4[10])
	 cwgt.area_y0_4=int(load_area4[12]+load_area4[13]+load_area4[14])
	 cwgt.area_x1_4=int(load_area4[16]+load_area4[17]+load_area4[18])
	 cwgt.area_y1_4=int(load_area4[20]+load_area4[21]+load_area4[22])
	 
	 
	 cwgt.setArea1=1
	 cwgt.setArea2=1
	 cwgt.setArea3=1
	 cwgt.setArea4=1
	 
	 ###################
	 
	 value_low_red=int(load_extract[12]+load_extract[13]+load_extract[14])
	 value_high_red=int(load_extract[16]+load_extract[17]+load_extract[18])
	 
	 value_low_green=int(load_extract[22]+load_extract[23]+load_extract[24])
	 value_high_green=int(load_extract[26]+load_extract[27]+load_extract[28])
	 
	 value_low_blue=int(load_extract[32]+load_extract[33]+load_extract[34])
	 value_high_blue=int(load_extract[36]+load_extract[37]+load_extract[38])
	 ####
	 value_partical1=int (load_partical[12]+load_partical[13]+load_partical[14])
	 value_partical2=int (load_partical[16]+load_partical[17]+load_partical[18])
	 value_partical3=int (load_partical[20]+load_partical[21]+load_partical[22])
	 value_partical4=int (load_partical[24]+load_partical[25]+load_partical[26])
	 ####
	 value_low_binary=int (load_binary[10]+load_binary[11]+ load_binary[12])
	 value_high_binary=int (load_binary[14]+load_binary[15]+ load_binary[16])
	 ####
	 
	 value_low_sobel=int (load_sobel[9]+load_sobel[10]+ load_sobel[11])
	 value_high_sobel=int (load_sobel[13]+load_sobel[14]+ load_sobel[15])
	 #########################
	 value_area1_x0=int(load_area1[8]+load_area1[9]+load_area1[10])
	 value_area1_y0=int(load_area1[12]+load_area1[13]+load_area1[14])
	 value_area1_x1=int(load_area1[16]+load_area1[17]+load_area1[18])
	 value_area1_y1=int(load_area1[20]+load_area1[21]+load_area1[22])
	 ####
	 value_area2_x0=int(load_area2[8]+load_area2[9]+load_area2[10])
	 value_area2_y0=int(load_area2[12]+load_area2[13]+load_area2[14])
	 value_area2_x1=int(load_area2[16]+load_area2[17]+load_area2[18])
	 value_area2_y1=int(load_area2[20]+load_area2[21]+load_area2[22])
	 ####
	 value_area3_x0=int(load_area3[8]+load_area3[9]+load_area3[10])
	 value_area3_y0=int(load_area3[12]+load_area3[13]+load_area3[14])
	 value_area3_x1=int(load_area3[16]+load_area3[17]+load_area3[18])
	 value_area3_y1=int(load_area3[20]+load_area3[21]+load_area3[22])
	 ####
	 value_area4_x0=int(load_area4[8]+load_area4[9]+load_area4[10])
	 value_area4_y0=int(load_area4[12]+load_area4[13]+load_area4[14])
	 value_area4_x1=int(load_area4[16]+load_area4[17]+load_area4[18])
	 value_area4_y1=int(load_area4[20]+load_area4[21]+load_area4[22])
	 
	############################
	 self.x0_1=value_area1_x0
	 self.y0_1=value_area1_y0
	 self.x1_1=value_area1_x1
	 self.y1_1=value_area1_y1
	 ####
	 self.x0_2=value_area2_x0
	 self.y0_2=value_area2_y0
	 self.x1_2=value_area2_x1
	 self.y1_2=value_area2_y1
	 ####
	 self.x0_3=value_area3_x0
	 self.y0_3=value_area3_y0
	 self.x1_3=value_area3_x1
	 self.y1_3=value_area3_y1
	 ####
	 self.x0_4=value_area4_x0
	 self.y0_4=value_area4_y0
	 self.x1_4=value_area4_x1
	 self.y1_4=value_area4_y1
	 ##############################
	 self.show_Extract()
	 self.ThExtract.withdraw()
	 
	 self.show_Partical()
	 self.ThPartical.withdraw()
	 
	 self.show_Binary()
	 self.ThBinary.withdraw()
	 
	 self.show_Sobel()
	 self.ThSobel.withdraw()
	 
	#######
	
	 #self.varThreshold.set(value_threshold)
	 
	 self.varRed_L.set(value_low_red)
	 self.varRed_H.set(value_high_red)
	 self.varGreen_L.set(value_low_green)
	 self.varGreen_H.set(value_high_green)
	 self.varBlue_L.set(value_low_blue)
	 self.varBlue_H.set(value_high_blue)
	 
	 self.varPartical1.set(value_partical1)
	 self.varPartical2.set(value_partical2)
	 self.varPartical3.set(value_partical3)
	 self.varPartical4.set(value_partical4)
	 
	 self.varLow.set(value_low_binary)
	 self.varHigh.set(value_high_binary)
	 
	 self.varLow_Sobel.set(value_low_sobel)
	 self.varHigh_Sobel.set(value_high_sobel)
	 
	 
	 self.text_Extract=text_extract
	 self.text_Partical=text_partical
	 self.text_binary=text_binary
	 self.text_Sobel=text_sobel
	 
	 self.text_area1=text_area1
	 self.text_area2=text_area2
	 self.text_area3=text_area3
	 self.text_area4=text_area4
	 
	 
	
	 self.infor_Alg1.delete('1.0',END)
	 self.infor_Alg1.insert(END,self.text_Extract)
	 
	 self.infor_Alg3.delete('1.0',END)
	 self.infor_Alg3.insert(END,self.text_Partical)
	 
	 self.infor_Alg4.delete('1.0',END)
	 self.infor_Alg4.insert(END,self.text_binary)
	 
	 self.infor_Alg5.delete('1.0',END)
	 self.infor_Alg5.insert(END,self.text_Sobel)
	 #######
	 self.infor_Area1.delete('1.0',END)
	 self.infor_Area1.insert(END,self.text_area1)
	 
	 self.infor_Area2.delete('1.0',END)
	 self.infor_Area2.insert(END,self.text_area2)
	 
	 self.infor_Area3.delete('1.0',END)
	 self.infor_Area3.insert(END,self.text_area3)
	 
	 self.infor_Area4.delete('1.0',END)
	 self.infor_Area4.insert(END,self.text_area4)
	 #####
	 
	 value_spec_area1=int(load_threshold[13]+load_threshold[14]+load_threshold[15])
	 value_spec_area2=int(load_threshold[17]+load_threshold[18]+load_threshold[19])
	 value_spec_area3=int(load_threshold[21]+load_threshold[22]+load_threshold[23])
	 value_spec_area4=int(load_threshold[25]+load_threshold[26]+load_threshold[27])
	 
	 
	 self.thresh_Area1=str(value_spec_area1)
	 self.thresh_Area2=str(value_spec_area2)
	 self.thresh_Area3=str(value_spec_area3)
	 self.thresh_Area4=str(value_spec_area4)
	 
	 self.specArea1=int(value_spec_area1)
	 self.specArea2=int(value_spec_area2)
	 self.specArea3=int(value_spec_area3)
	 self.specArea4=int(value_spec_area4)
	 
	 self.txt_thresh_Area1.delete('1.0',END)
	 self.txt_thresh_Area1.insert(END,self.thresh_Area1)
	 
	 self.txt_thresh_Area2.delete('1.0',END)
	 self.txt_thresh_Area2.insert(END,self.thresh_Area2)
	 
	 self.txt_thresh_Area3.delete('1.0',END)
	 self.txt_thresh_Area3.insert(END,self.thresh_Area3)
	 
	 self.txt_thresh_Area4.delete('1.0',END)
	 self.txt_thresh_Area4.insert(END,self.thresh_Area4)
	 
	 
	 #####
	 if self.SumData[0]=="1":
		self.var1.set(1)
	 else:
		 self.var1.set(0)
		 
	 if self.SumData[1]=="1":
		self.var2.set(1)
	 else:
		 self.var2.set(0)
	 
	 if self.SumData[2]=="1":
		self.var3.set(1)
	 else:
		 self.var3.set(0)
		 
	 if self.SumData[3]=="1":
		self.var4.set(1)
	 else:
		 self.var4.set(0)
		 
	 if self.SumData[4]=="1":
		self.var5.set(1)
	 else:
		 self.var5.set(0)
		 
	 #####
	 
	 if load_threshold[7]=="1":
		self.varArea1.set(1)
	 else:
		 self.varArea1.set(0)
		 
	 if load_threshold[8]=="1":
		self.varArea2.set(1)
	 else:
		 self.varArea2.set(0)
	 
	 if load_threshold[9]=="1":
		self.varArea3.set(1)
	 else:
		 self.varArea3.set(0)
		 
	 if load_threshold[10]=="1":
		self.varArea4.set(1)
	 else:
		 self.varArea4.set(0)
		 
	 
###################################################################################		 
 def getdata_Binary(self):
	 min_binary=inttotext1(self.varLow.get())
	 max_binary=inttotext1(self.varHigh.get())
	 
	 self.text_binary=str( min_binary + "," + max_binary )
	 if self.varHigh.get()>self.varLow.get():
		self.infor_Alg4.delete('1.0',END)
		self.infor_Alg4.insert(END,self.text_binary)
		self.ThBinary.withdraw()
	 else :
		 tkMessageBox.showinfo(title="fail",message="again")
 	 
####
 def getdata_Extract(self):
	
	
	 min_R=inttotext1(self.varRed_L.get())
	 max_R=inttotext1(self.varRed_H.get())
	 
	 min_G=inttotext1(self.varGreen_L.get())
	 max_G=inttotext1(self.varGreen_H.get())
	 
	 min_B=inttotext1(self.varBlue_L.get())
	 max_B=inttotext1(self.varBlue_H.get())
	 
	 self.text_Extract=str("R(" + min_R + "," + max_R +")"  + "G(" + min_G +"," + max_G +")" + "B(" + min_B +"," + max_B +")" )
	
	 if ((self.varRed_H.get()>self.varRed_L.get())and(self.varGreen_H.get()>self.varGreen_L.get())and(self.varBlue_H.get()>self.varBlue_L.get())):
		self.infor_Alg1.delete('1.0',END)
		self.infor_Alg1.insert(END,self.text_Extract)
		self.ThExtract.withdraw()
	 else :
		 tkMessageBox.showinfo(title="fail",message="again")
###############
 def getdata_Sobel(self):
	 min_sobel=inttotext1(self.varLow_Sobel.get())
	 max_sobel=inttotext1(self.varHigh_Sobel.get())
	 self.text_Sobel=str( min_sobel + "," + max_sobel )
	 if self.varHigh_Sobel.get()>self.varLow_Sobel.get():
		self.infor_Alg5.delete('1.0',END)
		self.infor_Alg5.insert(END,self.text_Sobel)
		self.ThSobel.withdraw()
	 else :
		 tkMessageBox.showinfo(title="fail",message="again")
		 
##############
 def getdata_Partical(self):
	 thresh_Partical=str(str(inttotext1(self.varPartical1.get()))+","+str(inttotext1(self.varPartical2.get()))+","+str(inttotext1(self.varPartical3.get()))+","+str(inttotext1(self.varPartical4.get())))
	 
	 self.text_Partical=str(thresh_Partical)
	 self.infor_Alg3.delete('1.0',END)
	 self.infor_Alg3.insert(END,self.text_Partical)
	 self.ThPartical.withdraw()
##############
 def SaveThreshold(self):
	 
	 self.thresh_area1=int(self.txt_thresh_Area1.get('1.0',END))
	 self.thresh_area2=int(self.txt_thresh_Area2.get('1.0',END))
	 self.thresh_area3=int(self.txt_thresh_Area3.get('1.0',END))
	 self.thresh_area4=int(self.txt_thresh_Area4.get('1.0',END))
	 
	 self.specArea1=int(self.thresh_area1)
	 self.specArea2=int(self.thresh_area2)
	 self.specArea3=int(self.thresh_area3)
	 self.specArea4=int(self.thresh_area4)
	 
	 self.enable_Area1()
	 self.enable_Area2()
	 self.enable_Area3()
	 self.enable_Area4()
	 
	
###############################################################################  ######
cwgt.aMenu = Menu(cwgt,tearoff=0)
cwgt.setArea1=0
cwgt.setArea2=0
cwgt.setArea3=0
cwgt.setArea4=0

def Area1():
	cwgt.setArea1=1;
	cwgt.area_x0_1=(cwgt.area_x0)
	cwgt.area_y0_1=(cwgt.area_y0)
	cwgt.area_x1_1=(cwgt.area_x1)
	cwgt.area_y1_1=(cwgt.area_y1)
	
def Area2():
	cwgt.setArea2=1
	cwgt.area_x0_2=(cwgt.area_x0)
	cwgt.area_y0_2=(cwgt.area_y0)
	cwgt.area_x1_2=(cwgt.area_x1)
	cwgt.area_y1_2=(cwgt.area_y1)
def Area3():
	cwgt.setArea3=1
	cwgt.area_x0_3=(cwgt.area_x0)
	cwgt.area_y0_3=(cwgt.area_y0)
	cwgt.area_x1_3=(cwgt.area_x1)
	cwgt.area_y1_3=(cwgt.area_y1)
def Area4():
	cwgt.setArea4=1
	cwgt.area_x0_4=(cwgt.area_x0)
	cwgt.area_y0_4=(cwgt.area_y0)
	cwgt.area_x1_4=(cwgt.area_x1)
	cwgt.area_y1_4=(cwgt.area_y1)
	
##################################################################   analysed	
def copyy(event):
	print "Copy"
	#cwgt.aMenu2.post(event.x_root+40, event.y_root)


cwgt.aMenu.add_command(label='Copy')
cwgt.aMenu.add_command(label='Exit')

cwgt.aMenu2 = Menu(cwgt,tearoff=0)
cwgt.aMenu2.add_command(label='Area1',command=Area1)
cwgt.aMenu2.add_command(label='Area2',command=Area2)
cwgt.aMenu2.add_command(label='Area3',command=Area3)
cwgt.aMenu2.add_command(label='Area4',command=Area4)

Area_1=BooleanVar()
cwgt.area=BooleanVar()
cwgt.area_x0=IntVar()
cwgt.area_y0=IntVar()
cwgt.area_x1=IntVar()
cwgt.area_y1=IntVar()

def leftclick(event):
    print("left")
    print event.x,event.y
    if event.y>50 and 350>event.y:
		cwgt.area_x0,cwgt.area_y0 = event.x,event.y-50
def middleclick(event):
    print("middle")
def rightclick(event):
		cwgt.aMenu.post(event.x_root, event.y_root)
def move(event):
	print event.x,event.y
def release(event):
    print("release")
    print event.x,event.y
    if ( event.x==cwgt.area_x0) and (event.y==cwgt.area_y0 +50):
		cwgt.area_x0,cwgt.area_y0,cwgt.area_x1,cwgt.area_y1=0,0,0,0
    else :
		if  event.y>50 and 350> event.y:
			cwgt.area_x1=event.x
			cwgt.area_y1=event.y-50
			cwgt.aMenu2.post(event.x_root, event.y_root)


#########

cwgt.after = Label(cwgt,text="ANALYSED")
cwgt.after.place(x=170,y=20)
		 
cwgt.bind("<Button-1>", leftclick)
cwgt.bind("<Button-2>", middleclick)
cwgt.bind("<Button-3>", rightclick)  
cwgt.bind("<B1-Motion>", move)   
cwgt.bind("<ButtonRelease-1>", release) 
###
cwgt.inforArea_Black=Text(cwgt,width=15,height=1)
cwgt.inforArea_Black.place(x=10,y=650)
###
cwgt.inforArea=Text(cwgt,width=15,height=1)
cwgt.inforArea.place(x=10,y=670)
	
#########################################################################################  origin
cwgt2.inforRGB=Text(cwgt2,width=15,height=1)
cwgt2.inforRGB.place(x=10,y=670)

#############
cwgt2.before = Label(cwgt2,text="ORIGIN")
cwgt2.before.place(x=170,y=20)

def move(event):
	if (event.y>50 and 350>event.y) and (event.x>0 and 400>event.x):
		img_RGB=cv2.imread("src.png")
		x=event.x
		y=event.y-50
		cwgt2.Red=img_RGB[y,x][2]
		cwgt2.Green=img_RGB[y,x][1]
		cwgt2.Blue=img_RGB[y,x][0]
		thongtinRGB=str(str(cwgt2.Red)+","+str(cwgt2.Green)+","+str(cwgt2.Blue))
		cwgt2.inforRGB.delete('1.0',END)
		cwgt2.inforRGB.insert(END,thongtinRGB) 
	
def leftclick2(event):
	if (event.y>50 and 350>event.y):
		img_RGB=cv2.imread("src.png")
		x=event.x
		y=event.y-50
		cwgt2.Red=img_RGB[y,x][2]
		cwgt2.Green=img_RGB[y,x][1]
		cwgt2.Blue=img_RGB[y,x][0]
		thongtinRGB=str(str(cwgt2.Red)+","+str(cwgt2.Green)+","+str(cwgt2.Blue))
		cwgt2.inforRGB.delete('1.0',END)
		cwgt2.inforRGB.insert(END,thongtinRGB) 
    
cwgt2.bind("<Button-1>", leftclick2)
cwgt2.bind("<B1-Motion>", move)

##################################

################################################


 
############################################################################################  main

	
root.geometry("1600x750+100+100")

app = Example(root)
root.mainloop()


###################


