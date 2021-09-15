from turtle import Turtle
import random as r
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.shapesize(0.5)
        self.penup()
        self.move()


    def move(self):
        self.setx(r.randint(-280, 280))
        self.sety(r.randint(-280, 280))