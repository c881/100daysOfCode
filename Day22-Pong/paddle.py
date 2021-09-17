from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.seth(UP)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.setposition(x=x, y=0)

    def up(self):
        self.setheading(UP)

    def down(self):
        self.setheading(DOWN)

    def move(self):
        if self.heading() == UP and self.ycor() < 250:
            self.forward(20)
        if self.heading() == DOWN and self.ycor() > -250:
            self.forward(20)
