# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:27:36 2019

@author: User
"""

from graphics import *
def main():

    win = GraphWin("Tutorial",600,600)
    win.setBackground("white")
    win.setCoords(0,0,100,100)
    '''for i in rang(0,101,10):
        line= Line(Point(i,0), Point(1,100))
        line.draw(win)
        
    a= Point(20,30)
    a.draw(win)
    point1= Point(80,80)
    point2 = Point(80,90)
    b = Line(point1,point2)
    b.draw(win)
    
    a = Line(Point(20,30),Point(100,100))
    a.setArrow
    a.draw(win)
    print(a.getCenter())
    print(a.getP1())
    
    a= Circle(Point(50,50),20)
    a.setFill("black")
    a.setOutline("pink")
    a.setWidth(5)
    a.draw(win)
    
    a= Rectangle(Point(20,30),Point(100,100))
    a.draw(win)
    
    a= Oval(Point(20,30),Point(100,100))
    a.draw(win)
    for i in range(0,50,5):
        a = Text(Point(50,90),"Welcome")
        a.setFace("helvetica")
        a.setSize(30)
        a.setTextColor("green")
        a.draw(win)
        
        """a.move(1,0)"""
    a = Entry(Point(50,50),20)
    a.setFill("white")
    a.draw(win)'''
    
    a= Rectangle(Point(20,30),Point(40,70))
    a.draw(win)
    
    b = Text(a.getCenter(),"Click me")
    b.draw(win)
    
    q= win.getMouse()
    if 20 <= q.x <=40 and 30 <= q.y <= 70:
        print("You clicked me")
        
    else:
        q.getMouse()
        
    win.close()
        
    
    
main()