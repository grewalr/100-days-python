import colorgram
from turtle import Turtle, Screen
import turtle as t
import random


def extract_colours():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb_colors.append(rgb)

    return rgb_colors


def print_spots(num_of_dots):
    for _ in range(num_of_dots):
        my_turtle.dot(20, random.choice(colors))
        my_turtle.fd(50)


t.colormode(255)
my_turtle = Turtle()
colors = extract_colours()
my_turtle.penup()

num_of_rows = 10
num_of_dots = 10
spacing = 50

for i in range(num_of_rows):
    y_coord = i * spacing
    my_turtle.setpos(0, y_coord)
    print_spots(num_of_dots)


screen = Screen()
screen.exitonclick()