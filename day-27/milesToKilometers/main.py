from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)


mileInput = Entry()
mileInput.grid(row=0, column=1)

def convertIt():
  miles = mileInput.get()
  output['text'] = float(miles) * 1.609344

milesLabel = Label(text='Miles')
milesLabel.grid(row=0, column=2)

equalToLabel = Label(text='is equal to')
equalToLabel.grid(row=1, column=0)

output = Label(text='0')
output.grid(row=1, column=1)

kmLabel = Label(text='Km')
kmLabel.grid(row=1, column=2)

submitButton = Button(text='Calculate', command=convertIt)
submitButton.grid(row=2, column=1)

window.mainloop()
