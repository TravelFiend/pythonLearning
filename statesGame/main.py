import turtle
import pandas as pd
from pandas.core.frame import DataFrame

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'statesGame/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

stateWriter = turtle.Turtle()
stateWriter.hideturtle()
stateWriter.penup()

statesData = pd.read_csv('statesGame/50_states.csv')
states = statesData.state.tolist()
guessedStates = []

while len(guessedStates) < 50:
  stateGuessed = screen.textinput(title=f'{len(guessedStates)}/50 States Guessed', prompt='Enter a state').title()

  if stateGuessed == 'Exit' or stateGuessed == 'End' or stateGuessed == 'Q':
    missedStates = []
    for state in states:
      if state not in guessedStates:
        missedStates.append(state)
    df = DataFrame(missedStates)
    df.to_csv('statesGame/missed_states.csv')
    break
  if stateGuessed in states and stateGuessed not in guessedStates:
    guessedStates.append(stateGuessed)
    stateRow = statesData[statesData.state == stateGuessed]
    stateWriter.goto(int(stateRow.x), int(stateRow.y))
    stateWriter.write(stateGuessed, align='center', font=('Callibri', 8, 'normal'))

screen.exitonclick()
