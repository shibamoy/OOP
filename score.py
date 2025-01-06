from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.scores = 0
        self.color("white")

    def scoreboard(self):
        self.clear()
        print(self.write(f"Score = {self.scores}", False, align="center", font=("Arial", 18, "normal")))
