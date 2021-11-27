from turtle import Turtle


FONT = ('Courier', 16, 'normal')

HIGH_SCORE = 0
with open('snakeGame/data.txt') as highScore:
  contents = highScore.read()
  if contents:
    HIGH_SCORE = int(contents)

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('deep sky blue')
    self.score = 0
    self.highScore = HIGH_SCORE
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.writeScore()

  def writeScore(self):
    self.clear()
    self.write(f'Score: {self.score} -> High Score: {self.highScore}', align='center', font=FONT)

  def addToScore(self):
    self.score += 1

  def reset(self):
    if self.score > HIGH_SCORE:
      with open('snakeGame/data.txt', mode='w') as file:
        file.write(f'{self.score}')
      self.highScore = self.score
    self.score = 0
    self.writeScore()


  def resetScore(self):
    self.score = 0
    self.writeScore()
