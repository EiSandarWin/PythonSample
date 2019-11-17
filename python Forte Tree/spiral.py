import turtle
from turtle import *


colors = ['red', 'purple', 'blue']
hellopen = turtle.Pen()
turtle.bgcolor("black")

begin_fill()
for x in range(90):
    hellopen.pencolor(colors[x % 3])
    hellopen.width(x/100 + 1)
    hellopen.forward(x)
    hellopen.left(59)
end_fill()
done()