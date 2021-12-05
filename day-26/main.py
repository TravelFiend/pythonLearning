import random


nums = [1, 2, 3]
newNums = [n + 1 for n in nums]
print(newNums)

print([n * 2 for n in range(1, 5)])

names = ['John', 'Sally', 'Suzy', 'Rosemary', 'Geoffrey']
upcaseNames = [name.upper() for name in names if len(name) > 4]
print(upcaseNames)

### LIST COMPREHENSION ###
### START OF CHALLENGE 1 ###

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [n**2 for n in numbers]

#Write your code 👆 above:

print(squared_numbers)

### END OF CHALLENGE 1 ###
### START OF CHALLENGE 2 ###

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [n for n in numbers if n % 2 == 0]

#Write your code 👆 above:

print(result)

### END OF CHALLENGE 2 ###
### START OF CHALLENGE 3 ###

with open('day-26/numList1.txt') as file1:
  file1data = file1.readlines()

with open('day-26/numList2.txt') as file2:
  file2data = file2.readlines()

result = [int(n) for n in file1data if n in file2data]

# Write your code above 👆

print(result)

### END OF CHALLENGE 3 ###

### DICTIONARY COMPREHENSION ###

personDict = {name: random.randint(0, 100) for name in names}
print(personDict)
passedStudents = {key: value for (key, value) in personDict.items() if value >= 60}
print(passedStudents)

### START DICT COMP CHALLENGE 1 ###

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

dictCompChal1Result = {word: len(word) for word in sentence.split()}

print(dictCompChal1Result)


### END DICT COMP CHALLENGE 1 ###

### START DICT COMP CHALLENGE 2 ###

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}

print(weather_f)

### END DICT COMP CHALLENGE 2 ###