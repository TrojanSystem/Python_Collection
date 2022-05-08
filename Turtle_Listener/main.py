from turtle import Turtle, Screen
import random

# from Event_Listener import EventListener
# x = EventListener()
# exitonclick()
all = [-70, -40, -10, 20, 50, 80]
turtle_color = ['red', 'green', 'blue', 'pink', 'black', 'cyan']

turtleList = []
screen = Screen()
screen.setup(500, 500)
ans = screen.textinput(' Turtle Race!', 'Place your bet ?').title()


def turtle_racing():
    for x in range(0, len(all)):
        turtle = Turtle(shape='turtle')
        turtle.color(turtle_color[x])
        turtle.penup()
        turtle.goto(-210, all[x])
        turtleList.append(turtle)
    run_again = True
    while run_again:
        for y in turtleList:

            y.forward(random.randint(0, 10))

            if y.xcor() > 210:

                print(y.pencolor())

                run_again = False
                if ans == y.pencolor():
                    print('you win')

                else:
                    print('you lost')


screen.exitonclick()
