from food import Food
from scoreboard import Scoreboard
from snake import Snake

import time as ti
from turtle import Screen
# import random as ran


screen = Screen()
# Screen Setup
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    ti.sleep(0.1)
    snake.move()
    scoreboard.write_score()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.refresh()
        snake.extend_snake()

    #detect collistion with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
