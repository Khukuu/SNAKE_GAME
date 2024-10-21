from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import scoreBoard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
user_score = scoreBoard()

screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision
    if snake.head.distance(food) < 15:
        #spawning food
        food.spawnFood()
        #extending the snake body
        snake.extend()
        user_score.addScore()
        user_score.scoreDisplay()
    
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameOn = False
        
    #Detect collision with tail
    for body in snake.snake[2:]:
        if snake.head.distance(body) < 10:
            gameOn = False

#if game ends
user_score.game_over()




screen.exitonclick()

