import turtle
from turtle import *
star = turtle.Turtle()
window = turtle.Screen()

color('#fcba03','#1a0fdb')

while True:
    for i in range(5):

        star.forward(150)
        begin_fill()
        star.right(144)
    if abs(pos())<1:
        break

end_fill()

turtle.done()