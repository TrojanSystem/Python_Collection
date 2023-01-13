from turtle import Turtle


class PongScore(Turtle):
    left_score = 0
    right_score = 0

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-120, 260)

        self.update()

    def update(self):
        self.write(f'Score: left: {self.left_score},right: {self.right_score} ', font=('Arial', 24, 'bold'))

    def update_left(self):
        self.left_score += 1
        self.clear()
        self.update()

    def update_right(self):
        self.right_score += 1
        self.clear()
        self.update()

    def l_score(self):
        self.write(f'Score: left: {self.left_score},right: {self.right_score} ', font=('Arial', 24, 'bold'))
