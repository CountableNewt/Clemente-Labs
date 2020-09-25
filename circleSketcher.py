# circleSketcher.py
#   Lab 3
#   Allow a user to draw a circle and then set the fill color of that circle
#   by: Sam Clemente
#   9/25/2020

from graphics import *
from math import *

def main():
    
    # Circle Sketcher window is created
    # with reset coordinates for ease of programming
    win = GraphWin("Circle Sketcher 0.5", 640,640)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # Initial message in Circle Sketcher
    message = Text(Point(5.0, 5.0), "Click to set your circle's center")
    message.draw(win)

    # Stores point for center of circle
    center = win.getMouse()
    Point(center.getX(), center.getY()).draw(win)
    
main()
