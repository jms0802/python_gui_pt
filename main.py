from tkinter import *
from PIL import Image, ImageTk   #이미지 열기

win = Tk()
win.title("Log-in")
win.geometry("400x400")
win.option_add("*Font","궁서 15")

#네이버 로고
lab_n = Label(win)
img= (Image.open("naver_log.jpg"))
img = img.resize((200, 80))
new_img = ImageTk.PhotoImage(img)
lab_n.config(image = new_img)
lab_n.pack()

#id 라벨
lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()

#id 입력창
ent1 = Entry(win)
ent1.insert(0, "sample@sample.com")

def clear(event):
  if ent1.get() == "sample@sample.com" :
    ent1.delete(0, len(ent1.get()))

ent1.bind("<Button-1>", clear)
ent1.pack()

#pw 라벨
lab2 = Label(win)
lab2.config(text="PW")
lab2.pack()

#pw 입력창
ent2 = Entry(win)
ent2.config(show="*")
ent2.pack()

#로그인 버튼
btn = Button(win)
btn.config(text="Login")

def login():
  my_id = ent1.get()
  my_pw = ent2.get()
  print(my_id, "\n" + my_pw)
  lab3.config(text="[Message] Log-in success!")

btn.config(command = login)
btn.pack()

#메시지 라벨
lab3 = Label(win)
lab3.pack()

win.mainloop()


#자동 로그인을 하고 싶다면 '구글드라이브'를 다운 받고 'selenium'라이브러리를 사용한다.

#https://www.youtube.com/watch?v=ajYZ-Ve6KRA&list=WL&index=19