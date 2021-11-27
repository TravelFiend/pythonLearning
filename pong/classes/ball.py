from turtle import Turtle


class Ball(Turtle):
  def __init__(self, color):
    super().__init__()
    self.color(color)
    self.shape('circle')
    self.penup()
    self.xMove = 10
    self.yMove = 10
    self. moveSpeed = 0.1

  def move(self):
    new_x = self.xcor() + self.xMove
    new_y = self.ycor() + self.yMove
    self.goto(new_x, new_y)

  def bounce_x(self):
    self.xMove *= -1
    self.moveSpeed *= 0.9

  def bounce_y(self):
    self.yMove *= -1
    self.moveSpeed *= 0.9

  def reset(self):
    self.goto(0, 0)
    self.moveSpeed = 0.1
    self.bounce_x()
