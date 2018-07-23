from cmlib import Library
class Example(Frame):
  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.parent = parent
    self.initUI()
  
  def initUI(self):
    self.parent.title("Scale")
    #self.style = Style()
    #self.style.theme_use("default")
  
    self.pack(fill=BOTH, expand=1)
  
    scale1 = Scale(self, from_=0, to=255, command=self.onScale1)
    scale1.pack(side=LEFT, padx=15)
  
    self.var1 = IntVar()
    self.label1 = Label(self, text=0, textvariable=self.var1)
    self.label1.pack(side=LEFT,padx=0)
    
    
    self.scale2 = Scale(self, from_=0, to=255, command=self.onScale2)
    self.scale2.pack(side=LEFT, padx=20)
  
    self.var2 = IntVar()
    self.label2 = Label(self, text=0, textvariable=self.var2)
    self.label2.pack(side=LEFT,padx=15)
    
    self.closeButton = Button(self, text="Close",background="green",command=self.close)
    self.closeButton.pack(side=RIGHT, padx=5, pady=5)
    
    self.replace = Button(self, text="replace",background="green")
    self.replace.pack(side=RIGHT, padx=5, pady=5)
  
  def onScale1(self, val):
    v = int(float(val))
    self.var1.set(v)
    print (v)
    
  def onScale2(self, val):
    v = int(float(val))
    self.var2.set(v)
    print (v)
    
  def close(self):
	  self.label1.destroy()
	  self.scale2.destroy()
	  #scale1.pack.quit()
	  self.replace.destroy()
  
  
root = Tk()
ex = Example(root)
root.geometry("250x100+300+300")
root.mainloop()
