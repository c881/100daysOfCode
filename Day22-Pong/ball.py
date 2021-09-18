from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("orange")
        self.speed("fastest")
        self.setheading(45)

    def move(self):
        self.forward(20)