from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__("square")
        car_colour = random.choice(COLORS)
        self.color(car_colour)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.move_speed = 0.1
        self.penup()
        self.start_position()

    def start_position(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-250, 260)
        self.goto(rand_x, rand_y)

    def reset_position(self):
        self.goto(280, self.ycor())

    def increase_move_speed(self):
        self.move_speed *= 0.5
