from turtle import Turtle

SPEED = 10


class CrossScore(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.color('black')

        self.penup()
        self.goto(-240, 240)
        self.write(f'Level: {self.level}')

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}')

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over! \n Level: {self.level}')
