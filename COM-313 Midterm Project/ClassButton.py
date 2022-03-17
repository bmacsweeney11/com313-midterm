# button.py
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(4)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True


    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgray') ##color the text "darkgray"
        self.rect.setWidth(1) ##set the outline to look finer/thinner
        self.active = False ##set the boolean variable that tracks "active"-ness to False
        

    def isClicked(self, pt):
        """Returns true if button active and Point pt is inside"""
        if self.active and pt.getX()>=self.xmin and pt.getX()<=self.xmax and pt.getY()>=self.ymin and pt.getY()<=self.ymax:
            return True
        else:
            return False

