from tkinter import *
import datetime
import time
from time import sleep
from threading import Thread


now_time = None
h = None
m = None
s = None
exit = True


def clock():
    global now_time, h, m, s, exit
    while exit:
        now_time = datetime.datetime.now().time()
        h = now_time.hour
        m = now_time.minute
        s = now_time.second
        sleep(1)


if __name__ == '__main__':
    Thread(target=clock).start()


def update():
    global now_time, h, m, s, exit
    while exit:
        if h < 10:
            h = f'0{h}'
        if m < 10:
            m = f'0{m}'
        if s < 10:
            s = f'0{s}'
        time['text'] = f'{h}:{m}:{s}'
        sleep(1)


form = Tk()
form.title('LiveClock')
form.geometry('400x120')
form.iconbitmap(r'C:\projects\Python\live_clock\icon.ico')
time = Label(form, font=("Times New Roman", 80,))
time.pack()
Thread(target=update).start()
form.mainloop()
exit = False


