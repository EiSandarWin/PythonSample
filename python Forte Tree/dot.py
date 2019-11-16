import turtle

dot = turtle.Turtle()

dot_distance = 50
width = 8
height = 8

dot.pendown()

for i in range (height):
    for x in range(width):
        dot.dot()
        dot.forward(dot_distance)
    dot.backward(dot_distance * width)
    dot.left(90)
    dot.forward(dot_distance)
    dot.right(90)

turtle.done()

