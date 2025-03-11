import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()
    car_manager.move_cars()

    # detect collision with the wall
    if player.is_finish_game():
        scoreboard.update_level()
        player.back_to_starting_point()
        car_manager.speed_up()

    # detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.write_game_over()

screen.exitonclick()
