from turtle import *
import random

hideturtle()
colormode(255)


def star():
    colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color(colors)
    begin_fill()
    left(36)
    while True:
        forward(200)
        left(144)

        if abs(pos()) < 1:
            break

    end_fill()
    done()


def dashed_line():
    while True:
        forward(10)
        penup()
        forward(10)
        pendown()
        if abs(pos()) > 300:
            break


# Spirograph
def spiral_circle(x):
    speed('fast')
    left(x + 10)
    circle(50)


# From Triangle to Decagon all in one
def multiple_shape(number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        right(angle)
        forward(100)


# Bulk layed out shapes
def multiple_shapes():
    # triangle
    right(120)
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    # rectangle
    right(90)
    forward(87)
    right(90)
    forward(100)
    right(90)
    forward(87)
    right(90)
    forward(100)
    # Pentagon
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    # Hexagon
    right(60)
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    # Pentgon
    right(51)
    forward(100)
    right(51)
    forward(100)
    right(51)
    forward(100)
    right(51)
    forward(100)
    right(51)
    forward(100)
    right(51)
    forward(100)
    right(51)
    forward(100)
    # Octagon
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    # Nonagon

    right(40)
    forward(100)
    right(40)
    forward(100)
    right(40)
    forward(100)
    right(40)
    forward(100)
    right(40)
    forward(100)
    right(40)
    forward(100)
    right(40)
    forward(100)
    right(40)
    forward(100)
    right(40)
    forward(100)
    # Decagon
    right(36)
    forward(100)
    right(36)
    forward(100)
    right(36)
    forward(100)
    right(36)
    forward(100)
    right(36)
    forward(100)
    right(36)
    forward(100)
    right(36)
    forward(100)
    right(36)
    forward(100)
    right(36)
    forward(100)
    right(36)
    forward(100)


def random_lines():
    colormode(255)
    direction = [0, 90, 180, 270]

    pensize(10)
    forward(40)

    for x in range(360):
        colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color(colors)
        setheading(random.choice(direction))
        forward(30)


colormode(255)


def dot_circle():
    for x in range(200):
        setheading(0)
        colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color(colors)
        pendown()
        begin_fill()
        circle(5)
        end_fill()
        penup()
        forward(20)
        pendown()
        if x % 10 == 0:
            penup()
            setheading(90)
            forward(30)
            setheading(180)
            forward(200)
            setheading(0)
            pendown()


class Graphics:
    pass
