from library import *
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
  frame = Frame(self, width=1500,height=200,relief=RAISED, borderwidth=1)
  frame.pack(expand=False)
  #frame.config(bg="blue")
  self.pack(expand=False)
  #####
 

  #####
  
  frame2 = Frame(self, width=1500,height=300,relief=RAISED, borderwidth=1)
  frame2.pack(expand=False)
  self.pack(expand=False)
  
  self.var0=BooleanVar()
  self.var1=BooleanVar() 
  self.var2=BooleanVar()
  self.var3=BooleanVar()
  self.var4=BooleanVar() 
  self.var5=BooleanVar()
  self.content=IntVar()

  
  reset_Area_Button = Button(self, width=10,text="reset_Area",command=self.reset_Area)
  reset_Area_Button.place(x=610,y=400)
  
  set_Area_Button = Button(self, width=10,text="set_Area",command=self.set_Area)
  set_Area_Button.place(x=610,y=430)
  
  show_Area_Button = Button(self, width=10,text="show_Area",command=self.show_Area)
  show_Area_Button.place(x=610,y=460)
  
  
  

  
  quitButton = Button(self,text="Quit",command=self.off_video)
  quitButton.place(x=50,y=20)
  
  startButton = Button(self,text="Video",command=self.on_start)
  startButton.place(x=100,y=20)
  
  TakePicButton = Button(self,text="TakePic",command=self.Takepic)
  TakePicButton.place(x=150,y=20)
  
  LoadDataButton = Button(self,text="Load_Data",bg="green",command=self.confirm_LoadData)
  LoadDataButton.place(x=550,y=90)
  
  SaveDataButton = Button(self,text="Save_Data",bg="green",command=self.confirm_SaveData)
  SaveDataButton.place(x=550,y=120)
  ######
  
  cb1 = Checkbutton(self, text="Binary", variable=self.var1 ,command=self.on_Binary)
  cb1.place(x=80, y=50)
 
  cb2 = Checkbutton(self, text="Partical", variable=self.var2 ,command=self.on_Partical)
  cb2.place(x=80, y=80)
  
  cb3 = Checkbutton(self, text="Sobel", variable=self.var3 ,command=self.on_Sobel)
  cb3.place(x=80, y=110)
  
  cb4 = Checkbutton(self, text="Median", variable=self.var4 ,command=self.on_Median)
  cb4.place(x=80, y=140)
  
  cb5 = Checkbutton(self, text="Level_Adjust", variable=self.var5 ,command=self.on_LevelAdjust)
  cb5.place(x=80, y=170)
  
  cb5 = Checkbutton(self, text="SaveImage", variable=self.var0 )
  cb5.place(x=550, y=20)
  #####
  
  ###################################
  
  
  AdjustBinaryButton = Button(self,text="Adjust_Binary",command=self.AdjustBinary)
  AdjustBinaryButton.place(x=340,y=50)
  
  AdjustExtractButton = Button(self,text="Adjust_Extract",command=self.AdjustExtract)
  AdjustExtractButton.place(x=340,y=80)
  
  AdjustBinaryButton = Button(self,text="Adjust_3",command=self.AdjustBinary)
  AdjustBinaryButton.place(x=340,y=110)
  
  AdjustExtractButton = Button(self,text="Adjust_4",command=self.AdjustExtract)
  AdjustExtractButton.place(x=340,y=140)
  
  AdjustExtractButton = Button(self,text="Adjust_5",command=self.AdjustExtract)
  AdjustExtractButton.place(x=340,y=170)
  
  
  

  ########
  self.infor_Alg1=Text(self,width=40,height=1)
  #self.infor_Alg1.pack(side=LEFT)
  self.infor_Alg1.place(x=130,y=250)
  #thongtin_Alg1="Binary : "
  #self.infor_Alg1.insert(END,thongtin_Alg1)
  self.label_Alg1 = Label(self,text="Binary: ")
  self.label_Alg1.place(x=50,y=250)
  ##
  self.infor_Alg2=Text(self,width=40,height=1)
  #self.infor_Alg2.pack(side=LEFT)
  self.infor_Alg2.place(x=130,y=270)
  
  #thongtin_Alg2="Extract : "
  #self.infor_Alg2.insert(END,thongtin_Alg2)
  self.label_Alg2 = Label(self,text="Extract: ")
  self.label_Alg2.place(x=50,y=270)
  ##
  self.infor_Alg3=Text(self,width=40,height=1)
  #self.infor_Alg3.pack()
  self.infor_Alg3.place(x=130,y=290)
  #thongtin_Alg3="Alg_3 : "
  #self.infor_Alg3.insert(END,thongtin_Alg3)
  self.label_Alg3 = Label(self,text="Alg3: ")
  self.label_Alg3.place(x=50,y=290)
  ##
  self.infor_Alg4=Text(self,width=40,height=1)
  #self.infor_Alg4.pack(side=LEFT)
  self.infor_Alg4.place(x=130,y=310)
  #thongtin_Alg4="Alg_4 : "
  #self.infor_Alg4.insert(END,thongtin_Alg4)
  self.label_Alg4 = Label(self,text="Alg4: ")
  self.label_Alg4.place(x=50,y=310)
  ##
  self.infor_Alg5=Text(self,width=40,height=1)
  #self.infor_Alg5.pack()
  self.infor_Alg5.place(x=130,y=330)
  #thongtin_Alg5="Alg_5 : "
  #self.infor_Alg5.insert(END,thongtin_Alg5)
  self.label_Alg5 = Label(self,text="Alg5: ")
  self.label_Alg5.place(x=50,y=330)
  ##
  
  
  self.infor_Area1=Text(self,width=20,height=1)
  self.infor_Area1.place(x=100,y=400)
  #thongtin_Area1="Area1:"
  #self.infor_Area1.insert(END,thongtin_Area1)
  self.label_Area1 = Label(self,text="Area1: ")
  self.label_Area1.place(x=50,y=400)
  
  ##
  self.infor_Area2=Text(self,width=20,height=1)
  self.infor_Area2.place(x=350,y=400)
  #thongtin_Area2="Area2:"
  #self.infor_Area2.insert(END,thongtin_Area2)
  self.label_Area2 = Label(self,text="Area2: ")
  self.label_Area2.place(x=300,y=400)
  ##
  self.infor_Area3=Text(self,width=20,height=1)
  self.infor_Area3.place(x=100,y=450)
  #thongtin_Area3="Area3:"
  #self.infor_Area3.insert(END,thongtin_Area3)
  self.label_Area3 = Label(self,text="Area3: ")
  self.label_Area3.place(x=50,y=450)
  ##
  self.infor_Area4=Text(self,width=20,height=1)
  self.infor_Area4.place(x=350,y=450)
  #thongtin_Area4="Area4:"
  #self.infor_Area4.insert(END,thongtin_Area4)
  self.label_Area4 = Label(self,text="Area4: ")
  self.label_Area4.place(x=300,y=450)
  #####
  
  
  ################################
  self.infor=Text(self,width=50,height=2)
  self.infor.pack()
  thongtin="CHAO MUNG DEN VOI CHUONG TRINH CRAVIS_V1  \n DESIGN BY VISUAL GROUP"
  self.infor.insert(END,thongtin)
  
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
 def on_Binary(self):
	 if self.var1.get() == True:
	  print ("Binary")
	  self.show_Binary() #show window
	 else :
		 
		 print("No_Binary")
		 if hasattr(self,'ThExtract'):
			 print "dsfsdfds"
			 self.ThBinary.withdraw()
		 else :
			 print "dddddddd"
		 
		 #self.ThBinary.withdraw()
 def on_Partical(self):
	 if self.var2.get() == True:
	  print ("Partical")
	  self.show_Extract()
	 else :
		 print("No_Partical")
		 self.ThExtract.withdraw()
			
	 
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
	 
     if camera.resolution==(400,300):
		print  ("ok")
		cwgt.camera.start_preview()
		
	
	
###############################################################################   button  to analyse image
 def Takepic(self):  ## take pic button 
	  
	  src = Frame(cwgt, width=400,height=300,relief=RAISED, borderwidth=1)
	  src=camera.capture('src.png')
	  analysed=camera.capture('analysed.png')
	  if self.var0.get()==1:
		camera.capture("/home/pi/Desktop/New/{0:%Y%m%d-%H%M%S}.png" .format(datetime.now()))
	  
	  #'{0:%Y%m%d-%H%M%S}: start.'.format(datetime.now())
	  #img_abc=PhotoImage(file="src.png")
	  #h=img_abc.width()
	  #w=img_abc.height()
	  #print h,w
	  
	  #cv2.imwrite("src.png",src)
	  
	  
	  #img_abc = cv2.imread("img.png",cv2.IMREAD_COLOR)
	  #cv2.rectangle(img_abc,(50,50),(100,50),(255,0,0),15)
	  #cv2.imwrite("out2.png",img_abc)
	  
	  img_origin=PhotoImage(file="src.png")
	  cwgt2.img=img_origin
	  cwgt2.create_image(200, 200,  image=img_origin)
	  
	  h=img_origin.width()
	  w=img_origin.height()
	  #print h,w
	  #px=img[55,55]
	  
	  
	  
	  #img_new=cv2.imread("out2.png")
	  
	  #pix=img_new[2,2]
	  #pix0=img_new[2,2][0]
	  #pix1=img_new[2,2][1]
	  #pix2=img_new[2,2][2]
	  #print pix,pix0,pix1,pix2
	  
	  #for j in range (0,h):
	#	  for i in range (0,w):
		#	  if img_new[i,j]
		
		#img_new[i,i]=[255,255,255]
	  #pix__=img_new[2,2][0]
	  #print pix__
	  
	  #cv2.imwrite("out3.png",img_new)
	  #img_x=PhotoImage(file="out3.png")
	  #cwgt2.img=img_x
	  #cwgt2.create_image(200, 200,  image=img_x)  
	  
	  
	  #if self.var1.get() == True:
		  
		#src=cv2.imread("src.png")
		#res=cv2.Canny(src,self.varLow.get(), self.varHigh.get())
		#retval,res = cv2.threshold(src, self.varLow.get(), self.varHigh.get(), cv2.THRESH_BINARY)
		#cv2.imwrite("analysed.png",res)
	 
	  if self.var2.get() == True:
		min_R=self.varRed_L.get()
		max_R=self.varRed_H.get()
	  
		min_G=self.varGreen_L.get()
		max_G=self.varGreen_H.get()
	  
		min_B=self.varBlue_L.get()
		max_B=self.varBlue_H.get()  
		
		pro_2 = cv2.imread('analysed.png')
		#hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
		lower= np.array([min_B,min_G,min_R],np.uint8)
		upper = np.array([max_B,max_G,max_R],np.uint8)
		mask = cv2.inRange(pro_2, lower, upper)
		analysed = cv2.bitwise_and(pro_2,pro_2, mask= mask)
		cv2.imwrite("analysed.png",analysed)
		#cv2.imshow('aaa',src)
		#
	    #img2=PhotoImage(file="out.png")
	    #cwgt.img2=img2
	    #cwgt.create_image(200, 200,  image=img2)
	  #cv2.imwrite("out3.png",img_new)
	  img_show=PhotoImage(file="analysed.png")
	  cwgt.img=img_show
	  cwgt.create_image(200, 200,  image=img_show)  
	  
	  if self.var1.get() == True:
		  
		src=cv2.imread("analysed.png")
		#analysed=cv2.Canny(src,self.varLow.get(), self.varHigh.get())
		retval,res = cv2.threshold(src, self.varLow.get(), self.varHigh.get(), cv2.THRESH_BINARY)
		cv2.imwrite("analysed.png",res)
	  
	  
	  
	  if self.var5.get() == True:
		  src=cv2.imread("analysed.png")
		  number=0;
		  for j in range(self.x0_1,self.x1_1):
			  for i in range(self.y0_1,self.y1_1):
				  if src[i,j][0]>0 and src[i,j][1]>0 and src[i,j][2]>0 :
					  src[i,j]=[255,255,255]
					  number=number+1
		  print number
		  if number>180 :
			tkMessageBox.showinfo(title="OK",message="OK")	
		  else :
			  tkMessageBox.showinfo(title="ng",message="ng")	
		  cv2.imwrite("analysed.png",src)
	  img_show=PhotoImage(file="analysed.png")
	  cwgt.img=img_show
	  cwgt.create_image(200, 200,  image=img_show) 
	  #img_show=PhotoImage(file="src.png")
	  #cwgt.img=img_show
	  #cwgt.create_image(200, 200,  image=img_show)
				  
		  
	   
	  #retval, after_Binary = cv2.threshold(img, self.varLow.get(), self.varHigh.get(), cv2.THRESH_BINARY)
		
		
		
		#after_Blurr =cv2.blur(img,(5,5))
		#after_MedianBlur=cv2.medianBlur(after_Blurr,5)
		
		#cv2.imwrite("out.png",res)
		#after_Binary=PhotoImage(file="out.png")
		#cwgt.img=res
		#cv2.imshow("show",res)
		#cwgt.create_image(0, 0,  image=after_Binary)
		#cwgt.create_image(0, 0,  image=mask)
	  if self.var3.get() == True:
			analysed=cv2.Canny(analysed,100,200)
	  img_show=PhotoImage(file="analysed.png")
	  cwgt.img=img_show
	  cwgt.create_image(200, 200,  image=img_show) 
			
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
	    
	    
	   
	  #else:
		#cwgt.create_image(0, 0,  image=img_origin)
		#print("xsfd")
		#print img_origin[100,100][0]
		#www=img_origin.width()
		#print www
	   
	  
	 
#

 def on_start(self):
	print("xsfd")
	self.showvideo()
	
 def off_video(self):
	 #cwgt.frame.destroy()
	 camera.stop_preview()

	 
	 
	 ########
 
 
 


 ######################################################################################   show window 
 def show_Binary(self):     ## input Thresh_Binary
	 
	 if (hasattr(self,'ThBinary')):
		 #(self.varHigh.get()> self.varLow.get())
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
		 #binary = Button(self.ThBinary, text="Get_Binary",background="green",command=self.getdata_Binary)
		 #binary.pack()
 
########
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
	 
 def  set_Area(self):
	 
	 self.text1=self.infor_Area1.get('1.0',END)
		
	 #self.x0_1=int(self.text1[0]+self.text1[1]  +self.text1[2])
	 #self.y0_1=int(self.text1[4]+self.text1[5] +self.text1[6])
	 #self.x1_1=int(self.text1[8]+self.text1[9] +self.text1[10])
	 #self.y1_1=int(self.text1[12]+self.text1[13]+self.text1[14])
	 
	 #########
	 
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
	 self.text1=str(inttotext1(cwgt.area_x0_1)+","+inttotext1(cwgt.area_y0_1)+","+inttotext1(cwgt.area_x1_1)+","+inttotext1(cwgt.area_y1_1))
	 self.infor_Area1.delete('1.0',END)
	 self.infor_Area1.insert(END,self.text1)
	 ####
	 self.x0_2=cwgt.area_x0_2
	 self.y0_2=cwgt.area_y0_2
	 self.x1_2=cwgt.area_x1_2
	 self.y1_2=cwgt.area_y1_2
	 self.text2=str(inttotext1(cwgt.area_x0_2)+","+inttotext1(cwgt.area_y0_2)+","+inttotext1(cwgt.area_x1_2)+","+inttotext1(cwgt.area_y1_2))
	 self.infor_Area2.delete('1.0',END)
	 self.infor_Area2.insert(END,self.text2)
	 ####
	 self.x0_3=cwgt.area_x0_3
	 self.y0_3=cwgt.area_y0_3
	 self.x1_3=cwgt.area_x1_3
	 self.y1_3=cwgt.area_y1_3
	 self.text3=str(inttotext1(cwgt.area_x0_3)+","+inttotext1(cwgt.area_y0_3)+","+inttotext1(cwgt.area_x1_3)+","+inttotext1(cwgt.area_y1_3))
	 self.infor_Area3.delete('1.0',END)
	 self.infor_Area3.insert(END,self.text3)
	 ####
	 self.x0_4=cwgt.area_x0_4
	 self.y0_4=cwgt.area_y0_4
	 self.x1_4=cwgt.area_x1_4
	 self.y1_4=cwgt.area_y1_4
	 self.text4=str(inttotext1(cwgt.area_x0_4)+","+inttotext1(cwgt.area_y0_4)+","+inttotext1(cwgt.area_x1_4)+","+inttotext1(cwgt.area_y1_4))
	 self.infor_Area4.delete('1.0',END)
	 self.infor_Area4.insert(END,self.text4)
	 
	 
	 
	
	 
 def show_Area(self):
	 font = cv2.FONT_HERSHEY_SIMPLEX
	 img = cv2.imread("src.png",cv2.IMREAD_COLOR)
	 #print self.x0_1
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
	 #img_show_Area=cv2.rectangle(img,(x0_1,y0_1),(x1_1,y1_1),(255,0,0),2)
	 cv2.imwrite("show_Area.png",img_show_Area)
	 img_show=PhotoImage(file="show_Area.png")
	 cwgt2.img=img_show
	 cwgt2.create_image(200, 200,  image=img_show)
	 #cv2.rectangle(img,(50,250),(100,500),(255,0,0),15)
	 
	 
 def AdjustBinary(self):
	 if self.var1.get()==True:
		self.ThBinary.withdraw()
		self.ThBinary.deiconify()
		
 def AdjustExtract(self):
	 if self.var2.get()==True:
		self.ThExtract.withdraw()
		self.ThExtract.deiconify()
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
	#text123 = self.content.get()
	#self.content.set(text123)
	
	#print(self.content.get()) 
############
 def getdata_Save(self):
	 print(self.entry.get())
	 self.set_Area()
	 if  self.infor_Alg1.get('1.0',END)=="\n":
		 self.text_binary="000,000"
	 if  self.infor_Alg2.get('1.0',END)=="\n":
		 self.text_Extract="R(000,000)G(000,000)B(000,000)"
	 if self.entry.get()=="1111":
		 self.master.destroy()
		 print "Save"
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
	#text_save_to = self.content_save.get()
	#self.content_save.set(text_save_to)
	#self.master.destroy()
	#print text123
	print(self.content_save.get())
########
 def SaveData(self): ## get password button
		 self.inforData_binary="Binary : (" + self.text_binary + ")"
		 self.inforData_Extract="Extract : " + self.text_Extract
		 self.inforData_Area1="Area1 : " + self.text1
		 
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
		 self.inforData=self.SumData + "\n" + self.inforData_binary + "\n" + self.inforData_Extract +"\n" + self.inforData_Area1
		 print self.inforData 
		
		 
		 #if self.var1.get()==1 :
			 
		 print(self.entry2.get())
		 f=open("/home/pi/Desktop/Program/"+str(self.entry2.get())+'.txt','w+')
		 f.write(self.inforData)
	 	 self.Save.destroy()
	 	 #"/home/pi/Desktop/New/{0:%Y%m%d-%H%M%S}.png
		 #tkMessageBox.showinfo(title="Save",message="SaveData success !!")
############################################################################################
 def confirm_LoadData(self):
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
		 #tkMessageBox.showinfo(title="Load",message="LoadData success !!")
		 self.Load_from_()
	 else:
	   tkMessageBox.showinfo(title="fail",message="again")	
 def Load_from_(self):
	self.Load = Tk()
	self.Load.title("Load_from_")
	self.Load.geometry("200x250+350+350")
	path="/home/pi/Desktop/Program"
	menu_program=os.listdir(os.path.expanduser(path))
	#print len(menu_program)
	##
	acts = ["Scarlet Johansson", "Rachel Weiss", "Natalie Portman", "Jessica Alba"]
	lb = Listbox(self)
	for i in acts:
		lb.insert(END, i)
		lb.bind("<<ListboxSelect>>", self.onSelect)
	lb.pack(pady=15)
	self.var = StringVar()
	self.label = Label(self, text=1, textvariable=self.var)
	self.label.pack()
	#def onSelect(self.Load, val):
	#	sender = val.widget
	#	idx = int(sender.curselection())
	#	value = sender.get(idx)
	#	self.var.set(value)
	#	print self.var.get()
 def has_choose(self):
	  print "vvvvv"
	 #self.LoadData()
 def LoadData(self):
	 print "Load"
	 #"/home/pi/Desktop/Program/"+str(self.entry2.get())+'.txt'
	 #f=open('a.txt','r')
	 f=open("/home/pi/Desktop/Program/"+str(self.Load_label.get()),'r')
	 
	 self.SumData=f.readline()
	 load_binary=f.readline()
	 load_extract=f.readline()
	 load_area1=f.readline()
	 
	 
	 #self.ThBinary.deiconify()
	 
	 text_binary=(load_binary[10]+load_binary[11]+load_binary[12]+load_binary[13]+load_binary[14]+load_binary[15]+load_binary[16])
	 text_extract=(load_extract[10]+load_extract[11]+load_extract[12]+load_extract[13]+load_extract[14]+load_extract[15]+load_extract[16]+load_extract[17]+load_extract[18]+load_extract[19]+load_extract[20]+load_extract[21]+load_extract[22]+load_extract[23]+load_extract[24]+load_extract[25]+load_extract[26]+load_extract[27]+load_extract[28]+load_extract[29]+load_extract[30]+load_extract[31]+load_extract[32]+load_extract[33]+load_extract[34]+load_extract[35]+load_extract[36]+load_extract[37]+load_extract[38]+load_extract[39])
	 text_area1=(load_area1[8]+load_area1[9]+load_area1[10]+load_area1[11]+load_area1[12]+load_area1[13]+load_area1[14]+load_area1[15]+load_area1[16]+load_area1[17]+load_area1[18]+load_area1[19]+load_area1[20]+load_area1[21]+load_area1[22])
	 
	 value_low_binary=int (load_binary[10]+load_binary[11]+ load_binary[12])
	 value_high_binary=int (load_binary[14]+load_binary[15]+ load_binary[16])
	 ####
	 value_low_red=int(load_extract[12]+load_extract[13]+load_extract[14])
	 value_high_red=int(load_extract[16]+load_extract[17]+load_extract[18])
	 
	 value_low_green=int(load_extract[22]+load_extract[23]+load_extract[24])
	 value_high_green=int(load_extract[26]+load_extract[27]+load_extract[28])
	 
	 value_low_blue=int(load_extract[32]+load_extract[33]+load_extract[34])
	 value_high_blue=int(load_extract[36]+load_extract[37]+load_extract[38])
	 ####
	 value_area1_x0=int(load_area1[8]+load_area1[9]+load_area1[10])
	 value_area1_y0=int(load_area1[12]+load_area1[13]+load_area1[14])
	 value_area1_x1=int(load_area1[16]+load_area1[17]+load_area1[18])
	 value_area1_y1=int(load_area1[20]+load_area1[21]+load_area1[22])
	#######
	 self.x0_1=value_area1_x0
	 self.y0_1=value_area1_y0
	 self.x1_1=value_area1_x1
	 self.y1_1=value_area1_y1
	 
	#######
	 self.varHigh=IntVar()
	 self.varLow=IntVar()
	 self.varRed_L=IntVar()
	 self.varRed_H=IntVar()
	 self.varGreen_L=IntVar()
	 self.varGreen_H=IntVar()
	 self.varBlue_L=IntVar()
	 self.varBlue_H=IntVar()
	
	
	 self.varLow.set(value_low_binary)
	 self.varHigh.set(value_high_binary)
	 self.varRed_L.set(value_low_red)
	 self.varRed_H.set(value_high_red)
	 self.varGreen_L.set(value_low_green)
	 self.varGreen_H.set(value_high_green)
	 self.varBlue_L.set(value_low_blue)
	 self.varBlue_H.set(value_high_blue)
	 
	 self.text_binary=text_binary
	 self.text_Extract=text_extract
	 self.text_area1=text_area1
	
	 self.infor_Alg1.delete('1.0',END)
	 self.infor_Alg1.insert(END,self.text_binary)
	 self.infor_Alg2.delete('1.0',END)
	 self.infor_Alg2.insert(END,self.text_Extract)
	 
	 self.infor_Area1.delete('1.0',END)
	 self.infor_Area1.insert(END,self.text_area1)
	 
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
		 
	 self.Load.destroy()
###################################################################################		 
 def getdata_Binary(self):
	 min_binary=inttotext1(self.varLow.get())
	 max_binary=inttotext1(self.varHigh.get())
	 
	 self.text_binary=str( min_binary + "," + max_binary )
	 if self.varHigh.get()>self.varLow.get():
		self.infor_Alg1.delete('1.0',END)
		self.infor_Alg1.insert(END,self.text_binary)
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
		self.infor_Alg2.delete('1.0',END)
		self.infor_Alg2.insert(END,self.text_Extract)
		self.ThExtract.withdraw()
	 else :
		 tkMessageBox.showinfo(title="fail",message="again")
