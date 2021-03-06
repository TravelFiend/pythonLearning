from turtle import Screen
from classes.snake import Snake
from classes.food import Food
from classes.scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Gameism')
screen.tracer(0)

snake = Snake('orange', 'square')
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

gameIsOn = True
while gameIsOn:
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.addToScore()
    scoreboard.writeScore()

  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()
    snake.reset()

  for block in snake.blocks[1:]:
    if snake.head.distance(block) < 10:
      scoreboard.reset()
      snake.reset()

screen.exitonclick()
