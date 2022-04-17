from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

scrn = Screen()
scrn.setup(width=600, height=600)
scrn.bgcolor("black")
scrn.title("Snake Game")
scrn.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
food = Food()

scrn.listen()
scrn.onkey(snake.up, "w")
scrn.onkey(snake.down, "s")
scrn.onkey(snake.left, "a")
scrn.onkey(snake.right, "d")

game_on = True

while game_on:
    scrn.update()
    time.sleep(0.1)
    snake.move()
    
    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
    
scrn.exitonclick()