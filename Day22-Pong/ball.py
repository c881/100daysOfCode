from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("orange")
        self.speed("fastest")
        self.setheading(45)

    def move(self, x, y):
        new_x = self.xcor() + x
        new_y = self.ycor() + y
        self.goto(new_x, new_y)

    def go_home(self):
        self.goto(0,0)