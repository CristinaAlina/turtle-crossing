from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LIMIT_Y = 250
LIMIT_X = 300


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(LIMIT_X, random.randint(-LIMIT_Y, LIMIT_Y))


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def generate_new_car(self):
        """Generates a new car on the screen"""
        car = Car()
        self.cars.append(car)

    def move_cars(self):
        """Moves each car from cars list, if a car is out of screen will be removed from the list."""
        if len(self.cars) > 0:
            for car in self.cars:
                if car.xcor() > -LIMIT_X:
                    new_x = car.xcor() - self.move_speed
                    car.goto(new_x, car.ycor())
                else:
                    car.hideturtle()
                    self.cars.remove(car)

    def increase_cars_speed(self):
        """Increase cars speed by 10 paces"""
        self.move_speed += MOVE_INCREMENT

    def reset_manager(self):
        """Resets the list of cars and hides each remained car from the screen"""
        for car in self.cars:
            car.hideturtle()
        self.cars = []

