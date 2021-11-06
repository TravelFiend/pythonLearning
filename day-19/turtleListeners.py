from turtle import Turtle, Screen

todd = Turtle()
screen = Screen()

todd.pencolor('salmon')
todd.pensize(10)

def forward():
  todd.fd(20)

def back():
  todd.bk(20)

def counter():
  todd.circle(80, 20)

def clockwise():
  todd.circle(-60, -20)

def erase():
  todd.home()
  todd.clear()

screen.listen()
screen.onkey(forward, 'w')
screen.onkey(back, 's')
screen.onkey(counter, 'a')
screen.onkey(clockwise, 'd')
screen.onkey(erase, 'c')

screen.exitonclick()
