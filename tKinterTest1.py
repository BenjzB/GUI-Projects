from tkinter import *

top = Tk()
playList = []

def results():
    print(playList)

def exportList():
    with open('text.txt', 'w') as f:
        for item in playList:
            f.write("%s/n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 2, row = 1)
    
    B1Main = Button(text = "Week 1", bg = "#c6edee", command = week1)
    B1Main.grid(column = 2, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "#c6edee")
    B2Main.grid(column = 2, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "#c6edee")
    B3Main.grid(column = 2, row = 4)

    Bclear = Button(text = "Main Menu", bg = "white", command = mainMenu)
    Bclear.grid(column = 3, row = 1)

def week2():
    clearWindow()
    L1W2 = Label(top, text = "Dice Roller Program")
    L1W2.grid(column = 0, row = 1)

    L2W2 = Label(top, text = "How many sides?")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text = "How many rolls?")
    L3W2.grid(column = 2, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)

    B1W2 = Button(text = "Roll!", bg = "red", command = week2)
    B1W2.grid(column = 2, row = 4)

    #to add: roll function and exit button

def week1():

    def addToList():
        newItem = E1.get()
        playList.append(newItem)
        E1.delete(0, END)

    clearWindow()
    
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
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "Export List", bg = "red", command = exportList)
    B3.grid(column = 1, row = 3)

    """
    Bclear = Button(text = "Clear Window", bg = "white", command = clearWindow)
    Bclear.grid(column = 3, row = 1)
    """


if __name__ == "__main__":
    mainMenu()
    top.mainloop()
