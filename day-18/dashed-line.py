from turtle import Turtle, Screen

turdle = Turtle()
turdle.shape('turtle')
turdle.color('green')

turdle.color("purple2", "SpringGreen")

for num in range(1, 51):
  turdle.pendown()
  turdle.forward(10)
  turdle.penup()
  turdle.forward(10)


screen = Screen()
screen.exitonclick()
