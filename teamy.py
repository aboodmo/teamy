from turtle import *
y = Turtle()
colormode(255)

def WriteText (centerX, centerY,text, color):
  #made by yasmine!
  y.penup()
  centerX=int(centerX)
  centerY=int(centerY)
  y.goto(centerX,centerY)
  y.color(color)
  y.write(text)
  
def DrawRect(topLeftX, topLeftY, width, height, color):
  #made by yasmineeee
  topLeftX=int(topLeftX)
  topLeftY=int(topLeftY)
  height=int(height)
  width=int(width)
  y.penup()
  y.goto(topLeftX, topLeftY)
  y.setheading(0)
  y.color(color)
  y.begin_fill()
  y.pendown()
  for i in range(2):
    y.forward(width)
    y.right(90)
    y.forward(height)
    y.right(90)
  y.end_fill()
  y.penup()
  
def window():
  #made by yasmine, not an object on its own
  y.pendown()
  y.forward(8)
  y.right(90)
  y.fillcolor("white")
  y.begin_fill()
  y.forward(8)
  y.right(90)
  y.forward(8)
  y.right(90)
  y.forward(8)
  y.right(90)
  y.penup()
  y.end_fill()
  
def makeRowOfWindows():
    for i in range (3):
      window()
      y.forward(12)
      y.pendown()
    y.penup()
    y.right(90)
    y.forward(16)
    y.right(90)
    y.forward(36)
    y.right(180)

def skyscraper():
  #made by yasmine
  y.fillcolor("black")
  y.begin_fill()
  y.pendown()
  y.forward(45)
  y.right(90)
  y.forward(300)
  y.right(90)
  y.forward(45)
  y.right(90)
  y.forward(300)
  y.right(180)
  y.pendown()
  y.forward(25)
  y.end_fill()
  y.penup()
  y.left(90)
  y.forward(6)
  for i in range (16):
   makeRowOfWindows()

 



update()
