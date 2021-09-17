from tkinter import *
import Engine as eng
import time
import RPi.GPIO as GPIO 


window = Tk()

window.title("Dijidom")
window.geometry('500x600')
lbl = Label(window, text="Dijidom İKA  Kontrol Paneli")
lbl.grid(column=1, row=0)

lbl_Acil = Label(window, text="Acil Kapatma")
lbl_Acil.grid(column=1, row=5)


def forw(e):
    eng.Forward()
def left(e):
    eng.Left()
def right(e):
    eng.Right()
def back(e):
    eng.Backward()
def stop(e):
    eng.stop()
def clean():
    eng.stop()
    GPIO.cleanup()
    quit()


btn_forw = Button(window, text="İleri")
btn_forw.grid(column=1, row=1)

btn_left = Button(window, text="Sola")
btn_left.grid(column=0, row=2)

btn_right = Button(window, text="Sağa")
btn_right.grid(column=3, row=2)

btn_back = Button(window, text="Geri")
btn_back.grid(column=1, row=4)

btn_stop_clean = Button(window, text="TEMİZLE VE DUR",command = clean)
btn_stop_clean.grid(column=1, row=6)


## Buton Enter Leave
btn_forw.bind("<Enter>",forw)
btn_forw.bind("<Leave>",stop)

btn_left.bind("<Enter>",left)
btn_left.bind("<Leave>",stop)

btn_right.bind("<Enter>",right)
btn_right.bind("<Leave>",stop)

btn_back.bind("<Enter>",back)
btn_back.bind("<Leave>",stop)

window.mainloop()