from Tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print e.get()

b = Button(master, text="get", width=10, command=callback)
b.pack()


mainloop()

content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
