from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.geometry("500x500")
win.title("Game")

cvs = Canvas(win)
cvs.config(width = 500, height = 500, bd = 0, highlightthickness=0)
p1 = (250,250)  #글자의 중심점을 잡아줌.
cvs.create_text(p1, text = "GAME", font = ("Arial", 50), fill = 'magenta')

img = Image.open('D:/temp/canon1.png')
img = img.resize((50,50), Image.ANTIALIAS)
img = img.rotate(10)
img = ImageTk.PhotoImage(img, master = win)
cvs.create_image(p1, image = img)
cvs.pack()


win.mainloop()