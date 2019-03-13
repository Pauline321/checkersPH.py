##checkers.py by Pauline Harrell

from graphics import *

sqSz = 50

chWin = GraphWin(" Checkers" , sqSz * 10, sqSz * 10)
chWin.setCoords(0, 0, sqSz * 10, sqSz * 10)


sQ = Rectangle(Point(sqSz, sqSz), Point(sqSz + sqSz, sqSz + sqSz))
sQ.setFill(color_rgb(255,0,0))
sQ.draw(chWin)
                                   
chWin.getMouse()
chWin.close()                        
