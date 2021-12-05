student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

natoDictDF = pandas.read_csv('day-26/NATO-alphabet/nato_phonetic_alphabet.csv')
natoAlphabetDict = {row.letter: row.code for (ind, row) in natoDictDF.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

enteredWord = input('Type a word: ').upper()
wordAsNatoAlphabet = [natoAlphabetDict[letter] for letter in enteredWord]
print(wordAsNatoAlphabet)
