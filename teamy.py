from turtle import *
from random import*
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
 y.penup()
 
def bus():
  #made by yasmineeeeeee
  y.color("yellow")
  y.begin_fill()
  y.right(90)
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
  y.forward(25)
  y.left(270)
  y.pendown()
  makeRowOfBusWindows()
  y.penup()
  y.left(90)
  y.forward(20)
  y.left(90)
  y.forward(13)
  y.pendown()
  y.color("black")
  y.begin_fill()
  for i in range(360):
    y.forward(.3)
    y.right(1)
  y.end_fill()
  y.forward(5)
  y.right(90)
  y.penup()
  y.forward(17)
  y.pendown()
  y.color("gray")
  y.begin_fill()
  for i in range(360):
    y.forward(.1)
    y.right(1)
  y.end_fill()
  y.penup()
  y.right(180)
  y.forward(20)
  y.right(90)
  y.forward(245)
  y.pendown()
  y.color("black")
  y.begin_fill()
  for i in range(360):
    y.forward(.3)
    y.right(1)
  y.end_fill()
  y.forward(5)
  y.right(90)
  y.penup()
  y.forward(17)
  y.pendown()
  y.color("gray")
  y.begin_fill()
  for i in range(360):
    y.forward(.1)
    y.right(1)
  y.end_fill()
  y.penup()
  y.right(180)
  y.forward(20)
  y.right(90)
  y.forward(20)
  y.left(90)
  y.forward(40)
  y.left(90)
  y.pendown()
  y.color("blue")
  y.begin_fill()
  for i in range(180):
      y.forward(.4)
      y.left(1)
  y.end_fill()
  y.penup()
  
  
def stickPerson():
#made by yasmine
#head and body
  y.pendown()
  y.pencolor("gray")
  y.fillcolor("gray")
  y.begin_fill()
  for i in range(360):
    y.forward(.5)
    y.left(1)
  y.end_fill()
  y.right(90)
  y.forward(125)
  #legs
  y.left(45)
  y.forward(85)
  y.right(180)
  y.forward(85)
  y.left(90)
  y.forward(85)
  # arms
  y.right(180)
  y.forward(85)
  y.left(45)
  y.forward(50)
  y.right(90)
  y.forward(85)
  y.left(180)
  y.forward(85)
  y.forward(85)
  y.penup()

def fish():
  #made by yasmine
  y.pencolor("black")
  y.fillcolor("orange")
  y.begin_fill()
  y.setheading(90)
  fishTailSize = random()*30+20 
  fishBodySize = random()*3+1   
  for i in range(5):
     y.forward(fishTailSize)
     y.right(120)
  y.end_fill()
  y.right(172)
  y.begin_fill()
  for i in range(60):
    y.forward(fishBodySize)
    y.right(1.4)
  y.right(90)
  for i in range(60):
    y.forward(fishBodySize)
    y.right(1.5)
  y.forward(5)
  y.end_fill()
  y.penup()

def starfish():
  #made by yasmine
  y.penup()
  y.pencolor("orange")
  y.fillcolor("orange")
  y.begin_fill()
  y.pendown()
  for i in range(5):
    y.forward(50)
    y.right(144)
  y.end_fill()
  y.penup()
 
def truck():
  #made by yasmine!
  y.color("black")
  y.begin_fill()
  y.forward(150)
  y.right(90)
  y.forward(75)
  y.right(90)
  y.forward(150)
  y.right(90)
  y.forward(75)
  y.end_fill()
  y.penup()
  y.right(90)
  y.forward(150)
  y.right(90)
  y.forward(75)
  y.left(90)
  y.pendown()
  y.color("black")
  y.begin_fill()
  for i in range(4):
    y.forward(35)
    y.left(90)
  y.end_fill()
  for i in range(2):
    y.forward(35)
    y.left(90)
  y.color("blue")
  y.begin_fill()
  for i in range(180):
      y.forward(.3)
      y.left(1)
  y.end_fill()
  y.penup()
  y.forward(-35)
  y.pendown()
  y.color("gray")
  y.begin_fill()
  for i in range(360):
    y.forward(.3)
    y.right(1)
  y.end_fill()
  y.right(180)
  y.forward(-5)
  y.left(90)
  y.penup()
  y.forward(15)
  y.pendown()
  y.color("black")
  y.begin_fill()
  for i in range(360):
    y.forward(.1)
    y.right(1)
  y.end_fill()
  y.right(180)
  y.penup()
  y.forward(15)
  y.left(90)
  y.forward(130)
  y.pendown()
  y.color("gray")
  y.begin_fill()
  for i in range(360):
    y.forward(.3)
    y.left(1)
  y.end_fill()
  y.forward(-5)
  y.left(90)
  y.penup()
  y.forward(15)
  y.pendown()
  y.color("black")
  y.begin_fill()
  for i in range(360):
    y.forward(.1)
    y.right(1)
  y.end_fill()
  y.penup()

def jellyfish():
  #made by yasmine!!!
  y.left(90)
  y.color("pink")
  y.begin_fill()
  for i in range(180):
    y.forward(1)
    y.right(1)
  y.right(90)
  y.forward(110)
  y.end_fill()
  y.forward(-10)
  y.left(90)
  #legs
  for i in range(4):
    y.pendown()
    for i in range(60):
      y.forward(.5)
      y.left(1)
    for i in range(15):
      y.forward(.1)
      y.right(1)
    for i in range(40):
      y.forward(.3)
      y.right(1)
    for i in range(70):
      y.forward(.5)
      y.right(1)
    y.right(180)
    for i in range(70):
      y.forward(.5)
      y.left(1)
    for i in range(40):
      y.forward(.3)
      y.left(1)
    for i in range(15):
      y.forward(.1)
      y.left(1)
    for i in range(60):
      y.forward(.5)
      y.right(1)
    y.penup()
    y.right(90)
    y.forward(30)
    y.right(90)
    y.penup()

def pumpkin():
  y.pendown()
  y.pencolor("brown")
  y.color("orange")
  y.begin_fill()
  for i in range(360):
    y.forward(1)
    y.left(1)
  y.end_fill()
  #pumpkin stem
  y.penup()
  y.color("green")
  y.forward(-15)
  y.left(90)
  y.forward(120)
  y.pendown()
  y.begin_fill()
  for i in range(6):
   y.forward(10)
   y.right(90)
   y.forward(15)
  y.forward(15)
  y.end_fill()
  y.penup()

def make_Boat():
  #by Abood
  bob.fillcolor('saddle brown')
  bob.begin_fill()
  bob.setheading(-85)
  for i in range(50):
      bob.forward(2)
      bob.left(1)
  bob.left(25)
  for i in range(60):
      bob.forward(5)
      bob.left(1)
  bob.left(25)
  for i in range(20):
      bob.forward(3)
      bob.left(1.5)
  bob.left(120)
  for i in range(43):
      bob.forward(8)
      bob.right(1.55)
  bob.right(120)
  for i in range(48):
      bob.forward(7)
      bob.right(1.1)
  bob.right(2)
  bob.end_fill()
  bob.fillcolor('chocolate')
  bob.begin_fill()
  bob.right(120)
  for i in range(48):
      bob.forward(7)
      bob.right(1.3)
  bob.right(135)
  for i in range(30):
      bob.forward(9)
      bob.right(.75)
  bob.end_fill()

  def make_seaweed():
    #by abood
  bob.fillcolor('dark green')
  bob.begin_fill()
  bob.setheading(135)
  for i in range(70):
      bob.forward(1.5)
      bob.right(1)
  for i in range(70):
      bob.forward(1.5)
      bob.left(1)
  for i in range(70):
      bob.forward(1.5)
      bob.right(1)
  bob.right(190)
  for i in range(70):
      bob.forward(1.5)
      bob.left(1)
  for i in range(70):
      bob.forward(1.5)
      bob.right(1)
  for i in range(70):
      bob.forward(1.5)
      bob.left(1)
  bob.left(90)
  bob.forward(10)
  bob.end_fill()

  def make_kite():
    #by abood
  bob.setheading(-90)
  bob.fillcolor('blue')
  bob.begin_fill()
  bob.forward(100)
  bob.left(90)
  bob.forward(5)
  bob.left(90)
  bob.forward(100)
  bob.right(45)
  bob.forward(50)
  for i in range(2):
      bob.left(90)
      bob.forward(53)
  bob.left(90)
  bob.forward(50)
  bob.end_fill()

  def make_cloud():
    #by abood
  bob.fillcolor('white')
  bob.begin_fill()
  bob.setheading(90)
  bob.forward(10)
  for i in range(180):
      bob.forward(1)
      bob.right(1)
  bob.right(180)
  for i in range(180):
      bob.forward(1)
      bob.right(1)
  bob.right(180)
  for i in range(180):
      bob.forward(1)
      bob.right(1)
  bob.forward(20)
  for i in range(90):
      bob.forward(1)
      bob.right(1)
  bob.forward(230)
  for i in range(98):
      bob.forward(1)
      bob.right(1)
  bob.end_fill()

  def make_UFO():
    #by abood
  bob.setheading(180)
  bob.fillcolor('gray')
  bob.begin_fill()
  for i in range(145):
      bob.forward(1)
      bob.left(1)
  for i in range (35):
      bob.forward(5)
      bob.left(1)
  for i in range(145):
      bob.forward(1)
      bob.left(1)
  for i in range (35):
      bob.forward(5)
      bob.left(1)
  bob.end_fill()
  bob.fillcolor('white')
  bob.begin_fill()
  bob.penup()
  bob.left(90)
  bob.forward(50)
  bob.pendown()
  bob.left(165)
  bob.forward(15)
  for i in range (12):
      bob.forward(6)
      bob.right(4)
  for i in range (44):
      bob.forward(4)
      bob.right(3)
  bob.forward(35)
  bob.right(45)
  for i in range (36):
      bob.forward(5)
      bob.right(2.80)
  bob.right(45)
  bob.forward(5)
  bob.end_fill()

  
update()
