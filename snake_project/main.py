from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
snake1 = Turtle('square')
snake2 = Turtle('square')
snake2.goto(-22, 0)
snake3 = Turtle('square')
snake3.goto(-44, 0)

food = Turtle()
food.penup()
food.hideturtle()
food.goto(50,50)
food.dot(10,'blue')
screen.exitonclick()
