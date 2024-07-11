from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBord
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake=Snake()
food = Food()
scoreboard = ScoreBord()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


games_is_on = True
while games_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        games_is_on=False

    for segment in snake.segments[1::]:
        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            games_is_on = False




screen.exitonclick()