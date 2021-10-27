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
        self.high_score = 0
        try:
            with open("data.txt", "r") as data:
                self.high_score = int(data.read())
        except:
            pass


    def write_score(self):
        self.write(arg=f"Score:{self.score}\t High score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.refresh()
    # def game_over(self):
    #     # self.clear() - The player can still see his final score
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)