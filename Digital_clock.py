from tkinter import *
import time
def update():
    curr_time = time.strftime("%I:%M:%S %p")
    time_label.config(text=curr_time)
    curr_day = time.strftime("%A")
    day_label.config(text=curr_day)
    curr_date = time.strftime("%B %d, %Y")
    date_label.config(text=curr_date)

    window.after(1000,update)

window =Tk()
window.geometry("500x500")
window.config(background="Black")
canvas = Canvas(window)
canvas.pack()
canvas.create_rectangle(0,10,500,500,fill="Black")
time_label = Label(window,bg="Black",fg="Green",font=("Kozuka Mincho Pro L",30))
canvas.create_window(190,110,window=time_label)
day_label = Label(window,bg="Black",fg="Green",font=("Kozuka Mincho Pro L",30),compound="bottom")
canvas.create_window(190,160,window=day_label)
date_label = Label(window,bg="Black",fg="Green",font=("Kozuka Mincho Pro L",30),compound="bottom")
canvas.create_window(190,210,window=date_label)
update()
window.mainloop()