from turtle import Turtle


class PaddleBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(1, 1)
        self.goto(0, 0)
        self.x_move = 0.05
        self.y_move = 0.05

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def wall_detection(self):
        self.y_move *= -1

    def paddle_detection(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.paddle_detection()
