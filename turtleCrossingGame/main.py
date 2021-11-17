from turtle import Screen
import time
from classes.player import Player
from classes.scoreboard import Scoreboard
from classes.carManager import CarManager


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Turtle Crossing (Frogger for poor people)')
screen.tracer(0)

turd = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(turd.move, 'Up')

sleepTime = 0.1
gameIsOn = True
while gameIsOn:
  screen.update()
  time.sleep(sleepTime)
  car.makeCar()
  car.moveLeft()

  for auto in car.allCars:
    if auto.distance(turd) < 20:
      gameIsOn = False
      scoreboard.gameOver()

  if turd.ycor() > 280:
    turd.backToStart()
    scoreboard.updateLevel()
    sleepTime *= 0.8

screen.exitonclick()
