from turtle import Turtle, Screen
from prettytable import PrettyTable


tommy = Turtle()
print(tommy)
tommy.shape('turtle')
tommy.color('black', 'green')
tommy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.field_names = ['Player', 'Team']
table.add_row(['Larry Byrd', 'Celtics'])
table.add_row(['Mark Price', 'Cavs'])
table.add_row(['Allen Iverson', 'Raptors'])
table.align = 'l'

print(table)
