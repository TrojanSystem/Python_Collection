import random
from turtle import Turtle

Colors = ['red', 'orange', 'green', 'yellow', 'blue']


class CarGenerated:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_distance = random.randint(0, 20)

        if random_distance == 1:
            new_Car = Turtle()
            new_Car.shape('square')
            new_Car.shapesize(stretch_len=2, stretch_wid=1)
            new_Car.color(random.choice(Colors))
            random_y = random.randint(-200, 200)
            new_Car.penup()
            new_Car.goto(300, random_y)
            self.all_cars.append(new_Car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(1)

