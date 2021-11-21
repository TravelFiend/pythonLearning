# with open('day-24/myFile.txt') as file:
#   contents = file.read()
#   print(contents)

# mode='w' : write (overwrites file contents)
# mode='a' : append (adds to end of file contents)
#### both create files if the file doesn't already exist ####

with open('../../../Desktop/newFile.txt', mode='a') as file:
  file.write('\nApplesauce Corn')
