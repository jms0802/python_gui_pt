from tkinter import *

win = Tk()
win.geometry("400x300")
win.title("grid")
win.option_add("*Font", "궁서 15")

xx=250
yy=0.7

btn = Button(win)
btn.config(text="{},{}".format(xx,yy))
btn.place(x=xx,rely=yy)



column_num = 3
row_num = 3

for j in range(0,row_num):
  for i in range(0, column_num):
    btn1 = Button(win)
    btn1.config(text="{},{}".format(i,j))
    btn1.grid(column = i,row = j, padx = 10, pady = 10)

btn2 = Button(win)
btn2.config(text="span")
btn2.grid(column = 1, row = 2, columnspan = 2)


####   pack은 grid와 같이 쓸 수 없다.
#btn3 = Button(win)
#btn3.config(text="pack")
#btn3.pack(side="right")

win.mainloop()