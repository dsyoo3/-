from tkinter import *
win = Tk()
win.title("Game")
win.geometry("2000x500")


def press(event):
    print(event)  #프린트를 이용하여 효율적으로 이벤트 구현

win.bind("<KeyPress>", press) #키를 눌렀을 때 반응

cvs = Canvas(win)
cvs.config(width = 2000, height= 500, bd = 0, highlightthickness=0)
#창 크기 옵션 추가
p1 = (1000,250)
txt = " "
event_txt = cvs.create_text(p1, text = txt, font = ("Arial", 20))
cvs.pack()

win.update()   #실시간으로 화면을 바꾸기 위해 mainloop대신 사용

while True: #update함수를 사용하기 위해 while문 사용
    cvs.delete(event_txt)
    event_txt = cvs.create_text(p1, text = txt, font = ("Arial", 20))
    win.update() 
