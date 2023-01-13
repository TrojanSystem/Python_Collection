from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.y_pos = 0.07

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def up_down(self):
        new_y = self.ycor() + self.y_pos
        self.goto(self.xcor(), new_y)

    def paddle_detection(self):
        self.y_pos *= -0.07

