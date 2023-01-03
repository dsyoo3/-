from tkinter import *
win = Tk()
win.title("Game")
win_w, win_h = (800,800)  #800 , 800을 변수로 선언하기 위해 넣어줌
win.geometry(f"{win_w}x{win_h}")

cvs = Canvas(win)
cvs.config(width = win_w , height = win_h, bd=0, highlightthickness = 0)
cvs.pack()

bot_h = round(win_h * 1/5)  #가장 아래에 오는 사각형
bot_c = "#808080"
cvs.create_rectangle((0, win_h - bot_h), (win_w, win_h), fill = bot_c, outline = bot_c)
#바깥 라인도 같은 색으로 하면 라인이 사라지는 효과 따라서 outline도 같은 색으로 지정

mid_h = round((win_h - bot_h) / 8)  #중간에 오는 사각형
mid_c = "#cc6600"
cvs.create_rectangle((0, win_h - bot_h-mid_h), (win_w, win_h-bot_h), fill = mid_c, outline = mid_c)

top_h = win_h - bot_h - mid_h   #위에 오는 사각형
top_c = "#336699"
cvs.create_rectangle((0, 0), (win_w, top_h), fill = top_c, outline = top_c)


win.mainloop()