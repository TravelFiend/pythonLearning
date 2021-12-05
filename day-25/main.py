# # import csv
import pandas as pd

# # with open('./day-25/weather_data.csv') as weatherFile:
# #   data = csv.reader(weatherFile)
# #   temperatures = []
# #   for row in data:
# #     if row[1] != 'temp':
# #       temperatures.append(row[1])
# #   print(temperatures)

# weatherData = pd.read_csv('./day-25/weather_data.csv')
# temperatureList = weatherData.temp.to_list()

# print(weatherData.temp.max())

# # Get Data in Column
# print(weatherData.condition)

# # Get Data in Row
# print(weatherData[weatherData.day == 'Monday'])
# print(weatherData[weatherData.temp == weatherData.temp.max()])

# # Convert to Fahrenheit
# monday = weatherData[weatherData.day == 'Monday']
# print((int(monday.temp) * 9 / 5) + 32)

# # Create a dataframe from scratch
# data_dict = {
#   'students': ['John', 'Jacob', 'Jingleheimerschmidt'],
#   'scores': [76, 56, 94]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv('day-25/new_data.csv')

squirrelData = pd.read_csv('day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
blackSquirrels = len(squirrelData[squirrelData['Primary Fur Color'] == 'Black'])
graySquirrels = len(squirrelData[squirrelData['Primary Fur Color'] == 'Gray'])
redSquirrels = len(squirrelData[squirrelData['Primary Fur Color'] == 'Cinnamon'])

squishedSquirrelColor = {
  'Fur Color': ['Black', 'Gray', 'Cinnamon'],
  'Count': [blackSquirrels, graySquirrels, redSquirrels]
}


# squishedSquirrelColor = {
#   'Fur Color': ['Black', 'Gray', 'Cinnamon'],
#   'Count': [0, 0, 0]
# }

# colorList = squirrelData["Primary Fur Color"].tolist()
# for color in colorList:
#   if color == 'Black':
#     squishedSquirrelColor['Count'][0] += 1
#   elif color == 'Gray':
#     squishedSquirrelColor['Count'][1] += 1
#   elif color == 'Cinnamon':
#     squishedSquirrelColor['Count'][2] += 1

colorCounts = pd.DataFrame(squishedSquirrelColor)
colorCounts.to_csv('day-25/squirrel_count.csv')
