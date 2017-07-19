
from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 500
y_pos = 300
#t.setposition(x_pos, y_pos)

### Write your code below:
def polygon(sides,length):
    for x in range (sides):
        forward (length)
        left(360/sides)
keepGoing = True
while keepGoing == True:
    sides = int(input("How many sides do you want me to draw?"))
    if sides == 0:
        keepGoing = False
    else:
        clear()
        polygon(sides,100)





# Close window on click.
exitonclick()
