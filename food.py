from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
    
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
