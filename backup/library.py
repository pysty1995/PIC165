from Tkinter import Tk, Frame, BOTH, Button,RIGHT,RAISED,LEFT,IntVar,BOTTOM
from Tkinter import BooleanVar,Checkbutton,PhotoImage,Canvas,W
from Tkinter import Scale,StringVar,END,Listbox,Label,Menu,Entry
from PIL import Image
import ttk
import time
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
import signal
import traceback
from datetime import datetime
from multiprocessing import Process

import picamera
import picamera.array
import cmlib
from cmlib import piLib
import os

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
