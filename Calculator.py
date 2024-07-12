from tkinter import *
def digit(num):
    global temp
    temp += str(num)
    label.config(text = temp)
def dele():
    global temp
    temp = temp[:-1]
    label.config(text = temp)
def clr():
    global temp
    temp = ""
    label.config(text="")
def symb(symbo):
    global temp
    temp += symbo
    label.config(text = temp)
def goback(temp,index):
        index_test = index - 1
        while index_test <len(temp) and index_test >= 0 and (temp[index_test].isdigit() == True) :
            index_test -= 1
        index_test += 1
        num1 = temp[index_test:index]
        try:
            n1 = int(num1)
        except ValueError:
            label.config(text = "Check your equation")
        return n1,index_test
def gofront(temp,index):
        index_test = index + 1
        while index_test <len(temp) and index_test >= 0 and (temp[index_test].isdigit() == True):
            index_test += 1
        index_test -= 1
        num2 = temp[index+1:index_test+1]
        try:
            n2 = int(num2)
        except ValueError:
            label.config(text = "Check your equation")
        return n2,index_test
def submit():
    global temp
    i = 0
    while i<len(temp):      
        if temp[i] == '/':
            n1,back_cut = goback(temp,i)
            n2,front_cut = gofront(temp,i) 
            try: 
                ans = str(n1/n2)
            except ZeroDivisionError:
                label.config(text = "Error")
            temp = temp[:back_cut] + ans + temp[front_cut+1:]
            i = back_cut + len(ans)
        else:
            i += 1
    i = 0
    while i<len(temp):       
        if temp[i] == '*':
            n1,back_cut = goback(temp,i)
            n2,front_cut = gofront(temp,i)
            ans = str(n1*n2)
            temp = temp[:back_cut] + ans + temp[front_cut+1:]
            i = back_cut + len(ans)
        else:
            i+=1
    i = 0
    while i<len(temp):  
        if temp[i] == '+':
            n1,back_cut = goback(temp,i)
            n2,front_cut = gofront(temp,i)
            ans = str(n1+n2)
            temp = temp[:back_cut] + ans + temp[front_cut+1:]
            i = back_cut + len(ans)
        else:
            i += 1
    i = 0
    while i<len(temp):
        if temp[i] == '-':
            n1,back_cut = goback(temp,i)
            n2,front_cut = gofront(temp,i)
            ans = str(n1-n2)
            temp = temp[:back_cut] + ans + temp[front_cut+1:]
            i = back_cut + len(ans)
        else:
            i += 1
    label.config( text = temp)
    
window = Tk()
window.config(background = "Black")
buttons = [('1', 2, 0), ('2', 2, 1), ('3', 2, 2),('4', 3, 0), ('5', 3, 1), ('6', 3, 2),('7', 4, 0), ('8', 4, 1), ('9', 4, 2),('0', 5, 0)]
temp = ""
for text,rows,cols in buttons:
    Button(window, text = text,font = ('OCR A Std',15),command = lambda n = text:digit(n),bg="Black",fg ="white", activebackground="Black",activeforeground="white",width = 5, height=2).grid(row = rows,column = cols)
operations = [('+', 2,3),('-',3,3),('*',4,3),('/',5,3)]
for text,rows,cols in operations:
    Button(window, text = text,font = ('OCR A Std',15),command = lambda m = text:symb(m),bg="Black",fg ="white", activebackground="Black",activeforeground="white",width = 5, height=2).grid(row = rows,column = cols)
label = Label(window,bg = "black", fg = "white",width = 5, height=2,font = ('OCR A Std',15))
label.grid(row = 0, column = 0, columnspan=4, sticky='ew')
back = Button(window, text = "Del",font = ('OCR A Std',15), command = dele,bg="Black",fg ="white", activebackground="Black",activeforeground="white",width = 5, height=2).grid(row = 5,column = 1)
clear = Button(window, text = "Clr",font = ('OCR A Std',15), command = clr,bg="Black",fg ="white", activebackground="Black",activeforeground="white",width = 5, height=2).grid(row = 5,column = 2)
submit = Button(window, text = '=',font = ('OCR A Std',15), command = submit,bg="Black",fg ="white", activebackground="Black",activeforeground="white",width = 5, height=2).grid(row = 1,column = 3)
window.mainloop()