# Function Mapper #############################################################################
# Python v3.4.3
# ~~~~Created by David M Carter (2016)~~~~
#
# This program maps functions on the Cartesian plane using Turtle Graphics
#
#
# INPUT:
#           f          function to map on [-4,4]
#
# OUTPUT:
#           window     function mapped in window
#                      function labeled in bottom left of window
#
###############################################################################################

import turtle, math

def main():

  ttl = turtle.Turtle()
  screen = turtle.Screen()
  ttl.penup()

  func = input("Enter function f to map over the interval [-4, 4] \n  (for example; math.sin(x**2)) \nf: ")

  #Configure the window
  screen.title("Function Mapper")
  screen.setup(900,900)

  #Create x axis
  ttl.goto(-400,0)
  ttl.pendown()
  ttl.goto(400,0)
  ttl.penup()

  #Create y axis
  ttl.goto(0,400)
  ttl.pendown()
  ttl.goto(0,-400)
  ttl.penup()

  #Add tick marks to the x-axis
  for x in range(0,9):
      ttl.goto((-400 + 100*x),5)
      ttl.pendown()
      ttl.goto((-400 + 100*x),-5)
      ttl.penup()

  #Add tick marks to the y-axis
  for y in range(0,9):
      ttl.goto(-5,(-400 + 100*y))
      ttl.pendown()
      ttl.goto(5,(-400 + 100*y))
      ttl.penup()

  #Label the tick marks on the x-axis
  for n in range (0,9):
      ttl.goto((-397 + n*100),-17)
      ttl.write(n - 4)

  #Label the tick marks on the y-axis
  for n in range (0,9):
      ttl.goto(7, (-408 + n*100))
      if (n != 4):
          ttl.write(n - 4)

  #Define a method that evaluates an arbitrary function f(x)
  def evalu(xLeft, xRight):
     ttl.penup()
     ttl.goto(xLeft, scale*f(xLeft/scale))
     ttl.pendown()
     
     while (xLeft <= xRight):
         ttl.goto(xLeft , scale*f(xLeft /scale))
         xLeft += 1

  #Map f(x)
  def drawFunc(left, right, color):
      ttl.pencolor(color)
      evalu(left, right)
  
  
  #Define f(x), the interval, color, and evaluate
  scale = 100
  ttl.pensize(3)

  #f(x)
  def f(x):
      return eval(func)
  leftBound = -4
  rightBound = 4
  drawFunc(leftBound*scale, rightBound*scale, "green")
  ttl.penup()
  ttl.goto(-440, -440)
  ttl.color("green")
  ttl.write(func)
  
main()
