import random
import turtle
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=400)
user_bet =  screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Choose a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

is_race_on = False
if user_bet:
    is_race_on = True
for turtle_index in range (0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-285, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor()>290:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The winner is the {winning_color} turtle")
            else:
                print(f"You have lost! The winner is the {winning_color} turtle")
            is_race_on = False



screen.exitonclick()


