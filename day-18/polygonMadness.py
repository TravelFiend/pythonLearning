from turtle import Turtle, Screen
import turtle

tabby = Turtle()

colors = ['purple', 'slate blue', 'royal blue', 'cadet blue', 'turquoise', 'cyan', 'aquamarine', 'spring green', 'lime green', 'forest green']
angleTotal = 180

for n in range(3, 11):
  angle = 180 - (angleTotal / n)

  for p in range(0, n):
    tabby.color(colors[n - 3])
    turtle.forward(100)
    turtle.right(angle)

  angleTotal += 180

screen = Screen()
screen.exitonclick()
