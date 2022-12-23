import random
from turtle import *

dice = [1, 2, 3, 4, 5, 6, 7]

is_game_finished = True
p1 = Turtle()
p2 = Turtle()
finish_line_2 = Turtle()
finish_line_1 = Turtle()
Screen().screensize(300, 300)
p1.shape('turtle')
p1.color("green")
p1.penup()
p1.goto(-350, 0)
p2.shape('turtle')
p2.color("red")
p2.penup()
p2.goto(-350, 100)
finish_line_1.penup()
finish_line_1.goto(300, -15)
finish_line_2.penup()
finish_line_2.goto(300, 85)
finish_line_1.pendown()
finish_line_2.pendown()
finish_line_1.color('blue')
finish_line_1.circle(20)
finish_line_2.color('orange')
finish_line_2.circle(20)
# guess = input('Enter your guess 1 or 2: ')
while is_game_finished:
    race_speed = random.choice(dice)
    race_speed_2 = random.choice(dice)
    if int(p1.xcor()) <= 300:
        p1.pendown()
        p1.forward(xcor() + race_speed)

    if int(p2.xcor()) <= 300:
        p2.pendown()
        p2.forward(xcor() + race_speed_2)

    else:
        is_game_finished = False
if p1.xcor() >= 300:

    print('Player 1 Wins')
elif p2.xcor() >= 300:

    print('Player 2 Wins')

exitonclick()
