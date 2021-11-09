from turtle import Turtle, up


STARTING_POSITIONS = [(0.00, 0.00), (0.00, -20.00), (0.00, -40.00)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self, color, shape):
    self.color = color
    self.shape = shape
    self.blocks = []
    self.create_snake()
    self.head = self.blocks[0]

  def create_snake(self):
    for pos in STARTING_POSITIONS:
      self.add_segment(pos)

  def add_segment(self, position):
    tom = Turtle(shape=self.shape)
    tom.color(self.color)
    tom.penup()
    tom.goto(position)
    self.blocks.append(tom)

  def extend(self):
    self.add_segment(self.blocks[-1].position())

  def move(self):
    for num in range(len(self.blocks) - 1, 0, -1):
      new_x = self.blocks[num - 1].xcor()
      new_y = self.blocks[num - 1].ycor()
      self.blocks[num].goto(new_x, new_y)

    self.head.fd(20)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
