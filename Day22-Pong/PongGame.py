from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Ball hit Top/Bottom screen
    if abs(ball.ycor()) > 280:
        ball.bounce_y()
    if 380 > abs(ball.xcor()) > 330:
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            print(ball.ycor(), r_paddle.ycor())
            print(ball.ycor(), l_paddle.ycor())
            ball.bounce_x()
    elif abs(ball.xcor()) > 370:
        if ball.xcor() > 0:
            scoreboard.increase_score_l()
        else:
            scoreboard.increase_score_r()
        ball.reset_position()
    ball.move()
    scoreboard.refresh()


screen.exitonclick()