from tkinter import *
from functools import partial
game = [[2,3,4],[5,6,7],[8,9,10]]
turn = 0
def mark(rownum,colnum,index,button_object,temp,label):
    global turn,game
    if temp == 0:
        if turn%2 == 0:
            game[rownum][colnum] = 0
            button_object[index].config(text = "O")
        else:
            game[rownum][colnum] = 1
            button_object[index].config(text = "X")
        turn+= 1
    elif temp == 1:
        if turn%2 == 0:
            game[rownum][colnum] = 1
            button_object[index].config(text = "X")
        else:
            game[rownum][colnum] = 0
            button_object[index].config(text = "O")
        turn += 1
    for i in range (3):
        if game[i][0] == game[i][1] == game[i][2]:
            label.config(text = f"Game Over! {button_object[index].cget('text')} wins")
            if i == 1:
                i+= 2
            elif i == 2:
                i += 4
            button_object[i].config(bg = "Green")
            button_object[i+1].config(bg = "Green")
            button_object[i+2].config(bg = "Green")

        elif game[0][i] == game[1][i] == game[2][i]:
            label.config( text = f"Game Over {button_object[index].cget('text')} wins")
            button_object[i].config(bg = "Green")
            button_object[i+3].config(bg = "Green")
            button_object[i+6].config(bg = "Green")
    if game[0][0] == game[1][1] == game[2][2]:
        label.config( text = f"Game Over {button_object[index].cget('text')} wins")
        button_object[0].config(bg = "Green")
        button_object[4].config(bg = "Green")
        button_object[8].config(bg = "Green")
    elif game[2][0] == game[1][1] == game[0][2]:
        label.config( text = f"Game Over {button_object[index].cget('text')} wins")
        button_object[2].config(bg = "Green")
        button_object[4].config(bg = "Green")
        button_object[6].config(bg = "Green")
    if turn == 9:
        label.config( text = "Game Over")
        for j in button_object:
            j.config(bg = "Yellow",fg = "Black")
        return 
def refresh(window):
    global turn, game
    turn = 0
    game = [[2,3,4],[5,6,7],[8,9,10]]
    window.destroy() 
def open_wind(temp):    
    global game,turn
    window = Tk()
    window.config( background = "Black")
    buttons = [(0,0,0),(0,1,1),(0,2,2),(1,0,3),(1,1,4),(1,2,5),(2,0,6),(2,1,7),(2,2,8)]
    button_object = [] 
    label = Label( window, font =('Stencil Std',15) ,bg = "Black", fg = "White",width = 15, height = 5,activebackground="Black", activeforeground="White")
    label.grid(row=3, column=0,columnspan=2,sticky='ew')
    for rownum,colnum,i in buttons:
        button = Button( window, font =('Stencil Std',15) ,bg = "Black", fg = "White", command = partial(mark,rownum,colnum,i,button_object, temp,label),width = 15, height = 5,activebackground="Black", activeforeground="White")
        button.grid(row =rownum, column=colnum)
        button_object.append(button)
    button = Button( window, font =('Stencil Std',15) ,text = "Play Again",bg = "Black", fg = "White", command =partial(refresh,window),width = 15, height = 5,activebackground="Black", activeforeground="White")
    button.grid(row=3, column=2)
    window.mainloop()

welcome_page = Tk()
welcome_page.config( background="Black")
label2 = Label( welcome_page, font =('Stencil Std',15) ,text = "TIC-TAC-TOE",bg = "Black", fg = "White",width = 15, height = 5,activebackground="Black", activeforeground="White")
label2.grid( row=2,column=1)
button = Button( welcome_page, font =('Stencil Std',15) ,text = "X STARTS",bg = "Black", fg = "White", command = partial(open_wind,1),width = 15, height = 5,activebackground="Black", activeforeground="White")
button.grid( row = 3, column = 0)
button = Button( welcome_page, font =('Stencil Std',15) ,text = "O STARTS",bg = "Black", fg = "White", command = partial(open_wind,0),width = 15, height = 5,activebackground="Black", activeforeground="White")
button.grid( row = 3, column = 2)
welcome_page.mainloop()