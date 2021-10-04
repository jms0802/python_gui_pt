from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()

win.geometry("700x400")
win.title("Cul")
win.option_add("*Font","맑은고딕 18")

ent = Entry(win)
ent.pack()
def get_n():
  n = ent.get()

  url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
  req = requests.get(url)
  soup = BeautifulSoup(req.text, "html.parser")
  txt1 = soup.find("div", {"class", "num win"}).get_text()
  win_n = txt1.split("\n")[3:9]
  txt2 = soup.find("div", {"class", "num bonus"}).get_text()
  bonus_n = txt2.split("\n")[2]
  txt3 = soup.find("div", {"class", "win_result"}).get_text()
  round_n = txt3.split("\n")[1]

  print(str(round_n) +"\n당첨번호 = " + str(win_n) + "\n보너스번호 = " + str(bonus_n))

def check():
  print("Hello")
  

btn = Button(win)
btn.config(text="Lotto")
btn.config(width = 25, height = 4)
btn.config(command = get_n)
btn.pack()


win.mainloop()

