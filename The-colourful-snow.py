# Feel Free to download,copy,ETC.
#Thanks to the Raspberry Pi Foundation www.raspberrypi.org for the main design!


import turtle
import random

wn = turtle.Screen()
b = turtle.Turtle()
wn.bgcolor("grey")


colours = ["cyan", "green", "purple", "blue", "magenta", "yellow", "orange", "red", "pink"]

b.penup()
b.forward(90)
b.left(45)
b.pendown()

def branch():
    for i in range(3):
        for i in range(3):
          b.forward(30)
          b.backward(30)
          b.right(45)
        b.left(90)
        b.backward(30)
        b.left(45)
    b.right (90)
    b.forward(90)


for i in range(8):
    b.color(random.choice(colours))
    branch()
    b.left(45)
    wn.bgcolor(random.choice(colours))
    
wn.exitonclick()
