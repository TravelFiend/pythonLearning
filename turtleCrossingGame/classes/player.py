from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.color('aquamarine')
    self.setheading(90)
    self.shape('turtle')
    self.penup()
    self.backToStart()

  def backToStart(self):
    self.goto(STARTING_POSITION)

  def move(self):
    newY = self.ycor() + MOVE_DISTANCE
    self.goto(0, newY)
