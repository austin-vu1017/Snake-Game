from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        
    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)
            
    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            self.body[seg_num].goto(self.body[seg_num - 1].xcor(), self.body[seg_num - 1].ycor())
        self.head.fd(MOVE_DISTANCE)
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def grow(self):
        self.add_segment(self.body[-1].position())
    
    def reset_snake(self):
        for seg_num in self.body:
            seg_num.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
