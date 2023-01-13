from turtle import Turtle


class CrossTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.left(90)
        self.penup()
        self.goto(0, -280)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def reset_position(self):
        self.goto(0, -280)
