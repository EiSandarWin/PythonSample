import turtle
from turtle import *
import random

window = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(50*1)
    turtle.circle(-50*1)
    turtle.left(i)

window.exitonclick()