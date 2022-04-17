from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.sety(260)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
    
    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()