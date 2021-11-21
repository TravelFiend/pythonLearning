#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

theLetter = ''
with open('mailMerge/Input/Letters/starting_letter.txt') as letterFile:
    theLetter = letterFile.read()

with open('mailMerge/Input/Names/invited_names.txt') as namesFile:
    names = namesFile.readlines()
    for name in names:
        letterCopy = theLetter
        newLetter = letterCopy.replace('[name]', name.strip())
        with open(f'mailMerge/Output/ReadyToSend/letter_for_{name}.txt', mode='w') as newFile:
            newFile.write(newLetter)





