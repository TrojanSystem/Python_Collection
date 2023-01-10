from pong_ball import PaddleBall
from pong_paddle import Paddle
from turtle import Screen

from pong_score import PongScore

screen = Screen()
screen.title('Pong')
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
score = PongScore()
ball = PaddleBall()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.listen()
game_is_on = True

while game_is_on:

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_detection()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.paddle_detection()
    if ball.xcor() > 360:
        ball.reset_position()
        score.update_left()
    elif ball.xcor() < -360:
        ball.reset_position()
        score.update_right()

    screen.update()
screen.exitonclick()
