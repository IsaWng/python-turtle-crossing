import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def add_car(self):
        chance = random.randint(1, 6)
        if chance == 3:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.setheading(180)
            car.goto(300, random.randint(-250, 260))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
