import time
class Robot(object):
    def __init__(self, x, y, size, colour = "black"):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
    def drawRobot(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill = self.colour)
    def moveRobot(self, a, b):
        self.a = a
        self.b = b
        self.x += self.a
        self.y += self.b
        self.canvas.coords(self.shape, self.x, self.y, self.x + self.size, self.y + self.size)
        time.sleep(0.005)
        self.canvas.update()
