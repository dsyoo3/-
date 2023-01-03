from tkinter import *
from datetime import datetime
win = Tk()
win.title("Game")
win.geometry("2000x500")

def press(event):
    global right_go, t_0   #어디서든 써주기 위해 전역변수 선언
    if event.keysym == "space" and right_go != True:  #처음 누른 순간에만 만족
        right_go = True
        t_0 = datetime.now() 

right_go = False
win.bind("<KeyPress>", press)

cvs = Canvas(win)
cvs.config(width = 2000, height= 500, bd = 0, highlightthickness=0)
#창 크기 옵션 추가
p1 = (0, 200)
p2 = (100, 300)
sqr = cvs.create_rectangle(p1, p2, fill = 'blue') #사각형 설정
velo = 2000/10 #속도 설정 (1초에 200픽셀 이동)
cvs.pack()

win.update()   #실시간으로 화면을 바꾸기 위해 mainloop대신 사용

while True: #update함수를 사용하기 위해 while문 사용
    cvs.delete(sqr)
    if right_go == True: 
        t_now = datetime.now()
        t_delta = (t_now - t_0).total_seconds()
        p1_x = round(0 + velo * t_delta)
        p2_x = p1_x + 100
        p1 = (p1_x, 200)
        p2 = (p2_x, 300)
    sqr = cvs.create_rectangle(p1, p2, fill = 'blue')
    win.update()