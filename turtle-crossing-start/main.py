import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

num_of_cars = random.randint(1, 50)
cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create the player
player = Player()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

# Create the cars
for _ in range(1, 10):
    car = CarManager()
    cars.append(car)

# Create the scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(cars[0].move_speed)

    for car in cars:
        random_distance = random.randint(0, 10)
        car.backward(random_distance)

        if car.xcor() < -280:
            car.reset_position()

        if player.is_at_finish_line():
            scoreboard.update_scoreboard()
            player.reset_position()
            car.increase_move_speed()

        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
