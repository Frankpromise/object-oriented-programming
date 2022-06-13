from turtle import Turtle, Screen

#
t = Turtle()


# t.up()
# t.shape('square')
# t.shapesize(5, 5, 5)
# t.fillcolor('red')
# t.stamp()
# screen = Screen()
# screen.exitonclick()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
screen = Screen()
screen.exitonclick()
