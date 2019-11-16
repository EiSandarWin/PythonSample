import turtle
from turtle import *
window = turtle.Screen()
#window.bgcolor("#0dd914")
window.bgpic("cat.gif")

color('#1013e3', '#f0300e')
begin_fill()
while True:
    forward(90)

    left(-60)
    backward(60)
    #right(50)
    if abs(pos())<1:
        break

end_fill()
done()