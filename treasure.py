from placeableObject import *
from RobotClass import *

class treasure(object):
    def __init__(self, v = 1, s = 0, score = 0):
        self.v = v
        self.s = s
        self.score = score

    def drawTreasure(self, canvas):
        self.canvas = canvas
        self.p = self.canvas.create_image(self.x, self.y, image = gif1, anchor = NW)
        self.canvas.update()

    def treasureFound(self, canvas):
        
