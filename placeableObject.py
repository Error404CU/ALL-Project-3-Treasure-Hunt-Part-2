from Tkinter import *

class placeableObject(object):
    def __init__(self, x, y, name = "", size = 0, oid = 0, txt = ""):
        self.x = x
        self.y = y
        self.name = name
        self.size = size
        self.oid = oid
        self.txt = txt

    def deleteObject(self):
        self.canvas = canvas
        self.canvas.delete(self)
        self.canvas.delete(self.txt)
        self.canvas.update()
