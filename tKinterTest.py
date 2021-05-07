from tkinter import *

top = Tk()
playList = []

def results():
    print(playList)

def addToList():
    newItem = E1.get()
    playList.append(newItem)
    E1.delete(0, END)

#This is a Label widget
L1 = Label(top, text = "Playlist Maker")
L1.grid(column = 0, row = 1)

#This is an Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#This is a Button widget
B1 = Button(text = "    Print Playlist    ", bg = "#c6edee", command = results)
B1.grid(column = 0, row = 3)

B2 = Button(text = "+", bg = "#feebe5", command = addToList)
B2.grid(column = 1, row = 3)




top.mainloop()
