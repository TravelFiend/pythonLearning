from turtle import Turtle


class Paddle(Turtle):
  def __init__(self, startX, color):
    super().__init__()
    self.startX = startX
    self.shape('square')
    self.color(color)
    self.shapesize(stretch_wid=5 , stretch_len=1)
    self.penup()
    self.goto(startX, 0)

  def moveUp(self):
    new_y = self.ycor() + 20
    self.goto(self.startX, new_y)

  def moveDown(self):
    new_y = self.ycor() - 20
    self.goto(self.startX, new_y)
