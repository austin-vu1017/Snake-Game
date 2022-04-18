from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.sety(260)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
    
    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.update()
        
    def increase_score(self):
        self.score += 1
        self.update()
