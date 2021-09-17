from turtle import Screen
from paddle import Paddle
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

pong1 = Paddle(350)
pong2 = Paddle(-350)


screen.listen()
screen.onkey(pong1.up, "Up")
screen.onkey(pong1.down, "Down")
screen.onkey(pong2.up, "w")
screen.onkey(pong2.down, "x")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong1.move()
    pong2.move()


screen.exitonclick()