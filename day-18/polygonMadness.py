from turtle import Turtle, Screen

tabby = Turtle()
tabby.shape('turtle')

colors = ['purple', 'slate blue', 'royal blue', 'cadet blue', 'turquoise', 'cyan', 'aquamarine', 'spring green', 'lime green', 'forest green']
angleTotal = 180

for n in range(3, 11):
  tabby.color(colors[n - 3])

  for p in range(0, n):
    angle = 180 - (angleTotal / n)
    tabby.forward(100)
    tabby.right(angle)

  angleTotal += 180

screen = Screen()
screen.exitonclick()
