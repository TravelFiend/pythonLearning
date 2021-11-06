import turtle as t
import random

t.colormode(255)
ted = t.Turtle()

degrees_to_turn = [0, 90, 180, 270]

def rand_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

ted.pensize(10)
ted.speed(0)


for n in range(0, 200):
  ted.color(rand_color())
  ted.seth(random.choice(degrees_to_turn))
  ted.forward(20)

screen = t.Screen()
screen.exitonclick()
