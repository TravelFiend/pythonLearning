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

screen.listen()
screen.onkey(turd.move, 'Up')

gameIsOn = True
while gameIsOn:
  time.sleep(0.1)
  screen.update()

  if turd.ycor() > 280:
    turd.backToStart()
    scoreboard.updateLevel()
