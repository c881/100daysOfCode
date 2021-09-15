from snake import Snake
from food import Food
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

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    ti.sleep(0.1)
    snake.move()
    screen.update()
    if snake.head.distance(food) < 15:
        food.move()



screen.exitonclick()
