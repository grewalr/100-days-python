import random
import turtle as t
from turtle import Turtle, Screen
import random
import tkinter as tk

tim = Turtle()
t.colormode(255)
# tim.shape("turtle")


# for _ in range(4):
#     tim.fd(10)
#     tim.right(90)


# for _ in range(15):
#     jeevan.pendown()
#     jeevan.fd(10)
#     jeevan.penup()
#     jeevan.fd(10)

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.fd(10)
#         tim.right(angle)
#
# for shape_size in range(3, 11):
#     draw_shape(shape_size)
#     tim.color(random.random(), random.random(), random.random())


### Random walk
# def get_heading():
#     return random.choice([0, 90, 180, 270])
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
#
# tim.pensize(15)
# tim.speed(0)
# for _ in range(100):
#     tim.color(random_color())
#     heading = get_heading()
#     tim.setheading(heading)
#     tim.fd(30)


### Spirograph
tim.reset()
tim.speed(0)
tilt = 5
number_of_circles = int(360 / tilt)
for _ in range(number_of_circles):
    tim.color(random_color())
    tim.circle(100)
    tim.left(tilt)


# tim.tilt(30)
# tim.fd(50)





screen = Screen()
screen.exitonclick()