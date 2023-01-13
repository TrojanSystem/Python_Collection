import time
from turtle import Screen

from crossing_road.cars_generated import CarGenerated
from crossing_road.cross_score import CrossScore
from crossing_road.cross_turtle import CrossTurtle

screen = Screen()
screen.title('Cross Road')
screen.setup(600, 600)
screen.bgcolor('white')
screen.tracer(0)
tu = CrossTurtle()
car = CarGenerated()
score = CrossScore()
game_is_on = True
screen.listen()
screen.onkeypress(tu.move_up, 'Up')
screen.onkeypress(tu.move_down, 'Down')

while game_is_on:
    car.create_car()
    car.move_car()
    screen.update()
    for cars in car.all_cars:
        if cars.distance(tu) < 20:
            game_is_on = False
            score.game_over()

    if tu.ycor() >= 200:
        score.increase_level()
        tu.reset_position()

screen.exitonclick()
