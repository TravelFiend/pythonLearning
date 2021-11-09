from turtle import Turtle


FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('deep sky blue')
    self.score = 0
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.writeScore()

  def writeScore(self):
    self.clear()
    self.write(f'Score: {self.score}', align='center', font=FONT)

  def addToScore(self):
    self.score += 1

  def gameOver(self):
    self.goto(0, 0)
    self.write('GAME OVER', align='center', font=FONT)

  def resetScore(self):
    self.score = 0
    self.writeScore()
