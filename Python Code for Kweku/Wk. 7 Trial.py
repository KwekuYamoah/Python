import math
from graphics import *

def square (x):
    return x ** 2

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def main():
    win = GraphWin("Draw a Triangle")
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    
p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
p2.draw(win)
p3 = win.getMouse()
p3.draw(win)

triangle = Polygon(p1, p2, p3)
triangle.draw(win)

perimeter = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
message.setText("The perimeter is: ", perimeter)