# import colorgram

# colorObjs = colorgram.extract('day-18/hirst/mountain-wallpaper-meadows.jpg', 10)
# colors = []
# for color in colorObjs:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   colors.append((r, g, b))

# print(colors)
from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

tammy = Turtle()
tammy.hideturtle()
tammy.shape('circle')
tammy.speed(7)

colors = [(147, 150, 188), (105, 100, 54), (49, 45, 20), (167, 158, 45), (84, 81, 22), (92, 97, 125), (46, 56, 43), (72, 84, 68), (113, 119, 163), (230, 220, 88)]
go_up_by = 0

def row_of_dots():
  for n in range(0, 10):
    tammy.dot(10, random.choice(colors))
    tammy.pu()
    tammy.fd(20)

for p in range(0, 10):
  row_of_dots()
  go_up_by += 20
  tammy.setpos(0, go_up_by)



screen = Screen()
screen.exitonclick()

# 10 x 10
# 20 in size for dots
# space by 50 spaces
