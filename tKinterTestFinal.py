from tkinter import *
import random

import tkinter.font as font

top = Tk()
playList = []
myRolls = []
rollTimes = 0
dieType = 0

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
    myFont1 = font.Font(family='Times', size=15, weight='bold')
    B1Main = Button(text='Week 1', bg='purple', fg='yellow', command = week1)
    B1Main.grid(column = 2, row = 2)
    # apply font to the button label
    B1Main['font'] = myFont1
    
    B2Main = Button(text = "Week 2", bg = "#c6edee", command = week2)
    B2Main.grid(column = 2, row = 3)
    myFont2 = font.Font(family='Times', size=15, weight='bold')
    B2Main = Button(text='Week 2', bg='orange', fg='white', command = week2)
    B2Main.grid(column = 2, row = 3)
    # apply font to the button label
    B2Main['font'] = myFont2
    
    B3Main = Button(text = "Week 3", bg = "#c6edee", command = week3)
    B3Main.grid(column = 2, row = 4)
    myFont3 = font.Font(family='Times', size=15, weight='bold')
    B3Main = Button(text='Week 3', bg='black', fg='white', command = week3)
    B3Main.grid(column = 2, row = 4)
    # apply font to the button label
    B3Main['font'] = myFont3

    Bclear = Button(text = "Main Menu", bg = "white", command = mainMenu)
    Bclear.grid(column = 3, row = 1)

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
    
def week2():
    def rollDice():
        #update our variable data
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        #clear window AFTER pulling Entry data
        clearWindow()
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
            
        #display dice rolls and present an exit button
        L4W2 = Label(top, text = "Here are your rolls!")
        L4W2.grid(column = 0, row = 1)
        #this one will use a .format() statement
        L5W2 = Label(top, text = "{}".format(myRolls))
        L5W2.grid(column = 0, row = 2)
        
        B2W2 = Button(text = "Main Menu", bg = "#2574a8", command = mainMenu)
        B2W2.grid(column = 0, row = 3)
            
    
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

    B1W2 = Button(text = "Roll!", bg = "#ff0099", command = rollDice)
    B1W2.grid(column = 2, row = 4)

    #to add: roll function and exit button

def week3():
    clearWindow()
    Bclear1 = Button(text = "Main Menu", bg = "#03fc5e", command = mainMenu)
    Bclear1.grid(column = 4, row = 1)
    def angryFace():
        import turtle
        smiles = turtle.Turtle()

        smiles.penup()
        smiles.goto(-105,155)
        smiles.pendown()
        smiles.goto(-45,115)

        smiles.penup()
        smiles.goto(-75,75)
        smiles.pendown()
        smiles.circle(10)

        smiles.penup()
        smiles.goto(105,155)
        smiles.pendown()
        smiles.goto(45,115)

        smiles.penup()
        smiles.goto(75,75)
        smiles.pendown()
        smiles.circle(10)

        smiles.penup()
        smiles.goto(0,25)
        smiles.pendown()
        smiles.circle(-100,80)

        smiles.penup()
        smiles.setheading(180)
        smiles.goto(0,25)
        smiles.pendown()
        smiles.circle(100,80)
        
    def sadFace():
        import turtle
        smiles = turtle.Turtle()
        smiles.penup()
        smiles.goto(-75,150)
        smiles.pendown()
        smiles.circle(10)

        smiles.penup()
        smiles.goto(75,150)
        smiles.pendown()
        smiles.circle(10)
        smiles.penup()
        smiles.goto(0,50)
        smiles.pendown()
        smiles.circle(-100,90)

        smiles.penup()
        smiles.setheading(180)
        smiles.goto(0,50)
        smiles.pendown()
        smiles.circle(100,90)

        turtle.done()

    def happyFace():
        import turtle
        smiles = turtle.Turtle()  
        smiles.penup()
        smiles.goto(-75,150)
        smiles.pendown()
        smiles.circle(10)

        smiles.penup()
        smiles.goto(75,150)
        smiles.pendown()
        smiles.circle(10)

        smiles.penup()
        smiles.goto(0,0)
        smiles.pendown()
        smiles.circle(100,90)

        smiles.penup()           
        smiles.setheading(180)
        smiles.goto(0,0)
        smiles.pendown()
        smiles.circle(-100,90)

    def nonEnthused():
        import turtle
        smiles = turtle.Turtle()

        #this part is the left eyebrow
        smiles.penup()
        smiles.goto(-105,105)
        smiles.pendown()
        smiles.goto(-45,115)

        #this part is the left eye
        smiles.penup()
        smiles.goto(-75,75)
        smiles.pendown()
        smiles.circle(10)

        #this part is the right eyebrow
        smiles.penup()
        smiles.goto(105,105)
        smiles.pendown()
        smiles.goto(45,115)

        #this part is the right eye
        smiles.penup()
        smiles.goto(75,75)
        smiles.pendown()
        smiles.circle(10)

        #this part is the right side of the smile
        smiles.penup()
        smiles.goto(0,25)
        smiles.pendown()
        smiles.goto(100, 25)
        
        #this part is the left side of the smile
        smiles.penup()
        smiles.setheading(180)
        smiles.goto(0,25)
        smiles.pendown()
        smiles.goto(-100,25)
        
    L1W3 = Label(top, text = "Drawing Expressions")
    L1W3.grid(column = 0, row = 1)

    E1W3 = Entry(top, bd = 5)
    E1W3.grid(column = 0, row = 2)

    B1W3 = Button(text = "Angry Face", bg = "red", command = angryFace)
    B1W3.grid(column = 0, row = 3)

    B2W3 = Button(text = "Sad Face", bg = "blue", command = sadFace)
    B2W3.grid(column = 1, row = 2)

    B3W3 = Button(text = "Happy Face", bg = "yellow", command = happyFace)
    B3W3.grid(column = 1, row = 3)

    B4W3 = Button(text = "Unenthused Face", bg = "white", command = nonEnthused)
    B4W3.grid(column = 0, row = 2)


    
if __name__ == "__main__":
    mainMenu()
    top.mainloop()
