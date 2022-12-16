"""
Program Name: CIS110 Program8
Program Description: Tic Tac Toe game!
Author Name: Lee Kitchen
Date Created: 11/03/2021
Notes: Lets Play Tic Tac Toe!!!


"""
from graphics import *
import time
def gameB(win):#function for making the playing board
    Text(Point(1.5,3.5),"Let's Play Tic-Tac-Toe").draw(win)
    board = Rectangle(Point(0,0),Point(3,3))
    board.setFill("yellow")
    board.draw(win)
def lines(win): #function to draw grid lines
    Line(Point(0,1),Point(3,1)).draw(win)
    Line(Point(0,2),Point(3,2)).draw(win)
    Line(Point(1,0),Point(1,3)).draw(win)
    Line(Point(2,0),Point(2,3)).draw(win)

def drawX(win):# function for drawing x on mouse centered on the mouse click
    msg= Text(Point(1.5,-.5),"Click to place an X")
    msg.draw(win)
    X1=Line(Point(.10,.90),Point(.90,.10))
    X1.setWidth(5)
    X2=Line(Point(.90,.90),Point(.10,.10))
    X2.setWidth(5)
    C= X1.getCenter()
    p= win.getMouse()
    dx= p.getX() -C.getX()
    dy= p.getY() - C.getY()
    X1 = X1.clone()
    X1.move(dx,dy)
    X2 = X2.clone()
    X2.move(dx,dy)
    X1.draw(win)
    X2.draw(win)
    msg.undraw()
    
def drawO(win):# function for drawing O on mouse centered on the mouse click
    msg= Text(Point(1.5,-.5),"Click to place an O")
    msg.draw(win)
    Center= Circle(Point(.5,.5),.45)
    Center.setWidth(3)
    Center= Center.clone()
    C= Center.getCenter()
    p= win.getMouse()
    dx= p.getX() -C.getX()
    dy= p.getY() - C.getY()
    Center= Center.clone()
    Center.move(dx,dy)
    Center.draw(win)
    msg.undraw()
    
    
    
def main():
    win= GraphWin("Game Board", 500,500) #Setting window size
    win.setCoords(-1,-1,4,4)# setting coordinate plane
    win.setBackground("white")
    gameB(win)
    lines(win)
    msg= Text(Point(1.5,-.5),"Click to place an X") #game prompt
    msg.draw(win)
    drawX(win)
    msg.undraw()
    drawO(win)
    for i in range(3):#loop for lessing repetion 
        drawX(win)
        msg.undraw()
        drawO(win)
    drawX(win)
    msg1=Text(Point(1.5,-.5),"Game Over! Click to close")
    msg1.draw(win)
    win.getMouse()
    win.close()#close window at the end of the program

    
    #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Program: Program8")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__ == '__main__':
    main()
