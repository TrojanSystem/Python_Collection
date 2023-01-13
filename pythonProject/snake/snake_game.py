from turtle import Screen

from score_board import Score
from snake import Snake
from snake_food import SnakeFood

screen = Screen()
screen.setup(600, 600)
screen.title('Snake Game')
screen.bgcolor('black')

snake = Snake()
food = SnakeFood()
score = Score()
game_is_on = True

screen.onkeypress(snake.move_left, 'a')
screen.onkeypress(snake.move_right, 'd')
screen.onkeypress(snake.move_up, 'w')
screen.onkeypress(snake.move_down, 's')

screen.listen()
while game_is_on:
    snake.move()
    if snake.segments[0].distance(food) < 15:
        snake.snake_length()
        food.refresh()

        score.update_score()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        game_is_on = False
        score.game_over()
    for seg in snake.segments:
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
