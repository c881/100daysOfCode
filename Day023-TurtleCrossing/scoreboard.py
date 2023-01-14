from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(x=-280, y = 270)
        self.level = 1
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Level: {self.level}")

    def up_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over")

