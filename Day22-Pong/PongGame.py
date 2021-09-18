from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
x_move = 10
y_move = 10
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Ball hit Top/Bottom screen
    if abs(ball.ycor()) > 270:
        y_move *= -1
    # Paddle missed the ball and it hit a side wall
    if abs(ball.xcor()) > 390:
        x_move *= -1
        ball.go_home()
    ball.move(x=x_move, y=y_move)
r_paddle.onclick()

screen.exitonclick()