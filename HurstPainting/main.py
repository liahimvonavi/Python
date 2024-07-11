import turtle
import random
from extracted_colors import colors

joe = turtle.Turtle()
joe.speed(0)
joe.hideturtle()
turtle.colormode(255)
joe.penup()
joe.setheading(225)
joe.forward(300)
joe.setheading(0)

number_of_dots = 100
for dot_count in range (1, number_of_dots+1):
    joe.dot(20, random.choice(colors))
    joe.forward(50)


    if dot_count%10==0:
        joe.setheading(90)
        joe.forward(50)
        joe.setheading(180)
        joe.forward(500)
        joe.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
