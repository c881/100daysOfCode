from turtle import Turtle, Screen
import random as ran
import time as ti

screen = Screen()
# Screen Setup
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake_segments = []
starting_positions = [(0, 0), (-20, 0), (-40,0)]
for position in starting_positions:
    new_turtle = Turtle("square")
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.goto(position)
    snake_segments.append(new_turtle)

game_is_on = True
while game_is_on:
    screen.update()
    # From last segment to the first(not included), move forward over the segment before you
    # Then move the first segment by 20
    for seg_num in range(len(snake_segments) - 1,0,-1):
        new_x = snake_segments[seg_num - 1].xcor()
        new_y = snake_segments[seg_num - 1].ycor()
        snake_segments[seg_num].goto(new_x, new_y)
    snake_segments[0].forward(20)
    ti.sleep(1)


screen.exitonclick()