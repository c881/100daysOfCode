import snake as s
from turtle import Screen
import random as ran
import time as ti

screen = Screen()
# Screen Setup
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = s.Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    ti.sleep(0.3)
    # From last segment to the first(not included), move forward over the segment before you
    # Then move the first segment by 20
    snake.move()


screen.exitonclick()