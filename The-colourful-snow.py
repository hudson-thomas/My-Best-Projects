# Feel Free to download,copy,ETC.
#This was done on my Raspberry Pi.  You can find them here: Raspberrypi.org. Happy 4th Birthday Raspberry Pi!


import turtle
import random

wn = turtle.Screen()
b = turtle.Turtle()
wn.bgcolor("grey")


colours = ["cyan", "green", "purple", "blue", "magenta", "orange", "red", "pink"]

colourstwo = ["white"]

b.penup()
b.forward(90)
b.left(45)
b.pendown()

def branch():
    for i in range(3):
        for i in range(3):
          b.color(random.choice(colours))
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

while True:
    wn.bgcolor(random.choice(colourstwo))
    
    
wn.exitonclick()
