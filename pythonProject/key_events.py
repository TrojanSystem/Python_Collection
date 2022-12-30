import random
from turtle import *

# t = Turtle()
# s = Screen()
#
# t.shape('turtle')
#
#
# def move_forward():
#     t.forward(10)
#
#
# def move_backward():
#     t.backward(10)
#
#
# def turn_right():
#     t.right(10)
#
#
# def turn_left():
#     t.left(10)


# s.onkeypress(move_forward, 'w')
# s.onkeypress(move_backward, 's')
# s.onkeypress(turn_left, 'a')
# s.onkeypress(turn_right, 'd')
# s.listen()
colors = [{'turtle_color': 'red', 'y': -100}, {'turtle_color': 'yellow', 'y': -50}, {'turtle_color': 'green', 'y': 0},
          {'turtle_color': 'blue', 'y': 50}, {'turtle_color': 'orange', 'y': 100}]
speed = [1, 2, 3, 4, 5, 6, ]
all_turtle = []
guess = Screen().textinput('User Guess', 'Enter your bet? ')
is_game_on = False
if guess:
    is_game_on = True
for x in range(0, 5):
    tx = Turtle()
    tx.shape('turtle')
    tx.color(colors[x]['turtle_color'])
    tx.penup()
    tx.goto(-float(Screen().window_width() / 2.1), colors[x]['y'])

    all_turtle.append(tx)

while is_game_on:
    for racing_turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        racing_turtle.forward(rand_distance)
        if racing_turtle.xcor() >= Screen().window_width() / 2.1:
            if guess == racing_turtle.fillcolor():
                print('You Win!')

            else:
                print('You Lose!')
            is_game_on = False
            break

exitonclick()
