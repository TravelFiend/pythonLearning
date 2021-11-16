from turtle import Turtle


FONT = ('courier', 24, 'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.levelNumber = 0
    self.color('red')
    self.penup()
    self.hideturtle()
    self.goto(-240, 270)
    self.updateLevel()

  def updateLevel(self):
    self.clear()
    self.levelNumber += 1
    self.write(f'Level {self.levelNumber}', align='center', font=FONT)
