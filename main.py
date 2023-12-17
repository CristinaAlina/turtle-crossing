import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(fun=player.move_up, key="Up")
screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # Move each car from car_manager
    car_manager.move_cars()
    screen.update()

    if random.randint(0, 4) == 1:
        # Generate a new car only in certain iterations
        car_manager.generate_new_car()

    # Detect collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.achieved_finish_line() and game_is_on:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.reset_manager()
        car_manager.increase_cars_speed()


screen.exitonclick()