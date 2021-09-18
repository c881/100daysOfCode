from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color("white")
        self.score_l = 0
        self.score_r = 0
        self.hideturtle()


    def write_score(self):
        self.write(arg=f"{self.score_l}\t\t\t{self.score_r} ", align=ALIGNMENT, font=FONT)


    def increase_score_l(self):
        self.score_l += 1

    def increase_score_r(self):
        self.score_r += 1


    def refresh(self):
        self.clear()
        self.write_score()


    def game_over(self):
        # self.clear() - The player can still see his final score
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)