from turtle import Turtle, Screen
import random


screen = Screen()
greenGuy = Turtle()
redGuy = Turtle()
blueGuy = Turtle()
orangeGuy = Turtle()
purpleGuy = Turtle()
yCoord = 130.00
keepGoing = True
ind = 0

turds = [greenGuy, redGuy, blueGuy, orangeGuy, purpleGuy]
colors = ['green', 'red', 'blue', 'orange', 'purple']

for turd in turds:
  turd.shape('turtle')
  turd.speed(8)
  turd.penup()
  turd.goto(-240.00, yCoord)
  turd.setheading(0)
  turd.color(colors[ind])
  yCoord -= 65.00
  ind += 1

choice = screen.textinput('Make your bet', 'Who will win? Enter a color (green, red, blue, orange, purple)').lower()
print(choice)
while keepGoing:
  for turd in turds:
    willMove = random.randint(0, 2)
    if willMove == 0:
      turd.fd(25)

      if round(turd.xcor(), 0) >= 315:
        keepGoing = False
        print(choice)

        if choice == turd.color()[0]:
          print(f'You win! The {choice} turtle finished first.')
        else :
          print(f'You lose. The {turd.color()[0]} turtle finished first.')

        break
    else:
      continue

screen.exitonclick()
