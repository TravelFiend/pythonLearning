from turtle import Screen
from classes.paddle import Paddle
from classes.ball import Ball
from classes.scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

rightPaddle = Paddle(350.00, 'dodger blue')
leftPaddle = Paddle(-350.00, 'dodger blue')
ball = Ball('red')
scoreboard = Scoreboard()

screen.listen()
screen.onkey(leftPaddle.moveUp, 'Up')
screen.onkey(leftPaddle.moveDown, 'Down')
screen.onkey(rightPaddle.moveUp, 'Left')
screen.onkey(rightPaddle.moveDown, 'Right')


gameIsOn = True
while gameIsOn:
  time.sleep(ball.moveSpeed)
  screen.update()
  ball.move()

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  if ball.xcor() > 390:
    ball.reset()
    scoreboard.lPoint()

  if ball.xcor() < -390:
    ball.reset()
    scoreboard.rPoint()
    # gameIsOn = False

screen.exitonclick()
