import turtle
from turtle import *
import random
import colorgram


def color_generator():
    t = Turtle()
    colors = colorgram.Color(r=255, g=255, b=255, proportion=1)

    Screen().screensize(300, 300)
    width = Screen().canvwidth
    height = Screen().canvheight
    turtle.colormode(255)
    t.speed(0)
    t.penup()
    t.goto(-width, -height)
    while t.xcor() <= 300 and t.ycor() <= 300:
        t.penup()

        t.color((random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)))
        t.begin_fill()
        t.pendown()
        t.circle(5)
        t.end_fill()
        t.penup()
        t.forward(20)
        t.pendown()
        if t.xcor() >= 300:
            height -= 20
            var = 1 * height
            t.penup()
            t.goto(-width, -var)
            t.pendown()
    exitonclick()



