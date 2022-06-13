# import turtle,

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('red')


def movement():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


movement()
timmy_the_turtle.forward(90)
timmy_the_turtle.right(90)
movement()
timmy_the_turtle.forward(90)

screen = Screen()
screen.exitonclick()

from turtle import Turtle, Screen

t = Turtle()
for i in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
screen = Screen()
screen.exitonclick()
