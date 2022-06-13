import turtle
from turtle import Turtle, Screen
import random

t = Turtle()

#
# def go_right(step):
#     t.setheading(0)
#     t.forward(step)
#
#
# def go_up(step):
#     t.setheading(90)
#     t.forward(step)
#
#
# def go_left(step):
#     t.setheading(180)
#     t.forward(step)
#
#
# def go_down(step):
#     t.setheading(270)
#     t.forward(step)
#
#
# def make_random_walk(step_size, step_number):
#     move_dict = {1: go_up,
#                  2: go_right,
#                  3: go_left,
#                  4: go_down
#                  }
#     for _ in range(step_number):
#         move_in_a_direction = move_dict[random.randint(1, 4)]
#         move_in_a_direction(step_size)
#
#
# if __name__ == "__main__":
#     t.hideturtle()
#     t.speed("fastest")
#     make_random_walk(15, 1000)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


#
# directions = [0, 90, 180, 270]
# t.pensize(10)
t.speed('fastest')


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(1)

#
# for _ in range(200):
#     t.color(random_color())
#     t.forward(30)
#     t.setheading(random.choice(directions))
screen = Screen()
screen.exitonclick()
random_color()
