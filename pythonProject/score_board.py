from turtle import Turtle


class Score(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.score = 0

        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-50, 250)
        self.update()

    def update(self):
        self.write(f'Score: {self.score}', font=('Arial', 24, 'bold'))

    def game_over(self):
        self.goto(-115, 0)
        self.write(f'GAME OVER!', font=('Arial', 24, 'bold'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update()
