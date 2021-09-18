from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("orange")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.x_move > 20:
            self.x_move += 1
        elif self.x_move > 10:
            self.x_move += 2
        elif self.x_move < -20:
            self.x_move -= 1
        else:
            self.x_move -= 2

    def reset_position(self):
        self.bounce_x()
        if self.x_move > 0:
            self.x_move = 10
        else:
            self.x_move = -10
        self.home()