from turtle import Screen , Turtle
from theSnake import snake
from food import Food
from score import score
import time

screen =Screen()
screen.setup(width=600 , height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

go_on = True
snake = snake()
food = Food()
score = score()
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while go_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extand()
        score.increase()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        go_on = False
        score.game_over()
    for segmen in snake.segmetan:
        if segmen == snake.head:
            pass
        elif snake.head.distance(segmen) < 10:
            go_on = False
            score.game_over()


screen.exitonclick()
