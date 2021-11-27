import turtle as t
import random

t.colormode(255)
tommy = t.Turtle()

tommy.speed(0)
heading = 10

def rand_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

for n in range(0, 36):
  tommy.color(rand_color())
  tommy.circle(100)
  tommy.seth(heading)
  heading += 10

screen = t.Screen()
screen.exitonclick()
