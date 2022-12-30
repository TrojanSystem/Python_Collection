from turtle import Turtle

new_position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    segments = []

    def __init__(self):
        self.segment = []
        self.snake_creation()

    def snake_creation(self):
        for snakes in new_position:
            self.add_snake(snakes)

    def add_snake(self, position):
        snake = Turtle()
        snake.shape('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        snake.speed('fastest')
        self.segments.append(snake)

    def snake_length(self):
        self.add_snake(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
