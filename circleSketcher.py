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
    centerPoint = Point(center.getX(), center.getY()).draw(win)

    # Changing message
    message.setText("Click again to define the radius of your circle")

    # Getting radius point
    edge = win.getMouse()

    # Using distance formula to find the radius
    radius = sqrt((center.getX() - edge.getX())**2 +
                  (center.getY() - edge.getY())**2)

    # Drawing circle
    circle1 = Circle(centerPoint, radius).draw(win)

    # Changing message
    message.setText("Click again to color the circle red")

    # Setting circle color after click
    win.getMouse()
    circle1.setFill("red")

    # Exit prompt
    message.setText("Click again to close")
    win.getMouse()
    win.close()
    
main()

