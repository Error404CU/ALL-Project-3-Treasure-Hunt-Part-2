import time
from Tkinter import *
import random
from random import randint
import time
# Window Defining
# Window Defining
window = Tk()
window.title('Treasure Hunt!')
canvas = Canvas(window, width = 1000, height = 600, bg = 'white')
canvas.pack(padx = 0, pady = 0)
# Lines
line1 = canvas.create_line((0, 600, 800, 600),(800, 0, 800, 800),
(800, 600, 1000, 600))

class Robot():
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
        time.sleep(0.05)
        self.canvas.update()

class Treasure():
    def __init__(self, x, y, size, colour = "green"):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
    def drawObject(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill = self.colour)
    def deleteObject(self, canvas, shape):
         self.canvas = canvas
         self.canvas.delete(self.shape)
         self.remove = remove

class Traps(Treasure, Robot): #Child Class is Traps, Parent classes are Treasure and Robot

    def drawTrap(self, canvas):
        self.canvas = canvas
        
        

ScoreList  = []
        
def Insertion_Sort(ScoreList):
    #starts at 1 so it can compare an element to the left of it (0)
    for index in range(1,len(ScoreList)):
        Cvalue = ScoreList[index]
        # -1, the element in the list left to the index
        j = index - 1
        while j >= 0:                       # J needs to stay in positive numbers for the sake of this list
            #whatever number is j
            if Cvalue < ScoreList[j]:
                #is to the right of j
                ScoreList[j+1] =ScoreList[j]   #Number in slot J becomes the number in j + 1 (Cvalue)
                ScoreList[j] = Cvalue       #Number in slot J+1 becomes the number in J
                j = j - 1
            else:
                break                       #No swapping needs to occur
Trap1 = Traps(randint(50,500),randint(50,500),size=20,colour="blue")    #Child Trap class inheriting from the parent Treasure class to draw the traps
Trap1.drawObject(canvas)
Trap2= Traps(randint(50,500), randint(50,500),size=20,colour="blue")
Trap2.drawObject(canvas)
x_min = 50
y_min = 50
x_max = 750
y_max = 550

a = 10
b = 10

Robot1 = Robot(100, 100, size=20, colour="black")
Robot1.drawRobot(canvas)

moveList = [10, -10, 10,-10]
TrList = []
ScoreList = []

CurrentScore = 0
TotalScore = 0


ScoreDraw = canvas.create_text(50,20, text='Robot1 Score: 0')

def Treasure1():
    if(var1.get()):
        var1.set(1)
        global Treasure1
        global TrList
        Treasure1 = Treasure(randint(50,500),randint(50,500),size=40,colour="green")
        Treasure1.drawObject(canvas)
        TrList.append(Treasure1)
def Treasure2():
    if(var3.get()):
       var3.set(1)
       global Treasure2
       Treasure2 = Treasure(randint(50,500),randint(50,500),size=40,colour="green")
       Treasure2.drawObject(canvas)
       TrList.append(Treasure2)

def Treasure3():
    if (var4.get()):
        var4.set(1)
        global Treasure3
        Treasure3 = Treasure(randint(50,500),randint(50,500),size=40,colour="green")
        Treasure3.drawObject(canvas)
        TrList.append(Treasure3)

def Treasure4():
    if (var5.get()):
        var5.set(1)
        global Treasure4
        Treasure4 = Treasure(randint(50,500),randint(50,500),size=40,colour="green")
        Treasure4.drawObject(canvas)
        TrList.append(Treasure4)
def Treasure5():
    if (var6.get()):
        var6.set(1)
        global Treasure5
        Treasure5= Treasure(randint(50,500),randint(50,500),size=40,colour="green")
        Treasure5.drawObject(canvas)
        TrList.append(Treasure5)
        

var1=IntVar()
checkbox1 = Checkbutton(window, text='Treasure 1   ', variable=var1, command=Treasure1)
checkbox1.pack(side = LEFT)
var3=IntVar()
checkbox3 = Checkbutton(window, text='Treasure 2   ', variable=var3, command=Treasure2)
checkbox3.pack(side = LEFT)
var4=IntVar()
checkbox4 = Checkbutton(window, text='Treasure 3  ', variable=var4, command=Treasure3)
checkbox4.pack(side = LEFT)
var5=IntVar()
checkbox5  = Checkbutton (window, text='Treasure 4  ', variable=var5, command=Treasure4)
checkbox5.pack(side = LEFT)
var6=IntVar()
checkbox6= Checkbutton(window, text='Treasure 5 ', variable=var6,command=Treasure5)
checkbox6.pack(side = LEFT)

def StartB():
    if(var2.get()):
        var2.set(1)
        for i in range(300):
                global a
                global b
                global score
                global ScoreDraw
                global TotalScore
                global CurrentScore
                global shape
                for j in range(0, len(TrList)):
                        Robot1.moveRobot(a,b)
                        if (Robot1.x >= TrList[j].x -40)and (Robot1.x <=TrList[j].x + 40)and (Robot1.y >= TrList[j].y -40)and (Robot1.y <= TrList[j].y + 40):
                            CurrentScore = randint(1,100)
                            ScoreList.append(CurrentScore)
                            TotalScore = TotalScore + CurrentScore
                            canvas.delete(ScoreDraw)
                            ScoreDraw = canvas.create_text(50,20, text= "Robot1 Score: %r "  %TotalScore)
                            a = random.choice(moveList)
                            b =  random.choice(moveList)
                            canvas.delete(TrList[j].shape)
                            TrList[j].x = 0
                            TrList[j].y = 0
                            print TotalScore
                        if (Robot1.x >= Trap1.x -40)and (Robot1.x <=Trap1.x + 40)and (Robot1.y >= Trap1.y -40)and (Robot1.y <= Trap1.y + 40):
                             canvas.delete(Trap1.shape)#Inheritance of Treasure class, using the deleteObject method
                             Trap1.x = 0                            #Inheritance using the drawObject method
                             Trap1.y = 0
                             a = 0 
                             b = 0
                             time.sleep(4)
                             a = random.choice(moveList)
                             b =  random.choice(moveList)
                        if(Robot1.x >= Trap2.x -40)and (Robot1.x <=Trap2.x + 40)and (Robot1.y >= Trap2.y -40)and (Robot1.y <= Trap2.y + 40):
                            canvas.delete(Trap2.shape)
                            Trap2.x = 0
                            Trap2.y = 0
                            a = 0
                            b = 0
                            time.sleep(4)
                            a = random.choice(moveList)
                            b =  random.choice(moveList)
                        if (Robot1.x <= x_min):
                            a = 10.0
                        elif (Robot1.x >= x_max):             
                            a =  -10.0
                        elif (Robot1.y <= y_min):                 
                            b = 10.0
                        elif (Robot1.y >= y_max):            
                            b = -10.0

        Insertion_Sort(ScoreList)#Calling the Insertion sort function
        print ScoreList #printing the results from the sort
var2 = IntVar()
checkbox2 =Checkbutton(window, text='Start!  ', variable=var2, command =StartB)
checkbox2.pack()
        
window. mainloop()

