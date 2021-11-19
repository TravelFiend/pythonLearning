from turtle import Turtle, shape
import random


COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISCTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
  def __init__(self):
    super().__init__()
    self.allCars = []
    self.makeCar()

  def makeCar(self):
    randChance = random.randint(1, 6)
    if randChance == 1:
      newCar = Turtle(shape='square')
      newCar.shapesize(stretch_wid=1, stretch_len=2)
      newCar.penup()
      newCar.color(random.choice(COLORS))
      randY = random.randint(-260, 260)
      newCar.goto(320, randY)
      self.allCars.append(newCar)

  def moveLeft(self):
    for car in self.allCars:
      car.backward(STARTING_MOVE_DISCTANCE)
