class Treasure():
    def __init__(self, x, y, size, colour = "green"):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
    def drawTreasure(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill = self.colour)
    def deleteTreasure(self, canvas, shape):
         self.canvas = canvas
         self.shape = shape
         self.canvas.update()
