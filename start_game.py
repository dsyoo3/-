from tkinter import *
import math 
import time 
import warnings
warnings.filterwarnings('ignore') 
from PIL import Image, ImageTk
import random 

import subprocess


start_go = Tk()

def go_game():
            subprocess.call("creative_sejong.py", shell=True)
            

def exit_start():
            start_go.destroy()

start_go.title("Main screen")
button1 = Button(start_go, text = "Start",command=go_game)
button2 = Button(start_go, text = "Search List")
button3 = Button(start_go, text = "Close", command=exit_start)
button1.pack(side = LEFT, padx=20 , pady = 20)
button2.pack(side = LEFT, padx=20 , pady = 20)
button3.pack(side = LEFT, padx=20 , pady = 20)




