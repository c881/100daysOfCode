from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.hideturtle()


    def write_score(self):
        self.write(arg=f"Score:{self.score} ", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1


    def refresh(self):
        self.clear()
        self.write_score()


    def game_over(self):
        # self.clear() - The player can still see his final score
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)