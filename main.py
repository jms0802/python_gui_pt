from tkinter import *
import random
from datetime import datetime

win = Tk()
win.geometry("400x150")
win.title("Aim_game")
win.option_add("*Font", "궁서 15")

#레이블
lab1 = Label(win)
lab1.config(text="Number")
lab1.grid(column = 0, row = 0, padx = 10, pady = 20)

#입력창
ent1 = Entry(win)
ent1.grid(column = 1, row = 0)

ck = 1

#랜덤 버튼 연속
def cc():
  global ck
  if ck < n:
    ck += 1
    btn.destroy()
    ran_btn()
  else:
    fin_time = datetime.now()
    t_time = (fin_time - start_time).total_seconds()
    btn.destroy()
    lab = Label(win)
    lab.config(text="Clear " + str(t_time) + "sec")
    lab.pack(pady = 180)


#랜덤 버튼
def ran_btn():
  global btn
  btn = Button(win)
  btn.config(bg = "red")
  btn.config(command = cc)
  btn.config(text = ck)
  btn.place(relx = random.random(), rely= random.random())

def gstart():
  global n
  global start_time
  n = int(ent1.get())
  for wg in win.grid_slaves():
    wg.destroy()
  win.geometry("400x400")
  ran_btn()
  start_time = datetime.now()

#버튼
btn1 = Button(win)
btn1.config(text="START!")
btn1.config(command = gstart)
btn1.grid(column = 0, row = 1,columnspan = 2, padx = 30, pady = 10)

win.mainloop()