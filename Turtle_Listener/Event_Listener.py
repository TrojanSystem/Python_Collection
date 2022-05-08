import random

from turtle import *

t = Turtle()
x = Turtle()
t.setposition(0, 0)


def left_move():
    left(90)


def forward_move():
    forward(20)


def backward_move():
    forward(-20)


def right_move():
    right(90)


def random_circle():
    speed('fastest')
    x.hideturtle()
    x.penup()
    x.begin_fill()
    x.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x.setposition(random.randint(0, 255), random.randint(0, 255))
    x.pendown()
    x.circle(5)
    x.end_fill()


class EventListener:
    colormode(255)

    t.screen.listen()
    x.screen.listen()
    x.screen.onkey(random_circle, 'space')

    t.screen.onkey(forward_move, 'w')
    t.screen.onkey(backward_move, 's')
    t.screen.onkey(left_move, 'a')
    t.screen.onkey(right_move, 'd')
